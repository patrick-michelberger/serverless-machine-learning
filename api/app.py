from flask import Flask
from flask import request
from flask import json
import boto3
import pickle

BUCKET_NAME = 'serverless-machine-learning'
MODEL_FILE_NAME = 'model.pkl'

app = Flask(__name__)

S3 = boto3.client('s3', region_name='eu-central-1')


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


@app.route('/', methods=['POST'])
def index():
    body_dict = request.get_json(silent=True)
    data = body_dict['data']

    prediction = predict(data)

    result = {'prediction': prediction}
    return json.dumps(result)


@memoize
def load_model(key):
    response = S3.get_object(Bucket=BUCKET_NAME, Key=key)
    model_str = response['Body'].read()

    model = pickle.loads(model_str)

    return model


def predict(data):
    model = load_model(MODEL_FILE_NAME)

    return model.predict(data).tolist()


if __name__ == '__main__':
    # listen on all IPs
    app.run(host='0.0.0.0')
