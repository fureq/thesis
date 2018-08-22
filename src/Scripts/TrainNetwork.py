import matplotlib

matplotlib.use("Agg")

from keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt

import src.images.ImagesHandler as ImagesHandler
import src.neural_networks.NetworkModel as Model

import ConfigParser

config = ConfigParser.ConfigParser()
config.read('./res/config.ini')
WIDTH = int(config.get('Image', 'Width'))
HEIGHT = int(config.get('Image', 'Height'))
DEPTH = int(config.get('Image', 'Depth'))
SCALE = float(config.get('Image', 'Scale'))

EPOCHS = int(config.get('Train', 'Epochs'))
BATCH_SIZE = int(config.get('Train', 'BatchSize'))

APPROACH = 'no_normalization'

DATASET_PATH = './res/dataset/' + APPROACH + '/quatro_size'
OUTPUT_MODEL_PATH = './src/model/' + APPROACH + '_quatro_size_500.model'
OUTPUT_MODEL_WEIGHTS = './src/model/' + APPROACH + '_quatro_size_500.h5'
OUTPUT_PLOT = './res/output/' + APPROACH + '_quatro_size_500.png'

imagesHandler = ImagesHandler.ImagesHandler()

images, labels, nClasses = imagesHandler.getImgesAndLabelsInPath(DATASET_PATH)
NetworkModel = Model.NetworkModel()

height = int(HEIGHT * SCALE)
width = int(WIDTH * SCALE)

model = NetworkModel.build(width=width, height=height, depth=DEPTH, nClasses=nClasses)

images = np.array(images, dtype="float") / 255.0
labels = np.array(labels)

(trainX, testX, trainY, testY) = train_test_split(images, labels, test_size=0.25, random_state=42)

print 'del images and labels'
del images
del labels

trainY = to_categorical(trainY, num_classes=nClasses)
testY = to_categorical(testY, num_classes=nClasses)

print("[INFO] compiling model...")
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

aug = ImageDataGenerator(rotation_range=30, width_shift_range=0.1,
                         height_shift_range=0.1, shear_range=0.2, zoom_range=0.2,
                         horizontal_flip=True, fill_mode="nearest")

print("[INFO] training network...")
H = model.fit_generator(aug.flow(trainX, trainY, batch_size=BATCH_SIZE),
                        validation_data=(testX, testY), steps_per_epoch=len(trainX) // BATCH_SIZE,
                        epochs=EPOCHS, verbose=1)

print("[INFO] serializing network...")
model.save(OUTPUT_MODEL_PATH)

plt.style.use("ggplot")
plt.figure()
N = EPOCHS
plt.plot(np.arange(0, N), H.history["loss"], label="train_loss")
plt.plot(np.arange(0, N), H.history["acc"], label="train_acc")
plt.title("Training Loss and Accuracy on first approach")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend(loc="lower left")
plt.savefig(OUTPUT_PLOT)

model.save_weights(OUTPUT_MODEL_WEIGHTS)
