#!/usr/bin/env bash

# Ставим флаг, который прервет выполнение скрипта, в случае любой ошибки.
set -e

# Ждем пока запустятся нужные нам приложения.
echo "Waiting for Postfix"
wait-for-it.sh \
	--host=${SMTP_HOST} \
	--port=${SMTP_PORT} \
	--timeout=15 \
	--strict \
	-- echo "Postfix is up"

# Выполняем команду. Вместо $@ будет подставлена команда для запуска.
exec $@
