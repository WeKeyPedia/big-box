FROM phusion/baseimage

RUN apt-get update
RUN apt-get -y install nginx

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN mkdir /etc/nginx/ssl
ADD nginx.default /etc/nginx/sites-available/default
ADD start.sh start.sh

EXPOSE 80

CMD /bin/sh ./start.sh