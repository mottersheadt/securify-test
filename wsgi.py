import sys, getopt
import os.path
import os
import logging
from app.main import app

if __name__ == "__main__":
  debug = "debug" in sys.argv
  app.run(debug=debug)
