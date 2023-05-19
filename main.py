from flask import Flask, request, make_response, jsonify
import constants, general, configs
import pickle
from urllib.request import urlopen

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/play-tennis/local', methods=['POST'])
def predictPlayTennisLocal():
    try:
        data = general.getData(request)
        loadedModel = pickle.load(open(constants.LOCAL_MODEL, 'rb'))
        result = loadedModel.predict([data])[0]
    
    except Exception as error:
        return make_response(jsonify({
            'error': str(error)
        }), 500)

    return general.makeResponse(result, constants.MODEL_TYPE['local'])

@app.route('/play-tennis/gcs', methods=['POST'])
def predictPlayTennisGCS():
    try:
        data = general.getData(request)
        loadedModel = pickle.load(urlopen(constants.GCS_MODEL))
        result = loadedModel.predict([data])[0]

    except Exception as error:
        return make_response(jsonify({
            'error': str(error)
        }), 500)

    return general.makeResponse(result, constants.MODEL_TYPE['gcs'])

@app.route('/play-tennis/drive', methods=['POST'])
def predictPlayTennisDrive():
    try:
        data = general.getData(request)
        loadedModel = pickle.load(urlopen(constants.DRIVE_MODEL))
        result = loadedModel.predict([data])[0]

    except Exception as error:
        return make_response(jsonify({
            'error': str(error)
        }), 500)

    return general.makeResponse(result, constants.MODEL_TYPE['drive'])

app.run(port=configs.PORT)