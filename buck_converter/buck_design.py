# Python code for buck converter design

# Main parameters

import math
import numpy as np
import matplotlib.pyplot as plt

Vo = 1.2 # Output Voltage (V)
Io = 6 # Maximum load current
eff = 0.87 # estimated efficiency @ max. load
fsw = 600e3 # switching frequency
Vin = 12 # DC input bus voltage
Vin_max = 16 # worst case max. DC input voltage
fbw = 6e3 # Control bandwidth
Istep = 3 # transient load step
Tboard = 75 # worst case board temperature deg C
Vin_pp = 0.24 #allowed input peak-to0peak ripple voltage
Vin_trans = 0.36 # allowed input transient overshoot or undershoot
L = 0.33e-6
# duty cycle
D = Vo/(Vin*eff)

# capacitance to meed ripple rating
C = D*(1-D)*Io/(Vin_pp*fsw)

# calculate capacitance taking into account capacitance tolerance 10%
Ctol = C * 1.1

# lookup capacitance as function of DC bias. C = Ctol @ Vin

D = np.arange(0.,1.,0.001)
# RMS input current rating
Iin_RMS = Io*np.sqrt(D*(1-D)+1./12.*(Vo/(L*fsw*Io)**2*((1-D)**2)*D))

fig, ax = plt.subplots()
ax.plot(D, Iin_RMS, 'k--', label='Iin_RMS')
plt.show()

print('')


## References:
# 1. https://www.ti.com/lit/an/slyt670/slyt670.pdf?ts=1691606063890
