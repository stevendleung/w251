#!/bin/bash

docker network create --driver bridge facecapture_net --attachable
docker run -d -p 1883:1883 --network facecapture_net -name mqtt
docker run -d --network facecapture_net listener_cloud:latest

