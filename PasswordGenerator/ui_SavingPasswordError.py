# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SavingPasswordErrorDDrTxv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(319, 62)
        Dialog.setMinimumSize(QSize(318, 62))
        Dialog.setMaximumSize(QSize(319, 62))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(9, 32, 301, 21))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 281, 17))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"No password!", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"No password has been generated yet!", None))
    # retranslateUi

