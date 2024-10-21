import wmi
def get_hardware_ids():
    c= wmi.WMI()

    for cpu in c.Win32_Processor():
        cpu_id = cpu.ProcessorId.strip()
        print(f"CPU ID: {cpu_id}")

    for motherborad in c.Win32_BaseBoard():
        motherborad_serial = motherborad.SerialNumber.strip()
        print(f'Motherboard Serial Number: {motherborad_serial}')
    
    for disk in c.Win32_PhysicalMedia():
        if disk.SerialNumber:
            disk_serial = disk.SerialNumber.strip()
            print(f"Hard Drive Serial Number: {disk_serial}")

    
if __name__ == "__main__":
    get_hardware_ids()
