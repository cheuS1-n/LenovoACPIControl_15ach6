import os
import subprocess
import argparse

# ACPI & DRIVER
def send_rapid_off():
    os.system("echo '\_SB.PCI0.LPC0.EC0.VPC0.SBMC 0x08' > /proc/acpi/call")
    s = subprocess.getstatusoutput('cat /proc/acpi/call')
    return s[1]
def send_rapid_on():
    os.system("echo '\_SB.PCI0.LPC0.EC0.VPC0.SBMC 0x07' > /proc/acpi/call")
    s = subprocess.getstatusoutput('cat /proc/acpi/call')
    return s[1]
def send_conversation_off():
    os.system("echo '\_SB.PCI0.LPC0.EC0.VPC0.SBMC 0x05' > /proc/acpi/call")
    s = subprocess.getstatusoutput('cat /proc/acpi/call')
    return s[1]
def send_conversation_on():
    os.system("echo '\_SB.PCI0.LPC0.EC0.VPC0.SBMC 0x03' > /proc/acpi/call")
    s = subprocess.getstatusoutput('cat /proc/acpi/call')
    return s[1]
def send_FN_lock_off():
    os.system("echo '0' > /sys/bus/platform/devices/VPC2004\:00/fn_lock")
    s = subprocess.getstatusoutput('cat /sys/bus/platform/devices/VPC2004\:00/fn_lock')
    return s[1]
def send_FN_lock_on():
    os.system("echo '1' > /sys/bus/platform/devices/VPC2004\:00/fn_lock")
    s = subprocess.getstatusoutput('cat /sys/bus/platform/devices/VPC2004\:00/fn_lock')
    return s[1]
def send_own_acpi_command(command):
    os.system(f"echo '{command}' > /proc/acpi/call")
    s = subprocess.getstatusoutput('cat /proc/acpi/call')
    return s[1]
###

# OTHER
def startwatch():
    os.system("watch -n 0.1 sudo python3 check_all_modes.py")