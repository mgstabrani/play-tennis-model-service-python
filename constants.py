import configs

OUTLOOK_VALUES = {
    'Overcast': 0,
    'Rain': 1,
    'Sunny': 2
}

TEMP_VALUES = {
    'Cool': 0,
    'Hot': 1,
    'Mild': 2
}

HUMIDITY_VALUES = {
    'High': 0,
    'Normal': 1
}

WIND_VALUES = {
    'Strong': 0,
    'Weak': 1
}

PLAY_VALUES = {
    0: 'No',
    1:'Yes'
}

LOCAL_MODEL = configs.LOCAL_MODEL_PATH
GCS_MODEL = configs.GCS_MODEL_URL
DRIVE_MODEL = configs.DRIVE_MODEL_URL

MODEL_TYPE = {
    'local': 'Local',
    'gcs': 'Google Cloud Storage',
    'drive': 'Google Drive'
}