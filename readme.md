# Обновление DockerCompose
https://docs.docker.com/compose/install/


# Распаковка и запуск
1. git clone https://github.com/YaSlavar/rtu_timetable_service.git
2. cd rtu_timetable_service
3. git submodule init
4. git submodule update --recursive --remote 
5. cd rtu_timetable_api
6. mkdir logs
7. git submodule init
8. git submodule update --force --recursive --init --remote
9. docker-compose build
10. docker-compose up

# BASH
docker exec -it <CONTAINER_NAME> bash

