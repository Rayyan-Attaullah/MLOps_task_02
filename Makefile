IMAGE_NAME = $(DOCKER_USERNAME)/mlops-model
TAG = latest

docker:
	docker build -t $(IMAGE_NAME):$(TAG) .

push:
	docker push $(IMAGE_NAME):$(TAG)

images:
	docker images

delete:
	docker rmi $(IMAGE_NAME):$(TAG)
	

containers:
	docker ps

start:
	docker run -d -p 5000:5000 --name MLOps_task $(IMAGE_NAME):$(TAG)

stop:
	@docker stop $(CONTAINER_ID)
