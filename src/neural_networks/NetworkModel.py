from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers import Dropout
from keras.layers.core import Flatten
from keras.layers.core import Dense

import ConfigParser

SECTION = "Network"
FIRST = 0
SECOND = 1
THIRD = 2
IMAGE_DATA_FORMAT = "chanells_first"

class NetworkModel:

    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read('./res/config.ini')
        self.PADDING = config.get(SECTION, 'Padding')
        self.ACTIVATION = config.get(SECTION, 'Activation')
        self.DENSE_ACTIVATION = config.get(SECTION, 'DenseActivation')
        self.CONV_FILTERS = [
            int(config.get(SECTION, 'FirstConvFilters')),
            int(config.get(SECTION, 'SecondConvFilters')),
            int(config.get(SECTION, 'ThirdConvFilters'))
        ]
        self.DROPOUT_RATIO = float(config.get(SECTION, 'DropoutRatio'))
        self.DENSE_DROPOUT_RATIO = float(config.get(SECTION, 'DenseDropoutRatio'))
        self.DENSE = int(config.get(SECTION, 'Dense'))
        self.CONV_KERNEL_SIZE = [
            (int(config.get(SECTION, 'FirstConvKernelWidth')), int(config.get(SECTION, 'FirstConvKernelHeight'))),
            (int(config.get(SECTION, 'SecondConvKernelWidth')), int(config.get(SECTION, 'SecondConvKernelHeight'))),
            (int(config.get(SECTION, 'ThirdConvKernelWidth')), int(config.get(SECTION, 'ThirdConvKernelHeight'))),
        ]
        self.MAX_POOLING_SIZE = [
            (int(config.get(SECTION, 'FirstMaxPoolingWidth')), int(config.get(SECTION, 'FirstMaxPoolingHeight'))),
            (int(config.get(SECTION, 'SecondMaxPoolingWidth')), int(config.get(SECTION, 'SecondMaxPoolingHeight'))),
            (int(config.get(SECTION, 'ThirdMaxPoolingWidth')), int(config.get(SECTION, 'ThirdMaxPoolingHeight'))),
        ]

    def build(self, width, height, depth, nClasses):
        model = Sequential()
        inputShape = (height, width, depth)

        model.add(Conv2D(self.CONV_FILTERS[FIRST], self.CONV_KERNEL_SIZE[FIRST], padding=self.PADDING, activation=self.ACTIVATION, input_shape=inputShape))
        model.add(Conv2D(self.CONV_FILTERS[FIRST], self.CONV_KERNEL_SIZE[FIRST], padding=self.PADDING, activation=self.ACTIVATION))
        model.add(MaxPooling2D(pool_size=self.MAX_POOLING_SIZE[FIRST]))
        model.add(Dropout(self.DROPOUT_RATIO))

        model.add(Conv2D(self.CONV_FILTERS[SECOND], self.CONV_KERNEL_SIZE[SECOND], padding=self.PADDING, activation=self.ACTIVATION))
        model.add(Conv2D(self.CONV_FILTERS[SECOND], self.CONV_KERNEL_SIZE[SECOND], activation=self.ACTIVATION))
        model.add(MaxPooling2D(pool_size=self.MAX_POOLING_SIZE[SECOND]))
        model.add(Dropout(self.DROPOUT_RATIO))

        model.add(Conv2D(self.CONV_FILTERS[THIRD], self.CONV_KERNEL_SIZE[THIRD], padding=self.PADDING, activation=self.ACTIVATION))
        model.add(Conv2D(self.CONV_FILTERS[THIRD], self.CONV_KERNEL_SIZE[THIRD], activation=self.ACTIVATION))
        model.add(MaxPooling2D(pool_size=self.MAX_POOLING_SIZE[THIRD]))
        model.add(Dropout(self.DROPOUT_RATIO))

        model.add(Flatten())
        model.add(Dense(self.DENSE, activation=self.ACTIVATION))
        model.add(Dropout(self.DENSE_DROPOUT_RATIO))
        model.add(Dense(nClasses, activation=self.DENSE_ACTIVATION))

        return model
