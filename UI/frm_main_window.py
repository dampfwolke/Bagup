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
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)
import UI.Icons.icons_rc

class Ui_frm_main_window(object):
    def setupUi(self, frm_main_window):
        if not frm_main_window.objectName():
            frm_main_window.setObjectName(u"frm_main_window")
        frm_main_window.resize(442, 667)
        font = QFont()
        font.setFamilies([u"Agency FB"])
        font.setPointSize(8)
        frm_main_window.setFont(font)
        icon = QIcon()
        icon.addFile(u":/images/money-bag.png", QSize(), QIcon.Normal, QIcon.Off)
        frm_main_window.setWindowIcon(icon)
        self.centralwidget = QWidget(frm_main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        font1 = QFont()
        font1.setFamilies([u"Agency FB"])
        font1.setPointSize(12)
        self.centralwidget.setFont(font1)
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.fr_input = QFrame(self.centralwidget)
        self.fr_input.setObjectName(u"fr_input")
        self.fr_input.setFrameShape(QFrame.Shape.StyledPanel)
        self.fr_input.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.fr_input)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.wg_input_le = QWidget(self.fr_input)
        self.wg_input_le.setObjectName(u"wg_input_le")
        self.horizontalLayout_2 = QHBoxLayout(self.wg_input_le)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lb_input = QLabel(self.wg_input_le)
        self.lb_input.setObjectName(u"lb_input")
        self.lb_input.setFont(font1)
        self.lb_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lb_input)

        self.le_input = QLineEdit(self.wg_input_le)
        self.le_input.setObjectName(u"le_input")

        self.horizontalLayout_2.addWidget(self.le_input)


        self.verticalLayout_2.addWidget(self.wg_input_le)

        self.wg_change_path = QWidget(self.fr_input)
        self.wg_change_path.setObjectName(u"wg_change_path")
        self.horizontalLayout_4 = QHBoxLayout(self.wg_change_path)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.rb_change_path = QRadioButton(self.wg_change_path)
        self.rb_change_path.setObjectName(u"rb_change_path")

        self.horizontalLayout_4.addWidget(self.rb_change_path)


        self.verticalLayout_2.addWidget(self.wg_change_path)

        self.wg_input_buttons = QWidget(self.fr_input)
        self.wg_input_buttons.setObjectName(u"wg_input_buttons")
        self.horizontalLayout_3 = QHBoxLayout(self.wg_input_buttons)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.pb_explorer = QPushButton(self.wg_input_buttons)
        self.pb_explorer.setObjectName(u"pb_explorer")
        self.pb_explorer.setMinimumSize(QSize(110, 0))
        icon1 = QIcon()
        icon1.addFile(u":/images/explorer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_explorer.setIcon(icon1)
        self.pb_explorer.setIconSize(QSize(22, 22))

        self.horizontalLayout_3.addWidget(self.pb_explorer)

        self.pb_create_backup = QPushButton(self.wg_input_buttons)
        self.pb_create_backup.setObjectName(u"pb_create_backup")
        self.pb_create_backup.setMinimumSize(QSize(110, 0))
        icon2 = QIcon()
        icon2.addFile(u":/images/diskette.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_create_backup.setIcon(icon2)
        self.pb_create_backup.setIconSize(QSize(22, 22))

        self.horizontalLayout_3.addWidget(self.pb_create_backup)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.wg_input_buttons)


        self.verticalLayout_3.addWidget(self.fr_input)

        self.fr_output = QFrame(self.centralwidget)
        self.fr_output.setObjectName(u"fr_output")
        self.fr_output.setFrameShape(QFrame.Shape.StyledPanel)
        self.fr_output.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.fr_output)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lb_output_upper = QLabel(self.fr_output)
        self.lb_output_upper.setObjectName(u"lb_output_upper")
        self.lb_output_upper.setFont(font1)
        self.lb_output_upper.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lb_output_upper)

        self.lb_output_name = QLabel(self.fr_output)
        self.lb_output_name.setObjectName(u"lb_output_name")
        self.lb_output_name.setFont(font1)
        self.lb_output_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lb_output_name)

        self.lb_output_success = QLabel(self.fr_output)
        self.lb_output_success.setObjectName(u"lb_output_success")
        self.lb_output_success.setFont(font1)
        self.lb_output_success.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lb_output_success)


        self.verticalLayout_3.addWidget(self.fr_output)

        self.fr_dragdrop = QFrame(self.centralwidget)
        self.fr_dragdrop.setObjectName(u"fr_dragdrop")
        self.fr_dragdrop.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.fr_dragdrop.setFrameShape(QFrame.Shape.StyledPanel)
        self.fr_dragdrop.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.fr_dragdrop)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_dragdrop = QLabel(self.fr_dragdrop)
        self.lb_dragdrop.setObjectName(u"lb_dragdrop")
        self.lb_dragdrop.setMaximumSize(QSize(300, 250))
        self.lb_dragdrop.setFont(font1)
        self.lb_dragdrop.setAcceptDrops(True)
        self.lb_dragdrop.setFrameShape(QFrame.Shape.Box)
        self.lb_dragdrop.setLineWidth(3)
        self.lb_dragdrop.setPixmap(QPixmap(u":/images/briefcase.gif"))
        self.lb_dragdrop.setScaledContents(True)
        self.lb_dragdrop.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_dragdrop)


        self.verticalLayout_3.addWidget(self.fr_dragdrop)

        frm_main_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(frm_main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 442, 33))
        frm_main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(frm_main_window)
        self.statusbar.setObjectName(u"statusbar")
        frm_main_window.setStatusBar(self.statusbar)

        self.retranslateUi(frm_main_window)
        self.rb_change_path.clicked["bool"].connect(self.le_input.setEnabled)

        QMetaObject.connectSlotsByName(frm_main_window)
    # setupUi

    def retranslateUi(self, frm_main_window):
        frm_main_window.setWindowTitle(QCoreApplication.translate("frm_main_window", u"BagUp", None))
        self.lb_input.setText(QCoreApplication.translate("frm_main_window", u"Dateipfad: ", None))
        self.rb_change_path.setText(QCoreApplication.translate("frm_main_window", u"Pfad editieren", None))
        self.pb_explorer.setText(QCoreApplication.translate("frm_main_window", u"  Explorer \u00f6ffnen", None))
        self.pb_create_backup.setText(QCoreApplication.translate("frm_main_window", u"  Sicherung erstellen", None))
        self.lb_output_upper.setText(QCoreApplication.translate("frm_main_window", u"Sicherung von", None))
        self.lb_output_name.setText(QCoreApplication.translate("frm_main_window", u"Dateiname", None))
        self.lb_output_success.setText(QCoreApplication.translate("frm_main_window", u"wurde erfolgreich erstellt.", None))
        self.lb_dragdrop.setText("")
    # retranslateUi

