# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\newprj\TemplateFolderDialog_UI.ui'
#
# Created: Tue Dec 13 17:28:09 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_TemplateFolderDialog_UI(object):
    def setupUi(self, TemplateFolderDialog_UI):
        TemplateFolderDialog_UI.setObjectName("TemplateFolderDialog_UI")
        TemplateFolderDialog_UI.resize(558, 75)
        self.formLayout = QtGui.QFormLayout(TemplateFolderDialog_UI)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(TemplateFolderDialog_UI)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtGui.QLineEdit(TemplateFolderDialog_UI)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtGui.QPushButton(TemplateFolderDialog_UI)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.pushButton_2 = QtGui.QPushButton(TemplateFolderDialog_UI)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.pushButton_2)

        self.retranslateUi(TemplateFolderDialog_UI)
        QtCore.QMetaObject.connectSlotsByName(TemplateFolderDialog_UI)

    def retranslateUi(self, TemplateFolderDialog_UI):
        TemplateFolderDialog_UI.setWindowTitle(QtGui.QApplication.translate("TemplateFolderDialog_UI", "Templates Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("TemplateFolderDialog_UI", "Template Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("TemplateFolderDialog_UI", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("TemplateFolderDialog_UI", "Create New Template", None, QtGui.QApplication.UnicodeUTF8))

