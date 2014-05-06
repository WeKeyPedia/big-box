from celery import Celery

import os


rabbitmq_host = os.environ['RABBITMQ_PORT_5672_TCP_ADDR']
mongodb_host = os.environ['MONGODB_PORT_27017_TCP_ADDR']

BROKER_URL = 'amqp://worker:98b4840644@%s:5672/worker'  % (rabbitmq_host)
RESULTS_URL = 'mongodb://%s:27017//' % (mongodb_host)

print "broker host: %s" % (BROKER_URL)
print "results host: %s" % (RESULTS_URL)

app = Celery(broker=BROKER_URL)

app.conf.update(
#  CELERY_BROKER_URL=BROKER_URL,
  CELERY_RESULT_BACKEND=RESULTS_URL,
  CELERY_ACCEPT_CONTENT = ['application/json']
)