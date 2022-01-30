from datetime import datetime
import logging
import sys
from . import client

log = logging.getLogger('app.main.business')

def submit(unsecure_data):
    log.info("Submitting unsecure data")
    secure_data = client.secure(unsecure_data)
    return secure_data