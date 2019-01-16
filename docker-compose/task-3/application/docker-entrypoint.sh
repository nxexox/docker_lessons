#!/usr/bin/env bash

# Ставим флаг, который прервет выполнение скрипта, в случае любой ошибки.
set -e

# Ждем пока запустятся нужные нам приложения.
echo "Waiting for Mongo"
wait-for-it.sh \
    --host=${MONGO_HOST} \
    --port=${MONGO_PORT} \
    --timeout=15 \
    --strict \
    -- echo "Mongo is up"

echo "Waiting for Minio S3"
wait-for-it.sh \
    --host=${MINIO_HOST} \
    --port=${MINIO_PORT} \
    --timeout=15 \
    --strict \
    -- echo "Minio S3 is up"

echo "Waiting for Postfix Backend"
wait-for-it.sh \
    --host=${EMAIL_SERVICE_HOST} \
    --port=${EMAIL_SERVICE_PORT} \
    --timeout=15 \
    --strict \
    -- echo "Postfix Backend is up"

echo "Waiting for Kafka"
wait-for-it.sh \
	--host=${KAFKA_HOST} \
	--port=${KAFKA_PORT} \
	--timeout=60 \
	--strict \
	-- echo "Kafka is up"

# Выполняем команду. Вместо $@ будет подставлена команда для запуска.
exec $@
