FROM phusion/baseimage

RUN apt-get update

RUN apt-get install -y -q software-properties-common python-software-properties python g++ make

RUN apt-get install -y git

RUN apt-get install -y python-pip
RUN apt-get install -y python-dev

RUN mkdir /server
RUN git clone https://github.com/WeKeyPedia/WKP-python-toolkit /server/python-toolkit

# VOLUME /server

WORKDIR /server/python-toolkit
RUN pip install -r requirements.txt
RUN pip install Celery

CMD "/bin/true"
