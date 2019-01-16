# Задание 5. Запустим nginx как морду для веб сервера.

## 1. Собираем наш Docker image

```bash
$ docker build -t task-five-image .
```

## 2. Проверим:

```bash
$ docker images
```

## 3. Запускаем подцепившись в сеть и убрав внешние порты.

# ВАЖНО!!! У вас будет свой путь до папки на хост машине!!!

```bash
$ docker run --rm -d -v ~/projects/docker_less/media/:/app/media -e smtp_host=postfix -e smtp_user=user -e smtp_password=password --name task-five-cont --net examplenet task-five-image
```

## 4. Билдим nginx образ, который будет проксировать запросы в контейнер с приложением.

```bash
$ cd nginx
$ docker build -t task-five-nginx-img .
$ docker run --rm -d -p 8000:80 -e BACKEND_HOST=task-five-cont -e BACKEND_PORT=5000 --name task-five-nginx-cont --net examplenet task-five-nginx-img
```

## 5. Проверим

Откроем браузер по ссылке [http://0.0.0.0:8000/email/](http://0.0.0.0:8000/email/) и попробуем отправить себе письмо

Откроем браузер по ссылке [http://0.0.0.0:8000/upload-file/](http://0.0.0.0:8000/upload-file/)

После загрузки открываем [http://0.0.0.0:8000/uploads/<filename>](http://0.0.0.0:8000/uploads/<filename>)

Проверим что в папке media появились файлы
