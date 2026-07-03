.PHONY: up down logs restart status

up:
	sudo docker compose -f docker/compose_serving.yml up -d

down:
	sudo docker compose -f docker/compose_serving.yml down

logs:
	sudo docker compose -f docker/compose_serving.yml logs -f

restart:
	sudo docker compose -f docker/compose_serving.yml restart

status:
	sudo docker compose -f docker/compose_serving.yml ps