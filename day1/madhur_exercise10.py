#!/usr/bin/env python

# Exercise10 (optional)
# Read the 'show_ip_bgp.txt' file.
# Strip out the header information so you are just left with the routes
# Parse each BGP line such that you retrieve the prefix and the as_path.
# Save the prefix and as_path to a file.

with open('show_ip_bgp.txt','r') as f:
    output = f.read().splitlines()

with open('bgp_out.txt','w') as f:
    for line in output:
        if '4.69.184.193' in line:
            list = line.split() 
            prefix = list[1]
            as_path = list[5:-1]
            as_path = " ".join(as_path)
            output_str = "Prefix: {}     as_path: {}\n".format(prefix, as_path)
            f.write(output_str)


