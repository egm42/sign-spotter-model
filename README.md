# sign-spotter-model
This will serve to document the process for training a CNN to detect road signs. This model is used in the [sign-spotter](https://github.com/RoninHunter/sign-spotter) application.

## Datasets
This project makes use of several datasets:

* [LISA Dataset](http://cvrr.ucsd.edu/LISA/lisa-traffic-sign-dataset.html)
* Our own collected and labeled data

## Training

## Resources

## Docker
Setup the Tensorflow Object Detection API using docker. Simply run the following commands from within the docker folder.

    docker-compose up

    docker exec -it <CONTAINER_ID>

Docker files cloned from [TannerGilbert's Repo](https://github.com/TannerGilbert/Tensorflow-Object-Detection-API-Train-Model).
