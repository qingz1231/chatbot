

from flask import Flask, jsonify, request
# import nltk
# from nltk.stem import WordNetLemmatizer
# lemmatizer = WordNetLemmatizer()
# import pickle
# import numpy as np
# import re
# from keras.models import load_model

app = Flask(__name__)

@app.route('/message', methods=['GET'])
def get_data():
    # message = request.args.get('message', 'Anonymous')

    data = {'message': 'Hello from the API!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)