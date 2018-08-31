import os
import time
import glob

# 28-0118312e61ff  28-0118314a18ff 

os.system('sudo modprobe w1-gpio')
os.system('sudo modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'

folders = glob.glob(base_dir + '28*')

def read_temp_raw(fldr):
    f = open(fldr+'/w1_slave', 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp(fldr):
    lines = read_temp_raw(fldr)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_f

while True:
    tempx = [read_temp(x) for x in folders]
    print([time.time()] + tempx)
    time.sleep(5)
