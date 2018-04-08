# coding: utf-8
from sqlalchemy import Column, DateTime, Float, Index, Integer, MetaData, String, Table


metadata = MetaData()


t_actionlog = Table(
    'actionlog', metadata,
    Column('msgid', Integer, unique=True),
    Column('coilid', Integer),
    Column('position', Integer),
    Column('time', DateTime),
    Column('username', String(252)),
    Column('action', String(252))
)


t_brightness = Table(
    'brightness', metadata,
    Column('material', Integer),
    Column('group_id', Integer),
    Column('brightness', Integer),
    Column('counter', Integer),
    Column('total_count', Integer),
    Column('avg_grey', Integer),
    Column('bright_dev', Integer),
    Index('material', 'material', 'group_id', unique=True)
)


t_cameras = Table(
    'cameras', metadata,
    Column('cameraid', Integer, unique=True),
    Column('nodeid', Integer),
    Column('side', String(252)),
    Column('type', String(252)),
    Column('x0', Integer),
    Column('x1', Integer),
    Column('rotate', Integer),
    Column('illuminationgroup', Integer)
)


t_coildb_sis01history = Table(
    'coildb_sis01history', metadata,
    Column('date', DateTime, unique=True),
    Column('version', String(252)),
    Column('changedby', String(252)),
    Column('class', String(252)),
    Column('linetype', String(252)),
    Column('comment', String(252))
)


t_coildbhistory = Table(
    'coildbhistory', metadata,
    Column('date', DateTime, unique=True),
    Column('version', String(252)),
    Column('changedby', String(252)),
    Column('class', String(252)),
    Column('linetype', String(252)),
    Column('comment', String(252))
)


t_coilevents = Table(
    'coilevents', metadata,
    Column('eventid', Integer, unique=True),
    Column('timestamp', DateTime),
    Column('coilid', Integer),
    Column('positionmd', Float(asdecimal=True)),
    Column('type', Integer),
    Column('description', String(252))
)


t_coilgrading = Table(
    'coilgrading', metadata,
    Column('classid', Integer, unique=True),
    Column('score1', Float(asdecimal=True)),
    Column('score2', Float(asdecimal=True)),
    Column('scorewarn', Float(asdecimal=True)),
    Column('scorealarm', Float(asdecimal=True))
)


t_coilresults = Table(
    'coilresults', metadata,
    Column('coilid', Integer),
    Column('classid', Integer),
    Column('defcnt1', Integer),
    Column('defcnt2', Integer),
    Column('defcnt3', Integer),
    Column('defcnt4', Integer),
    Column('defcnt5', Integer),
    Column('coilgrade', Integer),
    Column('status', String(252)),
    Index('coilid', 'coilid', 'classid', unique=True)
)


t_coils = Table(
    'coils', metadata,
    Column('coilid', Integer, unique=True),
    Column('starttime', DateTime),
    Column('endtime', DateTime),
    Column('paramset', Integer),
    Column('grade', Integer),
    Column('length', Float(asdecimal=True)),
    Column('width', Float(asdecimal=True)),
    Column('thickness', Float(asdecimal=True)),
    Column('weight', Float(asdecimal=True)),
    Column('charge', String(252)),
    Column('materialid', Integer),
    Column('status', String(252)),
    Column('bdecoilid', String(252)),
    Column('description', String(252)),
    Column('lastdefectid', Integer),
    Column('targetquality', Integer),
    Column('pdirecvtime', DateTime),
    Column('slength', Float(asdecimal=True)),
    Column('internalstatus', String(252)),
    Column('defectcount', Integer),
    Column('l2matid', String(252)),
    Column('coilnamefinal', String(252)),
    Column('spare2', String(252)),
    Column('spare3', String(252)),
    Column('spare4', String(252)),
    Column('spare5', String(252)),
    Column('spare6', String(252)),
    Column('spare7', String(252)),
    Column('spare8', String(252)),
    Column('spare9', String(252)),
    Column('spare10', String(252)),
    Column('standf4replen', String(252)),
    Column('standf4rollidtop', String(252)),
    Column('standf4rollidbot', String(252)),
    Column('standf4replentolp', String(252)),
    Column('standf4replentolm', String(252)),
    Column('standf5replen', String(252)),
    Column('standf5rollidtop', String(252)),
    Column('standf5rollidbot', String(252)),
    Column('standf5replentolp', String(252)),
    Column('standf5replentolm', String(252)),
    Column('standf6replen', String(252)),
    Column('standf6rollidtop', String(252)),
    Column('standf6rollidbot', String(252)),
    Column('standf6replentolp', String(252)),
    Column('standf6replentolm', String(252)),
    Column('confidencets', Float(asdecimal=True)),
    Column('confidencebs', Float(asdecimal=True))
)


t_coilstatistic = Table(
    'coilstatistic', metadata,
    Column('coilid', Integer),
    Column('classid', Integer),
    Column('grade', Integer),
    Column('numbers0', Integer),
    Column('numbers1', Integer),
    Index('coilid', 'coilid', 'classid', 'grade', unique=True)
)


