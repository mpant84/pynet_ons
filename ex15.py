#!/usr/bin/env python

net_device = {
  'ip_addr': '1.1.1.1',
  'user_name': 'mpant',
  'password': 'password',
  'vendor': 'cisco',
  'model': 'XXB'
}

for k, v in net_device.items():
     print k,v

net_device['password'] = 'password123'
net_device['secret'] = 'simple password'

try:
    device_type = net_device['device_type']
except KeyError:
    print '\nDevice Type Field not found\n'

