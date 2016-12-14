# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\newprj\NewTemplateDialog_UI.ui'
#
# Created: Tue Dec 13 17:28:08 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_NewTemplateDialog_UI(object):
    def setupUi(self, NewTemplateDialog_UI):
        NewTemplateDialog_UI.setObjectName("NewTemplateDialog_UI")
        NewTemplateDialog_UI.resize(400, 107)
        self.formLayout = QtGui.QFormLayout(NewTemplateDialog_UI)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(NewTemplateDialog_UI)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtGui.QLineEdit(NewTemplateDialog_UI)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtGui.QLabel(NewTemplateDialog_UI)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.comboBox = QtGui.QComboBox(NewTemplateDialog_UI)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBox)
        self.buttonBox = QtGui.QDialogButtonBox(NewTemplateDialog_UI)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(2, QtGui.QFormLayout.SpanningRole, self.buttonBox)

        self.retranslateUi(NewTemplateDialog_UI)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), NewTemplateDialog_UI.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), NewTemplateDialog_UI.reject)
        QtCore.QMetaObject.connectSlotsByName(NewTemplateDialog_UI)

    def retranslateUi(self, NewTemplateDialog_UI):
        NewTemplateDialog_UI.setWindowTitle(QtGui.QApplication.translate("NewTemplateDialog_UI", "Create New Template", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("NewTemplateDialog_UI", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("NewTemplateDialog_UI", "Copy From", None, QtGui.QApplication.UnicodeUTF8))

