from flask import Flask
from flask import request
from flask import json

BUCKET_NAME = 'zappa-10z1mxwy2'
MODEL_FILE_NAME = 'model.pkl'
MODEL_LOCAL_PATH = '/tmp/' + MODEL_FILE_NAME

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    payload = json.loads(request.get_data().decode('utf-8'))
    prediction = predict(payload['payload'])
    data = {}
    data['data'] = prediction[-1]
    return json.dumps(data)


def load_model():
    print
    'Loading model from S3'


def predict(data):
    print
    'Making predictions'


if __name__ == '__main__':
    # listen on all IPs
    app.run(host='0.0.0.0')
