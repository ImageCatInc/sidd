# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt\wdg_sel_attributes.ui'
#
# Created: Tue Jul 02 16:29:51 2013
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_widgetSelectAttribute(object):
    def setupUi(self, widgetSelectAttribute):
        widgetSelectAttribute.setObjectName(_fromUtf8("widgetSelectAttribute"))
        widgetSelectAttribute.resize(500, 32)
        self.lb_description = QtGui.QLabel(widgetSelectAttribute)
        self.lb_description.setGeometry(QtCore.QRect(420, 5, 71, 22))
        self.lb_description.setObjectName(_fromUtf8("lb_description"))
        self.cb_codes = QtGui.QComboBox(widgetSelectAttribute)
        self.cb_codes.setGeometry(QtCore.QRect(130, 5, 261, 22))
        self.cb_codes.setObjectName(_fromUtf8("cb_codes"))
        self.lb_attribute = QtGui.QLabel(widgetSelectAttribute)
        self.lb_attribute.setGeometry(QtCore.QRect(0, 5, 131, 22))
        self.lb_attribute.setObjectName(_fromUtf8("lb_attribute"))

        self.retranslateUi(widgetSelectAttribute)
        QtCore.QMetaObject.connectSlotsByName(widgetSelectAttribute)

    def retranslateUi(self, widgetSelectAttribute):
        widgetSelectAttribute.setWindowTitle(QtGui.QApplication.translate("widgetSelectAttribute", "Form", None, QtGui.QApplication.UnicodeUTF8))

