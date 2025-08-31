"""
POC to use Tektronix TDS2002C from remote computer
via USB and the VISA thing
"""

import pyvisa
import time
import numpy as np

rm = pyvisa.ResourceManager()
inst = rm.open_resource("USB0::1689::929::C010857::0::INSTR")
inst.timeout = 50000 # time in ms
print(inst.query("*IDN?"))
print(inst.query("*ESR?"))

print(inst.query("*ESR?"))
print(inst.query("ALLEV?"))
inst.write("FACTORY")
print(inst.query("CH1:VOLTS?"))
inst.write("CH1:VOLTS 5")
inst.write("HOR:MAIN:SCALE 500e-6")
print(inst.query("HOR:MAIN:SCALE?"))
inst.write("TRIG:MAIN:LEVEL 2.4")
print(inst.query("TRIG:MAIN:LEVEL?"))
print(inst.query("*ESR?"))
inst.write("ACQUIRE:STOPAFTER SEQUENCE")
inst.write("ACQUIRE:STATE ON")
print(inst.query("*OPC?"))
inst.write("MEASU:IMMED:TYPE MEAN")
print(inst.query("MEASU:IMMED:VALUE?"))
inst.write("MEASU:IMMED:TYPE FREQ")
print(inst.query("MEASU:IMMED:VALUE?"))
print(inst.query("*ESR?"))
print(inst.query("ALLEV?"))
inst.write("CURVE?")
values = inst.read_raw()

# Remove ":CURVE #42500"
# TODO find a better separator?
if b'00' in values:
    param, value = values.split(b'00')#, 1)
value = value[:-1]
#value = value[1::]

data = np.frombuffer(value, dtype='b')

# Print all measurement parameters
print(inst.query("WFMPRE?"))

# Retrieve info about values
# Xaxis * XINCR
xincr = inst.query("WFMP:XINCR?")
xincr = xincr.split(" ")[1]
xincr = float(xincr)
# Yaxis * YMULT
ymult = inst.query("WFMP:YMULT?")
ymult = ymult.split(" ")[1]
ymult = float(ymult)
# Number of points
nrpt = inst.query("WFMP:NR_P?")
nrpt = nrpt.split(" ")[1]
nrpt = int(nrpt)

if len(value) != nrpt:
    raise IOError("Number of samples retrieved do not match")

time_val = np.arange(0, nrpt * xincr, xincr)

data = data * ymult

# Export data
fulldata = np.concatenate([time_val[:, np.newaxis], data[:, np.newaxis]], axis=1)

np.savetxt("oscillo.csv", fulldata, delimiter=",", header="time (s), voltage (v)")

# Loading saved data
#newdata = np.loadtxt("oscillo.csv", delimiter=",")

# Plot
from matplotlib import pyplot as plt
plt.plot(time_val, data)
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.grid()
plt.savefig('oscillo.png')
