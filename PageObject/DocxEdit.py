import time

from docx import Document

# pip install python-docx

# --------------------------
# 1 = Linux  | 2 = Windows

system = 2
# -------------------------

if system == 1:
    pathFolder = "/home/krzys/"
    pathFile = "/home/krzys/Pattern-of-application.docx"
    newPathFile = "/home/krzys/New-Application.docx"
else:
    pathFolder = "E:/"
    pathFile = "E:/Pattern-of-application.docx"
    newPathFile = "E:/New-Application.docx"


def changeWordInDocument(oldWord1, newWord1, oldWord2, newWord2, oldWord3, newWord3):
    document = Document(pathFile)
    for paragraph in document.paragraphs:
        if oldWord1 in paragraph.text:
            paragraph.text = paragraph.text.replace(oldWord1, newWord1)
        if oldWord2 in paragraph.text:
            paragraph.text = paragraph.text.replace(oldWord2, newWord2)
        if oldWord3 in paragraph.text:
            paragraph.text = paragraph.text.replace(oldWord3, newWord3)
    document.save(newPathFile)

