minikube:
	./run_minikube.sh


port-forward:
	kubectl port-forward rabbitmq-depl-5b4c6577bf-zh9p5 5672:5672 25672:25672