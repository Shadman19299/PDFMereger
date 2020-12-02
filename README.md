# PDFMereger
"""
Author: Shadman UR Rabbi
Script Name: PDFMERGER
Description: This script merges two pdf into one and put them in a folder called Combined.
            This is specially designed to accomodate the need of Dept of Records and Information Service
            The two pdf has to have a requirement of a front page and a back page in the same folder
            The naming convention is front page: "XYZ.pdf" and Back page : "XYZ-bk.pdf"
Python Version Used: python3.9, Fundamental Packages: os, pathlib, PyPDF2, tkinter(for GUI)
Date Modified: 11/6/2020

"""
# Make The file Executable using pyinstallar
install pyinstaller(follow instruction on link: https://pypi.org/project/pyinstaller/)
open terminal.
cd Path:\to\file
pyinstaller --onefile PDFMergerMain.py
To find the executable file, open the dist folder: PDFMergerMain

