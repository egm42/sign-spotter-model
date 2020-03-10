## Install script
Use this script to install Docker, NVIDIA drivers and NVIDIA runtime toolkit. This script will also build a docker image called 'sign-spotter' and build a container called 'sign-spotter-model'. Edit lines 39 to 41 if a different name or different host:container volume mount is desired. The structure of the script assumes it is located where you want this repo to be cloned to.

    sudo chmod +x install_from_scratch.sh
    ./install_from_scratch.sh
    
    
 ## process_LISA.py script
 
 Defining componstents of the object tags.
   
  Pose: 
            Details about the orientation of the object being labeled.
            
            
  Truncated:
            Indicates that the bounding box specified for the object does 
            not correspond to the full extent of the object. For example, 
            if an object is visible partially in the image then we set truncated 
            to 1. If the object is fully visible then set truncated to 0
            

 Difficult:
            An object is marked as difficult when the object is considered 
            difficult to recognize. If the object is difficult to recognize 
            then we set difficult to 1 else set it to 0. 
            
            
 Bounding Box:
            Axis-aligned rectangle specifying the extent of the object visible in the image.
