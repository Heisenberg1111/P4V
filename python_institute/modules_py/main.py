#!/usr/bin/python3

from sys import path

path.append('mod_dir')

import module


zeroes =  [ 0 for i in range(5) ]
ones = [ 1 for i in range(5) ]

print(module.sum1(zeroes))

print(module.prod1(ones))



