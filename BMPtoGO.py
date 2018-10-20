import os
import os.path
from tkinter import Tk
from tkinter import StringVar
from tkinter import Label
from tkinter import Entry
from tkinter import Button
import tkinter.messagebox
from tkinter.filedialog import askdirectory
from PIL import Image   #PIL引用须放在tkinter之后


def convert():
    '''
    def is_img(ext):
        ext = ext.lower()
        if ext in ['.jpg', 'png', 'jpeg', 'bmp']:
            return Ture
        else :
            return False
    '''
    
    def selectPath():
        global path_
        path_ = askdirectory()
        path.set(path_)

        print(path_)
        return path_

    def bmp_to_jpg():
        rootdir = path_     #获取文件夹路径
        
        for root, dirnames, filenames in os.walk(rootdir):

            for filename in filenames:
                    
                    
                newFileName = filename.split('.')[0] + ".jpg"  # 重命名
                
                print("filename is:" + newFileName)  # 输出新文件名
                     
                im = Image.open(rootdir + "/" + filename)   #打开图片文件
                 
                im.save(rootdir + "/" + newFileName)    #另存为.jpg文件
                    
                
                

    root = Tk()
    path = StringVar()

    Label(root, text="目标路径:").grid(row=0, column=0)
    Entry(root, textvariable=path).grid(row=0, column=1)
    Button(root, text="路径选择", command=selectPath).grid(row=0, column=2)
    Button(root, text="转换", command=bmp_to_jpg).grid(row=0, column=3)

if __name__ == '__main__':
    convert()

