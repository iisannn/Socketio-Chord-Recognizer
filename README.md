
# Flask Socketio with Guitar Chord Recognizer
Utilize flask socketIo with feedforward neural network for live guitar chord recognition could later be implemented to A-frame. 



# Dependencies
suggest to create an conda virtual environmnment and set up in it. 

Make sure you have Python 3 installed, as well as the following libraries:
- [TensorFlow](https://www.tensorflow.org/install/)
- [Numpy](http://www.numpy.org/)
- [Sklearn](http://scikit-learn.org/stable/)
- [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/)
  * Note: PyAudio requires the prerequisite portaudio library to be installed. On Mac, this can be installed using homebrew.

# Usage

clone this repository,  run 

```
git clone https://github.com/iisannn/Socketio-Chord-Recognizer.git
cd Socketio-Chord-Recognizer
conda activate "ur virtual enviroment"　
python Live_demo2.py 
```

go to http://127.0.0.1:5000/ in your web browser 

# problem 
  the checkpoint in the neural network takes in a 2 channels wav file while web recording only allows one channel recording.


# References
- this neural network is built by nonnormcl (https://github.com/connormcl/chord_recognizer)
- Record audio wav file on html file with RecordRTC 
- connect web server communication with Flask_socketio 
- guitXR's github https://github.com/UWRealityLab/xrcapstone21sp-team4
