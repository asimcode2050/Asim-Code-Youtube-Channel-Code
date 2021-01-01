import sys
def check_compatible(platforms=['win32','linux2','darwin'], module=None):
    if sys.platform in platforms:
        return True
    print('module is not compatible with :'+ sys.platform )
print(check_compatible(platforms=['win32','linux2','darwin'], module='sys'))
