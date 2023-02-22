import sys
import subprocess

def create_bootable_usb(iso_file, usb_drive):
	#Unmount the USB drive
	subprocess.call(["diskutil","unmountDisk",usb_drive])

	#Write the ISO image to the USB drive
	subprocess.call(["sudo","dd","if="+iso_file,"of="+usb_drive,"bs=4m"])

	print("Bootable USB created successfully")


#probably make arg 1 constant and just figure out arg 2 with diskutil list
create_bootable_usb("/Users/admin/downloads/kali.iso", "/dev/disk2")