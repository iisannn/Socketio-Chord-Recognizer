import json
from types import FrameType
from typing import Type
from flask.json import jsonify
from flask.templating import render_template
import numpy as np
import tensorflow as tf
import wave, HPCP, config
import pyaudio
from network import Network
from flask import Flask
from flask import url_for
from  flask_socketio  import SocketIO, emit
from network import Network
import os, signal
import base64
from datauri import DataURI
from urllib.request import urlopen

app = Flask(__name__)
app.config['SECRET_KEY'] = 'difjeo4ihgjlkfn'
socketio = SocketIO(app, cors_allowed_origins="*")
chords = config.chords
WAVE_OUTPUT_FILENAME = "raw_chord.wav"
def print_probs(probs):
	indices = np.argsort(probs)[::-1]
	for i in range(5):
		print("P(%s) = %.2f%%, " % (chords[indices[i]], probs[indices[i]]*100), end='')
	print()

@app.route('/')
def sessions():
    return render_template('/index.html')

@socketio.on('stopsever')
def stopServer():
    os.kill(os.getpid(), signal.SIGINT)
    return jsonify({ "success": True, "message": "Server is shutting down..." })  


@socketio.on('connect', namespace= "/testone")
def client_connect():
    print('client connected')

@socketio.on('disconnect')
def client_disconnect():
    print('client disconnected')

@socketio.on('wav')
def Live_demo2(files):
    p = pyaudio.PyAudio()
    print('file received')
    waveFilesURL = files['audio']['dataURL'] #[43:]
    emit('confirmation','file received')
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 4

    net = Network('checkpoints/model0.ckpt')
    net.start_live_session()
    #while True: 
    f = urlopen(waveFilesURL)
    frames = []   
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        decoded_data = f.read(CHUNK)
        frames.append(decoded_data)
    f.close()
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(1)##need to make it 2.
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(44100)
    wf.writeframes(b''.join(frames))
    wf.close()
    chroma = HPCP.hpcp(WAVE_OUTPUT_FILENAME, norm_frames=False, win_size=4096, hop_size=1024, output='numpy')
    avg_chroma = np.mean(chroma, axis=0)
    avg_chroma /= sum(avg_chroma)
        #probs = net.live_sess.run(net.pred_probs, feed_dict={net.input: avg_chroma.reshape((1,12))})[0]
    responsebig =  net.classify(avg_chroma)
    print(responsebig)
    emit('results',responsebig)
 


if __name__ == '__main__':
    socketio.run(app, debug=True)
