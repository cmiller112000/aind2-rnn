import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras


# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series,window_size):
    # containers for input/output pairs
    X = []
    y = []

    # step through the input series and grab off window_size element sets and add to the X list, then grab
    # the next series entry one past the window size and add that element to the y list.
    # use list slicing to make it easy.  Make sure to end properly so we don't run off the end of the series

    for i in range(len(series)-window_size):
        X.append(series[i:i+window_size])
        y.append(series[i+window_size])

    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)

    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(step_size, window_size):
# given - fix random seed - so we can all reproduce the same results on our default time series
    np.random.seed(0)

    # TODO: build an RNN to perform regression on our time series input/output data
    model = Sequential()
    model.add(LSTM(5,input_shape=(window_size,step_size)))
    model.add(Dense(1))

    # build model using keras documentation recommended optimizer initialization
    optimizer = keras.optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)

    # compile the model
    model.compile(loss='mean_squared_error', optimizer=optimizer)

### TODO: list all unique characters in the text and remove any non-english ones

import re
def clean_text(text):

    # find all unique characters in the text
    chars=sorted(list(set(text)))

    # remove as many non-english characters and character sequences as you can
    # use the regex substitue function and remove all characters except those listed in
    # the regex expression
    text = re.sub(r'[^a-zA-Z.,?!;:\']', ' ',text)

    # shorten any extra dead space created above
    text = text.replace('  ',' ')
    return text

### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text,window_size,step_size):
    # containers for input/output pairs
    inputs = []
    outputs = []

    # step through and pick up the input text string of window_size characteres, and its corresponding output 'next' character
    # then step through all the text based on the input step size until all input/output pairs are collected

    for i in range(0,len(text)-window_size-step_size,step_size):
        inputs.append(text[i:i+window_size])
        outputs.append(text[i+window_size])

    return inputs,outputs