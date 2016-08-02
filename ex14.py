#!/usr/bin/env python

net_device = {}
net_device['ip_addr'] = '1.1.1.1'
net_device['user_name'] = 'mpant'
net_device['password'] = 'password'
net_device['vendor'] = 'juniper'
net_device['model'] = 'XXB'

for k, v in net_device.items():
     print k,v

net_device['password'] = 'password123'
net_device['secret'] = 'simple password'

device_type = net_device.get('device_type','cisco_ios')
print '\nDefault Device Type: {}\n'.format(device_type)

