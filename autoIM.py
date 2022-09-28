from zipfile import ZipFile
import wget
import os
import time
import colorama
from colorama import Fore, Back, Style
colorama.init 

def mainchoice():
    os.system('cls')
    print(''''''+Fore.MAGENTA+'''

  Aerobatics Prestige AutoIM V1.0.0 par Haruku (Open Beta seulement)'''+Fore.RESET+'''

        ['''+Fore.MAGENTA+'''1'''+Fore.RESET+'''] Installer le module Alphajet 2.5.5 par Jetesons

        ['''+Fore.MAGENTA+'''2'''+Fore.RESET+'''] Installer le module Extra330 2.7.2 par VARS

        ['''+Fore.MAGENTA+'''3'''+Fore.RESET+'''] Installer le module T45 1.01 par VNAO

        ['''+Fore.MAGENTA+'''4'''+Fore.RESET+'''] Installer le module Hercules 6.8.2 par Anubis
        
        ['''+Fore.MAGENTA+'''5'''+Fore.RESET+'''] Installer le module UH60-L 1.1 par Kinkku

        ----------------------------------------------------------

        ['''+Fore.MAGENTA+'''6'''+Fore.RESET+'''] Installer tous les modules

        ----------------------------------------------------------

        ['''+Fore.MAGENTA+'''X'''+Fore.RESET+'''] pour quitter
        ''')
    
    a = input('  Entrer votre choix : '+Fore.MAGENTA)
    if a == "1":
        alpha()
    if a == "2":
        extra()
    if a == "3":
        T45()
    if a == "4":
        hercules()
    if a == "5":
        UH60L()
    if a == "6":
        all()
    if a == "x" or "X":
        quit()
    else:
        print(""+Fore.RESET+"  Vous avez choisie une option non disponible.")
        time.sleep(1)
        mainchoice()

def alpha():
    user = os.getlogin()
    path = 'C:\\Users\\' + user + '\\Saved Games\\DCS.openbeta\\'
    url='https://www.dropbox.com/s/0s56ah02nbrqdzi/ModsAlpha.zip?dl=1'
    os.system('cls')
    print(""+Fore.MAGENTA+"\nAlphajet 2.5.5 par Jetesons...\n"+Fore.RESET)
    wget.download(url, out = path)
    print("\n\nInstallation...")
    with ZipFile('C:\\Users\\' + user + '\\Saved Games\\DCS.openbeta\\ModsAlpha.zip', 'r') as zipObj:
        zipObj.extractall(path)
    os.remove('C:\\Users\\' + user + '\\Saved Games\\DCS.openbeta\\ModsAlpha.zip')
    print(""+Fore.GREEN+"\nFini !")
    time.sleep(2)
    mainchoice()

def extra():
    user = os.getlogin()
    path = 'C:\\Users\\' + user + '\\Saved Games\\DCS.openbeta\\'
    url='https://www.dropbox.com/s/40zxw91vlg6ut9v/ModsE330.zip?dl=1'
    os.system('cls')
    print(""+Fore.MAGENTA+"\nExtra330 2.7.2 par VARS\n"+Fore.RESET)
    wget.download(url, out = path)
    print("\n\nInstallation...")
    with ZipFile('C:\\Users\\' + user + '\\Saved Games\\DCS.openbeta\\ModsE330.zip', 'r') as zipObj:
        zipObj.extractall(path)
    os.remove('C:\\Users\\' + user + '\\Saved Games\\DCS.openbeta\\ModsE330.zip')
    print(""+Fore.GREEN+"\nFini !")
    time.sleep(2)
    mainchoice()

def T45():
    user = os.getlogin()
    path = 'C:\\Users\\' + user + '\\Saved Games\\DCS.openbeta\\'
    url='https://www.dropbox.com/s/jklh4bqc82zey90/ModsT45.zip?dl=1'
    os.system('cls')
    print(""+Fore.MAGENTA+"\nT45 1.01 par VNAO\n"+Fore.RESET)
    wget.download(url, out = path)
    print("\n\nInstallation...")
    with ZipFile('C:\\Users\\' + user + '\\Saved Games\\DCS.openbeta\\ModsT45.zip', 'r') as zipObj:
        zipObj.extractall(path)
    os.remove('C:\\Users\\' + user + '\\Saved Games\\DCS.openbeta\\ModsT45.zip')
    print(""+Fore.GREEN+"\nFini !")
    time.sleep(2)
    mainchoice()

