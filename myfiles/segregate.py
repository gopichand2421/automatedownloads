import os
import sys
import shutil
from myfiles import Files
from .config import logconfig
import logging

userpath = os.path.expanduser('~')
downloads = os.path.join(userpath, 'Downloads')
a = Files.Files(str(downloads))
softwaredestipath = 'E:\softwares'
documentsdestipath = 'E:\documents'
videosdestipath = 'D:\\videos'
archivedestipath = 'E:\\archive'
documents = []
videofiles = []
softwares = []
archivefile = []
logconfig()
def checkpathexists(destipath):
    return os.path.exists(destipath)

class segregate:
    print(f"the path where the files are loading {downloads}")
    logging.info(f"the path where the files are loading {downloads}, {a.__class__.__name__} class")
    def segregateFiles(self):
        filesindownloads = a.FileNames
        try:
            if len(filesindownloads) != 0:
                logging.info(f"count of files in following path {downloads} is {len(filesindownloads)}")
                for i in filesindownloads:
                    extension = i[len(i)-3:len(i)]
                    if extension == 'pdf' or extension == 'doc':
                        documents.append(i)

                    elif extension == 'mkv' or extension == 'mp4':
                        videofiles.append(i)

                    elif extension == 'exe' or extension == 'msi':
                        softwares.append(i)

                    elif extension == 'zip' or extension == 'rar':
                        archivefile.append(i)
                    else:
                        continue
            else:
                print(f"there is no files are present in the following path {downloads}")
                logging.info(f"The total count of the files are {len(filesindownloads)}")
            logging.info(f"The total number of files in document format is {len(documents)}")
            logging.info(f"The total number of files in video format is {len(videofiles)}")
            logging.info(f"The total number of sofwares present in {len(softwares)}")

        except Exception as e:
            print(f"there is some error in while reading the file {e}")
            logging.error(f"this error from {self.__class__.__name__} method {e}")

class filesCopy:
    segregate().segregateFiles()
    softwarepathcheck = checkpathexists(softwaredestipath)
    documentpathcheck = checkpathexists(documentsdestipath)
    videospathcheck = checkpathexists(videosdestipath)
    archivespathcheck = checkpathexists(archivedestipath)

    if softwarepathcheck:
        try:
            for i in softwares:
                if os.path.exists(softwaredestipath+'\\'+i):
                    continue
                else:
                    pass
                shutil.move(downloads + '\\' + i, softwaredestipath)
                print(downloads+'\\'+i)
            logging.info(f"Files are moved to this path {softwaredestipath}: totals files are moved {len(softwares)}")
        except Exception as e:
            logging.error(f"The following errror is came {e}")
    else:
        os.mkdir(softwaredestipath)
    if documentpathcheck:
        try:
            for i in documents:
                if os.path.exists(documentsdestipath+'\\'+i):
                    continue
                else:
                    pass
                shutil.move(downloads+'\\'+i, documentsdestipath)
                print(downloads + '\\' + i)
            logging.info(f"Files are moved to this path {documentsdestipath}: totals files are moved {len(documents)}")
        except Exception as e:
            print(e)
            logging.info(f"The following errror is came {e}")
    else:
        os.mkdir(documentsdestipath)

    if videospathcheck:
        try:
            for i in videofiles:
                if os.path.exists(videosdestipath+'\\'+i):
                    continue
                else:
                    pass
                shutil.move(downloads+'\\'+i,videosdestipath)
                print(downloads+'\\'+i)
        except Exception as e:
            print(e)
            logging.info(f"The following errror is came {e}")

    else:
        os.mkdir(videosdestipath)

    if archivespathcheck:
        try:
            for i in archivefile:
                if os.path.exists(archivedestipath+'\\'+i):
                    continue
                else:
                    pass
                shutil.move(downloads+'\\'+i,archivedestipath)
                print(downloads+'\\'+i)
        except Exception as e:
            print(e)
            logging.info(f"The following errror is came {e}")
    else:
        os.mkdir(archivedestipath)




