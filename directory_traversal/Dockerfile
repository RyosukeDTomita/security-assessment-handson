FROM nginx:1.25.5
COPY nginx.conf /etc/nginx/nginx.conf
COPY index.html /usr/share/nginx/html
COPY img/ /var/img
COPY ./access.log_sample /var/log/nginx/

# Use 8080 instead of 80 to avoid the `nginx: [emerg] bind() to 0.0.0.0:80 failed (13: Permission denied)` when using ECS.
EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]
