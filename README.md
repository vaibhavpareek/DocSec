# DocSec
[![version](https://img.shields.io/badge/version-1.0.1-green.svg)](https://github.com/vaibhavpareek/docsec/)
<img src="https://img.shields.io/badge/made%20with-python-red.svg" alt="made with python">

*DocSec is a linux based python tool.It is designed to manage the secrets and credentials encrypted with the keys which are  provided by the OPEN SOURCE PROJECT (Vault). Vault is also installed on docker to provide the light weight service , it also helps in maintaining the vault robustly without the loss of key even if container gets down. In this tool VAULT HTTP API has been used with the libraries of python to provide a TUI Tool for UI/UX.*

![DocSec Logo](/logo/docsec.png)

# Prerequisite 
- [x]  Operating System  : Linux
- [x]  Python3 : Installed and Configured
- [x]  Permissions : Run as Root
- [x]  RAM : >2GB(Prefer)
- [x]  Space : Around 50MB (Later depends on Key Storage) 
- [x]  Updates : Keep Code Updated by `git pull`

## [Download](https://github.com/vaibhavpareek/DocSec/archive/master.zip) the DocSec
```
git clone https://github.com/vaibhavpareek/docsec.git
```

## Environment Setup
``` 
Follow these Steps to Configure your own vault with this python tool.(Locally)
Same Steps can be followed on AWS Instance or Google GCP CLOUD Instance
```

###### Step 1 : Install Required Python Libraries
```
pip3 install -r requirement.txt
```

###### Step 2 : Install Docker on Linux ([Documentation for Installation](https://docs.docker.com/engine/install/))
```
apt-get install docker (Debian System)
For other OS refer Documentation
```
###### Step 3 : Download [Vault](https://hub.docker.com/_/vault) Image from Docker HUB
```
docker pull vault:latest
```

###### Step 4 : Create Volume for Persistent Storage of Logs and Data
```
docker volume create log_vol
docker volume create data_vol
```

###### Step 5 : Run a Configured Container of Vault Image on Docker
## Development Mode (NON-PERSISTENT DATA)
```
docker run -dit --cap-add=IPC_LOCK 
-e 'VAULT_DEV_ROOT_TOKEN_ID=<vault token>' -e 'VAULT_DEV_LISTEN_ADDRESS=0.0.0.0:<vault local port number>'
-p <vault public port number>:<vault local port number>
--name <vault server name>  vault:latest
```
## Server in Development Mode (PERSISTENT DATA)
```
docker run -dit --cap-add=IPC_LOCK
-v data_vol:/vault/file -v log_vol:/vault/log
-e 'VAULT_ADDR=http://127.0.0.1:8200' 
-e 'VAULT_LOCAL_CONFIG={"backend":{"file":{
                              "path":"/vault/file"
                                          }
                                  },
                        "ui":true,
                        "tls_disable":1}'
-p <vault public port number>:<vault local port number>
--name <vault server name>  vault:latest server -dev
```
```
Replacable Variables(Including Brackets):
1. <vault token> : Replace with Vault Token Value
2. <vault local port number> : Provide any non-use Port Number Locally in Docker installed system(Default:8200)
3. <vault pubic port number> : Provide any non-use Port Number Publcally (Use for PATTING)
4. <vault server name> : Replace with any name for the running container
```

###### Step 6 : Run DocSec Tool 
```
python3 main.py
```

###### Step 7 : Manage Docker
## Development Mode (NON-PERSISTENT DATA)
```
1. docker container inspect <name of the vault server container>  (To inspect whole container)
2. docker status <name of the vault server container>    (To check the running status of the container)
3. docker stop/start/attach  <name of the vault server container>     (To Manage the running vault server)
```
## Server in Development Mode (PERSISTENT DATA)
```
docker exec -it <name of the vault server container> sh  ( To get the shell excess)
1. vault status (To check the status)
2. vault login token=<token value>
3. vault operator init -> (To Initialize)
4. vault auth enable -path=token (To enable token method of logging in)
5. vault auth list (To list all the authentication methods)
```

###### Step 8 : Manual or Help
```
Functionalities This Tool Provide
1. Create Own Key from multiple encrypting algorithms.
2. List All the Keys available in Vault.
3. Encrypt data of any credential file. 
4. Decrypt data of credential file to get back the original content.
```

## License
 This project is licensed under the GPL License - see the [LICENSE.md](/LICENSE) file for details
 
## Versioning 
**Version : 1.0.1
Next Version :soon:**

## Contributor
[![Linkedin](https://img.shields.io/badge/Linkedin-Vaibhav_Pareek-blue.svg)](https://www.linkedin.com/in/vaibhavvp/)

## [Demonstration of DocSec](/logo/docsec.mp4)
 
