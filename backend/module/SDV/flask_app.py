from sdv.single_table import CTGANSynthesizer
import pandas as pd
import base64
import time
import threading

from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
from os.path import join, dirname, realpath
import json
from flask_cors import CORS

def to_json(obj):
    return json.dumps(obj, default=lambda obj: obj.__dict__)

allowed_origin = os.environ.get("ALLOWED_ORIGIN", "http://localhost")

app = Flask(__name__)


CORS(app, resources={r"/*": {"origins": allowed_origin}})


# Get the uploaded files
@app.route("/upload", methods=['POST'])
def uploadFiles():
      # get the uploaded file
      print("UPLOAD PYTHON")
      uploaded_file =  pd.read_csv(request.files['file'])
      data = uploaded_file
      #data = data.to_json(orient = 'columns')  
      #print(data)
      #print(uploaded_file)
      metadata = SingleTableMetadata()

      metadata.detect_from_dataframe(
        data=uploaded_file
      )
      #meta = metadata
      synthesizer = CTGANSynthesizer(metadata)
      synthesizer.fit(data)

      synthetic_data = synthesizer.sample(num_rows=10)
      out = synthetic_data.to_json(orient = 'columns')  

      #print(synthetic_data)
      #df_header = synthetic_data.columns.values.tolist()
      #df_header = [df_header]
      #df_list = synthetic_data.values.tolist()
      #out = df_header+df_list
      JSONP_data = jsonify(out)
      return JSONP_data

      




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)