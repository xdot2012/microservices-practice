INSTALL DOCKER
https://docs.docker.com/desktop/install/linux-install/

INSTALL KUBECTL VIA MINIKUBE
https://minikube.sigs.k8s.io/docs/start/

INSTALL K9s
https://k9scli.io/

INSTALL SKAFFOLD
https://skaffold.dev/docs/install/#standalone-binary

RUN MINIKUBE
minikube start

RUN DEVELOPMENT SERVER
skaffold dev


EDIT HOST FILE
MacOS/Linux
/etc/hosts

if kubernetes is running in the local machine
127.0.0.1 microservices.com

if you are in minikube, get the ip with this command
mikube ip

<minikube_ip> microservices.com

minikube addons enable ingress

Error docker login
https://stackoverflow.com/questions/50151833/cannot-login-to-docker-account