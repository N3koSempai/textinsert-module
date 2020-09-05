# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 07:09:39 2020

@author: N3koSempai
"""

from io import open



def textinsert(initialcaract, myline, urlfile):
    """initialcaracter is the caracter for start.
myline is your custom line of text you need add in the midle of text file.
remember the initial space and finish space.
urlfile is the direction in windows example E:/ejem/ejem.txt
this funtion create a second file whit mod after normal name"""


    archivo = open(urlfile, "r")


    archivo.seek(0)

    first = archivo.read(initialcaract)

    xtra = archivo.read()
    stra = "".join(xtra)
#the mod archive finished in mod
    file = urlfile + "mod"

#creation of new file and writing
    newfile = open(file, "w")

    newfile.write(first)
    newfile.write(myline)
    newfile.write(stra)

    archivo.close()
    newfile.close()
