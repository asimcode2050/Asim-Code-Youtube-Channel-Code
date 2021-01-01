import pythoncom
import win32com.client

def check():
    try:
        pythoncom.CoInitialize()
        out = win32com.client.Dispatch('Outlook.Application').GetNameSpace('MAPI')
        return True
    except:
        return False
check()
