#!/bin/bash
#xhost +
#export DISPLAY=:0

kubectl apply -f mosquittoService.yaml
kubectl apply -f mosquitto.yaml
kubectl apply -f logger-deployment.yaml
kubectl apply -f listener-deployment.yaml
kubectl apply -f publisher-deployment.yaml
