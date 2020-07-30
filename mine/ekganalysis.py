'''
from matplotlib import pyplot as plt
import matplotlib
import pandas
import numpy as np
from scipy.fftpack import fft

import random

ekgDF1 = pandas.read_csv('ekg.csv')
ekgDF = pandas.read_csv('my.csv')

# arr = []
# for x in range(25000):
# 	arr.append(0.05)
# 	pass
ekgDF['Channel 1 (V)'] = ekgDF['Channel 1 (V)'][0:8000]
ekgDF['Time (s)'] = ekgDF1['Time (s)']


# print ('Sampling frequency is: ')
samplingFreq = 1/(ekgDF['Time (s)'][22]-ekgDF['Time (s)'][21])
# print (samplingFreq)
ekgDF

# Time Domain Signal
# matplotlib.rc('figure', figsize=(15, 8))
# plt.plot(ekgDF['Time (s)'],ekgDF['Channel 1 (V)'])

# Frequency Domain
# FFT len is half size of the signal len
# Because of nyquist theorem only half of the sampling frequency can be seen in the sprectrum
ekgData = ekgDF['Channel 1 (V)'].values
fftData = np.abs( fft(ekgData) )
fftLen = int(len(fftData) / 2)
freqs = np.linspace(0,samplingFreq/2, fftLen )

# matplotlib.rc('figure', figsize=(20, 8))
# # 
# plt.figure()
# plt.plot( freqs, fftData[0:fftLen] )
# plt.figure()

# plt.plot( freqs[0:400], fftData[0:400] )

## Design IIR filter
from scipy import signal
sos = signal.iirfilter(17, [2*np.pi*50, 2*np.pi*100], rs=60, btype='bandstop',
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

## filter out 50 Hz noise
ekgFiltered = signal.sosfilt(sos, ekgData)

# Time Domain Signal
# matplotlib.rc('figure', figsize=(15, 8))
# plt.plot(ekgDF['Time (s)'],ekgFiltered)

# Frequency Domain
# FFT len is half size of the signal len
# Because of nyquist theorem only half of the sampling frequency can be seen in the sprectrum
fftData = np.abs( fft(ekgFiltered) )
fftLen = int(len(fftData) / 2)
freqs = np.linspace(0,samplingFreq/2, fftLen )

# matplotlib.rc('figure', figsize=(15, 8))

# plt.figure()
# plt.plot( freqs, fftData[0:fftLen] )
# plt.figure()

# plt.plot( freqs[0:400], fftData[0:400] )

## Design IIR filter
sos2 = signal.iirfilter(17, [2*np.pi*50, 2*np.pi*100], rs=60, btype='bandpass',
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

## filter out 50 Hz noise
ekgFiltered2 = signal.sosfilt(sos2, ekgFiltered)

# Time Domain Signal
# matplotlib.rc('figure', figsize=(15, 8))
# plt.plot(ekgDF['Time (s)'],ekgFiltered2)

"""![](http://www.ni.com/cms/images/devzone/tut/2007-07-09_141618.jpg)"""

def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'same') / w

# Time Domain Signal
matplotlib.rc('figure', figsize=(15, 8))
plt.plot(ekgDF['Time (s)'], moving_average(ekgFiltered2, 100))

plt.show()
'''
'''------------------------------------------------------------------------'''

from matplotlib import pyplot as plt
import matplotlib
import pandas
import numpy as np
from scipy.fftpack import fft


import random


ekgDF1 = pandas.read_csv('ekg.csv')
ekgDF = pandas.read_csv('my.csv')


# arr = []
# for x in range(25000):
# 	arr.append(0.05)
# 	pass
ekgDF['Channel 1 (V)'] = ekgDF['Channel 1 (V)'][0:8000]
ekgDF['Time (s)'] = ekgDF1['Time (s)']




print ('Sampling frequency is: ')
samplingFreq = 1/(ekgDF['Time (s)'][22]-ekgDF['Time (s)'][21])
print (samplingFreq)
ekgDF


# Time Domain Signal
matplotlib.rc('figure', figsize=(15, 8))
plt.plot(ekgDF['Time (s)'],ekgDF['Channel 1 (V)'])


# Frequency Domain
# FFT len is half size of the signal len
# Because of nyquist theorem only half of the sampling frequency can be seen in the sprectrum
ekgData = ekgDF['Channel 1 (V)'].values
fftData = np.abs( fft(ekgData) )
fftLen = int(len(fftData) / 2)
freqs = np.linspace(0,samplingFreq/2, fftLen )


matplotlib.rc('figure', figsize=(20, 8))


plt.figure()
plt.plot( freqs, fftData[0:fftLen] )
plt.figure()


plt.plot( freqs[0:400], fftData[0:400] )


## Design IIR filter
from scipy import signal
sos = signal.iirfilter(17, [2*np.pi*50, 2*np.pi*300], rs=60, btype='bandstop',
                        analog=False, ftype='cheby2', fs=4000,
                        output='sos')
w, h = signal.sosfreqz(sos, 2000, fs=2000)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.semilogx(w, 20 * np.log10(np.maximum(abs(h), 1e-5)))
ax.set_title('Chebyshev Type II bandpass frequency response')
ax.set_xlabel('Frequency [Hz]')
ax.set_ylabel('Amplitude [dB]')
ax.axis((10, 1000, -100, 10))
ax.grid(which='both', axis='both')
plt.show()


## filter out 50 Hz noise
ekgFiltered = signal.sosfilt(sos, ekgData)


# Time Domain Signal
matplotlib.rc('figure', figsize=(15, 8))
plt.plot(ekgDF['Time (s)'],ekgFiltered)


# Frequency Domain
# FFT len is half size of the signal len
# Because of nyquist theorem only half of the sampling frequency can be seen in the sprectrum
fftData = np.abs( fft(ekgFiltered) )
fftLen = int(len(fftData) / 2)
freqs = np.linspace(0,samplingFreq/2, fftLen )


matplotlib.rc('figure', figsize=(15, 8))


plt.figure()
plt.plot( freqs, fftData[0:fftLen] )
plt.figure()


plt.plot( freqs[0:400], fftData[0:400] )


## Design IIR filter
sos2 = signal.iirfilter(17, [0.5, 200], rs=60, btype='bandpass',
                        analog=False, ftype='cheby2', fs=4000,
                        output='sos')
w, h = signal.sosfreqz(sos2, 2000, fs=2000)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.semilogx(w, 20 * np.log10(np.maximum(abs(h), 1e-5)))
ax.set_title('Chebyshev Type II bandpass frequency response')
ax.set_xlabel('Frequency [Hz]')
ax.set_ylabel('Amplitude [dB]')
ax.axis((10, 1000, -100, 10))
ax.grid(which='both', axis='both')
plt.show()


## filter out 50 Hz noise
ekgFiltered2 = signal.sosfilt(sos2, ekgFiltered)


# Time Domain Signal
matplotlib.rc('figure', figsize=(15, 8))
plt.plot(ekgDF['Time (s)'],ekgFiltered2)



def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'same') / w


# Time Domain Signal
matplotlib.rc('figure', figsize=(15, 8))
plt.plot(ekgDF['Time (s)'],moving_average(ekgFiltered2, 100))
