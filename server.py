from flask import Flask, Response, render_template
from camera import MyCamera

app = Flask(__name__)


@app.route('/')

def index():
	return render_template('index.html')

def gen(cam):
	while True:
		frame = cam.get_frame()
		yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(MyCamera(0,400,300)),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
		
if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 8314, debug=True)
