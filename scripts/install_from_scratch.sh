#!/bin/sh
sudo apt update
sudo apt upgrade -y

# 	Docker install
sudo apt-get remove docker docker-engine docker.io containerd runc
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io -y

#	NVIDIA Driver install
sudo apt install build-essential -y
wget http://us.download.nvidia.com/XFree86/Linux-x86_64/440.64/NVIDIA-Linux-x86_64-440.64.run
sudo chmod +x NVIDIA-Linux-x86_64-440.64.run
sudo ./NVIDIA-Linux-x86_64-440.64.run
#	Expected prompts
#	{
#	warning: OK
#	warning: OK
#	install complete: OK
#	}

#	NVIDIA Register runtime
curl -s -L https://nvidia.github.io/nvidia-container-runtime/gpgkey | sudo apt-key add -
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-container-runtime/$distribution/nvidia-container-runtime.list | sudo tee /etc/apt/sources.list.d/nvidia-container-runtime.list
sudo apt-get update
sudo apt-get install nvidia-container-runtime -y
sudo systemctl daemon-reload
sudo systemctl restart docker
nvidia-smi

#	Docker container build
git clone https://github.com/egm42/sign-spotter-model.git
cd sign-spotter-model/docker
sudo docker build -t sign-spotter -f Dockerfile.gpu .
sudo docker run -d --gpus=all --name sign-spotter-model -v ~/sign-spotter-model:/models/research/object_detection/sign-spotter -p 8888:8888 -p 6006:6006 -it sign-spotter:latest
sudo docker exec -it sign-spotter-model bash