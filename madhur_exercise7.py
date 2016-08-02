#!/usr/bin/env python

ip_addr = raw_input("Please enter an IP addr? ")
octets = ip_addr.split(".")

octets[3] = '0'

print ("{:<12} {:<12} {:<12} {:<12}".format("Octet 1","Octet 2","Octet 3","Octet 4"))
print ("{:<12} {:<12} {:<12} {:<12}".format(octets[0],octets[1],octets[2],octets[3]))
print ("{:<12} {:<12} {:<12} {:<12}".format(bin(int(octets[0])),bin(int(octets[1])),bin(int(octets[2])),bin(int(octets[3]))))