t_customclasses = Table(
    'customclasses', metadata,
    Column('customclassid', Integer, unique=True),
    Column('customclassname', String(252)),
    Column('color', String(252)),
    Column('rgb', Integer),
    Column('pattern', Integer),
    Column('patterncolor', Integer),
    Column('status', String(252)),
    Column('countdefects', Integer),
    Column('localizedcustomclassname', String(252))
)


t_defaultsettings = Table(
    'defaultsettings', metadata,
    Column('setting', String(252), unique=True),
    Column('settingvalue', Integer)
)


t_defectclasses = Table(
    'defectclasses', metadata,
    Column('classid', Integer, unique=True),
    Column('name', String(252)),
    Column('shortname', String(252)),
    Column('classlevel', String(252)),
    Column('customclassid', Integer),
    Column('status', String(252)),
    Column('localizedname', String(252)),
    Column('localizedshortname', String(252))
)


t_defectgrading = Table(
    'defectgrading', metadata,
    Column('classid', Integer),
    Column('grade', Integer),
    Column('sizecd', Float(asdecimal=True)),
    Column('sizemd', Float(asdecimal=True)),
    Column('area', Float(asdecimal=True)),
    Column('sideratio', Float(asdecimal=True)),
    Column('weight', Float(asdecimal=True)),
    Column('var', Float(asdecimal=True)),
    Index('classid', 'classid', 'grade', unique=True)
)


t_defects = Table(
    'defects', metadata,
    Column('coilid', Integer),
    Column('defectid', Integer),
    Column('class', Integer),
    Column('grade', Integer),
    Column('periodid', Integer),
    Column('periodlength', Float(asdecimal=True)),
    Column('positioncd', Float(asdecimal=True)),
    Column('positionrcd', Float(asdecimal=True)),
    Column('positionmd', Float(asdecimal=True)),
    Column('side', Integer),
    Column('sizecd', Float(asdecimal=True)),
    Column('sizemd', Float(asdecimal=True)),
    Column('camerano', Integer),
    Column('defectno', Integer),
    Column('mergedto', Integer),
    Column('confidence', Integer),
    Column('roix0', Integer),
    Column('roix1', Integer),
    Column('roiy0', Integer),
    Column('roiy1', Integer),
    Column('originalclass', Integer),
    Column('pp_id', Integer),
    Column('postcl', Integer),
    Column('mergerpp', Integer),
    Column('onlinecpp', Integer),
    Column('offlinecpp', Integer),
    Column('rollerid', Integer),
    Column('internalstatus', String(252)),
    Column('cl_prod_class', Integer),
    Column('cl_test_class', Integer),
    Column('absposcd', Float(asdecimal=True)),
    Column('sureness', Float(asdecimal=True)),
    Column('cgsisstate', Integer),
    Column('cgsiscount', Integer),
    Column('a', Float(asdecimal=True)),
    Column('var', Float(asdecimal=True)),
    Column('x_s', Float(asdecimal=True)),
    Column('y_s', Float(asdecimal=True)),
    Column('cd', Float(asdecimal=True)),
    Column('mgvdif', Float(asdecimal=True)),
    Column('rc_v_s_m', Float(asdecimal=True)),
    Column('d_max_seg_d', Float(asdecimal=True)),
    Column('o', Float(asdecimal=True)),
    Column('ast_factor_4', Float(asdecimal=True)),
    Column('perc_dark', Float(asdecimal=True)),
    Index('coilid', 'coilid', 'defectid', unique=True)
)


t_diaglog = Table(
    'diaglog', metadata,
    Column('msgid', Integer, unique=True),
    Column('comptype', Integer),
    Column('compidx', Integer),
    Column('compnode', String(252)),
    Column('state', Integer),
    Column('msglevel', Integer),
    Column('code', Integer),
    Column('contextid', Integer),
    Column('coilid', Integer),
    Column('position', Integer),
    Column('timestamp', DateTime),
    Column('args', String(252)),
    Column('acknowledged', Integer)
)


t_displaythresholds = Table(
    'displaythresholds', metadata,
    Column('targetquality', Integer),
    Column('classid', Integer),
    Column('threshold1', Integer),
    Column('threshold2', Integer),
    Index('targetquality', 'targetquality', 'classid', unique=True)
)


t_groups = Table(
    'groups', metadata,
    Column('groupid', Integer, unique=True),
    Column('systemlevel', Integer)
)


t_inspectionsystems = Table(
    'inspectionsystems', metadata,
    Column('sisid', Integer, unique=True),
    Column('name', String(252)),
    Column('plant', String(252)),
    Column('line', String(252)),
    Column('location', String(252)),
    Column('country', String(252)),
    Column('comment', String(252)),
    Column('servername', String(252))
)


