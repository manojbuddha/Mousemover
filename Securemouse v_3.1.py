try:
 from Tkinter import *
 import tkMessageBox
 import Tkinter
 import time
 import random
 import win32api, win32con
 import threading
 import base64
 import getpass
 import os
 import sys
 import win32gui
 import ast


except ModuleNotFoundError:
 from tkinter import *
 #import tkMessageBox
 import time
 import random
 import win32api, win32con
 import threading
 import base64
 import getpass
 import os
 import sys
 import win32gui
 import ast
 
"""
version 2   - GUI
version 2.3 - support threading for button depress issue
version 3   - support keystroke simulation and randomness into events
version 3.1 - Check box to enable/disable keystroke simulation

Troubleshooting thread:

print(threading.currentThread().getName())
print(threading.active_count())
print(threading.currentThread().getName())
"""

The_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(The_program_to_hide , win32con.SW_HIDE)


colors = ['red', 'green', 'blue', 'yellow', 'orange', 'white', 'cyan', 'purple']
Flag=True
Flag1="False"
time1=5

def Scanning():
       global Flag
       return Flag


def Timer():
  global time1
  Flag=Scanning()
  if Flag==True:
    sec=0
     
    t0=time.time()
    time1=frequency.get()
    if time1 is not "Random":
           time1=time1.split()[0]
    if time1=="Random":
           time1=int(random.randint(1,40))

    time1=int(time1)
    while sec<=time1:
        t1=time.time()
        sec=t1-t0
    mouse()

def mouse():
     global time1
     r1=random.randint(1,1001)
     r2=random.randint(1,1001)
     rc=random.randint(0,6)  
     lbl4.config(fg=str(colors[rc]), text=str(r1)+" "*2+str(r2)+" "*2+str(time1))
     win32api.SetCursorPos((10,10))
     win32api.SetCursorPos((10+r1,10+r2))
     print(keycheck_var.get(),type(keycheck_var.get()))
     if bool(keycheck_var.get()):
       for i in range(0,5):
         k=int(random.randint(65,90))
         k=65
         print(k)
         win32api.keybd_event(k,0,0,0)
         win32api.keybd_event(k,0,win32con.KEYEVENTF_KEYUP,0)
     Timer()
     

def startthread():

          lbl3.config(fg="green", text="Application running")
          window.title("MC-ready")
          lbl3.pack
          global Flag
          Flag=True
          threadcount=threading.active_count()
          threadcount=int(threadcount)
          if threadcount==1:
               x=threading.Thread(target=Timer)     
               x.start()
          else:
               print("I blocked a duplicate thread")
          print(threading.currentThread().getName())

def stopthread():

      global Flag    
      Flag=False
      print(bool(keycheck_var.get()))
      lbl3.config(fg="red", text="App stopped, press start button to start the application")
      window.title("MC-Not ready")
      print(threading.currentThread().getName())
      lbl3.pack()


def passcheck():
    global counter
    global Flag1
    try:
      password= base64.b64encode(e1.get())
    except (NameError,TypeError):
      print("inside except")
      password= base64.b64encode(e1.get().encode("utf-8"))
      password=password.decode("utf-8")
      print(password)
    if password=="SGVsbG90aGVyZQ==":
                Flag1="True"
                window_login.destroy()

              
    else:
 
                counter+=1
                if counter==3:
                    print("removing app data .....")
                    window_login.destroy()
                    os.remove(sys.argv[0])  
                    time.sleep(3)
                    raise Exception("Bye bye, you got me deleted..")
                    time.sleep(3)
                lbl2.config(fg="red", text="Re-enter password only "+str(3-counter)+" attempts left")


counter=0
window_login=Tk()

window_login.title("Secure Login")
login_button=Button(window_login, text="Enter",command=passcheck)

lbl1=Label(window_login, text="Password")
e1=Entry(window_login, show="*")

lbl2=Label(window_login, text="Welcome to the Secure mouse 3.0!!")

lbl1.pack()
e1.pack()
login_button.pack()
lbl2.pack()

window_login.mainloop()
    
print(threading.active_count())
print(threading.currentThread().getName())

if Flag1=="True":

    window=Tk()
    keycheck_var=IntVar()
    window.geometry("278x165")
    options=["5 sec","10 sec","20 sec","30 sec","60 sec","Random"]
    
    frequency=StringVar(window)
    frequency.set(options[2])
    drop=OptionMenu(window, frequency, *options)
    window.title("Magic mouse")
    start_button=Button(window, text="Start", command=startthread)
    pause_button=Button(window, text="Pause", command=stopthread)

    key_check=Checkbutton(window,text="Enable keystrokes", variable=keycheck_var, onvalue = True, offvalue = False, height=5,width = 20)

    lbl5=Label(window, text="frequency")
    lbl3=Label(window, text="Press start button to start the application")
    lbl4=Label(window, text="Co-ordinates here")
    lbl3.pack()
    lbl5.pack() 

    drop.pack()
    start_button.pack()
    pause_button.pack()
    lbl4.pack()

    key_check.pack()
    window.resizable(False,False)
    window.mainloop()
     

