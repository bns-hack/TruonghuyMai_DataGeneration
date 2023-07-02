#from sdv.datasets.local import load_csvs
#from sdv.datasets.demo import download_demo
#from sdv.metadata import SingleTableMetadata
#import pandas as pd

#print("tests")
#try:
    #datasets = load_csvs(folder_name='HepatitisCdata.csv')
   #test = pd.read_csv("HepatitisCdata.csv")
#except ValueError:
  #print('You have not uploaded any csv files. Using some demo data instead.')

#print (test)
#datasets=test
#print(datasets.keys())

#metadata = SingleTableMetadata()

#metadata.detect_from_dataframe(
    #data=datasets
#)

#print(metadata)
#metadata.validate()

#from sdv.single_table import CTGANSynthesizer

#synthesizer = CTGANSynthesizer(metadata)
#synthesizer.fit(datasets)

#synthetic_data = synthesizer.sample(num_rows=10)

#print(synthetic_data)



from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
from os.path import join, dirname, realpath
import json

def to_json(obj):
    return json.dumps(obj, default=lambda obj: obj.__dict__)


app = Flask(__name__)

# enable debugging mode
app.config["DEBUG"] = True

# Upload folder
UPLOAD_FOLDER = 'staticfiles'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

meta = ""
data = ""
# Root URL
@app.route('/')
def index():
     # Set The upload HTML template '\templates\index.html'
    return render_template('index.html')



# Get the uploaded files
@app.route("/", methods=['POST'])
def uploadFiles():
      # get the uploaded file
      uploaded_file =  pd.read_csv(request.files['file'])
      data = uploaded_file
      #print(uploaded_file)
      #metadata = SingleTableMetadata()

      #metadata.detect_from_dataframe(
        #data=uploaded_file
      #)
      #meta = metadata
      #synthesizer = CTGANSynthesizer(meta)
      #synthesizer.fit(data)

      #synthetic_data = synthesizer.sample(num_rows=10)
      #print(synthetic_data)
      #df_header = synthetic_data.columns.values.tolist()
      #df_header = [df_header]
      #df_list = synthetic_data.values.tolist()
      #out = df_header+df_list
      JSONP_data = jsonify(data)
      return JSONP_data

      




if (__name__ == "__main__"):
     app.run(port = 5000)