def hercules():
    user = os.getlogin()
    path = 'C:\\Users\\' + user + '\\Saved Games\\DCS.openbeta\\'
    url='https://www.dropbox.com/s/aw0b0a8onqoygzh/ModsHercules.zip?dl=1'
    os.system('cls')
    print(""+Fore.MAGENTA+"\nHercules 6.8.2 par Anubis\n"+Fore.RESET)
    wget.download(url, out = path)
    print("\n\nInstallation...")
    with ZipFile('C:\\Users\\' + user + '\\Saved Games\\DCS.openbeta\\ModsHercules.zip', 'r') as zipObj:
        zipObj.extractall(path)
    os.remove('C:\\Users\\' + user + '\\Saved Games\\DCS.openbeta\\ModsHercules.zip')
    print(""+Fore.GREEN+"\nFini !")
    time.sleep(2)
    mainchoice()

def UH60L():
    user = os.getlogin()
    path = 'C:\\Users\\' + user + '\\Saved Games\\DCS.openbeta\\'
    url='https://www.dropbox.com/s/0cjhc5gp1fo0v3l/ModsUH60L.zip?dl=1'
    os.system('cls')
    print(""+Fore.MAGENTA+"\nUH60-L 1.1 par Kinkku...\n"+Fore.RESET)
    wget.download(url, out = path)
    print("\n\nInstallation...")
    with ZipFile('C:\\Users\\' + user + '\\Saved Games\\DCS.openbeta\\ModsUH60L.zip', 'r') as zipObj:
        zipObj.extractall(path)
    os.remove('C:\\Users\\' + user + '\\Saved Games\\DCS.openbeta\\ModsUH60L.zip')
    print(""+Fore.GREEN+"\nFini !")
    time.sleep(2)
    mainchoice()

def all():
    user = os.getlogin()
    path = 'C:\\Users\\' + user + '\\Saved Games\\DCS.openbeta\\'
    os.system('cls')

    print(""+Fore.MAGENTA+"\nAlphajet 2.5.5 par Jetesons...\n"+Fore.RESET)
    wget.download('https://www.dropbox.com/s/0s56ah02nbrqdzi/ModsAlpha.zip?dl=1', out = path)
    print("\n\nInstallation...")
    with ZipFile('C:\\Users\\' + user + '\\Saved Games\\DCS.openbeta\\ModsAlpha.zip', 'r') as zipObj:
        zipObj.extractall(path)
    os.remove('C:\\Users\\' + user + '\\Saved Games\\DCS.openbeta\\ModsAlpha.zip')
    print(""+Fore.GREEN+"\nFini !")

    print(""+Fore.MAGENTA+"\nExtra330 2.7.2 par VARS\n"+Fore.RESET)
    wget.download('https://www.dropbox.com/s/40zxw91vlg6ut9v/ModsE330.zip?dl=1', out = path)
    print("\n\nInstallation...")
    with ZipFile('C:\\Users\\' + user + '\\Saved Games\\DCS.openbeta\\ModsE330.zip', 'r') as zipObj:
        zipObj.extractall(path)
    os.remove('C:\\Users\\' + user + '\\Saved Games\\DCS.openbeta\\ModsE330.zip')
    print(""+Fore.GREEN+"\nFini !")

    print(""+Fore.MAGENTA+"\nT45 1.01 par VNAO\n"+Fore.RESET)
    wget.download('https://www.dropbox.com/s/jklh4bqc82zey90/ModsT45.zip?dl=1', out = path)
    print("\n\nInstallation...")
    with ZipFile('C:\\Users\\' + user + '\\Saved Games\\DCS.openbeta\\ModsT45.zip', 'r') as zipObj:
        zipObj.extractall(path)
    os.remove('C:\\Users\\' + user + '\\Saved Games\\DCS.openbeta\\ModsT45.zip')
    print(""+Fore.GREEN+"\nFini !")

    print(""+Fore.MAGENTA+"\nHercules 6.8.2 par Anubis\n"+Fore.RESET)
    wget.download('https://www.dropbox.com/s/aw0b0a8onqoygzh/ModsHercules.zip?dl=1', out = path)
    print("\n\nInstallation...")
    with ZipFile('C:\\Users\\' + user + '\\Saved Games\\DCS.openbeta\\ModsHercules.zip', 'r') as zipObj:
        zipObj.extractall(path)
    os.remove('C:\\Users\\' + user + '\\Saved Games\\DCS.openbeta\\ModsHercules.zip')
    print(""+Fore.GREEN+"\nFini !")

    print(""+Fore.MAGENTA+"\nUH60-L 1.1 par Kinkku...\n"+Fore.RESET)
    wget.download('https://www.dropbox.com/s/0cjhc5gp1fo0v3l/ModsUH60L.zip?dl=1', out = path)
    print("\n\nInstallation...")
    with ZipFile('C:\\Users\\' + user + '\\Saved Games\\DCS.openbeta\\ModsUH60L.zip', 'r') as zipObj:
        zipObj.extractall(path)
    os.remove('C:\\Users\\' + user + '\\Saved Games\\DCS.openbeta\\ModsUH60L.zip')
    print(""+Fore.GREEN+"\nFini !")

    time.sleep(2)
    mainchoice()



if __name__ == "__main__":
    mainchoice()
