import os
import src.db.DatabaseHandler as DatabaseHandler
import src.images.ImagesHandler as ImagesHandler
import src.images.ImagesTransformator as ImageTransformator

IMAGES_PATH = './res/photos'
DATASET_PATH = './res/dataset/5_classes'
VALIDATION_PATH = './res/validation/5_classes'
CLASS_NUMBER = 5

COIL_ID = 0
CAMERA_ID = 1
DEFECT_NO = 2
DEFECT_CLASS = 3

X0 = 0
X1 = 1
Y0 = 2
Y1 = 3


def createClassFolders(defectClasses, dir, processedClasses):
    for key, value in defectClasses.iteritems():
        if key not in processedClasses:
            continue
        path = dir + '/' + value
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
    defectsCounterDict = {}
    counter = 0
    for defect in dbHandler.getDefectRecordsToGetFile():
        img = imgHandler.getImageBasedOnDatabaseRecord(defect[COIL_ID], defect[CAMERA_ID], defect[DEFECT_NO])
        if img is not None:
            matchedImgs[counter] = img
            matchedRecords[counter] = defect
            counter += 1
            if defect[DEFECT_CLASS] in defectsCounterDict:
                defectsCounterDict[defect[DEFECT_CLASS]] = defectsCounterDict.get(defect[DEFECT_CLASS]) + 1
            else:
                defectsCounterDict[defect[DEFECT_CLASS]] = 1
            if counter % 1000 == 0:
                print 'Got ' + str(counter) + ' records'
    return matchedRecords, matchedImgs, counter, defectsCounterDict


def preprocessData(defects, defectsImgs, defectsCounter, processedDefects):
    i = 0
    skipped = 0
    processedImages = []
    print 'Start processing images...'
    while i < defectsCounter:
        defect = defects[i]
        if skipped % 100 == 0:
            print 'Skipped ' + str(skipped) + ' images'
        if defect[DEFECT_CLASS] not in processedDefects:
            skipped += 1
            i += 1
            continue
        roi = dbHandler.getROIOfRecord(defect[COIL_ID], defect[CAMERA_ID], defect[DEFECT_NO])
        defectImg = imgTransformator.createImageBasedOnROI(defectsImgs[i], roi[X0], roi[X1], roi[Y0], roi[Y1])
        defectImg = imgTransformator.standarizeImage(defectImg)
        i += 1
        processedImages.append([defectImg, defect[DEFECT_CLASS]])
        if i % 100 == 0:
            print 'Process ' + str(i) + ' of ' + str(defectsCounter) + ' total images'
    return processedImages


def saveFilesToDataset(processedImages, defectClasses):
    i = 0
    for img in processedImages:
        if i % 10 == 0:
            path = VALIDATION_PATH + '/' + defectClasses[img[1]]
        else:
            path = DATASET_PATH + '/' + defectClasses[img[1]]
        imgHandler.saveImageToFile(img[0], path, str(i))
        if i % 1000 == 0:
            print 'Saved ' + str(i) + 'images'
        i += 1


def getClassesSet(classesCounterDict):
    classes = set()
    i = 0
    for key, value in sorted(classesCounterDict.iteritems(), key=lambda (k, v): (v, k), reverse=True):
        print key, value
        if i < CLASS_NUMBER:
            classes.add(key)
            i += 1
        else:
            return classes


print 'Creating handlers ...'
dbHandler = DatabaseHandler.DatabaseHandler()
imgHandler = ImagesHandler.ImagesHandler()
imgTransformator = ImageTransformator.ImagesTransformator()
print 'Handlers created'

print 'Getting defect classes'
defectClassesDict = dbHandler.getDefectClassDefectStringDictionary()
print 'Defect classes got'
print 'Getting defects, images and defects counter'
defects, defectImgs, defectsCounter, defectsCounterDict = getMatchedDefects()
print str(defectsCounter) + ' successfully got'

processedClasses = getClassesSet(defectsCounterDict)

createClassFolders(defectClassesDict, DATASET_PATH, processedClasses)
createClassFolders(defectClassesDict, VALIDATION_PATH, processedClasses)
# TODO: launch and test it
processedImages = preprocessData(defects, defectImgs, defectsCounter, processedClasses)
print '... all images successfully processed'
#
print 'Saving files to dataset...'
saveFilesToDataset(processedImages, defectClassesDict)
print 'Files successfully saved'
