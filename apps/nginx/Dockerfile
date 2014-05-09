FROM phusion/baseimage

RUN apt-get update
RUN apt-get -y install nginx

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN mkdir /etc/nginx/ssl

RUN apt-get install -y git

RUN apt-get -y install python-pip

RUN mkdir /server
RUN git clone https://github.com/WeKeyPedia/nginx-gateway /server/nginx/

EXPOSE 80

WORKDIR /server/nginx
RUN pip install -r requirements.txt

CMD /bin/sh start.sh