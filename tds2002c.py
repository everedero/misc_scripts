"""
POC to use Tektronix TDS2002C from remote computer
via USB and the VISA thing
"""

import pyvisa
import time
import numpy as np
from pathlib import Path

def connect():
    rm = pyvisa.ResourceManager()
    inst = rm.open_resource("USB0::1689::929::C010857::0::INSTR")
    inst.timeout = 50000 # time in ms
    idn = inst.query("*IDN?")
    print("Connected to:")
    print(idn)
    test_error(inst)
    return(inst)

def test_error(inst):
    err = inst.query("*ESR?")
    try:
        err = int(err)
    except:
        raise IOError(f"Invalid error code {err}")
    if err != 0:
        print(f"Error code {err}")

def set_up_scale(inst, time_div=500e-6, volt_div=5, trig_level=2.5):
    inst.write("FACTORY")
    inst.write(f"CH1:VOLTS {volt_div}")
    inst.write(f"HOR:MAIN:SCALE {time_div}")
    inst.write("TRIG:MAIN:LEVEL {trig_level}")

def exec_capture(inst):
    inst.write("ACQUIRE:STOPAFTER SEQUENCE")
    inst.write("ACQUIRE:STATE ON")
    print(inst.query("*OPC?"))

def retrieve_measure(inst):
    test_error(inst)
    metadata = dict()
    inst.write("MEASU:IMMED:TYPE MEAN")
    val = inst.query("MEASU:IMMED:VALUE?")
    print(val)
    val = val.split(" ")[1].rstrip()
    metadata["mean"] = float(val)
    inst.write("MEASU:IMMED:TYPE FREQ")
    val = inst.query("MEASU:IMMED:VALUE?")
    val = val.split(" ")[1].rstrip()
    metadata["freq"] = float(val)
    test_error(inst)
    inst.write("CURVE?")
    values = inst.read_raw()

    # Remove ":CURVE #42500"
    # TODO find a better separator?
    if b'00' in values:
        value = values[13::]
    value = value[:-1]

    data = np.frombuffer(value, dtype='b')

    # Print all measurement parameters
    print("Measurement params:")
    print(inst.query("WFMPRE?"))

    # Retrieve info about values
    # Xaxis * XINCR
    xincr = inst.query("WFMP:XINCR?")
    xincr = xincr.split(" ")[1]
    xincr = float(xincr)
    metadata["xincr"] = xincr
    # Yaxis * YMULT
    ymult = inst.query("WFMP:YMULT?")
    ymult = ymult.split(" ")[1]
    ymult = float(ymult)
    metadata["ymult"] = ymult
    # Number of points
    nrpt = inst.query("WFMP:NR_P?")
    nrpt = nrpt.split(" ")[1]
    nrpt = int(nrpt)
    # Description
    val = inst.query("WFMP:WFID?")
    val = val[13::]
    val = val.replace('"', "")
    metadata["description"] = val

    if len(value) != nrpt:
        raise IOError("Number of samples retrieved do not match")

    time_val = np.arange(0, nrpt * xincr, xincr) - (nrpt * xincr / 2)

    data = data * ymult

    # Export data
    fulldata = np.concatenate([time_val[:, np.newaxis], data[:, np.newaxis]], axis=1)
    return(fulldata, metadata)

def retrieve_cursors(inst):
    val = inst.query("CURSOR?")
    print(val)
    val = inst.query("CURSOR:FUNCTION?")
    if val.find("VBARS") > -1:
        is_vertical = True
        val1 = inst.query("CURSOR:VBARS:POSITION1?")
        val2 = inst.query("CURSOR:VBARS:POSITION2?")
    elif val.find("HBARS") > -1:
        is_vertical = False
        val1 = inst.query("CURSOR:HBARS:POSITION1?")
        val2 = inst.query("CURSOR:HBARS:POSITION2?")
    else:
        return None
    val1 = val1.split(" ")[1]
    val2 = val2.split(" ")[1]
    try:
        val1 = float(val1)
        val2 = float(val2)
    except:
        print("Invalid cursor values")
        return None

    ret = {"is_vertical": is_vertical, "v1": val1, "v2": val2}
    return(ret)

def save_data(fulldata, metadata, filename="oscillo", allscreen=True,
              cursors=None):
    np.savetxt(f"{filename}.csv", fulldata, delimiter=",",
               header=f"""{metadata["description"]}\ntime (s), voltage (v)""")
    if cursors is not None:
        with open(f"{filename}_cursors.txt", "w") as myfile:
            myfile.write(str(cursors))

    # Loading saved data
    #newdata = np.loadtxt(f"{filename}.csv", delimiter=",")

    # Plot
    from matplotlib import pyplot as plt
    plt.plot(fulldata[:,0], fulldata[:,1])
    plt.xlabel("Time (s)")
    plt.ylabel("Voltage (V)")
    if cursors is not None:
        if cursors["is_vertical"]:
            plt.axvline(x=cursors["v1"])
            plt.axvline(x=cursors["v2"])
        else:
            plt.axhline(y=cursors["v1"])
            plt.axhline(y=cursors["v2"])

    plt.title(metadata["description"])
    if allscreen:
        ymax = metadata["ymult"] * 25 * 4
        plt.ylim(-ymax, ymax)
    plt.grid()
    plt.savefig(f"{filename}.png")

if __name__ == "__main__":
    inst = connect()
    #set_up_scale(inst, time_div=500e-6, volt_div=5, trig_level=2.5)
    #exec_capture(inst)

    data, metadata = retrieve_measure(inst)
    cursors = retrieve_cursors(inst)
    filename_root = "oscillo"
    filename_num = 1
    filename = f"{filename_root}{filename_num}"

    while Path(filename + ".csv").exists():
        filename_num += 1
        filename = f"{filename_root}{filename_num}"
    print(f"Creating file {filename}")

    save_data(data, metadata, filename=filename, cursors=cursors)
