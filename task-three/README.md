# Задание 3. Соберем образ, и всю media вытащим из контейнера.

## 1. Нужно собрать Docker образ из

 * Dockerfile
 * entrypoint.sh
 * .dockerignore
 * app.py
 * requirements.txt

```bash
$ docker build -t task-three-image .
```

## 2. Проверим:

```bash
$ docker images
```

## 3. Создадим и запустим контейнер из образа. Контейнер не будет создан, т.к. команда запуска не будет выполнена.

```bash
$ docker run --rm -p 5000:5000 --name task-three-cont task-three-image  # Запуск контейнера с захватом консоли
$ docker run --rm -p 5000:5000 -d --name task-three-cont task-three-image  # Запуск контейнера в daemon режиме
```

## 4. Примаунтим папку с приложением:

```bash
$ docker run --rm -d -p 5000:5000 -v ~/projects/docker_less/media/:/app/media --name task-three-cont task-three-image
```

## 5. Проверим

Откроем браузер по ссылке [http://0.0.0.0:5000/upload-file/](http://0.0.0.0:5000/upload-file/)

После загрузки открываем [http://0.0.0.0:5000/uploads/<filename>](http://0.0.0.0:5000/uploads/<filename>)

Проверим что в папке media появились файлы
