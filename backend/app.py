


import pandas as pd
import base64
import time
import threading
import requests
from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
from os.path import join, dirname, realpath
import json
from flask_cors import CORS

def to_json(obj):
    return json.dumps(obj, default=lambda obj: obj.__dict__)

allowed_origin = os.environ.get("ALLOWED_ORIGIN", "http://localhost")
#allowed_origin = os.environ.get("ALLOWED_ORIGIN", "http://localhost:*")

app = Flask(__name__)


CORS(app, resources={r"/*": {"origins": allowed_origin}})

# Get the uploaded files
@app.route("/upload", methods=['POST'])
def uploadFiles():
      print("UPLOAD PYTHON")
   
      url = "http://52.36.211.168/upload"
      test_response = requests.post(url, files = {"file": request.files['file']})

      print(test_response.text)
      if test_response.ok:
        print("Upload completed successfully!")
        print(test_response.text)
        return test_response.text
      else:
        print("Something went wrong!")
        return "Error"
     
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)