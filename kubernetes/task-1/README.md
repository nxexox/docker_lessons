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

## 2. Проверить что уже запущено
`kubectl get all`

## 3. Создать деплоймент в Kubernetes

`kubectl apply -f deployment.yaml`

## 4. Проверить что уже запущено
`kubectl get all`

### Полезные команды:

* `kubectl get <deployment|deploy>` - Список деплойментов
* `kubectl get <pod|po>` - Список запущенных подов
* `kubectl apply -f <path_to_yaml_file>` - Применить все операции в yaml файле. Так можно создавать/изменять разные сущности
* `kubectl describe <deployment|pod> <deployment|pod name>` - Получить подробную информацию по поду deployment
* `kubectl logs <pod name>` - Получить логи конкретного пода
* `kubectl delete <deployment|pod> <name>` - Удалить деплоймент/под
