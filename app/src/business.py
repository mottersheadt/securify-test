from datetime import datetime
import logging
import os
import sys
from .client import VgsClient

log = logging.getLogger('app.main.business')

def retrieve(secure_data):
    log.info("Retrieving secured data for token: {0}".format(secure_data))
    client = VgsClient(
        os.environ['VGS_USERNAME'],
        os.environ['VGS_PASSWORD'],
        os.environ['VGS_TENANT_ID'],
        '/keys/outbound-cert.pem',
        os.environ['VGS_PROXY_BASE'])
    retrieved_data = client.retrieve(secure_data)
    return retrieved_data