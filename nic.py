import os
import time

pause = 0.33

nic = "sudo apt-get install broadcom-sta-dkms"
new = "sudo apt-get purge bcmwl-kernel-source"
new2 = "sudo apt-get install firmware-b43-installer"

print(nic)
time.sleep(pause)
os.system(nic)

print(new)
time.sleep(pause)
os.system(new)

print(new2)
time.sleep(pause)
os.system(new2)

