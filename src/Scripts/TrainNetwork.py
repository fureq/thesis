import src.images.ImagesHandler as ImagesHandler

DATASET_PATH = './res/dataset/'

imagesHandler = ImagesHandler.ImagesHandler()

images, labels = imagesHandler.getImagesAndLabelsInPath(DATASET_PATH)

