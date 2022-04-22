FROM nginx:latest
EXPOSE  80
COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY ./uwsgi_params /etc/nginx/uwsgi_params
USER root
RUN mkdir -p /vol/static
RUN chmod 755 /vol/static


CMD ["nginx", "-g", "daemon off;"]