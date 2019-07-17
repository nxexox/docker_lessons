# Задание 2. Бэкенд.

## 1. Нужно собрать Docker образ из

 * Dockerfile
 * entrypoint.sh
 * .dockerignore
 * requirements.txt
 *  app.py


```bash
$ docker build -t task-two-backend-image .
```

## 2. Проверим:

```bash
$ docker images
```

## 3. Взять уже собранный Docker образ


## Бэкенд умеет:

* /jobs/list(GET) - Список запросов от JOB в Kubernetes
* /hello-by-name(GET) - Приветствие по имени. Принимает name в JSON request query, возвращает message в JSON response body.
* /calculate(POST) - Выполняет математическую операцию над двумя числами. Принимает в JSON request body a, b - числа, operation - Сама операция(+ - * /)
Возвращает в JSON response body a, b, operation, result.


