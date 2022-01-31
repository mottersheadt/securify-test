from datetime import datetime
import logging
import os
import sys
from .client import VgsClient

log = logging.getLogger('app.main.business')

def retrieve(secure_data):
    load_cert()
    log.info("Retrieving secured data for token: {0}".format(secure_data))
    client = VgsClient(
        os.environ['VGS_USERNAME'],
        os.environ['VGS_PASSWORD'],
        os.environ['VGS_TENANT_ID'],
        '/app/keys/outbound-cert.pem',
        os.environ['VGS_PROXY_BASE'])
    retrieved_data = client.retrieve(secure_data)
    return retrieved_data


# Require that the cert is created and stored so we can use it when reaching out to outbound target.
# Because the python requests library 
def load_cert():
  cert_file = '/app/keys/outbound-cert.pem'
  
  if not os.path.exists(cert_file):
    logging.info("Loading cert...")
    os.makedirs(os.path.dirname(cert_file), exist_ok=True)
    with open(cert_file, "w") as f:
      logging.info("Wrote new cert to {0}".format(cert_file))
      f.write(os.environ['VGS_OUTBOUND_CERT'])
