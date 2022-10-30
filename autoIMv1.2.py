from calendar import c
from ensurepip import version
from tkinter import *
from tkinter import ttk
from turtle import back
from PIL import ImageTk, Image
from pyparsing import col
from tkinter import filedialog
import os
from zipfile import ZipFile
import wget
import tkinter
import webbrowser
import threading
import sys

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

buttonc = 0

def clicked():
    global buttonc
    buttonc = 1
    return buttonc

def dir():
    global path
    if buttonc == 0:
        path = 'C:\\Users\\' + os.getlogin() + '\\Saved Games\\'
    else:
        path = directory + "/"
    return path

window = Tk()
window.title('Aerobatics Prestige DCS AutoIM v1.2.0 par Haruku')
window.geometry("800x400")
window.resizable(False, False)
logoicopath = resource_path("logo.ico")
window.iconbitmap(logoicopath)
window.config(background='#262626')
themeazuretclpath = resource_path("azure.tcl")
window.tk.call("source", themeazuretclpath)
theme = resource_path("theme")
window.tk.call("set_theme", "dark")

class main():
    def __init__(self):
        pass

    backround = ttk.Frame(window)
    backround.pack(fill="both", expand=True)


    mainframe = ttk.Frame(window, width=800, height=110)
    style = Frame(backround, bg="#262626", width=780, height=240)

    imgpath = resource_path("logos.png")
    image = Image.open(imgpath)
    img = image.resize((100, 100))
    imgtk = ImageTk.PhotoImage(img)
    imgwidget = Label(window, image=imgtk, bd=0)
    imgwidget.place(x=190, y=15)

    textpre = ttk.Label(mainframe, text="    Aerobatics Prestige DCS AutoIM v1.2.0 par Haruku\n    Programme d'installation automatique de mods pour\n    DCS World. Contactez le discord de la VAP si problème.")
    textpre.place(x=200, y=35)

    infobar = ttk.Label(backround, text="V1.2.0 - Problèmes/Bugs -> GitHub/Discord")
    infobar.place(x=525, y=370)

    mainframe.place(x=80, y=0)
    style.place(x=10, y=125)

    textealpha = ttk.Label(style, text="Alphajet 2.5.5 \npar Jetesons ")
    textealpha.place(x=110, y=65)

    textealpha = ttk.Label(style, text="Extra330 2.7.2\npar VARS")
    textealpha.place(x=110, y=125)

    textealpha = ttk.Label(style, text="T45 1.01     \npar VNAO     ")
    textealpha.place(x=110, y=185)

    textealpha = ttk.Label(style, text="UH60-L 1.1    \npar Kinkku")
    textealpha.place(x=350, y=65)

    textealpha = ttk.Label(style, text="Hercules 6.8.2\npar Anubis")
    textealpha.place(x=350, y=125)

    global switch
    global var
    var = tkinter.IntVar()
    switch = ttk.Checkbutton(window, text = "Stable", style='Switch.TCheckbutton', variable=var)
    switch.place(x=690 , y=135)
    fs = ttk.Frame(window, height=28, width=65)
    fs.place(x=625, y=135)
    stexte = ttk.Label(window, text="Open Beta")
    stexte.place(x=625, y=138)

    global browsetext
    browsetext = ttk.Label(window,text='C:/Users/' + os.getlogin() + '/Saved Games')
    browsetext.place(x=255, y=140)

    def browseDirectory():
        global directory
        directory = filedialog.askdirectory()
        browsetext.configure(text=directory)
        clicked()
            
    button_explore = ttk.Button(window, text = "Parcourir répertoire Saved Games :", command=browseDirectory)
    button_explore.place(x=20, y=135)
    global versions
    versions = 'DCS.openbeta'

def hercules():
    if var.get() == 0:
        versions = 'DCS.openbeta'
        print(versions)
    elif var.get() == 1:
        versions = 'DCS World'
        print(versions)
    else:
        print(var.get())
        print("probleme")
    button_hercules.configure(text="...")
    print("\n\n" + str(dir()) + "\n\n" + versions + '/')
    url='https://www.dropbox.com/s/aw0b0a8onqoygzh/ModsHercules.zip?dl=1'
    print("\nHercules 6.8.2 par Anubis\n")
    def dlinh():
        statusdll.configure(text="Téléchargement... Hercules 6.8.2 par Anubis")
        window.update()
        wget.download(url, out = str(dir()) + versions + '/')
        statusdll.configure(text="Installation... Hercules 6.8.2 par Anubis")
        window.update()
        with ZipFile(str(dir()) + versions + '/' 'ModsHercules.zip', 'r') as zipObj:
            zipObj.extractall(str(dir()) + versions + '/')
        os.remove(str(dir()) + versions + '/' + 'ModsHercules.zip')
        button_hercules.configure(text="Fini !") 
        statusdll.configure(text="Idle")

    dlinht = threading.Thread(target=dlinh)
    dlinht.start()


def alpha():
    if var.get() == 0:
        versions = 'DCS.openbeta'
        print(versions)
    elif var.get() == 1:
        versions = 'DCS World'
        print(versions)
    else:
        print(var.get())
        print("probleme")
    button_alpha.configure(text="...")
    print("\n\n" + str(dir()) + "\n\n" + versions + '/')
    url='https://www.dropbox.com/s/0s56ah02nbrqdzi/ModsAlpha.zip?dl=1'
    print("\nAlphajet 2.5.5 par Jetesons...\n")
    def dlina():
        statusdll.configure(text="Téléchargement... Alphajet 2.5.5 par Jetesons")
        window.update()
        wget.download(url, out = str(dir()) + versions + '/')
        statusdll.configure(text="Installation... Alphajet 2.5.5 par Jetesons")
        window.update()
        with ZipFile(str(dir()) + versions + '/' 'ModsAlpha.zip', 'r') as zipObj:
            zipObj.extractall(str(dir()) + versions + '/')
        os.remove(str(dir()) + versions + '/' + 'ModsAlpha.zip')
        button_alpha.configure(text="Fini !")
        statusdll.configure(text="Idle")

    dlinat = threading.Thread(target=dlina)
    dlinat.start()

