# Docker доклад

## Задания

* [Задание 1](./task-one)
* [Задание 2](./task-two)
* [Задание 3](./task-three)
* [Задание 4](./task-foo)
* [Задание 5](./task-five)


## Несколько полезных комманд по докеру:

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