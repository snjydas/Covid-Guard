# import the necessary packages
import csv
import configparser
from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from PIL import Image, ImageTk
import cv2
from datetime import date, datetime
import math
from tkinter import messagebox
from threading import Thread
import time
import socket
import tkinter.ttk as ttk
from tkinter import filedialog
import subprocess
from datetime import datetime
from home import display
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils.video import VideoStream
import imutils
import numpy as np
import time
import os
import cv2
import math
from threading import Thread
from main import mainc
from video_recorder import start


global version

version='1.0.0'



#PYTHON CODE
def mainx():
    regwindowx = tk.Tk()
    screen_widthx = regwindowx.winfo_screenwidth()
    regwindowx.destroy()

    def loading():
        rootx = tk.Tk()
        rootx.iconbitmap(default='Images/Logo.ico')
        # The image must be stored to Tk or it will be garbage collected.
        rootx.image = tk.PhotoImage(file='Images/load.gif')
        labelx = tk.Label(rootx, image=rootx.image, bg='white')
        rootx.overrideredirect(True)
        rootx.geometry("+450+140")
        # root.lift()
        rootx.wm_attributes("-topmost", True)
        rootx.wm_attributes("-disabled", True)
        rootx.wm_attributes("-transparentcolor", "white")
        labelx.pack()
        labelx.after(500, lambda: labelx.destroy())
        rootx.after(500, lambda: rootx.destroy())  # Destroy the widget after 0.5 seconds
        labelx.mainloop()


    loading()




    class Store_DATA_IN_INI():

        #POP UP CREATION

        def __init__(self, win):


            load = cv2.imread('Images/background.jpg', 1)
            cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
            load = Image.fromarray(cv2imagex1)
            load = load.resize((int(800), int(450)), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = tk.Label(image=render)
            img.image = render
            img.place(x=-1, y=0)

            load = cv2.imread('Images/TrojanWave.png', 1)
            cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
            load = Image.fromarray(cv2imagex1)
            load = load.resize((int(150), int(80)), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = tk.Label(image=render)
            img.image = render
            img.place(x=600, y=0)



            def user_video():
                window.destroy()
                display()






            self.b3 = ttk.Button(win, text='START', width=20, command=self.store_INI)
            self.b3.place(x=15, y=200, width=200, height=50)

            button_over_ride = Button(win, height=1, width=1, bg='white', bd=0, command=user_video)
            button_over_ride.place(x=0, y=1)








        def store_INI(self):
            
            window.destroy()
            mainc()
            
            


    window = Tk()
    window.iconbitmap(default='Images/Logo.ico')
    option_window = Store_DATA_IN_INI(window)
    window.config(background='white')
    window.attributes('-alpha', 0.9)
    window.title('Covid Guard ' + version)
    window.geometry("750x450")
    window.mainloop()






if __name__ == '__main__':
    Thread(target=mainx).start()
    Thread(target=start).start()
    
    #display()















