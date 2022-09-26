import os
# from tkinter import W
from datetime import date
from datetime import datetime
# dia = date.today()
# Configuración carpetas
downloadsFolder = "d:/Downloads/"
musicfolder = "d:/Downloads/Musica/"
pdffolder = "d:/Downloads/PDFS/"
docfolder = "d:/Downloads/Documentos/"
videofolder = "d:/Downloads/Videos/"
compfolder = "d:/Downloads/Comprimidos/"
execfolder = "d:/Downloads/Ejecutables/"
imgfolder = "d:/Downloads/Imagenes/"

print("Escaneando.......")
if __name__ == "__main__":
    music = video = doc = pdf = comp = exec = img = 0
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)
        if extension in [".mp3", ".wav"]:
            os.rename(downloadsFolder + filename, musicfolder + filename)
            music += 1
        if extension in [".mp4", ".mkv", "avi"]:
            os.rename(downloadsFolder + filename, videofolder + filename)
            video += 1
        if extension in [".doc", ".xls", ".docx", ".xlsx", ".txt"]:
            os.rename(downloadsFolder + filename, docfolder + filename)
            doc += 1
        if extension in [".pdf"]:
            os.rename(downloadsFolder + filename, pdffolder + filename)
            pdf += 1
        if extension in [".zip", ".rar"]:
            os.rename(downloadsFolder + filename, compfolder + filename)
            comp += 1
        if extension in [".exe", ".msi"]:
            os.rename(downloadsFolder + filename, execfolder + filename)
            exec += 1
        if extension in [".jpg", ".png", ".gif", ".bmp"]:
            os.rename(downloadsFolder + filename, imgfolder + filename)
            img += 1

    if music == 0 and video == 0 and doc == 0 and pdf == 0 and comp == 0 and exec == 0 and img == 0:
        log = open("log.txt", "a")
        now = datetime.now()
        format = now.strftime('%d-%m-%Y | %H:%M:%S')
        log.write("\n"+format)
        # log.write("\n"+str(datetime.now()))
        log.write("\nSin Movimientos")
        log.write("\n*************************************")
        log.close()

    else:
        log = open("log.txt", "a")
        now = datetime.now()
        format = now.strftime('%d-%m-%Y | %H:%M:%S')
        log.write("\n"+format)
        log.write("\nArchivos Movidos")
        log.write("\n-------------------------------------")
        log.write(f"\nMusica: {music} Archivos")
        log.write(f"\nVideos: {video} Archivos")
        log.write(f"\nDocumentos: {doc} Archivos")
        log.write(f"\nPDF: {pdf} Archivos")
        log.write(f"\nComprimmidos: {comp} Archivos")
        log.write(f"\nEjecutables: {exec} Archivos")
        log.write(f"\nImagenes: {img} Archivos")
        log.write("\n*************************************")
        log.close()
