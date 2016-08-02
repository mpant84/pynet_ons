#!/usr/bin/env python

#Exercise16
#a. From your earlier exercise where you parsed the serial number from show_version
#b. Create two functions
#c. Function1 opens the file and returns all of the data in the file as a text string. filename is a function parameter
#d. Function2 parse show_version output and returns the serial number

def get_show_version(filename):
    with open(filename,'r') as f:
        output = f.read().splitlines()
    return output

def parse_show_version(showversion):    
    for line in output:
        if 'Processor board ID' in line:
            process_board_id, router_serial_no = line.split('Processor board ID ')   
    return router_serial_no

output = get_show_version('./day1/show_version.txt')
router_serial_no = parse_show_version(output)

print router_serial_no

