import sys, getopt
from dotenv import load_dotenv
from app.main import app

if __name__ == "__main__":
  load_dotenv()
  debug = "debug" in sys.argv
  app.run(debug=debug)