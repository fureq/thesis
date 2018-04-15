import src.db.DatabaseHandler as DatabaseHandler
import src.images.ImagesHandler as ImagesHandler
import src.images.ImagesTransformator as ImagesTransformator

COILD_ID = 675602
DEFECT_NO = 136
CAMERA_NO = 12

X0 = 0
X1 = 1
Y0 = 2
Y1 = 3

dbHandler = DatabaseHandler.DatabaseHandler()
imgHandler = ImagesHandler.ImagesHandler()
imgTransformator = ImagesTransformator.ImagesTransformator()

img = imgHandler.getImageBasedOnDatabaseRecord(COILD_ID, CAMERA_NO, DEFECT_NO)

roi = dbHandler.getROIOfRecord(COILD_ID, CAMERA_NO, DEFECT_NO)

transfomrmedImg = imgTransformator.createImageBasedOnROI(img, roi[X0], roi[X1], roi[Y0], roi[Y1])
print '(' + str(roi[X0]) + ',' + str(roi[Y0]) + ') (' + str(roi[X1]) + ',' + str(roi[Y1]) + ')'
imgHandler.showImage(transfomrmedImg)
