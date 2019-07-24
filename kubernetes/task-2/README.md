# Задание 2. Deployment

## 1. Нужно собрать Docker образ для бэкенда и фронта из

 * application/Dockerfile
 * application/entrypoint.sh
 * application/.dockerignore
 * application/requirements.txt
 * application/app.py


```bash
$ cd backend
$ docker build -t registry.skbkontur.ru/mc-k8s/task-2:backend .
$ cd ../front
$ docker build -t registry.skbkontur.ru/mc-k8s/task-2:front .
```

Или взять уже собранные образы:

* `registry.skbkontur.ru/mc-k8s/task-2:backend`
* `registry.skbkontur.ru/mc-k8s/task-2:front`

## 2. Проверить что уже запущено
`kubectl get all`

## 3. Создать деплоймент в Kubernetes

`kubectl apply -f deployment.yaml`

## 4. Проверить что уже запущено
`kubectl get all`

### Полезные команды:

* `kubectl get <pod|po>` - Список запущенных подов
* `kubectl get <deployment|deploy>` - Список деплойментов
* `kubectl apply -f <path_to_yaml_file>` - Применить все операции в yaml файле. Так можно создавать/изменять разные сущности
* `kubectl delete <deployment|pod> <name>` - Удалить деплоймент/под
