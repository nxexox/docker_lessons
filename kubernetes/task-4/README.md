# Задание 4. Ingress

## 1. Проверить что уже запущено. Должены быть запущены: Deployment, Service
`kubectl get all`

## 2. Создать Ingress
`kubectl apply -f ingress.yaml`

## 3. Проверить что ingress создался успешно
`kubectl get ingress`

`http://mc-k8s-m3.dev.kontur.ru:<your_port>`

### Полезные команды:

* `kubectl get <pod|po>` - Список запущенных подов
* `kubectl get <deployment|deploy>` - Список деплойментов
* `kubectl get service` - Список сервисов
* `kubectl get ingress` - Список игрессов
* `kubectl apply -f <path_to_yaml_file>` - Применить все операции в yaml файле. Так можно создавать/изменять разные сущности
* `kubectl delete <deployment|pod|service|ingress> <name>` - Удалить деплоймент/под/сервис/игресс