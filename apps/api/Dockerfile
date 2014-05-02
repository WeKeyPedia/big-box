FROM phusion/baseimage

RUN apt-get update

RUN apt-get install -y -q software-properties-common python-software-properties python g++ make
RUN add-apt-repository ppa:chris-lea/node.js

RUN apt-get update

RUN apt-get install -y -q nodejs

RUN apt-get install -y -q git

RUN npm install -g coffee-script
RUN npm install -g forever

RUN mkdir /server
RUN git clone https://github.com/WeKeyPedia/api /server/api

WORKDIR /server/api
RUN npm install

EXPOSE 3000

CMD forever -c coffee server.coffee