#!/usr/bin/ python3
# -*- coding: utf-8 -*-

# FOR WINDOWS:
from docx2pdf import convert

import sys
import subprocess
import re

pathDocxNewFile = "/home/krzys/New-Application.docx"
pathDocxNewFolder = "/home/krzys/"
pathDocxNewFileWin = "F:/New-Application.docx"


def convert_win(input_path, output_path):
    convert(input_path, output_path)


def convert_linux(folder, source, timeout=None):
    args = [libreoffice_exec(), '--headless', '--convert-to', 'pdf', '--outdir', folder, source]

    process = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
    filename = re.search('-> (.*?) using filter', process.stdout.decode())

    return filename.group(1)


def libreoffice_exec():
    # TODO: Provide support for more platforms
    if sys.platform == 'darwin':
        return '/Applications/LibreOffice.app/Contents/MacOS/soffice'
    return 'libreoffice'
