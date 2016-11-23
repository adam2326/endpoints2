from flask import Flask, jsonify
import random
import string


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index_page():
  word = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(5)])
  json_resp = jsonify(target_api='word_converter', word=word)
  return '<html><body>{}</body></html>'.format(json_response)
