# WeKeyPedia BigBox

The WeKeyPedia BigBox allows you to bootstrap a fully functional dev environment to play with different parts of the architecture. It is also the blueprint to the core infrastructure that allows the project to run effeciently.

You will only need to install [Vagrant](htt://vagrantup.com) and be free to use any of your daily tools (text editor, macros, etc).

The architecture is following:

- the main host is running a CoreOS system
- all services runs their own privileged OS (ranging from ubuntu server to more simpler linux distribs). It allows different users to have a coherent environment

## install

```sh
$ git clone https://github.com/WeKeyPedia/big-box.git
$ cd big-box
$ git submodule init
$ git submodule update
$ vagrant up
```

It will fetch the [CoreOS](https://coreos.com) image, build the host and then build several [docker containers](http://docker.io) with all the needed services. It takes some minutes to build up everything. You can start relax and warm yourself for some coding meanwhile.

## workflow



## outside

You will be able to access to the playground at the [http://172.17.8.101/](http://172.17.8.101/). You only need a web browser

## inside

- wekeypedia
  - robot workerz. tsss tsss.
  - playground
  - api

- neo4j
- zeromq
- mongodb

## developer mode

All WeKeyPedia code is pulled twice.

1. A first legacy version is located in the  `/server/` folder and run the production code.
2. A second version is located in `/src/` and is sync to the vagrant host and the developer OS. You can start the related service in dev mode by using a `-dev` alias (e.g. `wekeypedia/worker-dev`)


### manual commands

start a service:

```
core@core-01 ~ $ sudo systemctl start neo4j
```

stop a service:

```
core@core-01 ~ $ sudo systemctl stop neo4j
```

open the web interfaces (you need the register manually the web services first)

```
core@core-01 ~ $ sudo systemctl start nginx-localhost

OR

core@core-01 ~ $ docker run -d -p 80:80 wekeypedia/nginx-localhost
```


