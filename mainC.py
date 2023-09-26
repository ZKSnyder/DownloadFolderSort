import os
from pathlib import Path

#known file extensions
extensionNames = {
    "Audio": {'aif','cda','mid','midi','mp3','mpa','ogg','wav','wma'},
    "Compressed":{'7z','deb','pkg','rar','rpm', 'tar.gz','z', 'zip'},
    'Code':{'js','jsp','html','ipynb','py','java','css'},
    'Documents':{'ppt','pptx','pdf','xls', 'xlsx','doc','docx','txt', 'tex', 'epub'},
    'Images':{'bmp','gif .ico','jpeg','jpg','png','jfif','svg','tif','tiff'},
    'Softwares':{'apk','bat','bin', 'exe','jar','msi','py'},
    'Videos':{'3gp','avi','flv','h264','mkv','mov','mp4','mpg','mpeg','wmv'},
    'Others': {'NONE'}
}

#get path for downloads folder in E drive
dlPath = r"C:\Users\zacha\Downloads"

files = [os.path.join(dlPath, file)
        for file in os.listdir(dlPath)
            if os.path.isfile(os.path.join(dlPath, file))]
   
folders = [os.path.join(dlPath, file)
        for file in os.listdir(dlPath)
            if not os.path.isfile(os.path.join(dlPath, file))]
            
extensionFileTypeMap = {extension: fileType
        for fileType, extensions in extensionNames.items()
            for extension in extensions }
                      
#create folders for sorting
fPath = [os.path.join(dlPath, extensionName)
        for extensionName in extensionNames.keys()]
        
[os.mkdir(folderPath)
        for folderPath in fPath if not os.path.exists(folderPath)]
        
# move the files
def newPath(oldPath):
    extension = str(oldPath).split('.')[-1]
    ampFolder = extensionFileTypeMap[extension] if extension in extensionFileTypeMap.keys() else 'Others'
    finalPath = os.path.join(dlPath, ampFolder, str(oldPath).split('\\')[-1])
    return finalPath
    
[Path(eachfile).rename(newPath(eachfile)) for eachfile in files]

[Path(folder).rename(os.path.join(dlPath, "Others", str(folder).split('\\')[-1]))
        for folder in folders
            if str(folder).split('\\')[-1] not in extensionNames.keys()]
