WKPZ-python-toolkit
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