# Автор/Author: cheuS1(https://github.com/cheuS1-n/). Приємного користування! Good using!
import os
import subprocess
import sys
from os import system
from time import sleep

# IMPORT PACKAGE
from func import *


def modprobestart():
    os.system("sudo modprobe acpi_call")
    sleep(2)


settings = 0


def settingsc(int):
    global settings
    settings = int


def startmsg():
    os.system("export TERM=xterm-256color")
    os.system("clear")
    print("Lenovo ACPI/Driver command sender | by cheuS1 with love :3\n"
          "1. Send Rapid Charge OFF (ACPI)\n"
          "2. Send Rapid ON (ACPI)\n"
          "3. Send Conservation Mode OFF (ACPI)\n"
          "4. Send Conservation Mode ON (ACPI)\n"
          "5. Send FN_lock OFF (DRIVER)\n"
          "6. Send FN_lock ON (DRIVER)\n"
          "7. Start ACPI and Driver state monitor\n"
          "8. Send Your Own ACPI command (DANGER!!!)\n"
          "9. CPU Settings\n"
          "0. Exit to console\n"
          )

def pstatemsg(pstate):
    if pstate == "active":
        return "(For unlock all governors, change amd_pstate to passive)"
    else:
        return ""
def cpumsg():
    os.system("clear")
    print("CPU Settings | Lenovo ACPI/Driver command sender | by cheuS1 with love :3\n \n"
          f"AMD_PState: {parsepstate()} {pstatemsg(parsepstate())} \nAvailable scaling governors(core0): {parsescalinggovernors()}\nCurrent scaling governor(cpu0): {parsecurrentscalinggovernors()}\n\n"
          "1. Change governor to powersave\n"
          "2. Change governor to perfomance\n"
          "3. Change governor to ondemand\n"
          "4. Change governor to conservative\n"
          "5. Change governor to userspace\n"
          "6. Change governor to schedutil\n"
          "0. Exit to menu\n"
          )


modprobestart()
startmsg()
settingsc(0)


while True:
    vrt = input("What i can do?: ")

    if settings == 0:
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
            if cmdi == "0":
                startmsg()
            else:
                print(f"Command sended! Returned value: {send_own_acpi_command(cmdi)}\n")
                sleep(3)
                startmsg()
        elif vrt == "9":
            settingsc(1)
            cpumsg()
        elif vrt == "0":
            os.system("clear")
            print("Goodbye!")
            sleep(0.5)
            sys.exit()
    elif settings == 1:
        if vrt == "1":
            print(f"Governor change command sended! Returned value: ")
            print(change_scaling_governor("powersave"))
            sleep(1.5)
            cpumsg()
        if vrt == "2":
            print(f"Governor change command sended! Returned value: ")
            print(change_scaling_governor("perfomance"))
            sleep(1.5)
            cpumsg()
        if vrt == "3":
            print(f"Governor change command sended! Returned value: ")
            print(change_scaling_governor("ondemand"))
            sleep(1.5)
            cpumsg()
        if vrt == "4":
            print(f"Governor change command sended! Returned value: ")
            print(change_scaling_governor("conservative"))
            sleep(1.5)
            cpumsg()
        if vrt == "5":
            print(f"Governor change command sended! Returned value: ")
            print(change_scaling_governor("userspace"))
            sleep(1.5)
            cpumsg()
        if vrt == "6":
            print(f"Governor change command sended! Returned value: ")
            print(change_scaling_governor("schedutil"))
            sleep(1.5)
            cpumsg()
        if vrt == "0":
            settingsc(0)
            startmsg()
