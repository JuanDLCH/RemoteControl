import socket
from tkinter import *
import subprocess

root = Tk()
root.title("Remote Control")
root.geometry("300x200")
root.resizable(0, 0)
root.eval('tk::PlaceWindow . center')
s : subprocess.Popen = None

title = Label(root, text="Remote Control - Juandy", font=("Helvetica", 16))
ip = Label(root, text="IP:", font=("Helvetica", 12))
running = Label(root, text="Servicio detenido", font=("Helvetica", 12))
btnStart = Button(root, text="Start", font=("Helvetica", 12), command=lambda: start())
btnStop = Button(root, text="Stop", font=("Helvetica", 12), command=lambda: stop())

title.place(relx=0.5, rely=0.1, anchor=CENTER)
ip.place(relx=0.5, rely=0.3, anchor=CENTER)
running.place(relx=0.5, rely=0.5, anchor=CENTER)
btnStart.place(relx=0.4, rely=0.7, anchor=CENTER)
btnStop.place(relx=0.6, rely=0.7, anchor=CENTER)

def start():
    global s
    running.config(text="Servicio iniciado", fg="green")
    ip.config(text="IP: " + socket.gethostbyname(socket.gethostname()) + ':8000', fg="blue", font=("Helvetica", 12, "bold"))
    btnStart.config(state=DISABLED)
    btnStop.config(state=NORMAL)    
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    s = subprocess.Popen(["python3", "server.py"], startupinfo=startupinfo)

def stop():
    running.config(text="Servicio detenido", fg="red")
    ip.config(text="IP:", fg="black" , font=("Helvetica", 12))
    btnStart.config(state=NORMAL)
    btnStop.config(state=DISABLED)
    s.kill()

def on_closing():
    if s != None:
        s.kill()
    root.destroy()

def hola():
    print("Hola")


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
