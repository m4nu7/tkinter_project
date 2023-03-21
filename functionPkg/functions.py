import tkinter as tk
import os
import PyPDF2
import logging as lg

lg.basicConfig(filename="tkinterProject.log", level=lg.INFO, format="%(asctime)s - %(name)s - %(levelname)s %(message)s" )

def searchdir(e1, e2):
    """
    This function searches and lists all the files and folders in a given valid path

    :param e1: entry widget
    :param e2: Text widget
    :return: list of all files and folders in a given valid path
    """
    try:
        lg.info("Searchdir function START ")
        path = e1.get()
        path = path.strip()
        e2.delete("1.0", "end")  # to clear text both every time search button is clicked
        if os.path.isdir(path) or os.path.isfile(path):
            for index in range(len(os.listdir(path))):
                e2.insert(tk.INSERT, str(index) + ". " + os.listdir(path)[index] + "\n")
        else:
            e2.insert(tk.END, "PLEASE ENTER A VALID DIRECTORY NAME")
        lg.info("Inserted all the files and directories to Text widget ")
    except Exception as e:
        lg.error("ERROR OCCURRED in searchdir function !!! ")
        lg.exception(str(e))
        e2.insert(tk.END, str(e))



def pdflistgen(e1, e3):  # generator function to get .pdf files
    """
    This is a generator to get .pdf files in the path specified. Path should be valid.

    :param e1: entry widget
    :param e3: Text widget
    :return: yields .pdf files for iteration
    """
    try:
        lg.info("pdflistgen function START ")
        path = e1.get()
        path = path.strip()
        for file in os.listdir(path):
            if file.endswith(".pdf"):
                yield file
    except Exception as e:
        lg.error("ERROR OCCURRED pdflistgen generator function !!! ")
        lg.exception(str(e))
        e3.delete("1.0", "end")
        e3.insert(tk.INSERT, str(e))


def appendPdf(pdflistgen, e1, e3):
    """
    This function merges .pdf files in a given directory if they exists

    :param pdflistgen: generator to get .pdf files in the path specified. Path should be valid.
    :param e1: entry widget
    :param e3: Text widget
    :return: merged.pdf file after merging pdfs
    """
    try:
        lg.info("appendpdf function START ")
        s = {os.path.splitext(file)[1] for file in pdflistgen(e1, e3)}  # set comprehension to get unique file extensions

        if ".pdf" in s:
            if "merged.pdf" in os.listdir(e1.get().strip()):
                os.remove(os.path.join(e1.get().strip(),"merged.pdf"))
                lg.info("merged.pdf was removed from given directory ")

            pdfMerge = PyPDF2.PdfMerger()

            lg.info("MergeObj created ")

            for fname in pdflistgen(e1, e3):
                lg.info("OPEN file : " + str(fname))
                lg.info("CWD is : " + str(os.getcwd()))
                pdfFileObj = open(os.path.join(e1.get().strip(),fname), "rb")
                lg.info("OPEN EXECUTED!!")
                pdfReader = PyPDF2.PdfReader(pdfFileObj)
                pdfMerge.append(pdfReader)
                pdfFileObj.close()
                lg.info("file CLOSED : " + str(fname))

            pdfMerge.write(os.path.join(e1.get().strip(),"merged.pdf"))
            pdfMerge.close()
            lg.info("merged.pdf was created !!! ")

            e3.delete("1.0", "end")  # to clear text both every time search button is clicked
            e3.insert(tk.INSERT, "pdf Files are merged !!\n Merged pdf file name : merged.pdf ")

        else:
            lg.info("NO pdf in the given directory OR Path Specified is a File OR Path provided is INVALID ")
            e3.delete("1.0", "end")

            e3.insert(tk.INSERT,
                      "No Pdf files in the search path specified !! \n \t \t \t OR \nPath provided is a File !! \
                      \n \t \t \t OR \nPath provided is INVALID !!")

    except Exception as e:
        lg.error("ERROR OCCURRED in appendpdf function !!! ")
        lg.exception(str(e))
        e3.delete("1.0", "end")
        e3.insert(tk.INSERT, str(e))