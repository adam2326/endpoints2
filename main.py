from flask import Flask
import random
import string


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index_page():
  word = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(5)])
  return '<html><body>{}</body></html>'.format(word)
