## Docker
Setup the Tensorflow Object Detection API using docker. Simply run the following commands from within the docker folder.

    docker build -t sign-spotter -f <Dockerfile.gpu or Dockerfile.cpu> .

    docker run -d --gpus=all --name <CONTAINER_NAME> -v <HOST_FOLDER:CONTAINER_FOLDER> -p 8888:8888 -p 6006:6006 -it <DOCKER_IMAGE>:latest

    docker exec -it <CONTAINER_ID or CONTAINER_NAME> bash

Docker files cloned from [TannerGilbert's Repo](https://github.com/TannerGilbert/Tensorflow-Object-Detection-API-Train-Model).
