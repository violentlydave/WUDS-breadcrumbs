#!/bin/bash
# run WUDS
#  -- uses first wireless interface if IFACE isn't set in config

IFACE=`grep IFACE config.py | cut -d'=' -f 2 | sed "s/['\" ]//g"`

if [ "$IFACE" == "" ]; then 
	IFACE=`iwconfig 2>&1 | grep IEEE | cut -d" " -f 1`; 
	fi

sudo iw dev $IFACE interface add $IFACE type monitor
sudo ifconfig $IFACE up
sudo python ./core.py
sudo ifconfig $IFACE down
sudo iw dev $IFACE del
