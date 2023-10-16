import os
import subprocess
import sys
from os import system
from time import sleep

def modprobestart():
    os.system("sudo modprobe acpi_call")
    sleep(2)
def startmsg():
    os.system("export TERM=xterm-256color")
    os.system("clear")
    print("Lenovo ACPI/Driver comamnd sender | by cheuS1 with love :3\n"
      "1. Send Rapid Charge OFF (ACPI)\n"
      "2. Send Rapid ON (ACPI)\n"
      "3. Send Conversation Mode OFF (ACPI)\n"
      "4. Send Conversation Mode ON (ACPI)\n"
      "5. Send FN_lock OFF (DRIVER)\n"
      "6. Send FN_lock ON (DRIVER)\n"
      "7. Start ACPI and Driver state monitor\n"
      "8. Send Your Own ACPI command (DANGER!!!)\n"
      "0. Exit to console\n"
          )
modprobestart()
startmsg()

#DEFs


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

def startwatch():
    os.system("watch -n 0.1 sudo python3 check_all_modes.py")

##

while True:

    vrt = input("What i can do?: ")

    if vrt == "1":
        print(f"Command sended! Returned value: {send_rapid_off()}\n")
        sleep(1.5)
        startmsg()
    elif vrt == "2":
        print(f"Command sended! Returned value: {send_rapid_on()}\n")
        sleep(1.5)
        startmsg()
    elif vrt == "3":
        print(f"Command sended! Returned value: {send_conversation_off()}\n")
        sleep(1.5)
        startmsg()
    elif vrt == "4":
        print(f"Command sended! Returned value: {send_conversation_on()}\n")
        sleep(1.5)
        startmsg()
    elif vrt == "5":
        print(f"Command sended! Returned value: {send_FN_lock_off()}\n")
        sleep(1.5)
        startmsg()
    elif vrt == "6":
        print(f"Command sended! Returned value: {send_FN_lock_on()}\n")
        sleep(1.5)
        startmsg()
    elif vrt == "7":
        startwatch()
    elif vrt == "8":
        print("Type 0 for return to main menu\n")
        print("Type your command please: ")
        cmdi = input()
        if cmdi == 0:
            startmsg()
        else:
            print(f"Command sended! Returned value: {send_own_acpi_command(cmdi)}\n")
            sleep(3)
            startmsg()
    elif vrt == "0":
        os.system("clear")
        print("Goodbye!")
        sleep(0.5)
        sys.exit()