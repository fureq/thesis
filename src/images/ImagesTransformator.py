import ConfigParser
import copy
import cv2

SECTION = 'Image'

class ImagesTransformator:

    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read('./res/config.ini')
        self.WIDTH = config.get(SECTION, 'width')
        self.HEIGHT = config.get(SECTION, 'height')
        pass

    def createImageBasedOnROI(self, image, x0, x1, y0, y1):
        img = copy.copy(image)
        return img[y0:y0+y1, x0:x0+x1]

    def standarizeImage(self, image):
        return cv2.resize(copy.copy(image), (int(self.WIDTH), int(self.HEIGHT)))