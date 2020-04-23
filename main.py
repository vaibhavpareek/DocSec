import requests
from os import system,path
import json
base_url = 'http://192.168.43.226:4545/v1/transit/'

headers = {"X-Vault-Token" : 'root'}

dt = {
		 "type": "rsa-4096"
	 }

print("""
	Press 1 For Creating a New key
	Press 2 For Encrypting the data
	Press 3 For Decrypting the data
	Press 4 For Listing the keys
	Press 5 Exit
	""")

ch = int(input("Choice : "))
try:
	if(ch==1):
		key_name = input("Enter the Key Name : ")
		x = requests.post(base_url+"keys/"+str(key_name),  data = dt, headers = headers)
		print(x.text)
	elif(ch==2):
		key = input("Enter the Key Name : ")
		fl = input("Enter the File Name : ")
		if(path.isfile(fl)==False):
			print("No Such File Present in System")
		else:
			system("base64 "+str(fl)+" > base_encrypt")
			with open("base_encrypt") as f:
				de = f.readlines()
			data = {"plaintext":de}
			x = requests.post(base_url+"encrypt/"+str(key),  data = data, headers = headers)
			js = x.json()
			with open("encrypt"+str(fl),"w+") as f:
				f.write(js['data']['ciphertext'])
			print("Done Encrypting")
			system("rm a.txt base_encrypt")
	elif(ch==3):
		key = input("Enter the Key Name : ")
		fl = input("Enter the File Name : ")
		if(path.isfile(fl)==False):
			print("No Such File Present in System")
		else:
			with open(fl) as f:
				de = f.readlines()
			data = {"ciphertext":de}
			x = requests.post(base_url+"decrypt/"+str(key),  data = data, headers = headers)
			js = x.json()
			plain = js['data']['plaintext']
			system("echo "+ str(plain) + " | base64 -d > "+str(fl[int(fl.index("encrypt") + len("encrypt")):]))
			print("Done Decrypting")
	elif(ch==4):
		hd = "X-Vault-Token:root"
		system("curl --header "+str(hd)+" --request LIST "+str(base_url)+"keys > key.json")
		with open('key.json') as json_file:
			js = json.load(json_file)
		print("Available  keys : ")
		for i in js['data']['keys']:
			print(i)
		system("rm key.json")
	else:
		print("DOne")
except Exception as e:
	print(e)
	print("ErroR oCCURED")