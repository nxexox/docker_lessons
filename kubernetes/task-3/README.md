# Задание 3. Апи и фронт

# TODO: Доделать связь между контейнерами

## 1. Нужно собрать Docker образ для бэкенда и фронта из

 * application/Dockerfile
 * application/entrypoint.sh
 * application/.dockerignore
 * application/requirements.txt
 * application/app.py


```bash
$ cd backend
$ docker build -t registry.skbkontur.ru/mc-k8s/task-2-backend:deis .
$ cd ../front
$ docker build -t registry.skbkontur.ru/mc-k8s/task-2-front:deis .
```

Или взять уже собранные образы:

* `registry.skbkontur.ru/mc-k8s/task-2-backend:deis`
* `registry.skbkontur.ru/mc-k8s/task-2-front:deis`

## 2. Проверить что уже запущено
`kubectl get all`

## 3. Создать деплоймент в Kubernetes

`kubectl apply -f deployment.yaml`

## 4. Проверить что уже запущено
`kubectl get all`

## 5. Создать Service
`kubectl apply -f service.yaml`

## 6. Узнать, какой порт был назначен
`kubectl get service`

`http://mc-k8s-m3.dev.kontur.ru:<your_port>`
