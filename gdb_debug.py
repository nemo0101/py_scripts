#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import sys
import os

#sudo python /home/bishop/Documents/gdb_debug.py program2_10.c /home/bishop/Desktop/tests/

name_c_file = sys.argv[1]
path_c_file = sys.argv[2]

print(name_c_file)
print(path_c_file)

if name_c_file != "" and path_c_file != "":
	res_0 = os.system("cd " + path_c_file)
	
	if res_0 == 0:
		res_1 = os.system("gcc -O0 -g "+ path_c_file + name_c_file +" -o test")
		
		if res_1 == 0:
			print("* * *")
			print("-- commands: run, break .., print .., c, q ")
			print("* * *")
			res_2 = os.system("gdb ./test")
			
			if res_2 != 0:
				print("-- gdb fail")
		else:
			print("-- gcc fail")
	else:
		print("-- cd fail")

