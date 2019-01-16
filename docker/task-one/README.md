# Задание 1. Соберем первый образ и запустим.

## 1. Нужно собрать Docker образ из

 * Dockerfile
 * entrypoint.sh
 * .dockerignore
 * requirements.txt
 *  app.py


```bash
$ docker build -t task-one-image .
```

## 2. Проверим:

```bash
$ docker images
```

## 3. Создадим и запустим контейнер из образа:

```bash
$ docker run --rm --name task-one-cont task-one-image  # Запуск контейнера с захватом консоли
$ docker run --rm -d --name task-one-cont task-one-image  # Запуск контейнера в daemon режиме
```

## 4. Создадим и запустим контейнер, который будет доступен по tcp порту на хост машине

```bash
$ docker run -p 5000:5000 --rm --name task-one-cont task-one-image
```

## 5. Проверим

Откроем браузер по ссылке [http://0.0.0.0:5000](http://0.0.0.0:5000)
