# Задание 1. Запустим первое приложение.

## 1. Нужно собрать Docker образ из

 * application/Dockerfile
 * application/entrypoint.sh
 * application/.dockerignore
 * application/requirements.txt
 * application/app.py


```bash
$ docker build -t task-1-image .
```

Или взять уже собранный образ:

registry.skbkontur.ru/mc-k8s/task-1-application:deis


kubectl apply -f deployment.yaml
kubectl apply -f service.yaml