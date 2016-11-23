from flask import Flask, jsonify
import random
import string


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index_page():
  # perform some computation
  word = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(5)])
  # prepare the output
  json_response = jsonify(target_api='word_converter', word=word)
  # return the response
  return json_response
