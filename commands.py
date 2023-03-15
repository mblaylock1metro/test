import os
import time

pause = 0.33

first = "sudo apt-get update"

new = "sudo apt-get purge bcmwl-kernel-source"
new2 = "sudo apt-get install firmware-b43-installer"

blue = "sudo apt install bluez"
blueman = "sudo apt install blueman"
blueEnable = "sudo systemctl enable bluetooth.service"
startBlue = "sudo systemctl start bluetooth.service"
runBlue = "rfkill unblock bluetooth"

nic = "sudo apt-get install broadcom-sta-dkms"

video = "sudo apt install vlc"
openVideo = "cvlc v4l2:///dev/video0"

# print(first)
# time.sleep(pause)
# os.system(first)

print(nic)
time.sleep(pause)
os.system(nic)

print(new)
time.sleep(pause)
os.system(new)

print(new2)
time.sleep(pause)
os.system(new2)

print(blue)
time.sleep(pause)
os.system(blue)

print(blueman)
time.sleep(pause)
os.system(blueman)

print(blueEnable)
time.sleep(pause)
os.system(blueEnable)

print(startBlue)
time.sleep(pause)
os.system(startBlue)

print(runBlue)
time.sleep(pause)
os.system(runBlue)

#os.system(video)
#os.system(openVideo)

