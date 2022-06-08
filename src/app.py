import os
import time
import logging
import datetime
import socket
import redis

from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

logger = logging.getLogger('Flask server')
app.logger.addHandler(logging.StreamHandler())
app.logger.setLevel(logging.INFO)
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
app.logger.info("Server start at: {} at address: ".format(now, os.getenv('FLASK_PORT')))
app.logger.info("Author: {} {}".format(os.getenv('AUTHOR_FIRST_NAME'), os.getenv('AUTHOR_LAST_NAME')))


cache = redis.Redis(host='redis', port=os.getenv('REDIS_PORT'))


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    count = get_hit_count()
    address = request.remote_addr
    timezone = time.timezone
    now = datetime.datetime.now()
    local_now = now.astimezone()
    local_tz = local_now.tzinfo
    local_tzname = local_tz.tzname(local_now)
    now = now.strftime("%Y-%m-%d %H:%M:%S")
    return f"IP address: {address}\t, time: {now}, time zone: {local_tzname}, You visit site {count} times."
