# Docker и Docker-Compose доклад

## Задания по Docker

* [Задание 1](./docker/task-one)
* [Задание 2](./docker/task-two)
* [Задание 3](./docker/task-three)
* [Задание 4](./docker/task-foo)
* [Задание 5](./docker/task-five)


## Несколько полезных комманд по Docker:

* docker build - сборка `docker image` из `Dockerfile`.
* docker run - Запуск контейнера из образа. Образ локальный или из `docker registry`. ВСЕГДА создает новый контейнер.
* docker stop cont1 cont2… - Остановка контейнеров.
* docker ps - Список запущенных контейнеров на машине.
* docker ps -a - Список всех контейнеров на машине.
* docker images - Список `images`, которые есть на машине.
* docker volume ls - Список `docker volume`, которые есть на машине.
* docker rm cont1 cont2… - Удаление НЕ ЗАПУЩЕННЫХ контейнеров с машины.
* docker rmi img1 img2… - Удаление образов с машины.
* docker volume rm vol1 vol2... - Удаление `volume` с машины.
* docker logs - Весь stdout контейнера.
* docker logs --tail N - N последних строк stdout контейнера.
* docker cp path path - Копирование в/из контейнера файлов.
* docker network ls - Список docker сетей
* docker network rm - Удалить docker сеть
* docker history image -  Посмотреть слои образа

* docker images -q - ID образов
* docker images -f dangling=true - Список подвисших образов
* docker images -f dangling=true -q | xargs docker rmi - Удаление подвисших образов
* docker system prune  - Удалить все подвисшее


## Несколько полезных команд по docker-compose

* docker-compose up - Билд(если нет билда) и запуск всех контейнеров из `docker-compose.yml` файла.
* docker-compose build - Билд образов из `docker-compose.yml` файла.
* docker-compose up -d - Тоже что и `up`, только в демон режиме.
* docker-compose up --build - Тоже что и `up`, только всегда явно билдить новый образ.
* docker-compose build --no-cache - Не использовать закэшированные слои при билде образа.
* docker-compose <up/build/stop/restart> <service_name> <service_name> - Выполнить команду для некоторых сервисов из `docker-compose.yml` файла.
* docker-compose <command> -f <path-to-docker-compose> - Позволяет использовать любой `docker-compose` файл.
* docker-compose stop - Останавливает все контейнеры из `docker-compose.yml` файла.
* docker-compose down - Остановка контейнеров и удаление контейнеров, `network`, `volume` и `image`, созданных `up`.
* docker-compose restart - Перезапускает все контейнеры из `docker-compose.yml` файла.


## Задания по docker-compose

* [Задание 1](./docker-compose/task-1)
* [Задание 2](./docker-compose/task-2)
* [Задание 3](./docker-compose/task-3)

У нас есть приложение, которое состоит из АПИ шлюза, Консумера, пары воркеров.
Все это несколько докеров.
К нему прицеплены: Kafka, Postgresql, Postfix для рассылки, Mongo Как NoSQL хранилище.
И nginx как морда
