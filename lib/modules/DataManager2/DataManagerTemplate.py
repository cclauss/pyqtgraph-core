# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataManagerTemplate.ui'
#
# Created: Thu May 27 21:18:29 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.baseDirText = QtGui.QLineEdit(self.centralwidget)
        self.baseDirText.setObjectName("baseDirText")
        self.gridLayout.addWidget(self.baseDirText, 0, 1, 1, 1)
        self.selectDirBtn = QtGui.QPushButton(self.centralwidget)
        self.selectDirBtn.setObjectName("selectDirBtn")
        self.gridLayout.addWidget(self.selectDirBtn, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.currentDirText = QtGui.QLineEdit(self.centralwidget)
        self.currentDirText.setObjectName("currentDirText")
        self.gridLayout.addWidget(self.currentDirText, 1, 1, 1, 1)
        self.setCurrentDirBtn = QtGui.QPushButton(self.centralwidget)
        self.setCurrentDirBtn.setObjectName("setCurrentDirBtn")
        self.gridLayout.addWidget(self.setCurrentDirBtn, 1, 2, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.newFolderList = QtGui.QComboBox(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newFolderList.sizePolicy().hasHeightForWidth())
        self.newFolderList.setSizePolicy(sizePolicy)
        self.newFolderList.setObjectName("newFolderList")
        self.verticalLayout_2.addWidget(self.newFolderList)
        self.fileTreeWidget = FileTreeWidget(self.layoutWidget)
        self.fileTreeWidget.setObjectName("fileTreeWidget")
        self.fileTreeWidget.headerItem().setText(0, "1")
        self.fileTreeWidget.header().setVisible(False)
        self.verticalLayout_2.addWidget(self.fileTreeWidget)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.fileNameLabel = QtGui.QLabel(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileNameLabel.sizePolicy().hasHeightForWidth())
        self.fileNameLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setWeight(75)
        font.setBold(True)
        self.fileNameLabel.setFont(font)
        self.fileNameLabel.setText("")
        self.fileNameLabel.setObjectName("fileNameLabel")
        self.verticalLayout_4.addWidget(self.fileNameLabel)
        self.fileDisplayTabs = QtGui.QTabWidget(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileDisplayTabs.sizePolicy().hasHeightForWidth())
        self.fileDisplayTabs.setSizePolicy(sizePolicy)
        self.fileDisplayTabs.setObjectName("fileDisplayTabs")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.fileInfo = FileInfoView(self.tab)
        self.fileInfo.setObjectName("fileInfo")
        self.verticalLayout_3.addWidget(self.fileInfo)
        self.fileDisplayTabs.addTab(self.tab, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.selectedLogView = QtGui.QTextEdit(self.tab_4)
        self.selectedLogView.setReadOnly(True)
        self.selectedLogView.setObjectName("selectedLogView")
        self.verticalLayout_6.addWidget(self.selectedLogView)
        self.fileDisplayTabs.addTab(self.tab_4, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.dataViewWidget = FileDataView(self.tab_3)
        self.dataViewWidget.setObjectName("dataViewWidget")
        self.verticalLayout_7.addWidget(self.dataViewWidget)
        self.fileDisplayTabs.addTab(self.tab_3, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.fileDisplayTabs.addTab(self.tab_2, "")
        self.verticalLayout_4.addWidget(self.fileDisplayTabs)
        self.verticalLayout_5.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.logDock = QtGui.QDockWidget(MainWindow)
        self.logDock.setFloating(False)
        self.logDock.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.logDock.setObjectName("logDock")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logView = QtGui.QTextEdit(self.dockWidgetContents)
        self.logView.setReadOnly(True)
        self.logView.setObjectName("logView")
        self.verticalLayout.addWidget(self.logView)
        self.logEntryText = QtGui.QLineEdit(self.dockWidgetContents)
        self.logEntryText.setObjectName("logEntryText")
        self.verticalLayout.addWidget(self.logEntryText)
        self.logDock.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.logDock)

        self.retranslateUi(MainWindow)
        self.fileDisplayTabs.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Data Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Top-level Directory:", None, QtGui.QApplication.UnicodeUTF8))
        self.selectDirBtn.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Storage Directory:", None, QtGui.QApplication.UnicodeUTF8))
        self.setCurrentDirBtn.setText(QtGui.QApplication.translate("MainWindow", "Set", None, QtGui.QApplication.UnicodeUTF8))
        self.fileDisplayTabs.setTabText(self.fileDisplayTabs.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.fileDisplayTabs.setTabText(self.fileDisplayTabs.indexOf(self.tab_4), QtGui.QApplication.translate("MainWindow", "Log", None, QtGui.QApplication.UnicodeUTF8))
        self.fileDisplayTabs.setTabText(self.fileDisplayTabs.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Data", None, QtGui.QApplication.UnicodeUTF8))
        self.fileDisplayTabs.setTabText(self.fileDisplayTabs.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.logDock.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Current Log", None, QtGui.QApplication.UnicodeUTF8))

from FileInfoView import FileInfoView
from FileTreeWidget import FileTreeWidget
from FileDataView import FileDataView
