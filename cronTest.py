#!/usr/bin/python
# -*- coding: utf-8 -

import time
import subprocess

subprocess.call(['./Application/Tbs/startMail.sh'])
time.sleep(2)
while 2>= time.localtime().tm_hour:
    subprocess.call(['./Application/Tbs/sendMail.sh'])
    break
time.sleep(2)
subprocess.call(['./Application/Tbs/stopMail.sh'])

