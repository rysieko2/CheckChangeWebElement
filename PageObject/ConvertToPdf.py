#!/usr/bin/ python3
# -*- coding: utf-8 -*-

from docx2pdf import convert
import sys
import subprocess
import re

# --------------------------
# 1 = Linux  | 2 = Windows

system = 2
# -------------------------


# Windows install:
# pip install docx2pdf

# Linux install:
# apt-get install -y build-essential libssl-dev libffi-dev python-dev
# apt-get install -y libreoffice

if system == 1:
    path = "/home/krzys/"
    file = "/home/krzys/New-Application.docx"

else:
    path = "E:/New-Application.docx"
    newName = "E:/New-Application"


def convert_to(folder, source, timeout=None):
    args = [libreoffice_exec(), '--headless', '--convert-to', 'pdf', '--outdir', folder, source]

    process = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
    filename = re.search('-> (.*?) using filter', process.stdout.decode())

    return filename.group(1)


def libreoffice_exec():
    # TODO: Provide support for more platforms
    if sys.platform == 'darwin':
        return '/Applications/LibreOffice.app/Contents/MacOS/soffice'
    return 'libreoffice'
