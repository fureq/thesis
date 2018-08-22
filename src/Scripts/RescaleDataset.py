import os
import src.images.ImagesHandler as ImagesHandler
import src.images.ImagesTransformator as ImageTransformator

import ConfigParser

config = ConfigParser.ConfigParser()
config.read('./res/config.ini')
WIDTH = int(config.get('Image', 'Width'))
HEIGHT = int(config.get('Image', 'Height'))
DEPTH = int(config.get('Image', 'Depth'))
SCALE = float(config.get('Image', 'Scale'))

ROOT_DIRECTORY = './res/dataset/no_normalization/5_classes'
TARGET_DIRECTORY = './res/dataset/no_normalization/quatro_size'

imgHandler = ImagesHandler.ImagesHandler()
imgTransformator = ImageTransformator.ImagesTransformator()

newHeight = int(HEIGHT * SCALE)
newWidth = int(WIDTH * SCALE)

skipped = 0
processed = 0
for subdir, dirs, files in os.walk(ROOT_DIRECTORY):
    for file in files:
        path = subdir + '/' + file
        newSubdir = subdir.replace(ROOT_DIRECTORY, TARGET_DIRECTORY)
        if not os.path.exists(newSubdir):
            os.makedirs(newSubdir)
        img = imgHandler.openImage(subdir + '/' + file)
        height, width, channels = img.shape
        if height != HEIGHT or width != WIDTH:
            skipped += 1
            continue
        img = imgTransformator.resize(img, (newWidth, newHeight))
        processed += 1
        imgHandler.saveImageToFile(img, newSubdir, str(processed))
print 'processed:', processed
print 'skipped:', skipped
