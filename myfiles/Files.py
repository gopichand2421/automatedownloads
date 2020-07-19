import os
import sys

extensions = ['.pdf','.txt','.doc','.mp4','.avi']

class Files:

    def __init__(self,dirname):
        self.FolderCount = self.getCount(dirname)
        self.FilesCount = self.getFilesCount(dirname)
        self.FolederNames = self.folders(dirname)
        self.FileNames = self.filesNames(dirname)

    def getCount(self,dirname) -> int:
        count = int(len([name for name in os.listdir(dirname) if os.path.isdir(os.path.join(dirname,name))]))
        return count

    def getFolderCount(self):
        return self.FolderCount

    def getFilesCount(self, dirname) -> int:
        count=int(len([name for name in os.listdir(dirname) if os.path.isfile(os.path.join(dirname,name))]))
        return count


    def folders(self, dirname) -> list:
        folder = list([name for name in os.listdir(dirname) if os.path.isdir(os.path.join(dirname,name))])
        return folder

    def getFolder(self):
        return self.FolederNames

    def filesNames(self,dirname):
        files = list([name for name in os.listdir(dirname) if os.path.isfile(os.path.join(dirname,name))])
        return files

    def getFiles(self):
        return self.FileNames