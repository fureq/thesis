from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
import numpy as np

import src.images.ImagesHandler as ImagesHandler
import src.neural_networks.NetworkModel as Model

import ConfigParser

config = ConfigParser.ConfigParser()
config.read('./res/config.ini')
WIDTH = int(config.get('Image', 'Width'))
HEIGHT = int(config.get('Image', 'Height'))
DEPTH = int(config.get('Image', 'Depth'))
WEIGHT_PATH = './src/model/no_up_rescale/5_classes_100_epochs.h5'
DATASET_PATH = './res/dataset/no_up_rescale/5_classes'
BATCH_SIZE = int(config.get('Train', 'BatchSize'))

imagesHandler = ImagesHandler.ImagesHandler()

NetworkModel = Model.NetworkModel()

images, labels, nClasses = imagesHandler.getImagesAndLabelsInPath(DATASET_PATH)
NetworkModel = Model.NetworkModel()

model = NetworkModel.build(width=WIDTH, height=HEIGHT, depth=DEPTH, nClasses=nClasses)

images = np.array(images, dtype="float") / 255.0
labels = np.array(labels)

(trainX, testX, trainY, testY) = train_test_split(images, labels, test_size=0.25, random_state=42)

trainY = to_categorical(trainY, num_classes=nClasses)
testY = to_categorical(testY, num_classes=nClasses)

model.load_weights(filepath=WEIGHT_PATH)

print len(trainX) // BATCH_SIZE

Y_pred = model.predict_generator((testX, testY), len(trainX) // BATCH_SIZE+1)
y_pred = np.argmax(Y_pred, axis=1)
print(confusion_matrix((testX, testY).classes, y_pred))
