import _winreg
def create_reg_key(key,subkey, value):
    try:
        reg_key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,key,0,_winreg.KEY_WRITE)
        _winreg.SetValueEx(reg_key,subkey,0,_winreg.RG_SZ,value)
        _winreg.CloseKey(reg_key)
        return True
    except Exception as e:
        print(e)
        return False

