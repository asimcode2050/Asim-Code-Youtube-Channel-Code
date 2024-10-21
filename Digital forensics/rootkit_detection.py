import subprocess

def get_loaded_drivers():
    try:
        output = subprocess.check_output(['driverquery']).decode('utf-8')
        return [line.split()[0] for line in output.strip().split('\n')[3:]]
    except Exception as e:
        return []

def check_driver_integrity(drivers):
    known_good_drivers = {'mspmsnsv.dll','tcpip.sys'}
    suspicious_drivers = [drv for drv in drivers if drv not in known_good_drivers]
    return suspicious_drivers

def detect_hidden_processes():
    try:
        tasklist_output = subprocess.check_output(['tasklist']).decode('utf-8')
        process_ids = [line.split()[1] for line in tasklist_output.strip().split('\n')[3:]]

        return process_ids
    except Exception as e:
        print(f"Error detecting processes: {e}")

def main():
    loaded_drivers = get_loaded_drivers()
    suspicious_drivers = check_driver_integrity(loaded_drivers)

    hidden_processes = detect_hidden_processes()

    if suspicious_drivers:
        print("Suspicious Driver Found:")
        for drv in suspicious_drivers:
            print(f"- {drv}")

    print("Active Processes:")
    for proc in hidden_processes:
        print(f"- {proc}")

if __name__ == "__main__":
    main()



  
