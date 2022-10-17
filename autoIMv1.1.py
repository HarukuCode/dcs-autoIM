from zipfile import ZipFile
import wget
import os
import time
import colorama
from colorama import Fore, Back, Style
colorama.init 

def main():
    os.system('cls')
    choixversion = input('Quel est la version de votre DCS ? ('+Fore.MAGENTA+'['+Fore.YELLOW+'1a'+Fore.MAGENTA+'] Stable (DCS)'+Fore.RESET+' / '+Fore.MAGENTA+'['+Fore.YELLOW+'1b'+Fore.MAGENTA+'] Stable (DCS World)'+Fore.RESET+' / '+Fore.MAGENTA+'['+Fore.YELLOW+'2'+Fore.MAGENTA+'] Open Beta (DCS.openbeta)'+Fore.RESET+') : ')
    if choixversion == '1a':
        version = 'DCS'
    elif choixversion == '1b':
        version = 'DCS World'
    elif choixversion == '2':
        version = 'DCS.openbeta'
    else:
        os.system('cls')
        print('Veuillez choisir "'+Fore.MAGENTA+'1a'+Fore.RESET+'", "'+Fore.MAGENTA+'1b'+Fore.RESET+'" ou "'+Fore.MAGENTA+'2'+Fore.RESET+'".')
        time.sleep(2)
        os.system('cls')
        main()
    
    os.system('cls')
    choixsavedgames = input('Quel est le chemin d\'accès de votre "Saved Games" / "Parties enregistrées" ('+Fore.MAGENTA+'laisser vide si inchangé'+Fore.RESET+') \nExemple : '+Fore.MAGENTA+'C:\\Users\\user\\Saved Games'+Fore.RESET+' : ')
    if choixsavedgames == '' or ' ':
        savedgames = 'C:\\Users\\' + os.getlogin() + '\\Saved Games\\'
        
    else:
        savedgames = choixsavedgames + '\\'
        

    def mainchoice():
        os.system('cls')
        print(''''''+Fore.MAGENTA+'''

      Aerobatics Prestige AutoIM V1.1.0 par Haruku'''+Fore.RESET+'''

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
        print(' \n  Chemin d\'installation : ' + savedgames + version + '\\')
    
        a = input('\n  Entrer votre choix : '+Fore.MAGENTA)
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
        path = savedgames + version + '\\'
        url='https://www.dropbox.com/s/0s56ah02nbrqdzi/ModsAlpha.zip?dl=1'
        os.system('cls')
        print(""+Fore.MAGENTA+"\nAlphajet 2.5.5 par Jetesons...\n"+Fore.RESET)
        wget.download(url, out = path)
        print("\n\nInstallation...")
        with ZipFile(path + 'ModsAlpha.zip', 'r') as zipObj:
            zipObj.extractall(path)
        os.remove(path + 'ModsAlpha.zip')
        print(""+Fore.GREEN+"\nFini !")
        time.sleep(2)
        mainchoice()

    def extra():
        path = savedgames + version + '\\'
        url='https://www.dropbox.com/s/40zxw91vlg6ut9v/ModsE330.zip?dl=1'
        os.system('cls')
        print(""+Fore.MAGENTA+"\nExtra330 2.7.2 par VARS\n"+Fore.RESET)
        wget.download(url, out = path)
        print("\n\nInstallation...")
        with ZipFile(path + 'ModsE330.zip', 'r') as zipObj:
            zipObj.extractall(path)
        os.remove(path + 'ModsE330.zip')
        print(""+Fore.GREEN+"\nFini !")
        time.sleep(2)
        mainchoice()

    def T45():
        path = savedgames + version + '\\'
        url='https://www.dropbox.com/s/jklh4bqc82zey90/ModsT45.zip?dl=1'
        os.system('cls')
        print(""+Fore.MAGENTA+"\nT45 1.01 par VNAO\n"+Fore.RESET)
        wget.download(url, out = path)
        print("\n\nInstallation...")
        with ZipFile(path + 'ModsT45.zip', 'r') as zipObj:
            zipObj.extractall(path)
        os.remove(path + 'ModsT45.zip')
        print(""+Fore.GREEN+"\nFini !")
        time.sleep(2)
        mainchoice()

    def hercules():
        path = savedgames + version + '\\'
        url='https://www.dropbox.com/s/aw0b0a8onqoygzh/ModsHercules.zip?dl=1'
        os.system('cls')
        print(""+Fore.MAGENTA+"\nHercules 6.8.2 par Anubis\n"+Fore.RESET)
        wget.download(url, out = path)
        print("\n\nInstallation...")
        with ZipFile(path + 'ModsHercules.zip', 'r') as zipObj:
            zipObj.extractall(path)
        os.remove(path + 'ModsHercules.zip')
        print(""+Fore.GREEN+"\nFini !")
        time.sleep(2)
        mainchoice()

    def UH60L():
        path = savedgames + version + '\\'
        url='https://www.dropbox.com/s/0cjhc5gp1fo0v3l/ModsUH60L.zip?dl=1'
        os.system('cls')
        print(""+Fore.MAGENTA+"\nUH60-L 1.1 par Kinkku...\n"+Fore.RESET)
        wget.download(url, out = path)
        print("\n\nInstallation...")
        with ZipFile(path + 'ModsUH60L.zip', 'r') as zipObj:
            zipObj.extractall(path)
        os.remove(path + 'ModsUH60L.zip')
        print(""+Fore.GREEN+"\nFini !")
        time.sleep(2)
        mainchoice()

    def all():
        path = savedgames + version + '\\'
        os.system('cls')

        print(""+Fore.MAGENTA+"\nAlphajet 2.5.5 par Jetesons...\n"+Fore.RESET)
        wget.download('https://www.dropbox.com/s/0s56ah02nbrqdzi/ModsAlpha.zip?dl=1', out = path)
        print("\n\nInstallation...")
        with ZipFile(path + 'ModsAlpha.zip', 'r') as zipObj:
            zipObj.extractall(path)
        os.remove(path + 'ModsAlpha.zip')
        print(""+Fore.GREEN+"\nFini !")

        print(""+Fore.MAGENTA+"\nExtra330 2.7.2 par VARS\n"+Fore.RESET)
        wget.download('https://www.dropbox.com/s/40zxw91vlg6ut9v/ModsE330.zip?dl=1', out = path)
        print("\n\nInstallation...")
        with ZipFile(path + 'ModsE330.zip', 'r') as zipObj:
            zipObj.extractall(path)
        os.remove(path + 'ModsE330.zip')
        print(""+Fore.GREEN+"\nFini !")

        print(""+Fore.MAGENTA+"\nT45 1.01 par VNAO\n"+Fore.RESET)
        wget.download('https://www.dropbox.com/s/jklh4bqc82zey90/ModsT45.zip?dl=1', out = path)
        print("\n\nInstallation...")
        with ZipFile(path + 'ModsT45.zip', 'r') as zipObj:
            zipObj.extractall(path)
        os.remove(path + 'ModsT45.zip')
        print(""+Fore.GREEN+"\nFini !")

        print(""+Fore.MAGENTA+"\nHercules 6.8.2 par Anubis\n"+Fore.RESET)
        wget.download('https://www.dropbox.com/s/aw0b0a8onqoygzh/ModsHercules.zip?dl=1', out = path)
        print("\n\nInstallation...")
        with ZipFile(path + 'ModsHercules.zip', 'r') as zipObj:
            zipObj.extractall(path)
        os.remove(path + 'ModsHercules.zip')
        print(""+Fore.GREEN+"\nFini !")

        print(""+Fore.MAGENTA+"\nUH60-L 1.1 par Kinkku...\n"+Fore.RESET)
        wget.download('https://www.dropbox.com/s/0cjhc5gp1fo0v3l/ModsUH60L.zip?dl=1', out = path)
        print("\n\nInstallation...")
        with ZipFile(path + 'ModsUH60L.zip', 'r') as zipObj:
            zipObj.extractall(path)
        os.remove(path + 'ModsUH60L.zip')
        print(""+Fore.GREEN+"\nFini !")

        time.sleep(2)
        mainchoice()

    mainchoice()

main()
