import os
import src.db.DatabaseHandler as DatabaseHandler
import src.images.ImagesHandler as ImagesHandler
import src.images.ImagesTransformator as ImageTransformator

IMAGES_PATH = './res/photos'
DATASET_PATH = './res/dataset/'
VALIDATION_PATH = './res/validation/'

COIL_ID = 0
CAMERA_ID = 1
DEFECT_NO = 2
DEFECT_CLASS = 3

X0 = 0
X1 = 1
Y0 = 2
Y1 = 3


def createClassFolders(defectClasses, dir):
    for defectClass in defectClasses:
        path = dir + '/' + defectClass
        if not os.path.exists(path):
            print 'Creating ' + path
            os.makedirs(path)
    return


def createImageParamsArray():
    result = []
    i = 0
    for subdir, dirs, files in os.walk(IMAGES_PATH):
        for file in files:
            splittedFile = file.split('_')
            splittedFile[DEFECT_NO] = splittedFile[DEFECT_NO].split('.')[0]
            splittedFile.append(file)
            result.append(splittedFile)
    return result


def getMatchedDefects():
    matchedImgs = {}
    matchedRecords = {}
    counter = 0
    for defect in dbHandler.getDefectRecordsToGetFile():
        img = imgHandler.getImageBasedOnDatabaseRecord(defect[COIL_ID], defect[CAMERA_ID], defect[DEFECT_NO])
        if img is not None:
            matchedImgs[counter] = img
            matchedRecords[counter] = defect
            counter += 1
            if counter % 1000 == 0:
                print 'Got ' + str(counter) + ' records'
    return matchedRecords, matchedImgs, counter


def preprocessData(defects, defectsImgs, defectsCounter):
    i = 0
    processedImages = []
    print 'Start processing images...'
    while i < defectsCounter:
        defect = defects[i]
        roi = dbHandler.getROIOfRecord(defect[COIL_ID], defect[CAMERA_ID], defect[DEFECT_NO])
        defectImg = imgTransformator.createImageBasedOnROI(defectsImgs[i], roi[X0], roi[X1], roi[Y0], roi[Y1])
        defectImg = imgTransformator.standarizeImage(defectImg)
        i += 1
        processedImages.append([defectImg, defect[DEFECT_CLASS]])
        if i % 100 == 0:
            print 'Process ' + str(i) + ' of ' + str(defectsCounter) + ' total images'
    return processedImages


def saveFilesToDataset(processedImages, defectClasses):
    i=0
    for img in processedImages:
        if i%10 == 0:
            path = VALIDATION_PATH + '/' + defectClasses[img[1]]
        else:
            path = DATASET_PATH + '/' + defectClasses[img[1]]
        imgHandler.saveImageToFile(img[0], path, str(i))
        if i%1000==0:
            print 'Saved ' + str(i) + 'images'
        i+=1


print 'Creating handlers ...'
dbHandler = DatabaseHandler.DatabaseHandler()
imgHandler = ImagesHandler.ImagesHandler()
imgTransformator = ImageTransformator.ImagesTransformator()
print 'Handlers created'

print 'Getting defect classes'
defectClasses = dbHandler.getDefecotClassesString()
defectClassesDict = dbHandler.getDefectClassDefectStringDictionary()
print 'Defect classes got'
print 'Getting defects, images and defects counter'
defects, defectImgs, defectsCounter = getMatchedDefects()
print str(defectsCounter) + ' successfully got'

createClassFolders(defectClasses, DATASET_PATH)
createClassFolders(defectClasses, VALIDATION_PATH)
processedImages = preprocessData(defects, defectImgs, defectsCounter)
print '... all images successfully processed'

print 'Saving files to dataset...'
saveFilesToDataset(processedImages, defectClassesDict)
print 'Files successfully saved'
