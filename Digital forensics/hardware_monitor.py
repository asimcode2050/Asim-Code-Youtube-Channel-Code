import psutil
import time
from rich.console import Console
console = Console()

def display_graph(label, value, max_value, unit="%"):
    bar_length = 50
    filled_length = int(bar_length * value /max_value)
    bar = "#" * filled_length + '-' * (bar_length - filled_length)
    console.print(f"{label}: | {bar} | {value:.2f}{unit}")

def get_system_info():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    return cpu_usage, memory_usage, disk_usage

def main():
    console.print("Real-Time Hardware Monitoring\n",style="bold green")

    while True:
        cpu_usage , memory_usage , disk_usage = get_system_info()
        console.clear()
        display_graph("CPU Usage",cpu_usage,100)
        display_graph("Memory Usage",memory_usage,100)
        display_graph("Disk Usage",disk_usage,100)
        time.sleep(2)

if __name__=="__main__":
    main()

    
