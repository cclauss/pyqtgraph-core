#!/usr/bin/python -i
# -*- coding: utf-8 -*-
"""
cliAnalysis.py - Command line analysis interface 
Copyright 2010  Luke Campagnola
Distributed under MIT/X11 license. See license.txt for more infomation.

Run in interactive python. Useful for accessing data for manual analysis.
"""


import sys, os
pyfile = __file__
if pyfile[0] != '/':
   pyfile =  os.path.join(os.getcwd(), pyfile)
sys.path.append(os.path.split(pyfile)[0])
from lib.util.metaarray import *
from lib.util.pyqtgraph.ImageView import *
from lib.util.pyqtgraph.GraphicsView import *
from lib.util.pyqtgraph.graphicsItems import *
from lib.util.pyqtgraph.PlotWidget import *
from PyQt4 import QtCore, QtGui
from lib.util.functions import *

plots = []
images = []
if QtGui.QApplication.instance() is None:
    app = QtGui.QApplication([])


def showPlot(data=None, file=None, title=None):
    global plots
    if data is None:
        data = loadMetaArray(file)
    win = QtGui.QMainWindow()
    win.resize(800, 600)
    if data.ndim == 1:
        plot = PlotWidget()
        win.setCentralWidget(plot)
        plot.plot(data)
        plot.autoRange()
    elif data.ndim == 2:
        gv = GraphicsView()
        win.setCentralWidget(gv)
        l = QtGui.QGraphicsGridLayout()
        gv.centralWidget.setLayout(l)
        for i in range(data.shape[0]):
            p = PlotItem(gv.centralWidget)
            l.addItem(p, i, 0)
            p.plot(data[i])
            p.autoRange()
        
        
    tStr = "Plot %d" % len(plots)
    if title is not None:
        tStr += " - " + title
    win.setWindowTitle(tStr)
    plots.append({'win': win, 'data': data})
    win.show()

def showImage(data=None, file=None, title=None):
    global images
    if data is None:
        data = loadMetaArray(file)
    win = QtGui.QMainWindow()
    win.resize(800, 600)
    imv = ImageView()
    win.setCentralWidget(imv)
    imv.setImage(data.view(ndarray))
    
    tStr = "Image %d" % len(plots)
    if title is not None:
        tStr += " - " + title
    win.setWindowTitle(tStr)
    images.append({'win': win, 'data': data})
    win.show()
    

def dirDialog(startDir='', title="Select Directory"):
  return str(QtGui.QFileDialog.getExistingDirectory(None, title, startDir))

def fileDialog():
  return str(QtGui.QFileDialog.getOpenFileName())

def loadMetaArray(file=None):
    if file is None:
        file = fileDialog()
    return MetaArray(file=file)
    
