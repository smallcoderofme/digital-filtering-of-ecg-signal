import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.fftpack import fft


plt.rcParams['font.sans-serif']=['SimHei'] #中文显示乱码的问题
#plt.rcParams['axes.unicode_minus']=False #

data_16 = np.genfromtxt(r'data.txt', encoding='utf-8',delimiter =',',dtype=None)
#print(data_16)
l = np.array(data_16[0:1200])
#ekgDFT = pandas.read_csv(r'G:\孙帅\my.csv')
#print(x)
t = ""  #定义一个空值变量
for i in l:
    i = i.replace("\"","").replace("\"","")    #去掉字符串的两边引号
    t=t+i
    #print(np.array(i))
#print(t)


h = t.split('aaaaf108')
#print(h)


def toInt32(hexStr):    #转成32位整数
    intMin = -2147483648
    intMax = 2147483647
    real = int(hexStr,16)
    if real >= intMax:
        return real-intMax+intMin
    else:
        return real
y = []
for e in h:
    v = e[8:16]
    if v =="":
        #print('invalid v',e)  #给出异常情况
        continue
    pass
    #print(e[8:16])
    #print(toInt32(v))
    g = toInt32(v)
    y.append(g)
#print(b)
n = len(y)
#print(n)
Fs = 800
T = 1.0/ Fs
x = np.linspace(0.0, n*T, n)

# arr = []
# for x in range(25000):
# 	arr.append(0.05)
# 	pass
ekgDF= np.array(y[0:1001])  #取了y中的1000位数
print(ekgDF)
fftData=np.abs(fft(ekgDF))
fftLen=int(len(fftData)/2)
freqs=np.linspace(0,x/2,fftLen)     #可能会有问题


matplotlib.rc('figure',figsize=(20,8))
plt.figure()
plt.plot(freqs,fftData[0:fftLen])
plt.figure()
plt.show()