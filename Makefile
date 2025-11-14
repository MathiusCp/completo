APP_NAME=mateous
STACK_FILE=stack.yml
STACK_NAME=ecuador

build:
	docker build -t $(APP_NAME):latest .

deploy:
	docker stack deploy --with-registry-auth -c $(STACK_FILE) $(STACK_NAME)

rm:
	docker stack rm $(STACK_NAME)

ps:
	docker service ls

restart:
	make rm
	sleep 5
	make build
	make deploy