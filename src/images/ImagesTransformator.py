import copy


class ImagesTransformator:

    def __init__(self):
        pass

    def createImageBasedOnROI(self, image, x0, x1, y0, y1):
        img = copy.copy(image)
        return img[x0:x1, y0:y1]