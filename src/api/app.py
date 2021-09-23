from flask import Flask
from flask import request
import pickle
import numpy as np
import json


def process_input(request_data: str) -> np.array:
    parsed_body = np.asarray(json.loads(request_data)["features"])
    assert len(parsed_body.shape) == 2, "'inputs' must be a 2-d array"
    return parsed_body

SAVED_MODEL_PATH = "House-prices-prediction\src\models\model.pkl"

# LOADING THE CLASSIFIER FROM FILE
model = pickle.load(open(SAVED_MODEL_PATH, "rb"))

app = Flask(__name__)

@app.route("/")
def home() -> str:
    return("This is a house pricing prediction app"),200

@app.route("/predict", methods=["POST"])
def predict() -> str:
    try:
        input_params = process_input(request.data)
        predictions = model.predict(input_params)
        return json.dumps({"predicted price": predictions.tolist()})
    except (KeyError, json.JSONDecodeError, AssertionError):
        return json.dumps({"error": "CHECK INPUT"}), 400
    except:
        return json.dumps({"error": "PREDICTION FAILED"}), 500
app.run()