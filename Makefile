default: up 

up:
	docker compose up -d

simulation:
	docker exec -d simulator_container bash -ic "rosnode kill -a && roslaunch simulator ros_bridge.launch"
	docker exec -it simulator_container bash -ic "cd src/simulator &&  ign gazebo new_scene.sdf"

down:
	docker compose down