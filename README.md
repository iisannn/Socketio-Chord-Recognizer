
# Flask Socketio with Guitar Chord Recognizer
Utilize Flask SocketIo with feedforward neural network for live guitar chord recognition could later be implemented to A-frame. 



# Dependencies
Suggest to create an conda virtual environmnment and install Python3. 

Make sure you have Python 3 installed, as well as the following libraries:
- [TensorFlow](https://www.tensorflow.org/install/)
- [Numpy](http://www.numpy.org/)
- [Sklearn](http://scikit-learn.org/stable/)
- [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/)
- [Flask](https://flask-socketio.readthedocs.io/en/latest/intro.html#installation)


# Usage

clone this repository,  run 

```
git clone https://github.com/iisannn/Socketio-Chord-Recognizer.git
cd Socketio-Chord-Recognizer
conda activate "ur virtual enviroment"　
python Live_demo2.py 
```

go to http://127.0.0.1:5000/ in your web browser 

# Problem facing
  the checkpoint in the neural network takes in a 2 channels wav file while web recording only allows one channel recording. 


# References
- This neural network is built by nonnormcl (https://github.com/connormcl/chord_recognizer)
- Record audio wav file on html file with RecordRTC 
- Connect web server communication with Flask_socketio 
- guitXR's github https://github.com/UWRealityLab/xrcapstone21sp-team4
