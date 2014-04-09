WeKeyPedia python toolkit [![Build Status](https://travis-ci.org/WeKeyPedia/WKP-python-toolkit.png?branch=master)](https://travis-ci.org/WeKeyPedia/WKP-python-toolkit) [![Coverage Status](https://coveralls.io/repos/WeKeyPedia/WKP-python-toolkit/badge.png?branch=master)](https://coveralls.io/r/WeKeyPedia/WKP-python-toolkit?branch=master)
===================

## basic tasks

provide a list of keywords and get the network structure from wikipedia

```
$ python retrieve_wikipedia_network.py yourdata.txt
```

## workers

### examples

launch 2 workers with one prefork cpu each:

```
$ celery multistart w1 w2 -c 1
```