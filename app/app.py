from flask import Flask
from flask import request
import pickle
import numpy as np
import json
import os


def process_input(request_data: str) -> np.array:
    '''
    transforms JSON type data acquired from request and transforms it into 2D array the model understands
    :param posted_data:
    :return:np.array
    '''
    parsed_body = np.asarray(json.loads(request_data)["features"])
    assert len(parsed_body.shape) == 2, "'inputs' must be a 2-d array"
    return parsed_body

working_dir = os.getcwd()
SAVED_MODEL_PATH = working_dir + "/app/models/model.pkl"

model = pickle.load(open(SAVED_MODEL_PATH, "rb"))

app = Flask(__name__)

@app.route("/")
def home() -> str:
    return("This is a house pricing prediction app"),200

@app.route("/predict", methods=["POST"])
def predict() -> str:
     '''
    loads the data acquired from request to the model and returns the predicted value
    :return: prediction
    '''
    try:
        input_params = process_input(request.data)
        predictions = model.predict(input_params)
        return json.dumps({"predicted price": predictions.tolist()})
    except (KeyError, json.JSONDecodeError, AssertionError):
        return json.dumps({"error": "CHECK INPUT"}), 400
    except:
        return json.dumps({"error": "PREDICTION FAILED"}), 500
