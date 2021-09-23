# House Price Prediction Flask Application
## Description
This project involves building a machine learning model  to predict house prices and deploying it to the cloud(heroku)

## Getting Started
The app api can be found here - [House Prediction API](https://bhouse-prices-prediction.herokuapp.com/).
To predict house prices using the app, send a post request [here]( https://bhouse-prices-prediction.herokuapp.com/predict).
The predict endpoint takes only POST requests and request made to the endpoint should come with ```features```
as part of the request data. 

## Usage
Post request should be made using a list with 13 numbers. 2 lists can also be passed into the request.

```python
import json

url = "https://bhouse-prices-prediction.herokuapp.com/predict"
data =  {"features": [[1069e-01, 0.0000e+00, 1.3890e+01, 1.0000e+00, 5.5000e-01, 5.9510e+00, 9.3800e+01, 2.8893e+00, 45.0000e+00, 2.7600e+02, 1.6400e+01, 3.9690e+02, 1.7920e+01]]}

post_data = json.dumps(data)
resp = requests.post(url, data=post_data)
print(resp.status_code, resp.content)
```
```python
import json

url = "https://bhouse-prices-prediction.herokuapp.com/predict"
data = {"features": [[1069e-01, 0.0000e+00, 1.3890e+01, 1.0000e+00, 5.5000e-01, 5.9510e+00, 9.3800e+01, 2.8893e+00, 45.0000e+00, 2.7600e+02, 1.6400e+01, 3.9690e+02, 1.7920e+01],[6.320e-03, 1.800e+01, 2.310e+00, 0.000e+00, 5.380e-01, 6.575e+00,
       6.520e+01, 4.090e+00, 1.000e+00, 2.960e+02, 1.530e+01, 3.969e+02,
       4.980e+00]]}

post_data = json.dumps(data)
resp = requests.post(url, data=post_data)
print(resp.status_code, resp.content)
```

## License
The MIT License - Copyright (c) 2021 - Blessing Agadagba