# DocSec
[![version](https://img.shields.io/badge/version-1.0.1-green.svg)](https://github.com/vaibhavpareek/docsec/)
<img src="https://img.shields.io/badge/made%20with-python-red.svg" alt="made with python">

*DocSec is a linux based python tool.It is designed to manage the secrets and credentials encrypted with the keys provided the OPEN SOURCE PROJECT (Vault). Vault is also installed on docker to provide the light weight service , it also helps in maintaining the vault robustly without the key loss even if it get down.*

![FeatSel Logo](/logo/logo.png)

# Prerequisite 
- [x]  Operating System  : Linux
- [x]  Python3 : Installed and Configured
- [x]  Permissions : Run as Root
- [x]  RAM : >2GB(Prefer)
- [x]  Space : Around 50MB (Later depends on Dataset) 
- [x]  Updates : Keep Code Updated by `git pull`

## [Download](https://github.com/vaibhavpareek/docsec) the DocSec
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
```
docker run -dit --cap-add=IPC_LOCK 
-e 'VAULT_DEV_ROOT_TOKEN_ID=<vault token>' -e 'VAULT_DEV_LISTEN_ADDRESS=0.0.0.0:<vault local port number>'
-v log_vol:/vault/logs -v data_vol:/vault/file
-p <vault public port number>:<vault local port number>
--name <vault server name>  vault:latest

Replacable Variables(Including Brackets):
1. <vault token> : Replace with Vault Token Value
2. <vault local port number> : Provide any non-use Port Number Locally in Docker installed system(Default:8200)
3. <vault pubic port number> : Provide any non-use Port Number Publcally (Use for PATTING)
4. <vault server name> : Replace with any name for the running container
```


## License
 This project is licensed under the Apache License - see the [LICENSE.md](/LICENSE) file for details
 
## Versioning 
**Version : 1.0.1
Next Version :soon:**

## Contributor
[![Linkedin](https://img.shields.io/badge/Linkedin-Vaibhav_Pareek-<COLOR>.svg)](https://www.linkedin.com/in/vaibhavvp/)

## [Demonstration of FeatSel](https://www.linkedin.com/posts/vaibhavvp_quarantinedayss-coding-linux-activity-6657516985062125568-x6a7)
