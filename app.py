from flask import Flask, request, jsonify, render_template
import tensorflow as tf 
import numpy as np
import math
from waitress import serve #Production Environment
app = Flask(__name__)
model = tf.keras.models.load_model('model')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = math.ceil(prediction[0])

    return render_template('index.html', prediction_text='Y should be {} ± 2'.format(output))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = math.ceil(prediction[0])
    return jsonify(output)

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=5000,debug=True)
    serve(app, host='0.0.0.0', port=5000)