from datetime import time
from os import abort, name
import time
import flask
from flask import request, jsonify, abort
import math
import os
import ssl
from flask.helpers import make_response
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)
app.config["DEBUG"] = True
# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

password = "6e2ef669"

# Create some test data for our catalog in the form of a list of dictionaries.
data = []

def addHeaders(data):
    response = make_response(data)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route('/health', methods=['GET'])
@cross_origin()
def health():
    return jsonify("healthy")

@app.route('/api/v1/getOtp', methods=['GET'])
@cross_origin()
def getOTP():
    return jsonify(data)


@app.route('/api/v1/store', methods=['POST'])
@cross_origin()
def storeOTP():
    data.clear()
    if 'otp' in request.form and 'password' in request.form:
        if str(request.form['password']) != password:
            otp = int(request.form['otp'])
            item = {}
            item['otp'] = otp
            item['timestamp'] = math.floor(time.time())
            data.append(item)
            return jsonify("recorded")
        else: abort(404)
    else:
        abort(404)


# context = ssl.SSLContext()
# context.load_cert_chain('server.cert', 'server.key')
app.run(port=int("8123"))