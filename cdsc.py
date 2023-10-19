import os
import subprocess




def getDir():
    fdir1 = input("Please, write path to LenovoACPiControl dir(example: /home/some-user/LenovoACPIControl_15ach6):")
    if not fdir1.startswith("/"):
        print("Wrong directory, please restart script.")
        os.abort()
    return fdir1
fdir = getDir()

DEFAULT_DESKTOP_FILE = ("[Desktop Entry]\n"
                        "Version=1.0\n"
                        "Type=Application\n"
                        "Name=Lenovo ACPI Control\n"
                        "Comment=\n"
                        "Exec=sh run.sh\n"
                        f"Icon={fdir}/icon.png\n"
                        f"Path={fdir}\n"
                        "Terminal=true\n"
                        "StartupNotify=false")


def CPDSC():
    s = subprocess.getstatusoutput('xdg-user-dir DESKTOP')
    os.system(f"cp LenovoACPITool.desktop '{s[1]}'")


def WF():
    try:
        with open('LenovoACPITool.desktop', 'w') as f:
            f.write(DEFAULT_DESKTOP_FILE)
    except Exception as e:
        print(f"Sorry, but i can`t create shortcut.\nERROR: {e}")
    try:
        CPDSC()
    except Exception as e:
        print(f"Sorry, but i can`t copy shortcut to Desktop.\nERROR: {e}")


WF()
CPDSC()
print("Shortcut created! Please, allow executing to use him!")
