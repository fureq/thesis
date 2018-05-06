from imutils import paths
from keras.preprocessing.image import img_to_array
import cv2
import os
import random
# from sets import Set

FILE_NAME_PREFIX = 'P6810010'
IMAGES_DIR = '/res/photos'
DIR_DELIMITER = '/'
FILE_NAME_DELIMITER = '_'
FILE_EXETENSION = '.jpg'


class ImagesHandler:

    def __init__(self):
        pass

    def showImage(self, img):
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def saveImageToFile(self, img, dirpath, filename):
        filepath = dirpath + '/' + filename + FILE_EXETENSION
        cv2.imwrite(filepath, img)

    def getImageBasedOnDatabaseRecord(self, coilId, cameraId, defectNo):
        return cv2.imread(self.getFilePath(coilId, cameraId, defectNo), 0)

    def getFilePath(self, coilId, cameraId, defectNo):
        return IMAGES_DIR \
               + DIR_DELIMITER \
               + str(coilId).zfill(8) \
               + DIR_DELIMITER \
               + str(cameraId).zfill(2) \
               + DIR_DELIMITER \
               + FILE_NAME_PREFIX \
               + FILE_NAME_DELIMITER \
               + str(coilId).zfill(8) \
               + FILE_NAME_DELIMITER \
               + str(cameraId).zfill(2) \
               + FILE_NAME_DELIMITER \
               + 'srcimg' \
               + FILE_NAME_DELIMITER \
               + str(defectNo).zfill(4) \
               + FILE_EXETENSION

    def mapDirToNumber(self, path):
        number = 0
        numbderDirMap = {}
        for dir in sorted(os.listdir(path)):
            numbderDirMap[dir] = number
            number += 1
        return numbderDirMap

    def getImagesAndLabelsInPath(self, path):
        images = []
        labels = []
        classes = set()
        imagePaths = sorted(list(paths.list_images(path)))
        random.seed(42)
        random.shuffle(imagePaths)
        labelsMap = self.mapDirToNumber(path)

        for imgPath in imagePaths:
            image = cv2.imread(imgPath)
            image = img_to_array(image)
            images.append(image)

            label = imgPath.split(os.path.sep)[-2]
            labels.append(labelsMap[label])
            classes.add(label)

        return images, labels, len(classes)