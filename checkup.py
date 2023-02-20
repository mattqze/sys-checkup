import psutil
import shutil
import time
import datetime
print("Last Boot: " + datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%H:%M:%S %m-%d-%Y") + "\n")
print("CPU Usage: "+"\nCurrent Usage: "+str(psutil.cpu_percent(interval=0.5)) + "%" +"\nCores: "+str(psutil.cpu_count(logical=False))+"\nThreads: "+str(psutil.cpu_count(logical=True))+"\n")
print("RAM Usage: "+"\nUsing: "+str(psutil.virtual_memory().used >> 20) + " MB"+"\nAvailable: "+str(psutil.virtual_memory().available >> 20)+" MB" +"\nTotal + Page: "+str(psutil.virtual_memory().total >> 20)+" MB")
print("\n"+"Available Disks: ")
for disk in psutil.disk_partitions():
    if disk.fstype:
        print(disk.device)
        total, used, free = shutil.disk_usage(disk.device)
        print("Total: %d GB" % (total // (2**30)))
        print("Free: %d GB" % (free // (2**30)))
        print("Used: %d GB" % (used // (2**30)) + "\n")
print( psutil.net_if_stats().master)