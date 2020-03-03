## Install script
Use this script to install Docker, NVIDIA drivers and NVIDIA runtime toolkit. This script will also build a docker image called 'sign-spotter' and build a container called 'sign-spotter-model'. Edit lines 39 to 41 if a different name or different host:container volume mount is desired. The structure of the script assumes it is located where you want this repo to be cloned to.

    sudo chmod +x install_from_scratch.sh
    ./install_from_scratch.sh