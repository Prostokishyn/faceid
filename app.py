from flask import Flask, render_template, request, jsonify
import cv2
import base64
import numpy as np

app = Flask(__name__)
camera = cv2.VideoCapture(0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    success, frame = camera.read()
    if success:
        _, buffer = cv2.imencode('.jpg', frame)
        image_base64 = base64.b64encode(buffer).decode('utf-8')
        message = 'Image authenticated successfully.'
    else:
        message = 'Error capturing image from camera.'
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(debug=True)