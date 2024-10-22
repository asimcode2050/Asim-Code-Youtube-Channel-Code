import winreg as reg

def disable_windows_update():
    try:
        key_path =r'SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU'
        reg.CreateKey(reg.HKEY_LOCAL_MACHINE,key_path)
        key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, key_path,0,reg.KEY_SET_VALUE)
        reg.SetValueEx(key,'NoAutoUpdate',0,reg.REG_DWORD,1)
        reg.CloseKey(key)
        print("Windows Update has been disabled.")
    except Exception as e:
        print(f"Error: {e}")
    
if __name__=="__main__":
    disable_windows_update()
