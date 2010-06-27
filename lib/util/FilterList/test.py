# -*- coding: utf-8 -*-
import sys
sys.path.append('..')

from PyQt4.QtGui import *
from PyQt4 import QtCore
from FilterList import *
from pyqtgraph.PlotWidget import *
from numpy import *

app = QApplication([])
win = QMainWindow()
cw = QWidget()
hl = QHBoxLayout()
cw.setLayout(hl)
fl = FilterList()
hl.addWidget(fl)

vw = QWidget()
hl.addWidget(vw)
vl = QVBoxLayout()
vw.setLayout(vl)

p1 = PlotWidget()
p2 = PlotWidget()
vl.addWidget(p1)
vl.addWidget(p2)


win.setCentralWidget(cw)
win.show()

data = random.random(10000)
data[5000:6000] += 2
data[5500] += 20
data[6000:7000] -= 3
data += linspace(1, 3, 10000)
data += sin(linspace(0, 15, 10000))


p1.plot(data)

def replot():
    d2 = fl.processData(data.copy())
    p2.plot(d2, clear=True)
    
QtCore.QObject.connect(fl, QtCore.SIGNAL('changed'), replot)

app.exec_()