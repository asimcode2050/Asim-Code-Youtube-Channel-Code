import pefile
import pprint
putty = pefile.PE('/home/asim/Downloads/putty.exe')
#pprint.pprint(dir(putty))
sections = putty.FILE_HEADER.NumberOfSections
dll=putty.OPTIONAL_HEADER.DllCharacteristics
ver=putty.OPTIONAL_HEADER.MajorImageVersion
print("\n Numbers Of Sections:"+str(sections))
print("\n Dynamic :"+str(dll))
print("\n Image Version: "+str(ver))
