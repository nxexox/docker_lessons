# Задание 3. Service

## 1. Проверить что уже запущено. Должны быть запущены: Deployment
`kubectl get all`

## 2. Создать Service
`kubectl apply -f service.yaml`

## 3. Узнать, какой порт был назначен
`kubectl get service`

`http://mc-k8s-m3.dev.kontur.ru:<your_port>`

### Полезные команды:

* `kubectl get <pod|po>` - Список запущенных подов
* `kubectl get <deployment|deploy>` - Список деплойментов
* `kubectl get service` - Список сервисов
* `kubectl apply -f <path_to_yaml_file>` - Применить все операции в yaml файле. Так можно создавать/изменять разные сущности
* `kubectl delete <deployment|pod/service> <name>` - Удалить деплоймент/под/сервис
