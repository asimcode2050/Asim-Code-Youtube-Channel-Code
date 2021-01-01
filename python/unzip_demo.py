import os
import zipfile
def unzip_file(filename):
    z = zipfile.ZipFile(filename)
    path  =  os.path.dirname(filename)
    z.extractall(path=path)
    
unzip_file("/home/asim/demo.zip")