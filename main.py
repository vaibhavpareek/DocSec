from requests import post,get
from os import system,path
import json
from pyfiglet import Figlet
from clint.textui import colored
#The url of the running vault in docker , for the transit information exchange
base_url = 'http://192.168.43.226:8200/v1/transit/'

def banner():
	banner1 = Figlet(font='basic')
	print(colored.blue(banner1.renderText("DocSec")))
	banner2 = Figlet(font='digital')
	print(colored.blue(banner2.renderText(" | Secret Management Tool |")))
	print(colored.green(banner2.renderText(" 		By - Vaibhav Pareek")))


def exit_banner():
	banner1 = Figlet(font='digital')
	print("\n")
	print(colored.red(banner1.renderText("Thanks for Using DocSec")))



def keyInput():
	ch = input("Enter Key Technique (eg: rsa-4096) : ")
	return ch


	 
def menu():
	print("""
		Press 1 For Creating a New key
		Press 2 For Encrypting the data
		Press 3 For Decrypting the data
		Press 4 For Listing the keys
		Press 5 For Fetching Secrets
		Press 6 Exit
		""")

	ch = int(input("Choice : "))
	return ch

try:
	banner()
	token = input(" Vault Token : ")
	headers = {"X-Vault-Token" : str(token)}
	while True:
		system("clear")
		banner()
		ch = menu()
		if(ch==1):
			key_name = input("Enter the Key Name : ")
			key_t = keyInput()
			dt = {
				 "type": str(key_t)
	 			}
			x = post(base_url+"keys/"+str(key_name),  data = dt, headers = headers)
			print("Successfully Created Key!")
			input("Press Any Key to Continue..")
		elif(ch==2):
			key = input("Enter the Key Name : ")
			fl = input("Enter the File Name (Location): ")
			if(path.isfile(fl)==False):
				print("No Such File Present in System")
				input("Press Any Key to Continue..")
			else:
				system("base64 "+str(fl)+" > base_encrypt")
				with open("base_encrypt") as f:
					de = f.readlines()
				data = {"plaintext":de}
				x = post(base_url+"encrypt/"+str(key),  data = data, headers = headers)
				js = x.json()
				with open("encrypt"+str(fl),"w+") as f:
					f.write(js['data']['ciphertext'])
				print("Done Encrypting! Encrypted file saved with the name : encrypt"+str(fl))		
				system("rm "+str(fl)+" base_encrypt")
				input("Press Any Key to Continue..")
		elif(ch==3):
			key = input("Enter the Key Name : ")
			fl = input("Enter the File Name : ")
			if(path.isfile(fl)==False):
				print("No Such File Present in System")
				input("Press Any Key to Continue..")
			else:
				with open(fl) as f:
					de = f.readlines()
				data = {"ciphertext":de}
				x = post(base_url+"decrypt/"+str(key),  data = data, headers = headers)
				js = x.json()
				plain = js['data']['plaintext']
				system("echo "+ str(plain) + " | base64 -d > "+str(fl[int(fl.index("encrypt") + len("encrypt")):]))
				print("Done Decrypting! Orginal File has been saved with the name : "+str(fl[int(fl.index("encrypt") + len("encrypt")):]))
				input("Press Any Key to Continue..")
		elif(ch==4):
			hd = "X-Vault-Token:"+str(token)
			system("curl --header "+str(hd)+" --request LIST "+str(base_url)+"keys > key.json")
			with open('key.json') as json_file:
				js = json.load(json_file)
			print("Available  keys : ")
			for i in js['data']['keys']:
				print(i)
			system("rm key.json")
			input("Press Any Key to Continue..")
		elif(ch==5):
			sec_name = input("Enter the Secret Name : ")
			headers = {
			"X-Vault-Token":"root"
			}
			x = get("http://192.168.43.226:4545/v1/secret/data/"+str(sec_name),  headers = headers)
			js = x.json()
			print("Secret Listed Below")
			for key,value in js['data']['data'].items():
				print(key , " : ", value)
			input("Press Any Key to Continue..")
		elif(ch==6):
			exit_banner()
			exit(0)
except KeyboardInterrupt:
	exit_banner()
	exit(0)
except Exception as e:
	print("Error Occured  : " + str(e))
	exit_banner()
	exit(0)