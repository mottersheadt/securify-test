from datetime import datetime
import logging
import sys
from . import client

log = logging.getLogger('app.main.business')

def receive(secure_data):
    log.info("Received secured data", secure_data)
    return secure_data