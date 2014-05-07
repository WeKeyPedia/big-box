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
RUN git clone https://github.com/WeKeyPedia/playground-web /server/playground

WORKDIR /server/playground
RUN npm install -g bower
RUN npm install -g brunch
RUN bower install --allow-root --config.interactive=false
RUN npm install

EXPOSE 3000

CMD brunch watch & forever -c coffee server.coffee