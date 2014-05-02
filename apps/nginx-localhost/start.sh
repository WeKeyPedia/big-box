#!/bin/bash
/bin/sed -i "s/<api_addr>/${API_PORT_3000_TCP_ADDR}/" /etc/nginx/sites-available/default
/bin/sed -i "s/<api_port>/${API_PORT_3000_TCP_PORT}/" /etc/nginx/sites-available/default
nginx