import sys, getopt
import os.path
from dotenv import load_dotenv
import os
from app.main import app

# Require that the cert is created and stored so we can use it when reaching out to outbound target.
# Because the python requests library 
def load_cert():
  cert_file = '/keys/outbound-cert.pem'
  os.makedirs(os.path.dirname(cert_file), exist_ok=True)

  if os.path.exists(cert_file):
    os.remove(cert_file)

  with open(cert_file, "w") as f:
      f.write(os.environ['VGS_OUTBOUND_CERT'])

if __name__ == "__main__":
  load_dotenv()
  load_cert()

  debug = "debug" in sys.argv
  app.run(debug=debug)