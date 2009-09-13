# -*- coding: utf-8 -*-
from DeviceTemplate import Ui_Form
import time

class ScannerDeviceGui(QtGui.QWidget):
    def __init__(self, dev):
        QtGui.QWidget.__init__(self)
        self.dev = dev
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        ## Populate Device lists
        devs = self.dev.dm.listDevices()
        for d in devs:
            self.ui.cameraCombo.addItem(d)
            self.ui.laserCombo.addItem(d)
        
        self.updateCalibrationList()
        
        QtCore.QObject.connect(self.ui.calibrateBtn, QtCore.SIGNAL('clicked()'), self.calibrateClicked)
        QtCore.QObject.connect(self.ui.testBtn, QtCore.SIGNAL('clicked()'), self.testClicked)
        QtCore.QObject.connect(self.ui.deleteBtn, QtCore.SIGNAL('clicked()'), self.deleteClicked)
        
        
    def updateCalibrationList(self):
        self.ui.calibrationList.clear()
        
        ## Populate calibration lists
        index = self.dev.getCalibrationIndex()
        for cam in index:
            for laser in index[cam]:
                for obj in index[cam][laser]:
                    cal = index[cam][laser][obj]
                    spot = cal['spot']
                    date = cal['date']
                    self.ui.calibrationList.addItem([cam, obj, laser, str(spot), date])
        
        
    def calibrateClicked(self):
        cam = self.ui.cameraCombo.currentText()
        laser = self.ui.laserCombo.currentText()
        obj = self.dev.getObjective(cam)
        
        ## Run calibration
        #(cal, spot) = self.runCalibration()
        cal = MetaArray((512, 512, 2))
        spot = 100e-6
        date = time.strftime('%Y.%m.%d %H:%m', time.localtime())
        
        fileName = cam + '_' + laser + '_' + obj + '.ma'
        index = self.dev.getCalibrationIndex()
        
        if cam not in index:
            index[cam] = {}
        if laser not in index[cam]:
            index[cam][laser] = {}
        index[cam][laser][obj] = {'fileName': fileName, 'spot': spot, 'date': date}
           
        self.dev.writeCalibrationIndex(index)
        cal.writeFile(fileName)
        
        self.updateCalibrationList()

    def testClicked(self):
        pass

    def deleteClicked(self):
        cur = self.ui.calibrationList.currentItem()
        cam = cur.text(0)
        obj = cur.text(1)
        laser = cur.text(2)
        
        index = self.dev.getCalibrationIndex()
        
        cal = index[cam][laser][obj]
        fileName = cal['fileName']
        calDir = self.dev.config['calibrationDir']
        fileName = os.path.join(calDir, fileName)
        del index[cam][laser][obj]
        os.remove(fileName)
            
        self.dev.writeCalibrationIndex(index)
        
        self.updateCalibrationList()

    def runCalibration(self):
        ## Determine spot intensity and width
        
        ## Measure X/Y ranges
        
        ## Record full map
        
        ## Invert map
        
        return (invMap, spotWidth)


