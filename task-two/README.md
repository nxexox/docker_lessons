# Задание 2. Соберем образ без кода, и примаунтим код к приложению.

## 1. Нужно собрать Docker образ из

 * Dockerfile
 * entrypoint.sh
 * .dockerignore

```bash
$ docker build -t task-two-image .
```

## 2. Проверим:

```bash
$ docker images
```

## 3. Создадим и запустим контейнер из образа. Контейнер не будет создан, т.к. команда запуска не будет выполнена.

```bash
$ docker run --rm -p 5000:5000 --name task-two-cont task-two-image  # Запуск контейнера с захватом консоли
$ docker run --rm -p 5000:5000 -d --name task-two-cont task-two-image  # Запуск контейнера в daemon режиме
```

## 4. Примаунтим папку с приложением:

# ВАЖНО!!! У вас будет свой путь до папки на хост машине!!!

```bash
$ docker run --rm -d -p 5000:5000 -v ~/projects/docker_less/task-two/:/app --name task-two-cont task-two-image
```

## 5. Проверим

Откроем браузер по ссылке [http://0.0.0.0:5000](http://0.0.0.0:5000)
