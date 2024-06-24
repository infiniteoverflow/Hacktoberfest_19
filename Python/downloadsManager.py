import os
import shutil
import platform

# function to run on linux


def runLinux():
    print("on Linux")
    linuxUsername = str(os.getlogin())
    linuxDirectory = "/home/" + linuxUsername + "/Downloads"
    os.chdir(linuxDirectory)

    for f in os.listdir(linuxDirectory):
        fileSource = str(os.getcwd()) + "/" + str(f)
        fileTypeSplitList = list(os.path.splitext(f))
        fileType = fileTypeSplitList[1]
        if(fileType == '.torrent'):
            if not (os.path.isdir("Torrents")):
                os.mkdir("Torrents")
            shutil.move(fileSource, os.getcwd() + "/" + "Torrents")
        elif(fileType == '.mp3' or fileType == '.wav'):
            if not (os.path.isdir("Music")):
                os.mkdir("Music")
            shutil.move(fileSource, os.getcwd() + "/" + "Music")
        elif(fileType == '.mp4' or fileType == '.wmv' or fileType == '.ogg'):
            if not (os.path.isdir("Videos")):
                os.mkdir("Videos")
            shutil.move(fileSource, os.getcwd() + "/" + "Videos")
        elif(fileType == '.deb'):
            if not (os.path.isdir("Softwares")):
                os.mkdir("Softwares")
            shutil.move(fileSource, os.getcwd() + "/" + "Softwares")
        elif(fileType == '.tar' or fileType == '.7z' or fileType == '.rar' or fileType == '.zip'):
            if not (os.path.isdir("Softwares")):
                os.mkdir("Softwares")
            shutil.move(fileSource, os.getcwd() + "/" + "Softwares")
        elif(fileType == '.png' or fileType == '.jpg' or fileType == '.jpeg' or fileType == '.gif'):
            if not (os.path.isdir("Images")):
                os.mkdir("Images")
            shutil.move(fileSource, os.getcwd() + "/" + "Images")
        elif(fileType == '.pdf'):
            if not (os.path.isdir("PDF_Documents")):
                os.mkdir("PDF_Documents")
            shutil.move(fileSource, os.getcwd() + "/" + "PDF_Documents")

# function to run on windows


def runWindows():
    print("on windows")
    windowsUsername = str(os.getlogin())
    windowsDirectory = "C:/Users/" + windowsUsername + "/Downloads"
    os.chdir(windowsDirectory)

    for f in os.listdir():
        file_source = str(os.getcwd()) + "\\" + str(f)
        file_source = str(file_source.replace("\\", "/"))
        splitList = list(os.path.splitext(f))
        file_type = splitList[1]

        if(file_type == '.torrent'):
            if not (os.path.isdir("Torrents")):
                os.mkdir("Torrents")
            shutil.move(file_source, os.getcwd() + "\\" + "Torrents")

        elif(file_type == '.mp3'):
            if not (os.path.isdir("Music")):
                os.mkdir("Music")
            shutil.move(file_source, os.getcwd() + "\\" + "Music")

        elif(file_type == '.mp4'):
            if not (os.path.isdir("Videos")):
                os.mkdir("Videos")
            shutil.move(file_source, os.getcwd() + "\\" + "Videos")

        elif(file_type == '.zip' or file_type == '.rar'):
            if not (os.path.isdir("Archives")):
                os.mkdir("Archives")
            shutil.move(file_source, os.getcwd() + "\\" + "Archives")

        elif(file_type == '.exe'):
            if not (os.path.isdir("EXE")):
                os.mkdir("EXE")
            shutil.move(file_source, os.getcwd() + "\\" + "EXE")


def runMac():
    print("Since i cannot afford an apple computer to implement the function ,u cannot manage your downloads :-(")


operatingSystem = platform.system()

if(operatingSystem == 'Linux'):
    runLinux()
elif(operatingSystem == 'Windows'):
    runWindows()
else:
    runMac()