def extra():
    if var.get() == 0:
        versions = 'DCS.openbeta'
        print(versions)
    elif var.get() == 1:
        versions = 'DCS World'
        print(versions)
    else:
        print(var.get())
        print("probleme")
    button_extra.configure(text="...")
    print("\n\n" + str(dir()) + "\n\n" + versions + '/')
    url='https://www.dropbox.com/s/40zxw91vlg6ut9v/ModsE330.zip?dl=1'
    print("\nExtra330 2.7.2 par VARS\n")
    def dline():
        statusdll.configure(text="Téléchargement... Extra330 2.7.2 par VARS")
        window.update()
        wget.download(url, out = str(dir()) + versions + '/')
        statusdll.configure(text="Installation... Extra330 2.7.2 par VARS")
        window.update()
        with ZipFile(str(dir()) + versions + '/' 'ModsE330.zip', 'r') as zipObj:
            zipObj.extractall(str(dir()) + versions + '/')
        os.remove(str(dir()) + versions + '/' + 'ModsE330.zip')
        button_extra.configure(text="Fini !")
        statusdll.configure(text="Idle")
    
    dlinet = threading.Thread(target=dline)
    dlinet.start()

def T45():
    if var.get() == 0:
        versions = 'DCS.openbeta'
        print(versions)
    elif var.get() == 1:
        versions = 'DCS World'
        print(versions)
    else:
        print(var.get())
        print("probleme")
    button_T45.configure(text="...")
    print("\n\n" + str(dir()) + "\n\n" + versions + '/')
    url='https://www.dropbox.com/s/jklh4bqc82zey90/ModsT45.zip?dl=1'
    print("\nT45 1.01 par VNAO\n")
    def dlint():
        statusdll.configure(text="Téléchargement... T45 1.01 par VNAO")
        window.update()
        wget.download(url, out = str(dir()) + versions + '/')
        statusdll.configure(text="Installation... T45 1.01 par VNAO")
        window.update()
        with ZipFile(str(dir()) + versions + '/' 'ModsT45.zip', 'r') as zipObj:
            zipObj.extractall(str(dir()) + versions + '/')
        os.remove(str(dir()) + versions + '/' + 'ModsT45.zip')
        button_T45.configure(text="Fini !")
        statusdll.configure(text="Idle")

    dlintt = threading.Thread(target=dlint)
    dlintt.start()

def UH60L():
    if var.get() == 0:
        versions = 'DCS.openbeta'
        print(versions)
    elif var.get() == 1:
        versions = 'DCS World'
        print(versions)
    else:
        print(var.get())
        print("probleme")
    button_UH60L.configure(text="...")
    print("\n\n" + str(dir()) + "\n\n" + versions + '/')
    url='https://www.dropbox.com/s/0cjhc5gp1fo0v3l/ModsUH60L.zip?dl=1'
    print("\nUH60-L 1.1 par Kinkku...\n")
    def dlinu():
        statusdll.configure(text="Téléchargement... UH60-L 1.1 par Kinkku")
        window.update()
        wget.download(url, out = str(dir()) + versions + '/')
        statusdll.configure(text="Installation... UH60-L 1.1 par Kinkku")
        window.update()
        with ZipFile(str(dir()) + versions + '/' 'ModsUH60L.zip', 'r') as zipObj:
            zipObj.extractall(str(dir()) + versions + '/')
        os.remove(str(dir()) + versions + '/' + 'ModsUH60L.zip')
        button_UH60L.configure(text="Fini !")
        statusdll.configure(text="Idle")
    
    dlinut = threading.Thread(target=dlinu)
    dlinut.start()

def all():
    window.update()
    alpha()
    window.update()
    extra()
    window.update()
    T45()
    window.update()
    UH60L()
    window.update()
    hercules()
    window.update()

def opendiscord():
    webbrowser.open("https://discord.gg/PVY3wqYtBS")
def opengithub():
    webbrowser.open("https://github.com/HarukuCode")


global button_alpha
button_alpha = ttk.Button(window, text = "Installer :", command = alpha)
button_alpha.place(x=20, y=190)

global button_extra
button_extra = ttk.Button(window, text = "Installer :", command = extra)
button_extra.place(x=20, y=250)

global button_T45
button_T45 = ttk.Button(window, text = "Installer :", command = T45)
button_T45.place(x=20, y=310)

global button_UH60L
button_UH60L = ttk.Button(window, text = "Installer :", command = UH60L)
button_UH60L.place(x=260, y=190)

global button_hercules
button_hercules = ttk.Button(window, text = "Installer :", command = hercules)
button_hercules.place(x=260, y=250)

global button_all
button_all = ttk.Button(window, text = "  Cliquez pour tout installer ", command = all)
button_all.place(x=260, y=310)



global button_discord
button_discord = ttk.Button(window, text = "Discord", command = opendiscord)
button_discord.place(x=685, y=250)
global button_github
button_github = ttk.Button(window, text = "Github ", command = opengithub)
button_github.place(x=685, y=310) 

global statusdl
statusdl = tkinter.Label(window, text="Status :")
statusdl.place(x=10, y=370)

global statusdll
statusdll = tkinter.Label(window, text="Idle")
statusdll.place(x=58, y=370)

window.mainloop()

main()