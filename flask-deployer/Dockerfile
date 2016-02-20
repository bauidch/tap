############################################################
# Dockerfile to build Nginx with uwsgi for flask apps
# Based on Ubuntu
############################################################
FROM ubuntu:14.04

MAINTAINER bauidch

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get -y install nginx sed python3-pip python3-dev uwsgi-plugin-python supervisor

# Make logs dir
RUN mkdir -p /var/log/nginx/app
RUN mkdir -p /var/log/uwsgi/app/
RUN mkdir -p /var/log/supervisor

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN rm /etc/nginx/sites-enabled/default
COPY flask-deployer.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/flask-deployer.conf /etc/nginx/sites-enabled/flask-deployer.conf
COPY uwsgi.ini /usr/share/nginx/html/
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

RUN pip install uwsgi flask pymongo

CMD ["/usr/bin/supervisord"]
