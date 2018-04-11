import cv2
import os

FILE_NAME_PREFIX = 'P6810010'
IMAGES_DIR = './res/photos'
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