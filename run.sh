#!/usr/bin/env bash
if [ $EUID != 0 ]; then
    sudo "$0" "$@"
    exit $?
fi
REQUIRED_PKG="python3"
REQUIRED_PKG1="acpi-call"
echo "CHECKING Python3 PACKAGE"
PKG_OK=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED_PKG|grep "install ok installed")
echo Checking for $REQUIRED_PKG: $PKG_OK
if [ "" = "$PKG_OK" ]; then
  echo "No $REQUIRED_PKG. Setting up $REQUIRED_PKG."
  sudo apt-get --yes install $REQUIRED_PKG
fi
PKG_OK1=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED_PKG1|grep "install ok installed")
echo Checking for $REQUIRED_PKG1: $PKG_OK1
if [ "" = "$PKG_OK1" ]; then
  echo "No $REQUIRED_PKG1. Setting up $REQUIRED_PKG1."
  sudo apt-get --yes install $REQUIRED_PKG1
fi

sudo python3 main.py
