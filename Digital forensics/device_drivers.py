import wmi

def list_device_drivers():
    c = wmi.WMI()
    drivers = c.Win32_SystemDriver()

    for driver in drivers:
        print(f"Driver Name: {driver.name}, State: {driver.State}")

if __name__ == "__main__":
    list_device_drivers()


