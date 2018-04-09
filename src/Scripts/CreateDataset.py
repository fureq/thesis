import os
import src.db.DatabaseHandler as DatabaseHandler
import src.images.ImagesHandler as ImagesHandler
import src.images.ImagesTransformator as ImageTransformator

IMAGES_PATH = './res/photos'
DATASET_PATH = './res/dataset'

COIL_ID = 1
CAMERA_ID = 2
DEFECT_NO = 4
FILE_NAME = 5


def createDatasetFolder(defectClasses):
    for defectClass in defectClasses:
        path = DATASET_PATH + '/' + defectClass
        if not os.path.exists(path):
            print 'Creating ' + path
            os.makedirs(path)
    return

def createImageParamsArray():
    result = []
    i=0
    for subdir, dirs, files in os.walk(IMAGES_PATH):
        for file in files:
            splittedFile = file.split('_')
            splittedFile[DEFECT_NO] = splittedFile[DEFECT_NO].split('.')[0]
            splittedFile.append(file)
            result.append(splittedFile)
    return result


dbHandler = DatabaseHandler.DatabaseHandler()
imgHandler = ImagesHandler.ImagesHandler()
imgTranformator = ImageTransformator.ImagesTransformator()

defectClasses = dbHandler.getDefectClassesString()
defectClassesDict = dbHandler.getDefectClassesDictionary()
imgParams = createImageParamsArray()

createDatasetFolder(defectClasses)
