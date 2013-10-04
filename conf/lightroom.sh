#!/bin/bash
set -e
LOGFILE=/var/log/lightroom.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3
# user/group to run as
USER=www-data
GROUP=www-data
cd /srv/lightroom/lightroom
exec ../bin/gunicorn_django -w $NUM_WORKERS 
    --user=$USER --group=$GROUP --log-level=debug 
    --log-file=$LOGFILE 2>>$LOGFILE
