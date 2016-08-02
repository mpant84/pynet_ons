#!/usr/bin/env python

#Exercise17
#a. Construct a function that has three parameters x, y, z
#b. z has a default value of 20
#c. Return x + y + z
#d. Call this function using all three positional arguments
#e. Call this function using named arguments x, y (let z be the default)
#f. Call this function with one positional argument and two named arguments.
#g. Call this function using three strings.
#h. Call this function using three lists.


def funk(x,y,z=20):
    return x+y+z


output = funk(1,2,10)
print '\nOutput 1: {}'.format(output)
output = funk(1,10)
print '\nOutput 2: {}'.format(output)
output = funk(1,y=10,z=30)
print '\nOutput 3: {}'.format(output)
output = funk('abc', 'def', 'efg')
print '\nOutput 4: {}'.format(output)
output = funk(['a','b','c'], ['d','e','f'], ['ef','g'])
print '\nOutput 5: {}'.format(output)




