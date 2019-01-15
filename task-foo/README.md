# Задание 4. Запустим postfix в другом контейнере и научим приложение отправлять почту.

## 1. Сoздать network.

```bash
$ docker network create examplenet
```

## 2. Создать контейнер с postfix и прицепить его в нашу мост-сеть.

```bash
$ docker run -e maildomain=localhost -e smtp_user=user:password --name postfix -d --net examplenet catatnight/postfix
```

## 3. Собираем наш Docker image

```bash
$ docker build -t task-foo-image .
```

## 4. Проверим:

```bash
$ docker images
```

## 5. Запускаем подцепившись в сеть.

# ВАЖНО!!! У вас будет свой путь до папки на хост машине!!!

```bash
$ docker run --rm -d -p 5000:5000 -v ~/projects/docker_less/media/:/app/media -e smtp_host=postfix -e smtp_port=25 -e smtp_user=user -e smtp_password=password --name task-foo-cont --net examplenet task-foo-image
```

## 6. Проверяем

Откроем браузер по ссылке [http://0.0.0.0:5000/email/](http://0.0.0.0:5000/email/) и попробуем отправить себе письмо

Откроем браузер по ссылке [http://0.0.0.0:5000/upload-file/](http://0.0.0.0:5000/upload-file/)

После загрузки открываем [http://0.0.0.0:5000/uploads/<filename>](http://0.0.0.0:5000/uploads/<filename>)

Проверим что в папке media появились файлы
