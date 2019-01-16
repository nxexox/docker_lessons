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

# Выполняем команду. Вместо $@ будет подставлена команда для запуска.
exec $@
