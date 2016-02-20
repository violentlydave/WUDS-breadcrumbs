# WUDS: Wi-Fi User Detection - Modified #

** THIS WILL CHANGE ALOT WORKING UP TO MARCH 12/13th !

WUDS is the creation of Tim Tomes.  Any cool tricks are likely his, any sloppy
code is likely mine.  No ownership claimed, he's the man.

WUDS project site: https://bitbucket.org/LaNMaSteR53/wuds/

This is a slightly modified version of WUDS, mostly to add a few tiny things to
extend it to work w/ other tools in the "Breadcrumbs" repo.


## Changes
* run.sh - slight modifications, don't delete the interface at the end, use first wifi interface available if IFACE isn't configured in config.py
* core.py - add hostname to the records added to DB.  This is so the code can be used easily for multiple "sensors" that can eventually roll the data up to a centralized area -- all sensors have a unique hostname and are ntp sync'd, then the data is easy to mix up and sort out. 

## File Summary

* README - this file
* wudstobreadcrumbs.diff - a diff patch between the WUDS code and this version, if you'd rather use that.   This is auto-generated every time I push new code to the repo:  It pulls a copy of the WUDS code from Tim's site, creates the diff, and pushes it here.
*   






Original README Contents:

###############################################################################
# WUDS: Wi-Fi User Detection System

WUDS is a proximity detection system that uses Wi-Fi probe requests, signal strength, and a white list of MAC addresses to create a detection barrier and identify the presence of foreign devices within a protected zone. Designed with the Raspberry Pi in mind, WUDS can be installed and configured on any system with Python 2.x and a wireless card capable of Monitor mode. See [http://www.lanmaster53.com/2014/10/wifi-user-detection-system/](http://www.lanmaster53.com/2014/10/wifi-user-detection-system/) for more information.

## Setup

```bash
# install prerequisites
# iw      - control the wi-fi interface
# pycapy  - access full 802.11 frames
# sqlite3 - interact with the database
# screen  - (optional) daemonize WUDS
sudo apt-get install iw python-pcapy sqlite3 screen
# lauch a screen session
screen
# install WUDS
git clone https://LaNMaSteR53@bitbucket.org/LaNMaSteR53/wuds.git
cd wuds
# edit the config file
vim config.py
# execute the included run script
./run.sh
# Ctrl+A, D detaches from the screen session
```

## File Summary

* alerts.py - custom alert modules
* config.py - configuration file
* core.py - core library
* run.sh - startup script
* README - this file
