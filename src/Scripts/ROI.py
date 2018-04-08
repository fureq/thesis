import src.db.DatabaseHandler as DatabaseHandler
import src.images.ImagesHandler as ImagesHandler
import src.images.ImagesTransformator as ImagesTransformator

COILD_ID = 675593
DEFECT_NO = 10
CAMERA_NO = 12

dbHandler = DatabaseHandler.DatabaseHandler()
imgHandler = ImagesHandler.ImagesHandler()
imgTransformator = ImagesTransformator.ImagesTransformator()

img = imgHandler.getImageBasedOnDatabaseRecord(COILD_ID, CAMERA_NO, DEFECT_NO)

roi = dbHandler.getROIOfRecord(COILD_ID, CAMERA_NO, DEFECT_NO)

transfomrmedImg = imgTransformator.createImageBasedOnROI(img, roi[0], roi[1], roi[2], roi[3])
imgHandler.showImage(transfomrmedImg)