default: up 

up:
	docker compose up -d

simulation:
	docker exec -d simulator_container bash -ic "rosnode kill -a && roslaunch simulator ros_bridge.launch"
	docker exec -it simulator_container bash -ic "roslaunch simulator simulation.launch"

down:
	docker compose down