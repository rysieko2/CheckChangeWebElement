import time

# 1 = Linux
# 2 = Windows

system = 1

if system == 1:
    ramPath = "/proc/meminfo"
    pathLogFiles = "/home/krzys/tbs-wroclaw/LogsFiles/checkLogs.txt"
else:
    ramPath = "C:/Users/Prince/PycharmProjects/tbs-wroclaw/logsFiles/meminfo"
    pathLogFiles = "C:/Users/Prince/PycharmProjects/tbs-wroclaw/logsFiles/checkLogs.txt"


def actual_time():
    named_tuple = time.localtime()
    time_string = time.strftime("%H:%M:%S", named_tuple)
    time_string = str(time_string)
    return time_string


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
