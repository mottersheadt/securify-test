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

@app.route('/submit', methods=['POST'])
def submit():
  result = request.json['secret_data']
  return jsonify(result)


@app.route('/retrieve', methods=['GET'])
def retrieve():
  token = request.args['token']
  retrieved = business.retrieve(token)
  return jsonify({
    'secret_data': retrieved
  })