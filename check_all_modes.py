import os
import subprocess

def check_powermode():
    os.system("echo '\_SB.PCI0.LPC0.EC0.GZ44' > /proc/acpi/call")
    s = subprocess.getstatusoutput('cat /proc/acpi/call')
    return s[1]

def check_FNlock():
    s = subprocess.getstatusoutput('cat /sys/bus/platform/devices/VPC2004\:00/fn_lock')
    return s[1]

def check_conversation():
    os.system("echo '\_SB.PCI0.LPC0.EC0.BTSM' > /proc/acpi/call")
    s = subprocess.getstatusoutput('cat /proc/acpi/call')
    return s[1]
def text():
    cc = check_conversation()
    cp = check_powermode()
    cf = check_FNlock()
    a = (f"CHECK MODES\n"
      f"Perfomance mode: {cp}   0x2 Battery Save | 0x0 Balanced | 0x1 Max Perfomance  (Fn+Q)\n"
      f"FN_lock: {cf}\n"
      "Rapid Charge: DONT HAVE METHOD FOR PARSE STATE\n"
      f"Conversation mode: {cc}\n")
    return a

print(text())