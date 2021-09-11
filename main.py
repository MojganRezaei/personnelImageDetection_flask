from flask import Flask
from flask import request
from flask import jsonify
from src.DownloadImage import DownloadImage
from src.Detection import PersonnelDetection
app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def hello_world():
    download = DownloadImage(request.args.get('url'))
    download.download()
    detection = PersonnelDetection()
    return jsonify(detection.detection())
if __name__ == "__main__":
    app.run(host='127.0.0.1')