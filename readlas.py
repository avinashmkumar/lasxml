import lasio
from dateutil.parser import parse
import datetime
l = lasio.read("GENTIME.las")
start = "2017-02-14T18:21:14.345+05:30"
stdt = parse(start)

def getStartDatetime():
    dt = stdt + datetime.timedelta(0,l[0][0])
    microsecond = int(dt.microsecond)
    millisecond = int(round(microsecond/1000))
    dtstr = dt.isoformat()
    dtstr = dtstr.replace('.{:06d}'.format(microsecond), 
                        '.{:03d}'.format(millisecond))
    return dtstr

def getEndDatetime():
    dt = stdt + datetime.timedelta(0,l[0][getDataSize()-1])
    microsecond = int(dt.microsecond)
    millisecond = int(round(microsecond/1000))
    dtstr = dt.isoformat()
    dtstr = dtstr.replace('.{:06d}'.format(microsecond), 
                        '.{:03d}'.format(millisecond))
    return dtstr

def getStartDepth():
    return str(l[0][0])

def getEndDepth():
    return str(l[0][getDataSize()-1])

def getdate(stdt,step):
    dt = stdt + datetime.timedelta(0,l[0][step])
    microsecond = int(dt.microsecond)
    millisecond = int(round(microsecond/1000))
    dtstr = dt.isoformat()
    dtstr = dtstr.replace('.{:06d}'.format(microsecond), 
                        '.{:03d}'.format(millisecond))
    return dtstr

def getUnits():
    curvstr = ""
    for curve in l.curves:
        curvstr+=curve.unit+","
    curvstr = curvstr[:-1]
    return curvstr

def getMnemonics():
    mnemstr = ""
    for curve in l.curves:
        mnemstr+=curve.mnemonic+","
    mnemstr = mnemstr[:-1]
    return mnemstr

def getServiceCo():
    return l.well.SRVC.value
 
def getIndexType():  
    indextype=""
    if (l.curves[0].unit == 'S' or l.curves[0].unit == 's'):
        indextype="date time"
    else:
        indextype="depth"
    return indextype

def getIndexCurve():  
    return l.curves[0].mnemonic

def getDataSize():
    return len(l[0])

def getNullValue():
    return str(l.well.NULL.value)

def getTimeData(val):
            valstr = ""
            for mnem in range(1,len(l.keys())):
                valstr+=str(l[mnem][val])+","
            valstr = getdate(stdt,val)+","+valstr[:-1]
            return valstr

def getDepthData(val):
    #for val in range(0,len(l[0])):
            valstr = ""
            for mnem in range(0,len(l.keys())):
                valstr+=str(l[mnem][val])+","
            return valstr[:-1]

def getFormattedDate(dt):
    microsecond = int(dt.microsecond)
    millisecond = int(round(microsecond/1000))
    dtstr = dt.isoformat()
    dtstr = dtstr.replace('.{:06d}'.format(microsecond), 
                        '.{:03d}'.format(millisecond))
    return dtstr

'''


for val in range(0,len(l[0])):
        valstr = ""
        for mnem in range(1,len(l.keys())):
            valstr+=str(l[mnem][val])+","
        valstr = valstr[:-1]
        print getdate(stdt,val)+","+valstr



print getMnemonics()
print getUnits()
    

#print type(l[1])
#print type(l[1][0])
#print len(l.keys())    
#print l[1][0]
#print l[2][0]
#print l[3][0]
#print l[:,0]
for val in range(0,len(l[0])):
        valstr = ""
        for mnem in range(1,len(l.keys())):
            valstr+=str(l[mnem][val])+","
        print getdate()+","valstr
##print valstr
'''