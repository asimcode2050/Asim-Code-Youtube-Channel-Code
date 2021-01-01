words = []
fileOB = open('infile.txt',"r")
lines = fileOB.read().splitlines()
for line in lines:
    words.extend(line.split())

print(words)