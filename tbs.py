#!/usr/bin/ python3
# -*- coding: utf-8 -*-

from PageObject.File import File
from PageObject.Gmail import Gmail
from PageObject.WebDriver import *
from PageObject.metods import *

# 1 = Linux
# 2 = Windows
system = 1

d = Driver()
startFirst = d.first()
startBox = d.box()
actualBox = startBox
gm = Gmail('wroclaw.pip@gmail.com', "paleciak")
gm.send_message('kordecki.k@gmail.com', 'VPS-TBS ZOSTAŁ AKTYWOWANY'+str(free_ram()), 'Aktualnie:' + startFirst)

fileLog = File(pathLogFiles)
fileLog.create_add_string_begin(str(actual_time() + "," + str(free_ram()) + "," + startFirst))

counter = 0

while 23 > hour():
    try:
        print(str(counter) + " " + str(actual_time()))
        d.refresh()
        actualBox = d.box()
    except:
        fileLog.add_string_to_next_line(str(actual_time() + "," + str(free_ram()) + ",Ex: While23 - d.refresh(), C:"+str(counter)))
        gm.quit()
        gm = Gmail('wroclaw.pip@gmail.com', "paleciak")
        gm.send_mail_attach('kordecki.k@gmail.com', '>>> AWARIA "d.refresh()" <<<', '', pathLogFiles, "logsTbs.txt",
                            "txt")
        counter = 199
    counter += 1

    if counter == 200:
        ram = free_ram()
        try:
            d.quit()
        except:
            fileLog.add_string_to_next_line(
                str(actual_time() + "," + str(free_ram()) + ",Ex: Counter200 - d.quit()"))
        try:
            gm.quit()
        except:
            fileLog.add_string_to_next_line(
                str(actual_time() + "," + str(free_ram()) + ",Ex: Counter200 - gm.quit()"))
        try:
            d = Driver()
            actualBox = d.box()
        except:
            fileLog.add_string_to_next_line(
                str(actual_time() + "," + str(free_ram()) + ",Ex: Counter200 - d = Driver()"))
        try:
            gm = Gmail('wroclaw.pip@gmail.com', "paleciak")
        except:
            fileLog.add_string_to_next_line(
                str(actual_time() + "," + str(free_ram()) + ",Ex: Counter200 - gm = Gmail"))
        try:
            gm.send_message('kordecki.k@gmail.com', str(ram) + "," + str(free_ram()) + ", " + str(actual_time()),
                            d.first())
            fileLog.add_string_to_next_line(str(actual_time()) + "," + str(ram) + "," + str(free_ram()))
        except:
            fileLog.add_string_to_next_line(
                str(actual_time() + "," + str(free_ram()) + "Ex: Counter200 - gm.send_message"))
        counter = 0

    if startBox != actualBox:
        ram = free_ram()
        actualFirst = d.first()
        d.first_click()

        ad = d.ad_number()
        contents = d.ad_contents()
        d.back()
        try:
            gm.send_message('kordecki.k@gmail.com', "NEW:" + actualFirst, d.new_loc_link())
            gm.send_message('ania.puszczewicz@gmail.com', "NEW:" + actualFirst, d.new_loc_link())
            fileLog.add_string_to_next_line(str(actual_time()) + "," + str(ram) + "," + str(free_ram()))
        except:
            fileLog.add_string_to_next_line(
                str(actual_time() + "," + str(free_ram()) + ",Ex: Box!= -  gm.send_message"))

        startBox = actualBox

actualFirst = d.first()
try:
    gm.send_mail_attach('kordecki.k@gmail.com', 'VPS-TBS ZOSTAŁ WYŁĄCZONY', 'Aktualnie:' + actualFirst, pathLogFiles,
                        "logsTbs.txt", "txt")
    # gm.send_message('ania.puszczewicz@gmail.com', 'VPS-TBS ZOSTAŁ WYŁĄCZONY', 'Aktualnie:' + actualFirst)

except:
    fileLog.add_string_to_next_line(str(actual_time() + "," + str(free_ram()) + ",Ex: Exit -  gm.send_message"))
try:
    gm.quit()
except:
    fileLog.add_string_to_next_line(str(actual_time() + "," + str(free_ram()) + ",Ex: Exit -  gm.quit()"))
try:
    d.quit()
except:
    fileLog.add_string_to_next_line(str(actual_time() + "," + str(free_ram()) + ",Ex: Exit -  d.quit()"))

