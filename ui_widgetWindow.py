# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widgetWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(371, 284)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 30, 111, 16))
        self.btn_print = QPushButton(Form)
        self.btn_print.setObjectName(u"btn_print")
        self.btn_print.setGeometry(QRect(150, 90, 80, 23))
        self.btn_action = QPushButton(Form)
        self.btn_action.setObjectName(u"btn_action")
        self.btn_action.setGeometry(QRect(160, 140, 80, 23))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"widgetWindow", None))
        self.btn_print.setText(QCoreApplication.translate("Form", u"Print", None))
        self.btn_action.setText(QCoreApplication.translate("Form", u"Action", None))
    # retranslateUi

