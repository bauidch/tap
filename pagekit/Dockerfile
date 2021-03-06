############################################################
# Dockerfile to build Pagekit with Nginx and PHP-fpm
# Based on Ubuntu
# Date: 07.03.2016
# Version: 0.0.1
############################################################
FROM ubuntu:14.04
MAINTAINER bauidch

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y update
RUN apt-get -y install nginx php5-fpm php5-json php5-cli php5-mysql php5-curl unzip git supervisor wget curl

RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer

RUN mkdir -p /pagekit/public_html
RUN mkdir -p /pagekit/logs
RUN mkdir -p /var/log/supervisor

WORKDIR /pagekit
RUN wget https://github.com/pagekit/pagekit/releases/download/0.10.4/pagekit-0.10.4.zip
RUN unzip pagekit-0.10.4.zip -d public_html/
RUN rm pagekit-0.10.4.zip

RUN chown -R www-data: /pagekit/public_html/

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD pagekit_web /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/pagekit_web /etc/nginx/sites-enabled/pagekit_web

RUN sed -e 's/;daemonize = yes/daemonize = no/' -i /etc/php5/fpm/php-fpm.conf
RUN sed -e 's/;listen\.owner/listen.owner/' -i /etc/php5/fpm/pool.d/www.conf
RUN sed -e 's/;listen\.group/listen.group/' -i /etc/php5/fpm/pool.d/www.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

CMD ["/usr/bin/supervisord"]
