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

from tkinter import *
from tkinter import  filedialog
import os
import PyPDF2
from fnmatch import fnmatch
from pathlib import Path, PureWindowsPath
import ctypes
from tkinter import messagebox as mb
from datetime import datetime


#Global Variables
originalpath = r"Y:"
newpath ="" #input path
background ="" #background path
front = "" #front path
outputfolder =""
outputfilename =""

#Read the file using PdfFileReader

def pdfread(file):
    pdf = PyPDF2.PdfFileReader(file)
    return pdf
#Add to the writer
def addtowrite(pdf, writer):
    for i in range(pdf.getNumPages()):
        writer.addPage(pdf.getPage(i))
#Merge the front and back
def merge(file1, file2, output):
    pdf1 = pdfread(file1)
    pdf2 = pdfread(file2)

    writer = PyPDF2.PdfFileWriter()

    addtowrite(pdf1, writer)
    addtowrite(pdf2, writer)

    writer.write(output)
    output.close()
#Create The Folder of with path name
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
# This is the most important Method. It goes the to the Folder and subfolders and merge the pdf
def fileparse(path, outputfolderpath):
    try:
        root = path
        logpath = os.path.join(path, "log.txt")
        if (os.path.isfile(logpath)):
            log = open(logpath, "a")
        else:
            log = open(logpath,"w")
        date_time = datetime.now()
        time =date_time.strftime("%m/%d/%Y, %H:%M:%S")
        log.write("\n")
        log.write("Time and date of the run: "+time)
        log.write("\n")
        pattern = "*.pdf" # check the pattern
        for path, subdirs, files in os.walk(root):  #this for loop goes to all the directories
            for name in files: #goes to all the files
                if fnmatch(name, pattern): #if the pattern matches to the .pdf it works
                    if ("-bk" in name):
                        background = name
                        bkpath = os.path.join(path, background)
                        front = name.split("-bk")[0]
                        outputfilename =front + ".pdf" #+ "full.pdf" # Name is the same
                        opath =os.path.join(outputfolderpath, outputfilename)
                        front += ".pdf"
                        fpath = os.path.join(path, front)
                        isfpathexist = os.path.isfile(fpath)
                        isopathexist = os.path.isfile(opath)
                        if( (not isopathexist) and isfpathexist):
                            print(fpath)
                            print(bkpath)
                            print(opath)
                            frontpg = open(fpath, 'rb') # open the front page path
                            backpg = open(bkpath, 'rb') #open the back page path
                            output = open(opath, 'wb') #Open the Output page path
                            merge(frontpg,backpg,output)
                            frontpg.close()
                            backpg.close()
                            output.close()
                            #log.write("The file is comb")
                        else:
                            if(not isfpathexist):
                                log.write("The file's front page naming is a problem: " + bkpath + "\n")
                            else:
                                log.write("The file already exist in combined folder: " + fpath + "\n")
                            continue
                    else:
                        if("bk" in name  or "b k" in name):
                            log.write("The file's back page naming is a problem: " + name + "\n")
                        else:
                            continue
        log.close()
    except OSError as error:
        print(error)
#Message Box
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
#Call Box
def call():
    res=mb.askquestion('Are you Sure?', 'Do you want to Continue?')
    if res == 'yes' :
        #mb.showinfo('Continue', 'Continuing The Operation')
        #Mbox('Continue','Continuing The Operation', 0)
        return
    else :
        quit()
#It choose the outputfolder


def choose_outputfolder():
    window = Tk()
    window.title('Choose a directory')
    Mbox('Output','Choose an output Folder',0)
    window.withdraw()

    filename = filedialog.askdirectory(initialdir=originalpath)
    print(filename)
    path_on_windows = PureWindowsPath(filename)

    call()
    outputfolder= path_on_windows
    outputfolder = Path(outputfolder)
    outputfolder= os.path.join(outputfolder, "Combined")
    createFolder(outputfolder)
    print(outputfolder)
    return outputfolder

#Choose the input folder
def choose_inputfolder():
    window = Tk()
    window.title('Choose a directory')
    Mbox('Choose Folder','Choose a Folder From Which You want to Convert', 0)
    window.withdraw()
    filename = filedialog.askdirectory(initialdir=originalpath) #Goes to the original path
    print(filename)
    path_on_windows = PureWindowsPath(filename)
    call()
    newpath = path_on_windows
    newpath =Path(newpath)
    print(newpath)
    return newpath

if __name__ == '__main__':
    print("Author: Shadman UR Rabbi, \nScript Name: PDFMERGER, \nDescription: This script merges two pdf into one and put them in a folder called Combined. \n"
          "\tThis is specially designed to accomodate the need of Dept of Records and Information Service\n"
          "\tThe two pdf has to have a requirement of a front page and a back page in the same folder\n"
          "\tThe naming convention is front page: '\"'XYZ.pdf'\"' and Back page :'\"'XYZ-bk.pdf'\"' \n",
          "\nPython Version Used: python3.9, Fundamental Packages: os, pathlib, PyPDF2, tkinter(for GUI)\n"
          "Date Modified: 11/6/2020")
    newpath = choose_inputfolder()
    outputfolder = choose_outputfolder()
    fileparse(newpath, outputfolder)
