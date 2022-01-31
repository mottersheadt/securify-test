import sys, getopt
import os.path
from dotenv import load_dotenv
import os
import logging
from app.main import app

# Require that the cert is created and stored so we can use it when reaching out to outbound target.
# Because the python requests library 
def load_cert():
  cert_file = '/app/keys/outbound-cert.pem'
  os.makedirs(os.path.dirname(cert_file), exist_ok=True)
  logging.info("Loading cert...")
  
  if os.path.exists(cert_file):
    logging.info("Deleted old cert...")
    os.remove(cert_file)

  with open(cert_file, "w") as f:
    logging.info("Wrote new cert to {0}".format(cert_file))
    f.write(os.environ['VGS_OUTBOUND_CERT'])

if __name__ == "__main__":
  load_dotenv()
  load_cert()

  debug = "debug" in sys.argv
  app.run(debug=debug)