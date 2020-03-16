#!/usr/bin/ python3
# -*- coding: utf-8 -*-

from PageObject.ConvertToPdf import *
from PageObject.DocxEdit import *
from PageObject.File import *
from PageObject.Gmail import *
from PageObject.metods import *
from PageObject.WebDriver import *

# -------------------------
system = 1 
# 1 = Linux  | 2 = Windows
# -------------------------


if system == 1:
    pathLogFiles = "/home/krzys/CheckChangeWebElement/checkLogs.txt"
    pathFilePdf = "/home/krzys/New-Application.pdf"
else:
    pathLogFiles = "C:/Users/Prince/PycharmProjects/CheckChangeWebElement/checkLogs.txt"
    pathFilePdfW = "C:/Users/Prince/Desktop/New-Application"
    set_gecko_win()
    set_ram_pass_path()
    set_docx_edit_path_win()


d = Driver()
startFirst = d.first()
startBox = d.box()
actualBox = startBox
gm = Gmail(from_email(), password())
gm.send_message('kordecki.k@gmail.com', 'VPS-TBS ZOSTAŁ AKTYWOWANY'+str(free_ram()), 'Aktualnie:' + startFirst)

fileLog = File(pathLogFiles)
fileLog.create_add_string_begin(str(actual_time() + "," + str(free_ram()) + "," + startFirst))

counter = 0

while 15 > hour():
    try:
        print(str(counter) + " " + str(actual_time()))
        d.refresh()
        actualBox = d.box()
    except:
        fileLog.add_string_to_next_line(str(actual_time() + "," + str(free_ram()) + ",Ex: While23 - d.refresh(), C:"+str(counter)))
        gm.quit()
        gm = Gmail(from_email(), password())
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
            gm = Gmail(from_email(), password())
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

        changeWordInDocx("DATA", str(actual_date()), "OGŁOSZENIE", ad[14:21], "ULICA", actualFirst[2:])
 
        if system == 1:
            libreoffice_exec()
            convert_linux(pathDocxNewFolder, pathDocxNewFile, timeout=15)

        else:
            pathFilePdf = pathFilePdfW+str(ad[14:16])+".pdf"
            convert_win(pathDocxNewFileWin, pathFilePdf)

        d.back()
        try:
            gm.send_mail_attach('kordecki.k@gmail.com', "NEW:" + actualFirst, d.new_loc_link(), pathFilePdf, "Podanie.pdf", "pdf")
            gm.send_mail_attach('ania.puszczewicz@gmail.com', "NEW:" + actualFirst, d.new_loc_link(), pathFilePdf, "Podanie.pdf", "pdf")

            fileLog.add_string_to_next_line(str(actual_time()) + "," + str(ram) + "," + str(free_ram())+str(actualFirst))
        except:
            fileLog.add_string_to_next_line(
                str(actual_time() + "," + str(free_ram()) + ",Ex: Box!= -  gm.send_message"))

        startBox = actualBox
    
actualFirst = d.first()
try:
    gm.send_mail_attach('kordecki.k@gmail.com', 'VPS-TBS ZOSTAŁ WYŁĄCZONY', 'Aktualnie:' + actualFirst, pathLogFiles, "logs.txt", "txt")
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

