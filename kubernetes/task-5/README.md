# Задание 5. Jobs

## 1. Проверить что уже запущено
`kubectl get all`

## 2. Создать однораовую Job, который выводит текущее время в консоль.

`kubectl apply -f jobs.yaml`

## 3. Проверить, что она отработала
`kubectl get all`

## 4. Проверить, что она отработала корректно.
`kubectl logs job_pob_name`

## 5. Создать периодическую Job.
`kubectl apply -f cron_jobs.yaml`

## 6. Проверить как она работает
`kubectl get all`
`kubectl logs job_pob_name`

### Полезные команды:

* `kubectl get <deployment|deploy>` - Список деплойментов
* `kubectl get <pod|po>` - Список запущенных подов
* `kubectl apply -f <path_to_yaml_file>` - Применить все операции в yaml файле. Так можно создавать/изменять разные сущности
* `kubectl describe <deployment|pod> <deployment|pod name>` - Получить подробную информацию по поду deployment
* `kubectl logs <pod name>` - Получить логи конкретного пода
* `kubectl delete <deployment|pod> <name>` - Удалить деплоймент/под
