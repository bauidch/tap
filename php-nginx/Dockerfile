############################################################
# Dockerfile to build Nginx with PHP-fppm
# Based on Ubuntu
# Version: 0.0.1
############################################################
FROM ubuntu:14.04
MAINTAINER bauidch

ENV DEBIAN_FRONTEND noninteractives

RUN apt-get -y update
RUN apt-get -y install nginx php5-fpm php5-json php5-cli php5-mysql php5-curl unzip git supervisor wget curl

RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer

RUN mkdir -p /www/public_html
RUN mkdir -p /www/logs
RUN mkdir -p /var/log/supervisor

WORKDIR /www
RUN chown -R www-data: /www/public_html/

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN rm /etc/nginx/sites-enabled/default
COPY web_php /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/web_php /etc/nginx/sites-enabled/web_php

RUN sed -e 's/;daemonize = yes/daemonize = no/' -i /etc/php5/fpm/php-fpm.conf
RUN sed -e 's/;listen\.owner/listen.owner/' -i /etc/php5/fpm/pool.d/www.conf
RUN sed -e 's/;listen\.group/listen.group/' -i /etc/php5/fpm/pool.d/www.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

CMD ["/usr/bin/supervisord"]
