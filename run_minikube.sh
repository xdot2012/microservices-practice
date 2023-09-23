#! /bin/bash

minikube addons enable ingress
minikube addons enable ingress-dns
minikube tunnel
