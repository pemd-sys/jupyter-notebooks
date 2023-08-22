
import numpy as np
import json
import matplotlib.pyplot as plt
from scipy import signal


xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

#https://stackoverflow.com/questions/15424449/calculating-nth-roots-of-unity-in-python
svm_points = np.roots([1, 0, 0, 0, 0, 0, -1])
print(svm_points)

theta = np.arange(0,6,1)*2*np.pi/6;
svm_points = np.exp(1j*theta)

plt.plot(np.real(svm_points), np.imag(svm_points), 'bo')
axes=plt.gca()
axes.set_aspect('equal')


annotations = ["V1 \n (100)", "V2 \n (110)", "V3 \n (010)", "V4 \n (011)", "V5 \n (001)", "V6 \n (101)"]

annotations = ["(100)", "(110)", "(010)", "(011)", "(001)", "(101)"]

for xi, yi, text in zip(np.real(svm_points), np.imag(svm_points), annotations):
    axes.annotate(text,
                xy=(xi, yi), xycoords='data',
                xytext=(xi*15, yi*15), textcoords='offset points',ha='center',va='center')


plt.quiver(np.zeros(6), np.zeros(6), np.real(svm_points), np.imag(svm_points), color='b', units='xy', scale=1)


#append first point at end to complete the polygon
#https://stackoverflow.com/questions/7332841/add-single-element-to-array-in-numpy

plt.plot(np.append(np.real(svm_points),np.real(svm_points)[0]), np.append(np.imag(svm_points),np.imag(svm_points)[0]), linestyle='dashed')


plt.show() 

Vout = 400; # LL rms
Vdc = 800;
fsw = 5e3;
fo = 50;




M = 0.9 #2/np.sqrt(3) # Vout*1.414/1.732/(Vdc/2);

TimePeriod = 1/fo;
dt = 1/(fsw*1000);
Ts = 1/fsw
t=np.arange(0,TimePeriod,dt).reshape(-1, 1); 
fo = np.array([1,1,1]).reshape(1, -1)*50
phase_shift = np.array([0,-2*np.pi/3,2*np.pi/3]).reshape(1, -1)

Timag = Ts*M/2*np.sin(2*np.pi*fo*t-phase_shift);
Tmax = Timag.max(axis=1).reshape(-1,1)
Tmin = Timag.min(axis=1).reshape(-1,1)

Teff = Tmax - Tmin

Toffset_min = -Tmin
Toffset_max = Ts - Tmax

# sine pwm
Toffset = Ts/2

#space vector
Toffset = 1/2*(Ts-Teff) - Tmin
plt.plot(t,Tmin,t,Tmax,t,Ts/2*np.ones(len(t)),t,Tmin+Tmax,t,Toffset)
plt.show()


Tg = Timag + Toffset
#Tg += Toffset
#Tg = Ts - Tg

#
#plt.plot(t,Timag>0)

Ttotal = Tmin + Tmax

#60 deg
Toffset = np.multiply(Ttotal>=0,Ts-Tmax)
Toffset += np.multiply(Ttotal<0,-Tmin)

#plt.plot(t,Tmin,t,Tmax,t,Toffset_min,t,Toffset_max,t,Ts/2*np.ones(len(t)),t,Ttotal,t,Toffset)

# Create plots with pre-defined labels.
fig, ax = plt.subplots()
ax.plot(t, Tmin, 'k--', label='Tmin')
ax.plot(t, Tmax, 'k:', label='Tmax')
ax.plot(t, Toffset_min, 'b--', label='Toffset_min')
ax.plot(t, Toffset_max, 'b:', label='Toffset_max')
ax.plot(t, Ts/2*np.ones(len(t)), 'r', label='Ts/2')
ax.plot(t, Ttotal, 'g--', label='Ttotal')
ax.plot(t, Toffset, 'g:', label='Toffset')

legend = ax.legend(loc='upper right')

plt.show()

#30 deg
Toffset = np.multiply(Ttotal>=0,-Tmin)
Toffset += np.multiply(Ttotal<0,Ts-Tmax)

Vn = ((Timag+Toffset)/(Ts/2.0) -1.0)*Vdc/2.0

#plt.plot(t,Toffset_min,t,Toffset_max,t,Ts/2*np.ones(len(t)),t,Toffset)
#plt.plot(t,Tmin,t,Tmax,t,Ts/2*np.ones(len(t)),t,Ttotal,t,Toffset)

#plt.plot(t,Vn)
#plt.show()


# variable phase shift
phase_delay = -np.pi/6. + np.pi/3.

#protection
if phase_delay >=np.pi/3:
    phase_delay = np.pi/3
if phase_delay <= -np.pi/3:
    phase_delay = -np.pi/3


Timag_shft = Ts*M/2*np.sin(2*np.pi*fo*t-phase_shift-phase_delay);
Tmax_shft = Timag_shft.max(axis=1).reshape(-1,1)
Tmin_shft = Timag_shft.min(axis=1).reshape(-1,1)

Teff_shft = Tmax_shft - Tmin_shft

Toffset_min_shft = -Tmin_shft
Toffset_max_shft = Ts - Tmax_shft

Ttotal_shft = Tmin_shft + Tmax_shft

#60 deg
Toffset = np.multiply(Ttotal_shft>=0,Ts-Tmax)
Toffset += np.multiply(Ttotal_shft<0,-Tmin)

# Create plots with pre-defined labels.
fig, ax = plt.subplots()
ax.plot(t, Tmin, 'k--', label='Tmin')
ax.plot(t, Tmax, 'k:', label='Tmax')
ax.plot(t, Toffset_min, 'b--', label='Toffset_min')
ax.plot(t, Toffset_max, 'b:', label='Toffset_max')
ax.plot(t, Ts/2*np.ones(len(t)), 'r', label='Ts/2')
ax.plot(t, Ttotal, 'g--', label='Ttotal')
ax.plot(t, Toffset, 'r', label='Toffset')

legend = ax.legend(loc='upper right')

plt.show()

Vn = ((Timag+Toffset)/(Ts/2.0) -1.0)*Vdc/2.0
plt.plot(t,Vn[:,0],t,Vn[:,0]-Vn[:,1])
plt.show()

triangle = signal.sawtooth(2 * np.pi * fsw * t, 0.5)