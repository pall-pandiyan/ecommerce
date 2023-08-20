FROM nginx:1.24.0

# install logrotate
RUN apt-get update && apt-get -y install logrotate

# copy my configs
copy default.conf /etc/nginx/conf.d/default.conf
copy logrotate_nginx.conf /etc/logrotate.d/nginx

# start nginx and cron as a service
cmd service cron start && nginx -g 'daemon off;'
