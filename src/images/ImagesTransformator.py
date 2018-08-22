import ConfigParser
import copy
import cv2

SECTION = 'Image'


class ImagesTransformator:

    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read('./res/config.ini')
        self.WIDTH = int(config.get(SECTION, 'Width'))
        self.HEIGHT = int(config.get(SECTION, 'Height'))
        pass

    def createImageBasedOnROI(self, image, x0, x1, y0, y1):
        img = copy.copy(image)
        return img[y0:y1, x0:x1]

    def standarizeImage(self, image):
        return self.resize(copy.copy(image), (self.WIDTH, self.HEIGHT))

    def resize(self, image, size):
        return cv2.resize(image, size)
