import sys, socket
try:
    res = socket.gethostbyaddr("172.217.19.174")
    print ("The host name is :")
    print(" "+res[0])
    print("\n Address:")
    for i in res[2]:
        print(" "+i)
except socket.herror, e:
    print("Error resolving ip address:",e)

