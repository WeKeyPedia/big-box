FROM phusion/baseimage

RUN apt-get update

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv F7B8CEA6056E8E56
RUN echo "deb http://www.rabbitmq.com/debian/ testing main" > /etc/apt/sources.list.d/rabbitmq.list

RUN apt-get update

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get install -y rabbitmq-server
RUN /usr/sbin/rabbitmq-plugins enable rabbitmq_management

# RUN apt-get install -y scutil

ENV HOSTNAME rabbitmq

ADD set_user.sh set_user.sh
RUN sh set_user.sh

EXPOSE 5672 15672 4369

EXPOSE 27017

CMD /usr/sbin/rabbitmq-server