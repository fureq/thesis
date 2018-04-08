import src.db.DatabaseHandler as DatabaseHandler
import src.images.ImagesHandler as ImagesHandler

dbHandler = DatabaseHandler.DatabaseHandler()
imagesHandler = ImagesHandler.ImagesHandler()

foundedImage = 0
notFounded = 0

for row in dbHandler.getDefectRecordsToGetFile():
    img = imagesHandler.getImageBasedOnDatabaseRecord(row[0], row[1], row[2])
    if img is not None:
        foundedImage += 1
    else:
        notFounded += 1

allImages = dbHandler.countDefects()
print 'all: ' + str(allImages)
print 'founded: ' + str(foundedImage)
print 'not founded: ' + str(notFounded)
precent = round(float(foundedImage) / float(allImages) * 100, 0)

print 'Matched records: ' + str(precent) + '%'