import linecache
import time
from datetime import date

# --------------------------
system = 1
# 1 = Linux  | 2 = Windows
# -------------------------

if system == 1:
    ramPath = "/proc/meminfo"
    passwordPath = "/home/krzys/mailAndPass.txt"
else:
    ramPath = "E:/meminfo"
    passwordPath = "E:/mailAndPass.txt"


def password():
    line = linecache.getline(passwordPath, 2)
    return line


def from_email():
    line = linecache.getline(passwordPath, 1)
    return line


def actual_time():
    named_tuple = time.localtime()
    time_string = time.strftime("%H:%M:%S", named_tuple)
    time_string = str(time_string)
    return time_string


def actual_date():
    a_date = date.today()
    return a_date


def hour():
    h = time.localtime().tm_hour
    return h


def free_ram():
    with open(ramPath, 'r') as mem:
        ret = {}
        for i in mem:
            sline = i.split()
            if str(sline[0]) == 'MemFree:':
                ret['free'] = int(sline[1])
        ram = str(int(ret['free'] / 1024))
        return ram


