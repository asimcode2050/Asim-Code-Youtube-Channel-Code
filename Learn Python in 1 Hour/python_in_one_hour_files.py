#https://www.youtube.com/watch?v=z_eALBTtQTk&ab_channel=AsimCode
filename = '/home/asimcode/python/readme.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line)
