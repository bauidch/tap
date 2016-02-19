FROM ubuntu

MAINTAINER bauidch

RUN echo "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -sc) main universe" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential
RUN apt-get install -y python python-dev python-distribute python-pip

ADD /pydata /pydata

RUN pip install -r /pydata/requirements.txt

EXPOSE 80

WORKDIR /pydata

CMD python server.py
