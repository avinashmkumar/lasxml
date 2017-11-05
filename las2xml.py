import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime
import readlas as LAS
from io import BytesIO
# build a tree structure
logs = ET.Element("logs")
logs.set('xmlns','http://www.witsml.org/schemas/1series')
logs.set('xmlns:xsi','http://www.w3.org/2001/XMLSchema-instance')
logs.set('xsi:schemaLocation','http://www.witsml.org/schemas/1series ../xsd_schemas/obj_log.xsd')
logs.set('version','1.4.1.1')
log = ET.SubElement(logs, 'log')
log.set('uidWell','well_uid_here')
log.set('uidWellbore','wellbore_uid_here')
log.set('uid','log_uid_here')
wellname=ET.SubElement(log,'nameWell')
wellname.text='Well Name'
wellborename=ET.SubElement(log,'nameWellbore')
wellborename.text='Well Bore Name'
objgr=ET.SubElement(log,'objectGrowing')
objgr.text='false'
servco=ET.SubElement(log,'serviceCompany')
servco.text=LAS.getServiceCo()
runno=ET.SubElement(log,'runNumber')
runno.text='1'
crdt=ET.SubElement(log,'creationDate')
crdt.text=LAS.getFormattedDate(datetime.utcnow())+"Z"
indtyp=ET.SubElement(log,'indexType')
indtyp.text=LAS.getIndexType()
if(LAS.getIndexType() == 'date time'):
    strdt=ET.SubElement(log,'startDateTimeIndex')
    strdt.text=LAS.getStartDatetime()
    endt=ET.SubElement(log,'endDateTimeIndex')
    endt.text=LAS.getEndDatetime()
else:
    stdep=ET.SubElement(log,'startDepthIndex')
    stdep.text=LAS.getStartDepth()
    endep=ET.SubElement(log,'endDepthIndex')
    endep.text=LAS.getEndDepth()
drn=ET.SubElement(log,'direction')
drn.text='increasing'
incrv=ET.SubElement(log,'indexCurve')
incrv.text=LAS.getIndexCurve()
nval=ET.SubElement(log,'nullValue')
nval.text=LAS.getNullValue()
logdata=ET.SubElement(log,'logData')
mnemlist=ET.SubElement(logdata,'mnemonicList')
mnemlist.text=LAS.getMnemonics()
unitlist=ET.SubElement(logdata,'unitList')
unitlist.text=LAS.getUnits()
if LAS.getIndexType() == 'date time':
    for val in range(0,LAS.getDataSize()):
        data=ET.SubElement(logdata, 'data', {})
        data.text=LAS.getTimeData(val)
else:
    for val in range(0,LAS.getDataSize()):
        data = ET.SubElement(logdata, 'data', {})
        data.text=LAS.getDepthData(val)
cdata=ET.SubElement(log,'commonData')
tcr=ET.SubElement(cdata, 'dTimCreation', {})
tcr.text=LAS.getFormattedDate(datetime.utcnow())+"Z"
tlc=ET.SubElement(cdata, 'dTimLastChange', {})
tlc.text=LAS.getFormattedDate(datetime.utcnow())+"Z"

# wrap it in an ElementTree instance, and save as XML
tree = ET.ElementTree(logs)
'''
fr = BytesIO()
tree.write(fr, encoding='utf-8', xml_declaration=True) 
xmlstr=fr.getvalue()
prettyxmlstr = minidom.parseString(xmlstr).toprettyxml(indent="   ")
'''
xmlstr = minidom.parseString(ET.tostring(logs)).toprettyxml(indent="   ")
print xmlstr
with open("New_Database.xml", "w") as f:
    f.write(xmlstr)