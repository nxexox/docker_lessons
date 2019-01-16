#!/usr/bin/env sh

set -e

echo "Starting Nginx server"

echo "Waiting for Backend"
wait-for-it.sh \
	--host=${BACKEND_HOST} \
	--port=${BACKEND_PORT} \
	--timeout=80 \
	--strict \
	-- echo "Backend is up"

echo "Create cache dirs"
mkdir -p /var/lib/nginx/cache /var/lib/nginx/proxy

envsubst < /etc/nginx/nginx.tmpl > /etc/nginx/nginx.conf

exec $@