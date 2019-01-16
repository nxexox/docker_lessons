FROM nginx:stable-alpine

ARG environment
ENV ENVIRONMENT=$environment

# Install bash
RUN apk add --update bash && rm -rf /var/cache/apk/*

# Remove preinstalled configs (except mime.types) and static files
RUN find /etc/nginx/* ! -name 'mime.types' -delete
RUN rm -r /usr/share/nginx/html/*

# Copy our own configs
COPY nginx.tmpl /etc/nginx/nginx.tmpl

# Create bin directory for custom scripts
RUN mkdir -p /opt/bin

# Copy waiting script and custom entrypoint
COPY entrypoint.sh wait-for-it.sh /usr/local/bin/

# Make entrypoint and waiting script executable
RUN chmod +x /usr/local/bin/entrypoint.sh /usr/local/bin/wait-for-it.sh

# Write access and error logs to stdout and stderr
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

ENTRYPOINT ["entrypoint.sh"]
CMD nginx
