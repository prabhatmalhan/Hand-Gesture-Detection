# Import necessary libraries
from flask import Flask, render_template, Response
import cv2 as cv
from keras.models import model_from_json
import pickle as pkl
import json as js
from PreProcessor import cleanImg as cimg
import numpy as np
# Initialize the Flask app

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("model.h5")

with open('class_label', 'rb') as f:
    classLabel = pkl.load(f)

classLabel = {str(value): key for key, value in classLabel.items()}

with open('config.json', 'r') as f:
    p = js.load(f)['gesture']

pred = ' '


app = Flask(__name__)

video = cv.VideoCapture(0)


def gen_frames():
    while True:
        try:

            success, frame = video.read()  # read the camera frame
            if not success:
                break
            else:
                frame = cv.flip(frame, 1)
                cropRegion = frame[50:350, 250:550]
                cv.rectangle(frame, (250, 50), (550, 350), (0, 255, 0), 2)
                cv.waitKey(60)

                cropRegion = cimg(cropRegion)
                cropRegion = cropRegion.reshape(200, 200, 1)

                pred = np.round(loaded_model.predict(np.array([cropRegion])))
                ind = np.where(pred[0] == 1.)
                if(len(ind[0])) > 0:
                    pred = p[classLabel[str(ind[0][0])]]

                cv.putText(frame, pred, (50, 450),
                           fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 0, 255), thickness=2)
                ret, buffer = cv.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        except:
            pass


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)
