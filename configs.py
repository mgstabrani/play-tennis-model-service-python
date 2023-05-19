from dotenv import load_dotenv
import os

load_dotenv()

PORT = os.environ['PORT']

LOCAL_MODEL_PATH = os.environ['LOCAL_MODEL_PATH']
GCS_MODEL_URL = os.environ['GCS_MODEL_URL']
DRIVE_MODEL_URL = os.environ['DRIVE_MODEL_URL']