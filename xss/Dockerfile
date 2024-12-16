FROM public.ecr.aws/eks-distro-build-tooling/eks-distro-minimal-base-nginx:latest-al23 AS deploy

# Change owner to allow non-root users to start the service
USER root
RUN <<EOF
mkdir -p /var/log/nginx
chown -R nginx:nginx /var/log/nginx
touch /run/nginx.pid
chown -R nginx:nginx /run/nginx.pid
EOF

COPY nginx.conf /etc/nginx/nginx.conf
COPY *.html /usr/share/nginx/html/

EXPOSE 8080
USER nginx
CMD ["nginx", "-g", "daemon off;"]
