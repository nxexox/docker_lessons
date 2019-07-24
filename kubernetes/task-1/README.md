# Задание 1. Запустим первое приложение. POD

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

`registry.skbkontur.ru/mc-k8s/task-1:application`

## 2. Проверить что уже запущено
`kubectl get all`

## 3. Создать под в Kubernetes

`kubectl apply -f pod.yaml`

## 4. Проверить что уже запущено
`kubectl get all`

### Полезные команды:

* `kubectl get <pod|po>` - Список запущенных подов
* `kubectl apply -f <path_to_yaml_file>` - Применить все операции в yaml файле. Так можно создавать/изменять разные сущности
* `kubectl delete pod <name> - Удалить под
