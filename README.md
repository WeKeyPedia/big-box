# WeKeyPedia BigBox

The WeKeyPedia BigBox allows you to bootstrap a fully functional dev environment to play with different parts of the architecture. It is also the blueprint to the core infrastructure that allows the project to run effeciently.

You will need to install [Vagrant](htt://vagrantup.com).

The architecture is following:

- the main host is running a CoreOS system
- all services runs their own privileged OS (ranging from ubuntu server to more simpler linux distribs). It allows different users to have a coherent environment

## install

```
# git clone https://github.com/WeKeyPedia/big-box.git
# cd big-box
# vagrant up
```

## outside

You will be able to access to the playground at the [http://172.17.8.101/](http://172.17.8.101/). You only need a web browser

## inside

- wekeypedia
  - playground
  - api

- neo4j
- zeromq