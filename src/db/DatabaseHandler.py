from sqlalchemy import *
import ConfigParser
import tables
from sqlalchemy import func

SECTION = 'Database'


class DatabaseHandler:

    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read("./res/config.ini")
        self.USERNAME = config.get(SECTION, 'Username')
        self.PASSWORD = config.get(SECTION, 'Password')
        self.URL = config.get(SECTION, 'Url')
        self.PORT = config.get(SECTION, 'Port')
        self.DB_NAME = config.get(SECTION, 'DbName')
        self.DB_TYPE = config.get(SECTION, 'DbType')
        self.engine = create_engine(self.getDbSQLPath())
        self.engine.connect()
        self.defectsTable = tables.t_defects
        self.defectsClassesTable = tables.t_defectclasses
        pass

    def getDbSQLPath(self):
        return self.DB_TYPE + '://' \
               + self.USERNAME + ':' \
               + self.PASSWORD + '@' \
               + self.URL + ':' \
               + self.PORT + '/' \
               + self.DB_NAME

    def countDefects(self):
        query = select([func.count()]).select_from(self.defectsTable)
        return self.engine.execute(query).scalar()

    def getDefectRecordsToGetFile(self):
        query = select([
            self.defectsTable.c.coilid,
            self.defectsTable.c.camerano,
            self.defectsTable.c.defectno
        ])
        return self.engine.execute(query)

    def getROIOfRecord(self, coilId, cameraNo, defectNo):
        query = select([
            self.defectsTable.c.roix0,
            self.defectsTable.c.roix1,
            self.defectsTable.c.roiy0,
            self.defectsTable.c.roiy1
        ]).where(and_(
            self.defectsTable.c.coilid == coilId,
            self.defectsTable.c.camerano == cameraNo,
            self.defectsTable.c.defectno == defectNo
        ))
        return self.engine.execute(query).fetchone()

    def getDefectClasses(self):
        query = select([
            self.defectsClassesTable.c.classid,
            self.defectsClassesTable.c.name,
        ])
        return self.engine.execute(query)

    def getDefectClassString(self, defectClass):
        return (str(defectClass[0]) + '_' + str(defectClass[1])).replace(' ', '_')

    def getDefectClassesString(self):
        defectClassesStrings = []
        for defectClass in self.getDefectClasses():
            defectClassString = self.getDefectClassString(defectClass)
            defectClassesStrings.append(defectClassString)
        return defectClassesStrings

    def getDefectClassesDictionary(self):
        defectsDict = {}
        for defectClass in self.getDefectClasses():
            defectsDict[defectClass[0]] = defectClass[1]
        return defectsDict
