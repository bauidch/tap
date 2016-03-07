############################################################
# Dockerfile to build Pagekit with Nginx and PHP-fpm
# Based on Ubuntu
############################################################
FROM ubuntu:14-04

MAINTAINER bauidch

ENV DEBIAN_FRONTEND noninteractive

RUN echo 'deb http://us.archive.ubuntu.com/ubuntu/ precise universe' >> /etc/apt/sources.list
RUN apt-get -y update
RUN apt-get -y install nginx php5-fpm php5-json php5-cli php5-mysql php5-curl unzip git supervisor nano

RUN git clone git://github.com/pagekit/pagekit.git
RUN chown -R www-data:www-data /pagekit

WORKDIR /pagekit

# Install Composer
RUN php -r "readfile('https://getcomposer.org/installer');" | php
RUN php ./composer.phar install

# Make logs dir
RUN mkdir -p /var/log/nginx/app
RUN mkdir -p /var/log/supervisor

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN rm /etc/nginx/sites-enabled/default
COPY pagekit.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/pagekit.conf /etc/nginx/sites-enabled/pagekit.conf

RUN sed -e 's/;daemonize = yes/daemonize = no/' -i /etc/php5/fpm/php-fpm.conf
RUN sed -e 's/;listen\.owner/listen.owner/' -i /etc/php5/fpm/pool.d/www.conf
RUN sed -e 's/;listen\.group/listen.group/' -i /etc/php5/fpm/pool.d/www.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

CMD ["/usr/bin/supervisord"]
