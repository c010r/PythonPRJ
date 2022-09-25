import os
# Configuración carpetas
downloadsFolder = "d:/Downloads/"
musicfolder = "d:/Downloads/Musica/"
pdffolder = "d:/Downloads/PDFS/"
docfolder = "d:/Downloads/Documentos/"
videofolder = "d:/Downloads/Videos/"
compfolder = "d:/Downloads/Comprimidos/"
execfolder = "d:/Downloads/Ejecutables/"

print("Escaneando.......")
if __name__ == "__main__":
    music=0
    video=0
    doc=0
    pdf=0
    comp=0
    exec=0

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
    if music == 0 and video == 0 and doc == 0 and pdf == 0 and comp == 0 and exec == 0:
        print ("No se movio ningún archivo...")
    else:
        print("Archivos Movidos")
        print("-------------------------------------")
        print(f"Musica: {music} Archivos")
        print(f"Videos: {video} Archivos")
        print(f"Documentos: {doc} Archivos")
        print(f"PDF: {pdf} Archivos")
        print(f"Comprimmidos: {comp} Archivos")
        print(f"Ejecutables: {exec} Archivos")
        print("-------------------------------------")
