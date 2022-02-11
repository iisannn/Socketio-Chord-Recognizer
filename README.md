
# Flask Socketio with Guitar Chord Recognizer
Utilize flask socketIo with Feedforward neural network for live guitar chord recognition could potentially be implement to A-frame. 


# Dependencies
Make sure you have Python 3 installed, as well as the following libraries:
- [TensorFlow](https://www.tensorflow.org/install/)
- [Numpy](http://www.numpy.org/)
- [Sklearn](http://scikit-learn.org/stable/)
- [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/)
  * Note: PyAudio requires the prerequisite portaudio library to be installed. On Mac, this can be installed using homebrew.

# Usage

suggest to create an conda Virtual environmnment and set up the environment. 
Simply clone this repository, and run 

'''
git clone https://github.com/connormcl/chord_recognizer.git
cd chord_recognizer
conda activate "ur virtual enviroment"　
python Live_demo2.py 
```

go to http://127.0.0.1:5000/ in ur web browser 

# problem 
  the checkpoint in the neural network takes in a 2 channels wave file while web recording only allows one channel recording.


# References
- this neural network is built by nonnormcl (https://github.com/connormcl/chord_recognizer)
- Record on html file with RecordRTC 
- connect with Flask_socketio 
