import tkinter as tk
from tkinter import *
import numpy as np
import cv2
import matplotlib.pyplot as plt

root = tk.Tk()
root.title("Face_Eye_Detector")
root.geometry("500x500")
root.resizable(0,0)
root.configure(bg='black')
T = Text(root, height=2, width=18,font=("Comic Sans MS", 32),bg='khaki') 
T.pack() 
T.insert(END, 'Face_Eye_Detector')

def box():

    face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')
    
    
    def detect_human(img):
        face_img=img.copy()
        face_rect=face_cascade.detectMultiScale(face_img)
        face_img=img.copy()
        eyes_rect=eye_cascade.detectMultiScale(face_img,scaleFactor=1.15,minNeighbors=7)
    
        for (x,y,w,h) in face_rect:
            cv2.rectangle(face_img,(x,y),(x+w,y+h),(0,255,255),10)
        
        for (x,y,w,h) in eyes_rect:
            cv2.rectangle(face_img,(x,y),(x+w,y+h),(255,0,255),10)

        return face_img
    
    
    cap=cv2.VideoCapture(0)

    while True:
        ret,frame=cap.read(0)
        frame=detect_human(frame)  
    
        cv2.imshow("Detector",frame)
    
        k=cv2.waitKey(1)
        if k==27:
            break

    cap.release()
    cv2.destroyAllWindows()


    f = tk.Tk()
    f.geometry("500x500")
    f.title("Loading")
    tkinter.messagebox.showinfo("Ok")
    f.mainloop()


b=tk.Button(root,text="Detect",height=5,width=15,font=('Comic Sans MS',25,'bold'),bg='DarkOrchid3',fg='Yellow',command=box)
b.place(relx=0.5,rely=0.5,anchor='c')
tk.mainloop()
