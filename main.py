# Server
import RPi.GPIO as GPIO
from flask import Flask, render_template
from flask_socketio import SocketIO, send

led = 14
app = Flask(__name__)
socketio = SocketIO(app)

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

@app.route('/')
def index():
    return "Server running"

@app.route('/turn_on')
def turn_on_web():
    try:
        GPIO.output(led, True)
    except:
        return "Ocurrió un error"
    return "Se prendió el led"

@app.route('/turn_off')
def turn_off_web():
    try:
        GPIO.output(led, False)
    except:
        return "Ocurrió un error"
    return "Se apagó el led"

@socketio.on('turn_on')
def turn_on():
    GPIO.output(led, True)

@socketio.on('turn_off')
def turn_off():
    GPIO.output(led, True)


if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0')