import pandas
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.fftpack import fft
from scipy import signal


plt.rcParams['font.sans-serif']=['SimHei'] #中文显示乱码的问题
#plt.rcParams['axes.unicode_minus']=False #




#data_16 = np.genfromtxt(r'G:\孙帅\data.txt', encoding='utf-8',delimiter =',',dtype=None)


#print(data_16)
data_16 = pandas.read_csv(r'my.csv')
# print(data_16)
#l= data_16['Channel 1 (V)'][0:4000]
y = data_16['Channel 1 (V)'][0:4000]

ekgDFT = pandas.read_csv(r'ekg.csv')
#print(ekgDFT)
t = ekgDFT['Time (s)'][0:4000]
#print(x)
samplingFreq = 1/(t[22]-t[21])
#print(samplingFreq)


#print(x)


# t = ""  #定义一个空值变量
# for i in l:
#     i = i.replace("\"","").replace("\"","")    #去掉字符串的两边引号
#     t=t+i
#     #print(np.array(i))
# #print(t)


#
# h = t.split('aaaaf108')
# #print(h)
# def toInt32(hexStr):    #转成32位整数
#     # 4294967296
#     intMin = -2147483648
#     intMax = 2147483647
#     #print(type(hexStr))
#     real = int(hexStr,16)
#     if real >= intMax:
#         return real-intMax+intMin
#     else:
#         return real
# q = []
# for e in h:
#     v = e[8:16]
#     if v =="":
#         #print('invalid v',e)  #给出异常情况
#         continue
#     pass
#     #print(e[8:16])
#     #print(toInt32(v))
#     g = toInt32(v)
#     q.append(g)
# #print(len(y))
# y= q[0:4000]


# matplotlib.rc('figure', figsize=(15, 8))
# plt.plot(x,y)
# plt.show()


#ekgData = y.values


fftData = np.abs( fft(y))
fftLen = int(len(fftData) / 2)
# freqs = np.linspace(0,samplingFreq/2, fftLen )
# matplotlib.rc('figure', figsize=(20, 8))
# plt.figure()
# plt.plot( freqs, fftData[0:fftLen] )
# plt.figure()
# plt.plot( freqs[0:400], fftData[0:400] )
# plt.show()


##设计IIR滤波器
sos = signal.iirfilter(17, [2*np.pi*50, 2*np.pi*300], rs=60, btype='bandstop',
                        analog=False, ftype='cheby2', fs=4000,
                        output='sos')
w, h = signal.sosfreqz(sos, 2000, fs=2000)
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.semilogx(w, 20 * np.log10(np.maximum(abs(h), 1e-5)))
# ax.set_title('Chebyshev Type II bandpass frequency response')
# ax.set_xlabel('Frequency [Hz]')
# ax.set_ylabel('Amplitude [dB]')
# ax.axis((10, 1000, -100, 10))
# ax.grid(which='both', axis='both')
# plt.show()


##去除50Hz-300Hz噪音
ekgFiltered = signal.sosfilt(sos, y)


##时域信号
# matplotlib.rc('figure', figsize=(15, 8))
# plt.plot(x,ekgFiltered)


# 频率
# FFT长度是信号长度的一半
# 由于奈奎斯特定理，在光谱中只能看到一半的采样频率
# fftData = np.abs( fft(ekgFiltered) )
# fftLen = int(len(fftData) / 2)
# freqs = np.linspace(0,samplingFreq/2, fftLen )
#
# # matplotlib.rc('figure', figsize=(15, 8))
# #
# # plt.figure()
# # plt.plot( freqs, fftData[0:fftLen] )
# # plt.figure()
# # plt.plot( freqs[0:400], fftData[0:400] )


## 设计第二次IIR滤波器
sos2 = signal.iirfilter(17, [2*np.pi*50, 2*np.pi*300], rs=60, btype='bandpass',
                        analog=False, ftype='cheby2', fs=4000,
                        output='sos')
w, h = signal.sosfreqz(sos2, 2000, fs=2000)
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.semilogx(w, 20 * np.log10(np.maximum(abs(h), 1e-5)))
# ax.set_title('Chebyshev Type II bandpass frequency response')
# ax.set_xlabel('Frequency [Hz]')
# ax.set_ylabel('Amplitude [dB]')
# ax.axis((10, 1000, -100, 10))
# ax.grid(which='both', axis='both')
# plt.show()


##第二次去掉50Hz-300Hz噪音
ekgFiltered2 = signal.sosfilt(sos2, ekgFiltered)


# ## 第二次时域信号
# matplotlib.rc('figure', figsize=(15, 8))
# plt.plot(x,ekgFiltered2)
# plt.show()




def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'same') / w


# Time Domain Signal
matplotlib.rc('figure', figsize=(15, 8))
# print(ekgFiltered2)
plt.plot(t,moving_average(ekgFiltered2, 100))
plt.show()