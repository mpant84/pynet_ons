#!/usr/bin/env python

ip_addr = raw_input("Please enter an IP addr? ")
octets = ip_addr.split(".")

print ("{:<12} {:<12} {:<12} {:<12}".format(octets[0],octets[1],octets[2],octets[3]))

