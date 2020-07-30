'''
def toInt32(hexStr):
	#4294967296
	intMin=-2147483648
	intMax=2147483647
	real = int(hexStr, 16)
	if real >= intMax:
		return real - intMax + intMin
	else:
		return real
'''

import csv
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import scipy

dataset = pd.read_csv("my.csv")
timeset = pd.read_csv("ekg.csv")

# import json

# f = open('final.txt')
# # print(json.loads(f.read())[0])
# dataset = json.loads(f.read())
# f.close()

y = dataset.hart.values
y = y[0:8000]
t = timeset['Time (s)'].values

N = len(y)
Fs = 1000
T = 1.0 / Fs

# x = np.linspace(0.0, N*T, N)
x = np.linspace(0.0, 25, N)

fig_td = plt.figure()
fig_td.canvas.set_window_title('ECG_0')
ax = fig_td.add_subplot(311)
ax.set_title('image_0')

ax.plot(x, y, color='r', linewidth=0.7)

from scipy.fftpack import fft
from scipy import signal

samplingFreq = 1/(t[22]-y[21])


ax1 = fig_td.add_subplot(312)
ax1.set_title('image_1')

fftData = np.abs( fft(y) )
fftLen = int(len(fftData) / 2)
freqs = np.linspace(0,samplingFreq/2, fftLen )


from scipy import signal
sos = signal.iirfilter(17, [2*np.pi*50, 2*np.pi*100], rs=60, btype='bandstop',
                        analog=False, ftype='cheby2', fs=4000,
                        output='sos')
w, h = signal.sosfreqz(sos, 2000, fs=2000)

ekgFiltered = signal.sosfilt(sos, y)


fftData = np.abs( fft(ekgFiltered) )
fftLen = int(len(fftData) / 2)
freqs = np.linspace(0,samplingFreq/2, fftLen )


sos2 = signal.iirfilter(17, [2*np.pi*50, 2*np.pi*100], rs=60, btype='bandpass',
                        analog=False, ftype='cheby2', fs=4000,
                        output='sos')
w, h = signal.sosfreqz(sos2, 2000, fs=2000)

ekgFiltered2 = signal.sosfilt(sos2, ekgFiltered)

def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'same') / w

ax1.plot(t, moving_average(ekgFiltered2, 100), color='g')


ax2 = fig_td.add_subplot(313)
ax2.set_title('image_1')
fft=scipy.fft(moving_average(ekgFiltered2, 100))
bp=fft[:]
for i in range(len(bp)): # (H-red)
 	if i>=100:bp[i]=0
ibp=scipy.ifft(bp) 
ax2.plot(ibp/max(ibp), 'b', color='b', linewidth=0.7)

plt.show()