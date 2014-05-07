# WeKeyPedia BigBox

The WeKeyPedia BigBox allows you to bootstrap a fully functional dev environment to play with different parts of the architecture. It is also the blueprint to the core infrastructure that allows the project to run effeciently.

You will only need to install [Vagrant](htt://vagrantup.com) and be free to use any of your daily tools (text editor, macros, etc).

The architecture is following:

- the main host is running a CoreOS system
- all services runs their own privileged OS (ranging from ubuntu server to more simpler linux distribs). It allows different users to have a coherent environment

## install

```
# git clone https://github.com/WeKeyPedia/big-box.git
# cd big-box
# git submodule init
# vagrant up
```

It will fetch the CoreOs image, build the host and then build several docker containers with all the needed service. It takes some minutes to build up everything. You can start relax and warm yourself for some coding meanwhile.

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
- mongodv

## developer mode

All WeKeyPedia code is pulled twice.

1. A first legacy version is located in the  `/server/` folder and run the production code.
2. A second version is located in `/src/` and is sync to the vagrant host and the developer OS. You can start the related service in dev mode by using a `-dev` alias (e.g. `wekeypedia/worker-dev`)