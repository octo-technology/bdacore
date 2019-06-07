from keras.layers import Dense, Activation, Embedding, LSTM
from keras.layers import Dropout, Conv1D, MaxPooling1D
from keras.models import Sequential

from bdacore.neural_networks.keras_factory import KerasFactory

__author__ = "VLE"
__copyright__ = "Copyright 2017, OCTO Technology"
__version__ = "1.0"
__email__ = "vlevorato@octo.com"


class LSTMFactory(KerasFactory):
    def create_model(self, dictionary_size, num_labels=2):
        """
        Build a keras model with several layers:
        
        - Embedding
        - LSTM
        - Dense
        - Activation
        
        Mostly used for text classification.
        
        Parameters
        ----------
        dictionary_size: int
            Size of the vocabulary
        num_labels: int, optional (default=2)
            Number of classes.

        Returns
        -------
        Keras model

        """
        model = Sequential()
        model.add(Embedding(dictionary_size, 128))
        model.add(LSTM(32, dropout=0.1, recurrent_dropout=0.1))
        model.add(Dense(num_labels))
        model.add(Activation('softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model


class CNN_LSTMFactory(KerasFactory):
    """
        Build a keras model with several layers:

        - Embedding
        - Dropout
        - Conv1D
        - MaxPooling1D
        - LSTM
        - Dense
        - Activation

        Mostly used for text classification.

        Parameters
        ----------
        dictionary_size: int
            Size of the vocabulary
        num_labels: int, optional (default=2)
            Number of classes.

        Returns
        -------
        Keras model

        """

    def create_model(self, dictionary_size, num_labels=2):
        model = Sequential()
        model.add(Embedding(dictionary_size, 128))
        model.add(Dropout(0.1))
        model.add(Conv1D(64,
                         5,
                         padding='valid',
                         activation='relu',
                         strides=1))
        model.add(MaxPooling1D(pool_size=4))
        model.add(LSTM(64, dropout=0.1, recurrent_dropout=0.1))
        model.add(Dense(num_labels))
        model.add(Activation('softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model
