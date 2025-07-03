# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)
import UI.Icons.icons_rc

class Ui_frm_main_window(object):
    def setupUi(self, frm_main_window):
        if not frm_main_window.objectName():
            frm_main_window.setObjectName(u"frm_main_window")
        frm_main_window.resize(550, 667)
        font = QFont()
        font.setFamilies([u"Agency FB"])
        font.setPointSize(8)
        frm_main_window.setFont(font)
        self.centralwidget = QWidget(frm_main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        font1 = QFont()
        font1.setFamilies([u"Agency FB"])
        font1.setPointSize(12)
        self.centralwidget.setFont(font1)
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.fr_upper = QFrame(self.centralwidget)
        self.fr_upper.setObjectName(u"fr_upper")
        self.fr_upper.setFrameShape(QFrame.Shape.StyledPanel)
        self.fr_upper.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.fr_upper)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lb_output = QLabel(self.fr_upper)
        self.lb_output.setObjectName(u"lb_output")
        self.lb_output.setFont(font1)
        self.lb_output.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lb_output)


        self.verticalLayout_3.addWidget(self.fr_upper)

        self.fr_dragdrop = QFrame(self.centralwidget)
        self.fr_dragdrop.setObjectName(u"fr_dragdrop")
        self.fr_dragdrop.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.fr_dragdrop.setFrameShape(QFrame.Shape.StyledPanel)
        self.fr_dragdrop.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.fr_dragdrop)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_dragdrop = QLabel(self.fr_dragdrop)
        self.lb_dragdrop.setObjectName(u"lb_dragdrop")
        self.lb_dragdrop.setMaximumSize(QSize(250, 250))
        self.lb_dragdrop.setFont(font1)
        self.lb_dragdrop.setAcceptDrops(True)
        self.lb_dragdrop.setPixmap(QPixmap(u":/myicons/drag-and-drop.png"))
        self.lb_dragdrop.setScaledContents(True)
        self.lb_dragdrop.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_dragdrop)


        self.verticalLayout_3.addWidget(self.fr_dragdrop)

        frm_main_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(frm_main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 550, 33))
        frm_main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(frm_main_window)
        self.statusbar.setObjectName(u"statusbar")
        frm_main_window.setStatusBar(self.statusbar)

        self.retranslateUi(frm_main_window)

        QMetaObject.connectSlotsByName(frm_main_window)
    # setupUi

    def retranslateUi(self, frm_main_window):
        frm_main_window.setWindowTitle(QCoreApplication.translate("frm_main_window", u"MainWindow", None))
        self.lb_output.setText(QCoreApplication.translate("frm_main_window", u"Platzhalter", None))
        self.lb_dragdrop.setText("")
    # retranslateUi

