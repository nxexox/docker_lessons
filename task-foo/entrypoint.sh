#!/usr/bin/env bash

# Ставим флаг, который прервет выполнение скрипта, в случае любой ошибки.
set -e

# СОвершаем какие либо действия перед запуском самого приложения.
echo "RUN COMMAND $@ IN DOCKER"

echo "Waiting for Postfix"
wait-for-it.sh \
	--host=${smtp_host} \
	--port=${smtp_port} \
	--timeout=15 \
	--strict \
	-- echo "Postfix is up"

# Выполняем команду. Вместо $@ будет подставлена команда для запуска.
exec $@
