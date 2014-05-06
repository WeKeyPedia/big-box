/etc/init.d/rabbitmq-server start

rabbitmqctl add_user worker 98b4840644
rabbitmqctl add_vhost worker
rabbitmqctl set_permissions -p worker worker ".*" ".*" ".*"

/etc/init.d/rabbitmq-server stop