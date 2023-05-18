import constants
from flask import jsonify, make_response

def getData(request):
    body = request.json
    outlook = body['outlook']
    temp = body['temp']
    humidity = body['humidity']
    wind = body['wind']

    data = [
        constants.OUTLOOK_VALUES[outlook],
        constants.TEMP_VALUES[temp],
        constants.HUMIDITY_VALUES[humidity],
        constants.WIND_VALUES[wind]
    ]

    return data

def makeResponse(result, modelType):
    return make_response(jsonify(
        {
            'message': 'Success',
            'data': {
                'modelType': modelType,
                'play': constants.PLAY_VALUES[result]
            }
        }
    ))