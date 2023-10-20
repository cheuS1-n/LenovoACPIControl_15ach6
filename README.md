
# LenovoACPIControl

A script for controlling fan modes, fast charging mode, battery saving, FN_lock, using ACPI and kernel driver. There is also a function of manually entering ACPI commands.

# LenovoACPIControl

A script for controlling fan modes, fast charging mode, battery saving, FN_lock, using ACPI and kernel driver. There is also a function of manually entering ACPI commands.

![LenovoACPITool menu](https://github.com/cheuS1-n/LenovoACPIControl_15ach6/blob/main/image.png?raw=true)

# Run

    sudo apt install git 

    git clone https://github.com/cheuS1-n/LenovoACPIControl_15ach6 

    cd LenovoACPIControl_15ach6 
    
    chmod +x run.sh

    ./run.sh 

# Changing perfomance mode
Press Fn+Q.
You won't see anything to indicate that the regime has changed, but it is changing. Check through point 7 of the script.

# Create shortcut
Just add --create-shortcut option when start run.sh


# How change AMD_PState to passive
You need add to your boot configuration `amd_pstate=passive`
https://wiki.archlinux.org/title/kernel_parameters
## Addition
If you have additional codes for ACPI, then please send them to Issues with a description of the actions of this code, thanks!

[Українська мова/Ukrainian language](https://github.com/cheuS1-n/LenovoACPIControl_15ach6/blob/main/README.uk.md)



# Run

    sudo apt install git 

    git clone https://github.com/cheuS1-n/LenovoACPIControl_15ach6 

    cd LenovoACPIControl_15ach6 
    
    chmod +x run.sh

    ./run.sh 

# Changing perfomance mode
Press Fn+Q.
You won't see anything to indicate that the regime has changed, but it is changing. Check through point 7 of the script.

# Create shortcut
Just add --create-shortcut option when start run.sh


# How change AMD_PState to passive
You need add to your boot parameters `amd_pstate=passive`
https://wiki.archlinux.org/title/kernel_parameters
## Addition
If you have additional codes for ACPI, then please send them to Issues with a description of the actions of this code, thanks!

[Українська мова/Ukrainian language](https://github.com/cheuS1-n/LenovoACPIControl_15ach6/blob/main/README.uk.md)


