#!/usr/bin/python3

# Simple program to determine the methods and functions
#
# Available in a python module or library


def printDir(mod_name):
	
	moduleName=importlib.import_module(mod_name)	

	mod_list=dir(moduleName)
	mod_list.sort()
	print(mod_list)

import importlib

mod=str(input("Enter Module Name: "))

printDir(mod)
	