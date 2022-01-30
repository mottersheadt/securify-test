import sys
from flask import Flask, jsonify, request
from flask_cors import CORS
from app.src import business
import logging;

app = Flask('app.main')

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
app.logger.addHandler(handler)
app.logger.setLevel(logging.DEBUG)

# enable CORS
CORS(app, resources={'/*': {'origins': '*'}})

@app.route('/', methods=['POST', 'GET'])
def submit_data():
  count = business.submit(request.args, request.json)
  app.logger.info(request.json)
  return jsonify({
    "count": count,
    "body": request.json
  })
