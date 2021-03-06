from distutils.log import error
from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np
from pip import main
import logging

app = Flask(__name__)

# prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 12)
    loaded_model = pickle.load(open("model.pkl", "rb"))
    # loaded_model = pickle.load(open("https://pklfilestorage.file.core.windows.net/pklfile/model.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/')
def index():     
    return render_template('index.html')
 
@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        prediction = ValuePredictor(to_predict_list)    
        return render_template("prediction.html", prediction = prediction)
    if error:
        logging.basicConfig(filename='app.log')
        logging.error(error)

if __name__ == "__main__":
    app.run()