t_materials = Table(
    'materials', metadata,
    Column('materialid', Integer, unique=True),
    Column('materialname', String(252)),
    Column('paramsetid', Integer),
    Column('comment', String(252)),
    Column('paramsetid1', Integer),
    Column('status', String(252))
)


t_outcoils = Table(
    'outcoils', metadata,
    Column('outcoilid', Integer, unique=True),
    Column('outpdicoilid', String(252)),
    Column('slength', Float(asdecimal=True)),
    Column('sstarttime', DateTime),
    Column('sendtime', DateTime),
    Column('inpdicoilidfirst', String(252)),
    Column('inpdicoilidlast', String(252)),
    Column('incoilidfirst', Integer),
    Column('incoilidlast', Integer),
    Column('incoilindex', Integer),
    Column('description', String(252)),
    Column('pdirecvtime', DateTime),
    Column('status', String(252)),
    Column('length', Float(asdecimal=True)),
    Column('starttime', DateTime),
    Column('endtime', DateTime),
    Column('lastdefectid', Integer),
    Column('defectcount', Integer)
)


t_paramsets = Table(
    'paramsets', metadata,
    Column('paramsetid', Integer, unique=True),
    Column('paramsetname', String(252)),
    Column('comment', String(252)),
    Column('creationtime', DateTime),
    Column('createdby', String(252)),
    Column('parameter', String(252)),
    Column('status', String(252))
)


t_qlistthresholds = Table(
    'qlistthresholds', metadata,
    Column('customclassid', Integer),
    Column('grade', Integer),
    Column('thresholdwarn', Integer),
    Column('thresholdalarm', Integer),
    Index('customclassid', 'customclassid', 'grade', unique=True)
)


t_rollers = Table(
    'rollers', metadata,
    Column('rollerid', Integer, unique=True),
    Column('info', String(252)),
    Column('side', Integer),
    Column('periodlength', Float(asdecimal=True)),
    Column('tolminus', Float(asdecimal=True)),
    Column('tolplus', Float(asdecimal=True)),
    Column('dynamic', Float(asdecimal=True)),
    Column('e1used', Float(asdecimal=True)),
    Column('e2used', Float(asdecimal=True)),
    Column('priority', Float(asdecimal=True))
)


t_sectiongrading = Table(
    'sectiongrading', metadata,
    Column('materialid', Integer),
    Column('defectgrade', Integer),
    Column('sectiongrade', Integer),
    Column('nrofdefects', Float(asdecimal=True)),
    Column('length', Float(asdecimal=True)),
    Index('materialid', 'materialid', 'defectgrade', 'sectiongrade', unique=True)
)


t_sections = Table(
    'sections', metadata,
    Column('sectionid', Integer, unique=True),
    Column('outcoilid', Integer),
    Column('incoilid', Integer),
    Column('starttime', DateTime),
    Column('endtime', DateTime),
    Column('startposmd', Float(asdecimal=True)),
    Column('endposmd', Float(asdecimal=True)),
    Column('startposcd', Float(asdecimal=True)),
    Column('endposcd', Float(asdecimal=True)),
    Column('startoutposmd', Float(asdecimal=True)),
    Column('daughteridoffset', Integer)
)


t_standardrollers = Table(
    'standardrollers', metadata,
    Column('rollerid', Integer, unique=True),
    Column('rollername', String(252)),
    Column('side', Integer),
    Column('periodlength', Float(asdecimal=True)),
    Column('tolminus', Float(asdecimal=True)),
    Column('tolplus', Float(asdecimal=True))
)


t_unknownmaterials = Table(
    'unknownmaterials', metadata,
    Column('materialname', String(252), unique=True),
    Column('firstcoil', Integer),
    Column('announcementcnt', Integer)
)


t_userrights = Table(
    'userrights', metadata,
    Column('userright', String(252), unique=True),
    Column('level0', Integer),
    Column('level1', Integer),
    Column('level2', Integer),
    Column('level3', Integer),
    Column('level4', Integer),
    Column('level5', Integer),
    Column('level6', Integer),
    Column('level7', Integer),
    Column('level8', Integer),
    Column('level9', Integer)
)


t_users = Table(
    'users', metadata,
    Column('userid', Integer, unique=True),
    Column('username', String(252)),
    Column('password', String(252)),
    Column('grouplevel', Integer),
    Column('autologin', String(252))
)


t_web_customclasses = Table(
    'web_customclasses', metadata,
    Column('customclassid', Integer),
    Column('customclassname', String(252)),
    Column('color', String(252)),
    Column('rgb', Integer),
    Column('pattern', Integer),
    Column('patterncolor', Integer),
    Column('status', String(252)),
    Column('countdefects', Integer),
    Column('localizedcustomclassname', String(252))
)


t_web_qlistthresholds = Table(
    'web_qlistthresholds', metadata,
    Column('customclassid', Integer),
    Column('grade', Integer),
    Column('thresholdwarn', Integer),
    Column('thresholdalarm', Integer),
    Index('customclassid', 'customclassid', 'grade', unique=True)
)
