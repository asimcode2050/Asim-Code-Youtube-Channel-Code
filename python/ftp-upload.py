import os
import sys
import ftplib
def ftp():
    FILENAME="/home/asim/file.txt"
    try:
        FTP_SERVER="ftp.xxx.com"
        ftp_username= "ftp_username"
        ftp_password = "ftp_password"
        SSL=0
        OUT_DIR="/"
        if SSL==0:
            ft=ftplib.FTP(FTP_SERVER,ftp_username,ftp_password)
        elif SSL==1:
            ft.ftplib.FTP_TLS(FTP_SERVER,ftp_username,ftp_password)
        ft.cwd(OUT_DIR)
        fp=open(FILENAME,'rb')
        cmd='STOR'+' '+FILENAME
        ft.storebinary(cmd,fp)
        ft.quit()
        fp.close()
        os.remove(FILENAME)
    except Exception as e:
        print e

ftp()

        
