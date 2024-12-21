FROM openresty/openresty:1.21.4.1-0-bullseye-fat
# NOTE: nginxの-pオプションの代わりにWORKDIRで指定
WORKDIR /usr/local/openresty
USER root

COPY ./nginx.conf /usr/local/openresty/nginx/conf/nginx.conf
COPY . /usr/share/nginx/html/
RUN chmod -R 755 /usr/share/nginx/html
EXPOSE 8080
# Not using daemon mode.
CMD ["openresty", "-g", "daemon off;"]

