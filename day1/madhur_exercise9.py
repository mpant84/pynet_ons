#!/usr/bin/env python

#Exercise9
#a. Read a show version output from a router (in a file)
#b. Find the router serial number in the output
#c. Parse the serial number and return it is a variable. Use .split() and substr in str to 
#   accomplish this

with open('show_version.txt','r') as f:
    output = f.read().splitlines()
    
for line in output:
    if 'Processor board ID' in line:
        process_board_id, router_serial_no = line.split('Processor board ID ')   
        print router_serial_no
