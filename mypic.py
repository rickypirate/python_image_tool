#-*- coding:utf-8 -*-
import sys
import os
from PIL import Image
def picture(mydir):
        
        myDirname = os.path.dirname(mydir)
        myBasename = os.path.basename(mydir)
        myNewdir  = os.path.join(myDirname,myBasename+' copy')
        os.mkdir(myNewdir)
        
        def nextdir(mydir,myNewdir):        
                nextList = os.listdir(mydir)
                for myFile in nextList:
                        if os.path.isfile(os.path.join(mydir,myFile)):
                        
                                image = Image.open(os.path.join(mydir,myFile))
                                out = image.resize((720,450),Image.ANTIALIAS)
                                out.save(os.path.join(myNewdir,myFile))
                        if os.path.isdir(os.path.join(mydir,myFile)):
                        
                                newCreateddir = os.path.join(mydir,myFile)
                                myNewdir  = os.path.join(myNewdir,myFile)
                                os.mkdir(myNewdir)
                                nextdir(newCreateddir,myNewdir)
        nextdir(mydir,myNewdir)

if __name__ =="__main__":
	mydir = sys.argv[1]
	picture(mydir)
	print "successful！！！"
