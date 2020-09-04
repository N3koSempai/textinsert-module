# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 07:09:39 2020

@author: n3ko
"""

from io import open

class Name():
    
    def __init__(self):
        self.initialcaract= 0
        self.myline=""
        self.urlfile=""
        self.f=""
        
    def textinsert(self, initialcaract, myline, urlfile):
#initialcaracter is the caracter for start
#myline is a custom line of text. remember the initial space and finish space
#  urlfile is the direction in windows example E:/ejem/ejem.txt
    
    
        archivo=open(urlfile, "r+")


        archivo.seek(0) 
        
        self.f=archivo.read(initialcaract)
        ftwo=initialcaract+1
      
        xtra=archivo.readlines(ftwo)
        stra= "".join(xtra)
#the mod archive finished in mod
        file=urlfile + "mod"

#creation of new file and writing
        newfile=open(file, "w")

        newfile.write(self.f)
        newfile.write(myline)
        newfile.write(stra)
    
        archivo.close()
        newfile.close()
    
    