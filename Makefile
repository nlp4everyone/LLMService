COMPOSE = sudo docker compose --project-directory . -f docker/compose_monitoring.yml -f docker/compose_serving.yml

.PHONY: up down restart logs ps

up:
	$(COMPOSE) up -d

down:
	$(COMPOSE) down

restart:
	$(COMPOSE) restart

logs:
	$(COMPOSE) logs -f vllm

ps:
	$(COMPOSE) ps