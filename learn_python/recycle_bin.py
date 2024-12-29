import ctypes
def empty_recycle_bin():
    try:
        print("Starting the process to empty the Recycle Bin...")
        ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 0)
        print("The Recycle Bin has been emptied successfully!")
    except Exception as e:
        print(f"Something went wrong: {str(e)}")

empty_recycle_bin()
