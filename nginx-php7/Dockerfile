############################################################
# Dockerfile to build Nginx and PHP7-fpm
# Based on Ubuntu
# Date: 10.03.2016
# Version: 0.0.1
############################################################
FROM ubuntu:14.04
MAINTAINER bauidch

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y install software-properties-common
RUN add-apt-repository ppa:ondrej/php
RUN apt-get -y update
RUN apt-get purge php5-*
RUN apt-get autoremove
RUN apt-get -y install nginx php7.0-fpm php7.0-json php7.0-cli php7.0-mysql php7.0-curl unzip git supervisor wget curl

RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer

RUN mkdir -p /htdocs/public_html
RUN mkdir -p /htdocs/logs
RUN mkdir -p /var/log/supervisor

WORKDIR /htdocs

RUN chown -R www-data: /htdocs/public_html/

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD web_side /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/web_side /etc/nginx/sites-enabled/web_side

RUN sed -e 's/;daemonize = yes/daemonize = no/' -i /etc/php7.0/fpm/php-fpm.conf
RUN sed -e 's/;listen\.owner/listen.owner/' -i /etc/php7.0/fpm/pool.d/www.conf
RUN sed -e 's/;listen\.group/listen.group/' -i /etc/php7.0/fpm/pool.d/www.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

CMD ["/usr/bin/supervisord"]
