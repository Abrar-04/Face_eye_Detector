import tkinter as tk
import tkinter.messagebox
import numpy as np
import cv2
import matplotlib.pyplot as plt

root = tk.Tk()


#window ka title name rakhre appan yaaper!
root.title("Face_Eye_Detector")

#window ka size set karre aur tum resize nai karsakna 
#bolke cuz buttons ki gicchi hoti naito phir!!
root.geometry("500x500")
root.resizable(0,0)


#giving color to the background 
root.configure(bg='black')

def box():

	#paste your program here (in this function) so that It will run when you click the button!!
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


#create button wid som colors and shet,  
#!!!!!!!!command bolto the function which gets called when you click the button!!!!!!!
b=tk.Button(root,text="Click Me UwU!!",height=5,width=15,font=('cooperblack',10,'bold'),bg='MediumPurple3',fg='white',command=sTfU)

#self explanatory shet (-_-)... still... we placin the buton and anchorin kinda..
b.place(relx=0.5,rely=0.5,anchor='c')



tk.mainloop()