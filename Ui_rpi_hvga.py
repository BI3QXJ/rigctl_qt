# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rpi_hvga.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(480, 320)
        Form.setMinimumSize(QSize(480, 320))
        Form.setMaximumSize(QSize(480, 320))
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.group_rig_lcd = QGroupBox(Form)
        self.group_rig_lcd.setObjectName(u"group_rig_lcd")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_rig_lcd.sizePolicy().hasHeightForWidth())
        self.group_rig_lcd.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.group_rig_lcd)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 8, 4, 3)
        self.lbl_background = QLabel(self.group_rig_lcd)
        self.lbl_background.setObjectName(u"lbl_background")
        self.lbl_background.setMinimumSize(QSize(458, 55))
        self.lbl_background.setMaximumSize(QSize(458, 55))
        self.lbl_background.setPixmap(QPixmap(u"lcd.png"))

        self.horizontalLayout.addWidget(self.lbl_background)


        self.verticalLayout_3.addWidget(self.group_rig_lcd)

        self.tab_main = QTabWidget(Form)
        self.tab_main.setObjectName(u"tab_main")
        self.tab_main.setEnabled(True)
        font = QFont()
        font.setFamily(u"Arial")
        self.tab_main.setFont(font)
        self.tab_basic = QWidget()
        self.tab_basic.setObjectName(u"tab_basic")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_basic)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.layout_mode = QVBoxLayout()
        self.layout_mode.setSpacing(2)
        self.layout_mode.setObjectName(u"layout_mode")
        self.layout_mode.setContentsMargins(1, 1, 1, 1)
        self.lbl_mode = QLabel(self.tab_basic)
        self.lbl_mode.setObjectName(u"lbl_mode")
        self.lbl_mode.setMinimumSize(QSize(0, 0))
        self.lbl_mode.setMaximumSize(QSize(16777215, 15))

        self.layout_mode.addWidget(self.lbl_mode)

        self.gridLayout_mode = QGridLayout()
        self.gridLayout_mode.setSpacing(2)
        self.gridLayout_mode.setObjectName(u"gridLayout_mode")
        self.gridLayout_mode.setContentsMargins(1, 1, 1, 1)
        self.btn_mode_lsb = QPushButton(self.tab_basic)
        self.btn_mode_lsb.setObjectName(u"btn_mode_lsb")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_mode_lsb.sizePolicy().hasHeightForWidth())
        self.btn_mode_lsb.setSizePolicy(sizePolicy1)
        self.btn_mode_lsb.setMinimumSize(QSize(65, 40))
        self.btn_mode_lsb.setMaximumSize(QSize(65, 40))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(11)
        self.btn_mode_lsb.setFont(font1)

        self.gridLayout_mode.addWidget(self.btn_mode_lsb, 0, 0, 1, 1)

        self.btn_mode_usb = QPushButton(self.tab_basic)
        self.btn_mode_usb.setObjectName(u"btn_mode_usb")
        self.btn_mode_usb.setMinimumSize(QSize(65, 40))
        self.btn_mode_usb.setMaximumSize(QSize(65, 40))
        self.btn_mode_usb.setFont(font1)

        self.gridLayout_mode.addWidget(self.btn_mode_usb, 0, 1, 1, 1)

        self.btn_mode_am = QPushButton(self.tab_basic)
        self.btn_mode_am.setObjectName(u"btn_mode_am")
        self.btn_mode_am.setMinimumSize(QSize(65, 40))
        self.btn_mode_am.setMaximumSize(QSize(65, 40))
        self.btn_mode_am.setFont(font1)

        self.gridLayout_mode.addWidget(self.btn_mode_am, 0, 2, 1, 1)

        self.btn_mode_cwl = QPushButton(self.tab_basic)
        self.btn_mode_cwl.setObjectName(u"btn_mode_cwl")
        self.btn_mode_cwl.setMinimumSize(QSize(65, 40))
        self.btn_mode_cwl.setMaximumSize(QSize(65, 40))
        self.btn_mode_cwl.setFont(font1)

        self.gridLayout_mode.addWidget(self.btn_mode_cwl, 1, 0, 1, 1)

        self.btn_mode_cwu = QPushButton(self.tab_basic)
        self.btn_mode_cwu.setObjectName(u"btn_mode_cwu")
        self.btn_mode_cwu.setMinimumSize(QSize(65, 40))
        self.btn_mode_cwu.setMaximumSize(QSize(65, 40))
        self.btn_mode_cwu.setFont(font1)

        self.gridLayout_mode.addWidget(self.btn_mode_cwu, 1, 1, 1, 1)

        self.btn_mode_fm = QPushButton(self.tab_basic)
        self.btn_mode_fm.setObjectName(u"btn_mode_fm")
        self.btn_mode_fm.setMinimumSize(QSize(65, 40))
        self.btn_mode_fm.setMaximumSize(QSize(65, 40))
        self.btn_mode_fm.setFont(font1)

        self.gridLayout_mode.addWidget(self.btn_mode_fm, 1, 2, 1, 1)

        self.btn_mode_rttyl = QPushButton(self.tab_basic)
        self.btn_mode_rttyl.setObjectName(u"btn_mode_rttyl")
        self.btn_mode_rttyl.setMinimumSize(QSize(65, 40))
        self.btn_mode_rttyl.setMaximumSize(QSize(65, 40))
        self.btn_mode_rttyl.setFont(font1)

        self.gridLayout_mode.addWidget(self.btn_mode_rttyl, 2, 0, 1, 1)

        self.btn_mode_rttyu = QPushButton(self.tab_basic)
        self.btn_mode_rttyu.setObjectName(u"btn_mode_rttyu")
        self.btn_mode_rttyu.setMinimumSize(QSize(65, 40))
        self.btn_mode_rttyu.setMaximumSize(QSize(65, 40))
        self.btn_mode_rttyu.setFont(font1)

        self.gridLayout_mode.addWidget(self.btn_mode_rttyu, 2, 1, 1, 1)

        self.btn_mode_c4fm = QPushButton(self.tab_basic)
        self.btn_mode_c4fm.setObjectName(u"btn_mode_c4fm")
        self.btn_mode_c4fm.setMinimumSize(QSize(65, 40))
        self.btn_mode_c4fm.setMaximumSize(QSize(65, 40))
        self.btn_mode_c4fm.setFont(font1)

        self.gridLayout_mode.addWidget(self.btn_mode_c4fm, 2, 2, 1, 1)

        self.btn_mode_datal = QPushButton(self.tab_basic)
        self.btn_mode_datal.setObjectName(u"btn_mode_datal")
        self.btn_mode_datal.setMinimumSize(QSize(65, 40))
        self.btn_mode_datal.setMaximumSize(QSize(65, 40))
        self.btn_mode_datal.setFont(font1)

        self.gridLayout_mode.addWidget(self.btn_mode_datal, 3, 0, 1, 1)

        self.btn_mode_datau = QPushButton(self.tab_basic)
        self.btn_mode_datau.setObjectName(u"btn_mode_datau")
        self.btn_mode_datau.setMinimumSize(QSize(65, 40))
        self.btn_mode_datau.setMaximumSize(QSize(65, 40))
        self.btn_mode_datau.setFont(font1)

        self.gridLayout_mode.addWidget(self.btn_mode_datau, 3, 1, 1, 1)

        self.btn_mode_datafm = QPushButton(self.tab_basic)
        self.btn_mode_datafm.setObjectName(u"btn_mode_datafm")
        self.btn_mode_datafm.setMinimumSize(QSize(65, 40))
        self.btn_mode_datafm.setMaximumSize(QSize(65, 40))
        self.btn_mode_datafm.setFont(font1)

        self.gridLayout_mode.addWidget(self.btn_mode_datafm, 3, 2, 1, 1)


        self.layout_mode.addLayout(self.gridLayout_mode)

        self.layout_mode.setStretch(0, 1)
        self.layout_mode.setStretch(1, 10)

        self.horizontalLayout_2.addLayout(self.layout_mode)

        self.layout_band = QVBoxLayout()
        self.layout_band.setSpacing(2)
        self.layout_band.setObjectName(u"layout_band")
        self.layout_band.setContentsMargins(1, 1, 1, 1)
        self.lbl_band = QLabel(self.tab_basic)
        self.lbl_band.setObjectName(u"lbl_band")
        self.lbl_band.setMaximumSize(QSize(16777215, 15))

        self.layout_band.addWidget(self.lbl_band)

        self.gridLayout_band = QGridLayout()
        self.gridLayout_band.setSpacing(2)
        self.gridLayout_band.setObjectName(u"gridLayout_band")
        self.gridLayout_band.setContentsMargins(1, 1, 1, 1)
        self.btn_band_430 = QPushButton(self.tab_basic)
        self.btn_band_430.setObjectName(u"btn_band_430")
        self.btn_band_430.setMinimumSize(QSize(65, 40))
        self.btn_band_430.setMaximumSize(QSize(65, 40))
        self.btn_band_430.setFont(font)

        self.gridLayout_band.addWidget(self.btn_band_430, 2, 3, 1, 1)

        self.btn_band_mw = QPushButton(self.tab_basic)
        self.btn_band_mw.setObjectName(u"btn_band_mw")
        self.btn_band_mw.setMinimumSize(QSize(65, 40))
        self.btn_band_mw.setMaximumSize(QSize(65, 40))
        self.btn_band_mw.setFont(font)

        self.gridLayout_band.addWidget(self.btn_band_mw, 3, 3, 1, 1)

        self.btn_band_10 = QPushButton(self.tab_basic)
        self.btn_band_10.setObjectName(u"btn_band_10")
        self.btn_band_10.setMinimumSize(QSize(65, 40))
        self.btn_band_10.setMaximumSize(QSize(65, 40))
        self.btn_band_10.setFont(font)

        self.gridLayout_band.addWidget(self.btn_band_10, 1, 1, 1, 1)

        self.btn_band_18 = QPushButton(self.tab_basic)
        self.btn_band_18.setObjectName(u"btn_band_18")
        self.btn_band_18.setMinimumSize(QSize(65, 40))
        self.btn_band_18.setMaximumSize(QSize(65, 40))
        self.btn_band_18.setFont(font)

        self.gridLayout_band.addWidget(self.btn_band_18, 2, 0, 1, 1)

        self.btn_band_21 = QPushButton(self.tab_basic)
        self.btn_band_21.setObjectName(u"btn_band_21")
        self.btn_band_21.setMinimumSize(QSize(65, 40))
        self.btn_band_21.setMaximumSize(QSize(65, 40))
        self.btn_band_21.setFont(font)

        self.gridLayout_band.addWidget(self.btn_band_21, 2, 1, 1, 1)

        self.btn_band_3_5 = QPushButton(self.tab_basic)
        self.btn_band_3_5.setObjectName(u"btn_band_3_5")
        self.btn_band_3_5.setMinimumSize(QSize(65, 40))
        self.btn_band_3_5.setMaximumSize(QSize(65, 40))
        self.btn_band_3_5.setFont(font)

        self.gridLayout_band.addWidget(self.btn_band_3_5, 0, 1, 1, 1)

        self.btn_band_air = QPushButton(self.tab_basic)
        self.btn_band_air.setObjectName(u"btn_band_air")
        self.btn_band_air.setMinimumSize(QSize(65, 40))
        self.btn_band_air.setMaximumSize(QSize(65, 40))
        self.btn_band_air.setFont(font)

        self.gridLayout_band.addWidget(self.btn_band_air, 0, 3, 1, 1)

        self.btn_band_24 = QPushButton(self.tab_basic)
        self.btn_band_24.setObjectName(u"btn_band_24")
        self.btn_band_24.setMinimumSize(QSize(65, 40))
        self.btn_band_24.setMaximumSize(QSize(65, 40))
        self.btn_band_24.setFont(font)

        self.gridLayout_band.addWidget(self.btn_band_24, 2, 2, 1, 1)

        self.btn_band_7_0 = QPushButton(self.tab_basic)
        self.btn_band_7_0.setObjectName(u"btn_band_7_0")
        self.btn_band_7_0.setMinimumSize(QSize(65, 40))
        self.btn_band_7_0.setMaximumSize(QSize(65, 40))
        self.btn_band_7_0.setFont(font)

        self.gridLayout_band.addWidget(self.btn_band_7_0, 1, 0, 1, 1)

        self.btn_band_144 = QPushButton(self.tab_basic)
        self.btn_band_144.setObjectName(u"btn_band_144")
        self.btn_band_144.setMinimumSize(QSize(65, 40))
        self.btn_band_144.setMaximumSize(QSize(65, 40))
        self.btn_band_144.setFont(font)

        self.gridLayout_band.addWidget(self.btn_band_144, 1, 3, 1, 1)

        self.btn_band_14 = QPushButton(self.tab_basic)
        self.btn_band_14.setObjectName(u"btn_band_14")
        self.btn_band_14.setMinimumSize(QSize(65, 40))
        self.btn_band_14.setMaximumSize(QSize(65, 40))
        self.btn_band_14.setFont(font)

        self.gridLayout_band.addWidget(self.btn_band_14, 1, 2, 1, 1)

        self.btn_band_28 = QPushButton(self.tab_basic)
        self.btn_band_28.setObjectName(u"btn_band_28")
        self.btn_band_28.setMinimumSize(QSize(65, 40))
        self.btn_band_28.setMaximumSize(QSize(65, 40))
        self.btn_band_28.setFont(font)

        self.gridLayout_band.addWidget(self.btn_band_28, 3, 0, 1, 1)

        self.btn_band_1_8 = QPushButton(self.tab_basic)
        self.btn_band_1_8.setObjectName(u"btn_band_1_8")
        self.btn_band_1_8.setMinimumSize(QSize(65, 40))
        self.btn_band_1_8.setMaximumSize(QSize(65, 40))
        self.btn_band_1_8.setFont(font)

        self.gridLayout_band.addWidget(self.btn_band_1_8, 0, 0, 1, 1)

        self.btn_band_50 = QPushButton(self.tab_basic)
        self.btn_band_50.setObjectName(u"btn_band_50")
        self.btn_band_50.setMinimumSize(QSize(65, 40))
        self.btn_band_50.setMaximumSize(QSize(65, 40))
        self.btn_band_50.setFont(font)

        self.gridLayout_band.addWidget(self.btn_band_50, 3, 1, 1, 1)

        self.btn_band_gen = QPushButton(self.tab_basic)
        self.btn_band_gen.setObjectName(u"btn_band_gen")
        self.btn_band_gen.setMinimumSize(QSize(65, 40))
        self.btn_band_gen.setMaximumSize(QSize(65, 40))
        self.btn_band_gen.setFont(font)

        self.gridLayout_band.addWidget(self.btn_band_gen, 3, 2, 1, 1)

        self.btn_band_5_0 = QPushButton(self.tab_basic)
        self.btn_band_5_0.setObjectName(u"btn_band_5_0")
        self.btn_band_5_0.setMinimumSize(QSize(65, 40))
        self.btn_band_5_0.setMaximumSize(QSize(65, 40))
        self.btn_band_5_0.setFont(font)

        self.gridLayout_band.addWidget(self.btn_band_5_0, 0, 2, 1, 1)


        self.layout_band.addLayout(self.gridLayout_band)

        self.layout_band.setStretch(0, 1)
        self.layout_band.setStretch(1, 10)

        self.horizontalLayout_2.addLayout(self.layout_band)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 4)
        self.tab_main.addTab(self.tab_basic, "")
        self.tab_vfo = QWidget()
        self.tab_vfo.setObjectName(u"tab_vfo")
        self.horizontalLayout_4 = QHBoxLayout(self.tab_vfo)
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.layout_vfo = QGridLayout()
        self.layout_vfo.setObjectName(u"layout_vfo")
        self.btn_vfo_num2 = QPushButton(self.tab_vfo)
        self.btn_vfo_num2.setObjectName(u"btn_vfo_num2")
        self.btn_vfo_num2.setMinimumSize(QSize(50, 32))
        self.btn_vfo_num2.setMaximumSize(QSize(50, 32))

        self.layout_vfo.addWidget(self.btn_vfo_num2, 3, 3, 1, 1)

        self.btn_vfo_num3 = QPushButton(self.tab_vfo)
        self.btn_vfo_num3.setObjectName(u"btn_vfo_num3")
        self.btn_vfo_num3.setMinimumSize(QSize(50, 32))
        self.btn_vfo_num3.setMaximumSize(QSize(50, 32))

        self.layout_vfo.addWidget(self.btn_vfo_num3, 3, 4, 1, 1)

        self.btn_vfo_num9 = QPushButton(self.tab_vfo)
        self.btn_vfo_num9.setObjectName(u"btn_vfo_num9")
        self.btn_vfo_num9.setMinimumSize(QSize(50, 32))
        self.btn_vfo_num9.setMaximumSize(QSize(50, 32))

        self.layout_vfo.addWidget(self.btn_vfo_num9, 1, 4, 1, 1)

        self.btn_vfo_qmb_recall = QPushButton(self.tab_vfo)
        self.btn_vfo_qmb_recall.setObjectName(u"btn_vfo_qmb_recall")
        self.btn_vfo_qmb_recall.setMinimumSize(QSize(50, 32))
        self.btn_vfo_qmb_recall.setMaximumSize(QSize(16777215, 32))

        self.layout_vfo.addWidget(self.btn_vfo_qmb_recall, 4, 1, 1, 1)

        self.btn_vfo_am = QPushButton(self.tab_vfo)
        self.btn_vfo_am.setObjectName(u"btn_vfo_am")
        self.btn_vfo_am.setMinimumSize(QSize(50, 32))
        self.btn_vfo_am.setMaximumSize(QSize(16777215, 32))

        self.layout_vfo.addWidget(self.btn_vfo_am, 0, 0, 1, 1)

        self.btn_vfo_mem_up = QPushButton(self.tab_vfo)
        self.btn_vfo_mem_up.setObjectName(u"btn_vfo_mem_up")
        self.btn_vfo_mem_up.setMinimumSize(QSize(50, 32))
        self.btn_vfo_mem_up.setMaximumSize(QSize(16777215, 32))

        self.layout_vfo.addWidget(self.btn_vfo_mem_up, 1, 1, 1, 1)

        self.btn_vfo_num4 = QPushButton(self.tab_vfo)
        self.btn_vfo_num4.setObjectName(u"btn_vfo_num4")
        self.btn_vfo_num4.setMinimumSize(QSize(50, 32))
        self.btn_vfo_num4.setMaximumSize(QSize(50, 32))

        self.layout_vfo.addWidget(self.btn_vfo_num4, 2, 2, 1, 1)

        self.btn_vfo_set_b = QPushButton(self.tab_vfo)
        self.btn_vfo_set_b.setObjectName(u"btn_vfo_set_b")
        self.btn_vfo_set_b.setMinimumSize(QSize(50, 32))
        self.btn_vfo_set_b.setMaximumSize(QSize(50, 32))

        self.layout_vfo.addWidget(self.btn_vfo_set_b, 4, 4, 1, 1)

        self.btn_vfo_ba = QPushButton(self.tab_vfo)
        self.btn_vfo_ba.setObjectName(u"btn_vfo_ba")
        self.btn_vfo_ba.setMinimumSize(QSize(50, 32))
        self.btn_vfo_ba.setMaximumSize(QSize(16777215, 32))

        self.layout_vfo.addWidget(self.btn_vfo_ba, 3, 0, 1, 1)

        self.text_vfo = QLineEdit(self.tab_vfo)
        self.text_vfo.setObjectName(u"text_vfo")
        self.text_vfo.setMinimumSize(QSize(0, 30))
        self.text_vfo.setMaxLength(9)
        self.text_vfo.setFrame(True)
        self.text_vfo.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.layout_vfo.addWidget(self.text_vfo, 0, 2, 1, 3)

        self.btn_vfo_num0 = QPushButton(self.tab_vfo)
        self.btn_vfo_num0.setObjectName(u"btn_vfo_num0")
        self.btn_vfo_num0.setMinimumSize(QSize(50, 32))
        self.btn_vfo_num0.setMaximumSize(QSize(50, 32))

        self.layout_vfo.addWidget(self.btn_vfo_num0, 4, 3, 1, 1)

        self.btn_vfo_num7 = QPushButton(self.tab_vfo)
        self.btn_vfo_num7.setObjectName(u"btn_vfo_num7")
        self.btn_vfo_num7.setMinimumSize(QSize(50, 32))
        self.btn_vfo_num7.setMaximumSize(QSize(50, 32))

        self.layout_vfo.addWidget(self.btn_vfo_num7, 1, 2, 1, 1)

        self.btn_vfo_num1 = QPushButton(self.tab_vfo)
        self.btn_vfo_num1.setObjectName(u"btn_vfo_num1")
        self.btn_vfo_num1.setMinimumSize(QSize(50, 32))
        self.btn_vfo_num1.setMaximumSize(QSize(50, 32))

        self.layout_vfo.addWidget(self.btn_vfo_num1, 3, 2, 1, 1)

        self.btn_vfo_num6 = QPushButton(self.tab_vfo)
        self.btn_vfo_num6.setObjectName(u"btn_vfo_num6")
        self.btn_vfo_num6.setMinimumSize(QSize(50, 32))
        self.btn_vfo_num6.setMaximumSize(QSize(50, 32))

        self.layout_vfo.addWidget(self.btn_vfo_num6, 2, 4, 1, 1)

        self.btn_vfo_qmb_save = QPushButton(self.tab_vfo)
        self.btn_vfo_qmb_save.setObjectName(u"btn_vfo_qmb_save")
        self.btn_vfo_qmb_save.setMinimumSize(QSize(50, 32))
        self.btn_vfo_qmb_save.setMaximumSize(QSize(16777215, 32))

        self.layout_vfo.addWidget(self.btn_vfo_qmb_save, 3, 1, 1, 1)

        self.btn_vfo_ab = QPushButton(self.tab_vfo)
        self.btn_vfo_ab.setObjectName(u"btn_vfo_ab")
        self.btn_vfo_ab.setMinimumSize(QSize(50, 32))
        self.btn_vfo_ab.setMaximumSize(QSize(16777215, 32))

        self.layout_vfo.addWidget(self.btn_vfo_ab, 4, 0, 1, 1)

        self.btn_vfo_num8 = QPushButton(self.tab_vfo)
        self.btn_vfo_num8.setObjectName(u"btn_vfo_num8")
        self.btn_vfo_num8.setMinimumSize(QSize(50, 32))
        self.btn_vfo_num8.setMaximumSize(QSize(50, 32))

        self.layout_vfo.addWidget(self.btn_vfo_num8, 1, 3, 1, 1)

        self.btn_vfo_ma = QPushButton(self.tab_vfo)
        self.btn_vfo_ma.setObjectName(u"btn_vfo_ma")
        self.btn_vfo_ma.setMinimumSize(QSize(50, 32))
        self.btn_vfo_ma.setMaximumSize(QSize(16777215, 32))

        self.layout_vfo.addWidget(self.btn_vfo_ma, 1, 0, 1, 1)

        self.btn_vfo_mem_down = QPushButton(self.tab_vfo)
        self.btn_vfo_mem_down.setObjectName(u"btn_vfo_mem_down")
        self.btn_vfo_mem_down.setMinimumSize(QSize(50, 32))
        self.btn_vfo_mem_down.setMaximumSize(QSize(16777215, 32))

        self.layout_vfo.addWidget(self.btn_vfo_mem_down, 2, 1, 1, 1)

        self.btn_vfo_num5 = QPushButton(self.tab_vfo)
        self.btn_vfo_num5.setObjectName(u"btn_vfo_num5")
        self.btn_vfo_num5.setMinimumSize(QSize(50, 32))
        self.btn_vfo_num5.setMaximumSize(QSize(50, 32))

        self.layout_vfo.addWidget(self.btn_vfo_num5, 2, 3, 1, 1)

        self.btn_vfo_clear = QPushButton(self.tab_vfo)
        self.btn_vfo_clear.setObjectName(u"btn_vfo_clear")
        self.btn_vfo_clear.setMinimumSize(QSize(50, 32))
        self.btn_vfo_clear.setMaximumSize(QSize(16777215, 32))

        self.layout_vfo.addWidget(self.btn_vfo_clear, 0, 1, 1, 1)

        self.btn_vfo_swap = QPushButton(self.tab_vfo)
        self.btn_vfo_swap.setObjectName(u"btn_vfo_swap")
        self.btn_vfo_swap.setMinimumSize(QSize(50, 32))
        self.btn_vfo_swap.setMaximumSize(QSize(16777215, 32))

        self.layout_vfo.addWidget(self.btn_vfo_swap, 2, 0, 1, 1)

        self.btn_vfo_set_a = QPushButton(self.tab_vfo)
        self.btn_vfo_set_a.setObjectName(u"btn_vfo_set_a")
        self.btn_vfo_set_a.setMinimumSize(QSize(50, 32))
        self.btn_vfo_set_a.setMaximumSize(QSize(50, 32))

        self.layout_vfo.addWidget(self.btn_vfo_set_a, 4, 2, 1, 1)


        self.horizontalLayout_4.addLayout(self.layout_vfo)

        self.layout_channel = QVBoxLayout()
        self.layout_channel.setSpacing(0)
        self.layout_channel.setObjectName(u"layout_channel")
        self.spacer_up = QSpacerItem(20, 12, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout_channel.addItem(self.spacer_up)

        self.table_mem = QTableWidget(self.tab_vfo)
        if (self.table_mem.columnCount() < 3):
            self.table_mem.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_mem.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_mem.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_mem.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.table_mem.setObjectName(u"table_mem")
        self.table_mem.setMinimumSize(QSize(0, 0))

        self.layout_channel.addWidget(self.table_mem)

        self.spacer_down = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout_channel.addItem(self.spacer_down)


        self.horizontalLayout_4.addLayout(self.layout_channel)

        self.tab_main.addTab(self.tab_vfo, "")
        self.tab_rx = QWidget()
        self.tab_rx.setObjectName(u"tab_rx")
        self.tab_rx.setEnabled(True)
        self.verticalLayout_7 = QVBoxLayout(self.tab_rx)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(1, 1, 1, 1)
        self.layout_rx_up = QHBoxLayout()
        self.layout_rx_up.setSpacing(0)
        self.layout_rx_up.setObjectName(u"layout_rx_up")
        self.layout_rx_rf = QVBoxLayout()
        self.layout_rx_rf.setSpacing(2)
        self.layout_rx_rf.setObjectName(u"layout_rx_rf")
        self.lbl_rf = QLabel(self.tab_rx)
        self.lbl_rf.setObjectName(u"lbl_rf")

        self.layout_rx_rf.addWidget(self.lbl_rf)

        self.dial_rf = QDial(self.tab_rx)
        self.dial_rf.setObjectName(u"dial_rf")

        self.layout_rx_rf.addWidget(self.dial_rf)

        self.layout_rx_rf.setStretch(0, 1)
        self.layout_rx_rf.setStretch(1, 8)

        self.layout_rx_up.addLayout(self.layout_rx_rf)

        self.layout_rx_af = QVBoxLayout()
        self.layout_rx_af.setSpacing(2)
        self.layout_rx_af.setObjectName(u"layout_rx_af")
        self.lbl_af = QLabel(self.tab_rx)
        self.lbl_af.setObjectName(u"lbl_af")

        self.layout_rx_af.addWidget(self.lbl_af)

        self.dial_af = QDial(self.tab_rx)
        self.dial_af.setObjectName(u"dial_af")

        self.layout_rx_af.addWidget(self.dial_af)

        self.layout_rx_af.setStretch(0, 1)
        self.layout_rx_af.setStretch(1, 8)

        self.layout_rx_up.addLayout(self.layout_rx_af)

        self.layout_rx_sql = QVBoxLayout()
        self.layout_rx_sql.setSpacing(2)
        self.layout_rx_sql.setObjectName(u"layout_rx_sql")
        self.lbl_sql = QLabel(self.tab_rx)
        self.lbl_sql.setObjectName(u"lbl_sql")

        self.layout_rx_sql.addWidget(self.lbl_sql)

        self.dial_sql = QDial(self.tab_rx)
        self.dial_sql.setObjectName(u"dial_sql")

        self.layout_rx_sql.addWidget(self.dial_sql)

        self.layout_rx_sql.setStretch(0, 1)
        self.layout_rx_sql.setStretch(1, 8)

        self.layout_rx_up.addLayout(self.layout_rx_sql)

        self.layout_rx_width = QVBoxLayout()
        self.layout_rx_width.setSpacing(2)
        self.layout_rx_width.setObjectName(u"layout_rx_width")
        self.lbl_width = QLabel(self.tab_rx)
        self.lbl_width.setObjectName(u"lbl_width")

        self.layout_rx_width.addWidget(self.lbl_width)

        self.dial_width = QDial(self.tab_rx)
        self.dial_width.setObjectName(u"dial_width")

        self.layout_rx_width.addWidget(self.dial_width)

        self.layout_rx_width.setStretch(0, 1)
        self.layout_rx_width.setStretch(1, 8)

        self.layout_rx_up.addLayout(self.layout_rx_width)


        self.verticalLayout_7.addLayout(self.layout_rx_up)

        self.layout_rx_down = QHBoxLayout()
        self.layout_rx_down.setSpacing(0)
        self.layout_rx_down.setObjectName(u"layout_rx_down")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.tab_rx)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_6.addWidget(self.label_2)

        self.btn_ipo_on = QPushButton(self.tab_rx)
        self.btn_ipo_on.setObjectName(u"btn_ipo_on")
        self.btn_ipo_on.setMinimumSize(QSize(45, 23))
        self.btn_ipo_on.setMaximumSize(QSize(45, 23))

        self.horizontalLayout_6.addWidget(self.btn_ipo_on)

        self.btn_ipo_off = QPushButton(self.tab_rx)
        self.btn_ipo_off.setObjectName(u"btn_ipo_off")
        self.btn_ipo_off.setMinimumSize(QSize(45, 23))
        self.btn_ipo_off.setMaximumSize(QSize(45, 23))

        self.horizontalLayout_6.addWidget(self.btn_ipo_off)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_17 = QLabel(self.tab_rx)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_7.addWidget(self.label_17)

        self.btn_att_on = QPushButton(self.tab_rx)
        self.btn_att_on.setObjectName(u"btn_att_on")
        self.btn_att_on.setMinimumSize(QSize(45, 23))
        self.btn_att_on.setMaximumSize(QSize(45, 23))

        self.horizontalLayout_7.addWidget(self.btn_att_on)

        self.btn_att_off = QPushButton(self.tab_rx)
        self.btn_att_off.setObjectName(u"btn_att_off")
        self.btn_att_off.setMinimumSize(QSize(45, 23))
        self.btn_att_off.setMaximumSize(QSize(45, 23))

        self.horizontalLayout_7.addWidget(self.btn_att_off)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)


        self.layout_rx_down.addLayout(self.verticalLayout_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_20 = QLabel(self.tab_rx)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_8.addWidget(self.label_20)

        self.btn_nar_on = QPushButton(self.tab_rx)
        self.btn_nar_on.setObjectName(u"btn_nar_on")
        self.btn_nar_on.setMinimumSize(QSize(45, 23))
        self.btn_nar_on.setMaximumSize(QSize(45, 23))

        self.horizontalLayout_8.addWidget(self.btn_nar_on)

        self.btn_nar_off = QPushButton(self.tab_rx)
        self.btn_nar_off.setObjectName(u"btn_nar_off")
        self.btn_nar_off.setMinimumSize(QSize(45, 23))
        self.btn_nar_off.setMaximumSize(QSize(45, 23))

        self.horizontalLayout_8.addWidget(self.btn_nar_off)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_24 = QLabel(self.tab_rx)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_9.addWidget(self.label_24)

        self.btn_shift_on = QPushButton(self.tab_rx)
        self.btn_shift_on.setObjectName(u"btn_shift_on")
        self.btn_shift_on.setMinimumSize(QSize(45, 23))
        self.btn_shift_on.setMaximumSize(QSize(45, 23))

        self.horizontalLayout_9.addWidget(self.btn_shift_on)

        self.btn_shift_off = QPushButton(self.tab_rx)
        self.btn_shift_off.setObjectName(u"btn_shift_off")
        self.btn_shift_off.setMinimumSize(QSize(45, 23))
        self.btn_shift_off.setMaximumSize(QSize(45, 23))

        self.horizontalLayout_9.addWidget(self.btn_shift_off)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)


        self.layout_rx_down.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_23 = QLabel(self.tab_rx)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_10.addWidget(self.label_23)

        self.btn_agc_off = QPushButton(self.tab_rx)
        self.btn_agc_off.setObjectName(u"btn_agc_off")
        self.btn_agc_off.setMinimumSize(QSize(30, 23))
        self.btn_agc_off.setMaximumSize(QSize(16777215, 23))

        self.horizontalLayout_10.addWidget(self.btn_agc_off)

        self.btn_agc_fast = QPushButton(self.tab_rx)
        self.btn_agc_fast.setObjectName(u"btn_agc_fast")
        self.btn_agc_fast.setMinimumSize(QSize(30, 23))
        self.btn_agc_fast.setMaximumSize(QSize(16777215, 23))

        self.horizontalLayout_10.addWidget(self.btn_agc_fast)

        self.btn_agc_mid = QPushButton(self.tab_rx)
        self.btn_agc_mid.setObjectName(u"btn_agc_mid")
        self.btn_agc_mid.setMinimumSize(QSize(30, 23))
        self.btn_agc_mid.setMaximumSize(QSize(16777215, 23))

        self.horizontalLayout_10.addWidget(self.btn_agc_mid)

        self.btn_agc_slow = QPushButton(self.tab_rx)
        self.btn_agc_slow.setObjectName(u"btn_agc_slow")
        self.btn_agc_slow.setMinimumSize(QSize(30, 23))
        self.btn_agc_slow.setMaximumSize(QSize(16777215, 23))

        self.horizontalLayout_10.addWidget(self.btn_agc_slow)

        self.btn_agc_auto = QPushButton(self.tab_rx)
        self.btn_agc_auto.setObjectName(u"btn_agc_auto")
        self.btn_agc_auto.setMinimumSize(QSize(30, 23))
        self.btn_agc_auto.setMaximumSize(QSize(16777215, 23))

        self.horizontalLayout_10.addWidget(self.btn_agc_auto)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.spinBox_2 = QSpinBox(self.tab_rx)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMinimumSize(QSize(65, 23))
        self.spinBox_2.setMaximumSize(QSize(16777215, 23))

        self.horizontalLayout_11.addWidget(self.spinBox_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer)

        self.label_9 = QLabel(self.tab_rx)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_11.addWidget(self.label_9)

        self.btn_scan_up = QPushButton(self.tab_rx)
        self.btn_scan_up.setObjectName(u"btn_scan_up")
        self.btn_scan_up.setMinimumSize(QSize(0, 23))
        self.btn_scan_up.setMaximumSize(QSize(40, 23))

        self.horizontalLayout_11.addWidget(self.btn_scan_up)

        self.btn_scan_stop = QPushButton(self.tab_rx)
        self.btn_scan_stop.setObjectName(u"btn_scan_stop")
        self.btn_scan_stop.setMinimumSize(QSize(0, 23))
        self.btn_scan_stop.setMaximumSize(QSize(40, 23))

        self.horizontalLayout_11.addWidget(self.btn_scan_stop)

        self.btn_scan_down = QPushButton(self.tab_rx)
        self.btn_scan_down.setObjectName(u"btn_scan_down")
        self.btn_scan_down.setMinimumSize(QSize(0, 23))
        self.btn_scan_down.setMaximumSize(QSize(40, 23))

        self.horizontalLayout_11.addWidget(self.btn_scan_down)

        self.horizontalLayout_11.setStretch(0, 5)
        self.horizontalLayout_11.setStretch(2, 1)
        self.horizontalLayout_11.setStretch(3, 1)
        self.horizontalLayout_11.setStretch(4, 1)
        self.horizontalLayout_11.setStretch(5, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout_11)


        self.layout_rx_down.addLayout(self.verticalLayout_6)

        self.layout_rx_down.setStretch(0, 2)
        self.layout_rx_down.setStretch(1, 2)
        self.layout_rx_down.setStretch(2, 3)

        self.verticalLayout_7.addLayout(self.layout_rx_down)

        self.tab_main.addTab(self.tab_rx, "")
        self.tab_tx = QWidget()
        self.tab_tx.setObjectName(u"tab_tx")
        self.horizontalLayout_16 = QHBoxLayout(self.tab_tx)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setSpacing(2)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(1, -1, 1, -1)
        self.label_33 = QLabel(self.tab_tx)
        self.label_33.setObjectName(u"label_33")

        self.verticalLayout_30.addWidget(self.label_33)

        self.dial_power = QDial(self.tab_tx)
        self.dial_power.setObjectName(u"dial_power")

        self.verticalLayout_30.addWidget(self.dial_power)

        self.spin_power = QSpinBox(self.tab_tx)
        self.spin_power.setObjectName(u"spin_power")
        self.spin_power.setMinimum(5)
        self.spin_power.setMaximum(100)

        self.verticalLayout_30.addWidget(self.spin_power)

        self.verticalLayout_30.setStretch(0, 1)
        self.verticalLayout_30.setStretch(1, 6)
        self.verticalLayout_30.setStretch(2, 1)

        self.horizontalLayout_16.addLayout(self.verticalLayout_30)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setSpacing(2)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(1, -1, 1, -1)
        self.label_35 = QLabel(self.tab_tx)
        self.label_35.setObjectName(u"label_35")

        self.verticalLayout_32.addWidget(self.label_35)

        self.dial_vox = QDial(self.tab_tx)
        self.dial_vox.setObjectName(u"dial_vox")

        self.verticalLayout_32.addWidget(self.dial_vox)

        self.spin_vox = QSpinBox(self.tab_tx)
        self.spin_vox.setObjectName(u"spin_vox")
        self.spin_vox.setMaximum(100)

        self.verticalLayout_32.addWidget(self.spin_vox)

        self.verticalLayout_32.setStretch(0, 1)
        self.verticalLayout_32.setStretch(1, 6)
        self.verticalLayout_32.setStretch(2, 1)

        self.horizontalLayout_16.addLayout(self.verticalLayout_32)

        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setSpacing(2)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(1, -1, 1, -1)
        self.label_37 = QLabel(self.tab_tx)
        self.label_37.setObjectName(u"label_37")

        self.verticalLayout_34.addWidget(self.label_37)

        self.dial_mic = QDial(self.tab_tx)
        self.dial_mic.setObjectName(u"dial_mic")

        self.verticalLayout_34.addWidget(self.dial_mic)

        self.spin_mic = QSpinBox(self.tab_tx)
        self.spin_mic.setObjectName(u"spin_mic")
        self.spin_mic.setMaximum(100)

        self.verticalLayout_34.addWidget(self.spin_mic)

        self.verticalLayout_34.setStretch(0, 1)
        self.verticalLayout_34.setStretch(1, 6)
        self.verticalLayout_34.setStretch(2, 1)

        self.horizontalLayout_16.addLayout(self.verticalLayout_34)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_18 = QLabel(self.tab_tx)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_9.addWidget(self.label_18)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.btn_vox_on = QPushButton(self.tab_tx)
        self.btn_vox_on.setObjectName(u"btn_vox_on")
        self.btn_vox_on.setMinimumSize(QSize(30, 0))

        self.horizontalLayout_13.addWidget(self.btn_vox_on)

        self.btn_vox_off = QPushButton(self.tab_tx)
        self.btn_vox_off.setObjectName(u"btn_vox_off")
        self.btn_vox_off.setMinimumSize(QSize(30, 0))

        self.horizontalLayout_13.addWidget(self.btn_vox_off)


        self.verticalLayout_9.addLayout(self.horizontalLayout_13)

        self.label_19 = QLabel(self.tab_tx)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_9.addWidget(self.label_19)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(2)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.btn_moni_on = QPushButton(self.tab_tx)
        self.btn_moni_on.setObjectName(u"btn_moni_on")
        self.btn_moni_on.setMinimumSize(QSize(30, 0))

        self.horizontalLayout_14.addWidget(self.btn_moni_on)

        self.btn_moni_off = QPushButton(self.tab_tx)
        self.btn_moni_off.setObjectName(u"btn_moni_off")
        self.btn_moni_off.setMinimumSize(QSize(30, 0))

        self.horizontalLayout_14.addWidget(self.btn_moni_off)


        self.verticalLayout_9.addLayout(self.horizontalLayout_14)

        self.label_22 = QLabel(self.tab_tx)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_9.addWidget(self.label_22)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(2)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.btn_atu_on = QPushButton(self.tab_tx)
        self.btn_atu_on.setObjectName(u"btn_atu_on")
        self.btn_atu_on.setMinimumSize(QSize(50, 0))
        self.btn_atu_on.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_15.addWidget(self.btn_atu_on)

        self.btn_atu_off = QPushButton(self.tab_tx)
        self.btn_atu_off.setObjectName(u"btn_atu_off")
        self.btn_atu_off.setMinimumSize(QSize(50, 0))
        self.btn_atu_off.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_15.addWidget(self.btn_atu_off)


        self.verticalLayout_8.addLayout(self.horizontalLayout_15)

        self.btn_atu_tune = QPushButton(self.tab_tx)
        self.btn_atu_tune.setObjectName(u"btn_atu_tune")
        self.btn_atu_tune.setMinimumSize(QSize(50, 0))
        self.btn_atu_tune.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_8.addWidget(self.btn_atu_tune)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)


        self.horizontalLayout_16.addLayout(self.verticalLayout_9)

        self.horizontalLayout_16.setStretch(0, 4)
        self.horizontalLayout_16.setStretch(1, 4)
        self.horizontalLayout_16.setStretch(2, 4)
        self.horizontalLayout_16.setStretch(3, 1)
        self.tab_main.addTab(self.tab_tx, "")
        self.tab_dsp = QWidget()
        self.tab_dsp.setObjectName(u"tab_dsp")
        self.horizontalLayout_5 = QHBoxLayout(self.tab_dsp)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setSpacing(2)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_27 = QLabel(self.tab_dsp)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_24.addWidget(self.label_27)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.btn_nb_on = QPushButton(self.tab_dsp)
        self.btn_nb_on.setObjectName(u"btn_nb_on")
        self.btn_nb_on.setMinimumSize(QSize(50, 0))
        self.btn_nb_on.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_32.addWidget(self.btn_nb_on)

        self.btn_nb_off = QPushButton(self.tab_dsp)
        self.btn_nb_off.setObjectName(u"btn_nb_off")
        self.btn_nb_off.setMinimumSize(QSize(50, 0))
        self.btn_nb_off.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_32.addWidget(self.btn_nb_off)


        self.verticalLayout_24.addLayout(self.horizontalLayout_32)

        self.dial_nb = QDial(self.tab_dsp)
        self.dial_nb.setObjectName(u"dial_nb")

        self.verticalLayout_24.addWidget(self.dial_nb)

        self.spin_nb = QSpinBox(self.tab_dsp)
        self.spin_nb.setObjectName(u"spin_nb")

        self.verticalLayout_24.addWidget(self.spin_nb)

        self.verticalLayout_24.setStretch(0, 1)
        self.verticalLayout_24.setStretch(1, 1)
        self.verticalLayout_24.setStretch(2, 6)
        self.verticalLayout_24.setStretch(3, 1)

        self.horizontalLayout_5.addLayout(self.verticalLayout_24)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setSpacing(2)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_28 = QLabel(self.tab_dsp)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_25.addWidget(self.label_28)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.btn_nr_on = QPushButton(self.tab_dsp)
        self.btn_nr_on.setObjectName(u"btn_nr_on")
        self.btn_nr_on.setMinimumSize(QSize(50, 0))
        self.btn_nr_on.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_33.addWidget(self.btn_nr_on)

        self.btn_nr_off = QPushButton(self.tab_dsp)
        self.btn_nr_off.setObjectName(u"btn_nr_off")
        self.btn_nr_off.setMinimumSize(QSize(50, 0))
        self.btn_nr_off.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_33.addWidget(self.btn_nr_off)


        self.verticalLayout_25.addLayout(self.horizontalLayout_33)

        self.dial_nr = QDial(self.tab_dsp)
        self.dial_nr.setObjectName(u"dial_nr")

        self.verticalLayout_25.addWidget(self.dial_nr)

        self.spin_nr = QSpinBox(self.tab_dsp)
        self.spin_nr.setObjectName(u"spin_nr")

        self.verticalLayout_25.addWidget(self.spin_nr)

        self.verticalLayout_25.setStretch(0, 1)
        self.verticalLayout_25.setStretch(1, 1)
        self.verticalLayout_25.setStretch(2, 6)
        self.verticalLayout_25.setStretch(3, 1)

        self.horizontalLayout_5.addLayout(self.verticalLayout_25)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setSpacing(2)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_30 = QLabel(self.tab_dsp)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_27.addWidget(self.label_30)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.btn_contour_on = QPushButton(self.tab_dsp)
        self.btn_contour_on.setObjectName(u"btn_contour_on")
        self.btn_contour_on.setMinimumSize(QSize(50, 0))
        self.btn_contour_on.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_35.addWidget(self.btn_contour_on)

        self.btn_contour_off = QPushButton(self.tab_dsp)
        self.btn_contour_off.setObjectName(u"btn_contour_off")
        self.btn_contour_off.setMinimumSize(QSize(50, 0))
        self.btn_contour_off.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_35.addWidget(self.btn_contour_off)


        self.verticalLayout_27.addLayout(self.horizontalLayout_35)

        self.dial_contour = QDial(self.tab_dsp)
        self.dial_contour.setObjectName(u"dial_contour")

        self.verticalLayout_27.addWidget(self.dial_contour)

        self.spin_contour = QSpinBox(self.tab_dsp)
        self.spin_contour.setObjectName(u"spin_contour")

        self.verticalLayout_27.addWidget(self.spin_contour)

        self.verticalLayout_27.setStretch(0, 1)
        self.verticalLayout_27.setStretch(1, 1)
        self.verticalLayout_27.setStretch(2, 6)
        self.verticalLayout_27.setStretch(3, 1)

        self.horizontalLayout_5.addLayout(self.verticalLayout_27)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setSpacing(2)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_32 = QLabel(self.tab_dsp)
        self.label_32.setObjectName(u"label_32")

        self.verticalLayout_29.addWidget(self.label_32)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.btn_notch_on = QPushButton(self.tab_dsp)
        self.btn_notch_on.setObjectName(u"btn_notch_on")
        self.btn_notch_on.setMinimumSize(QSize(50, 0))
        self.btn_notch_on.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_37.addWidget(self.btn_notch_on)

        self.btn_notch_off = QPushButton(self.tab_dsp)
        self.btn_notch_off.setObjectName(u"btn_notch_off")
        self.btn_notch_off.setMinimumSize(QSize(50, 0))
        self.btn_notch_off.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_37.addWidget(self.btn_notch_off)


        self.verticalLayout_29.addLayout(self.horizontalLayout_37)

        self.dial_notch = QDial(self.tab_dsp)
        self.dial_notch.setObjectName(u"dial_notch")

        self.verticalLayout_29.addWidget(self.dial_notch)

        self.spin_notch = QSpinBox(self.tab_dsp)
        self.spin_notch.setObjectName(u"spin_notch")

        self.verticalLayout_29.addWidget(self.spin_notch)

        self.verticalLayout_29.setStretch(0, 1)
        self.verticalLayout_29.setStretch(1, 1)
        self.verticalLayout_29.setStretch(2, 6)
        self.verticalLayout_29.setStretch(3, 1)

        self.horizontalLayout_5.addLayout(self.verticalLayout_29)

        self.tab_main.addTab(self.tab_dsp, "")
        self.tab_cd = QWidget()
        self.tab_cd.setObjectName(u"tab_cd")
        self.horizontalLayout_23 = QHBoxLayout(self.tab_cd)
        self.horizontalLayout_23.setSpacing(2)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(2, 2, 2, 2)
        self.groupBox_6 = QGroupBox(self.tab_cd)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.horizontalLayout_17 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_17.setSpacing(3)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(3, 2, 2, 2)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_13 = QLabel(self.groupBox_6)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_5.addWidget(self.label_13, 0, 0, 1, 1)

        self.btn_bk_on = QPushButton(self.groupBox_6)
        self.btn_bk_on.setObjectName(u"btn_bk_on")
        self.btn_bk_on.setMinimumSize(QSize(10, 0))

        self.gridLayout_5.addWidget(self.btn_bk_on, 0, 1, 1, 1)

        self.btn_bk_off = QPushButton(self.groupBox_6)
        self.btn_bk_off.setObjectName(u"btn_bk_off")
        self.btn_bk_off.setMinimumSize(QSize(10, 0))

        self.gridLayout_5.addWidget(self.btn_bk_off, 0, 2, 1, 1)

        self.label_15 = QLabel(self.groupBox_6)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_5.addWidget(self.label_15, 1, 0, 1, 1)

        self.btn_keyer_on = QPushButton(self.groupBox_6)
        self.btn_keyer_on.setObjectName(u"btn_keyer_on")
        self.btn_keyer_on.setMinimumSize(QSize(10, 0))

        self.gridLayout_5.addWidget(self.btn_keyer_on, 1, 1, 1, 1)

        self.btn_keyer_off = QPushButton(self.groupBox_6)
        self.btn_keyer_off.setObjectName(u"btn_keyer_off")
        self.btn_keyer_off.setMinimumSize(QSize(10, 0))

        self.gridLayout_5.addWidget(self.btn_keyer_off, 1, 2, 1, 1)

        self.label_14 = QLabel(self.groupBox_6)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_5.addWidget(self.label_14, 2, 0, 1, 1)

        self.spin_delay = QSpinBox(self.groupBox_6)
        self.spin_delay.setObjectName(u"spin_delay")

        self.gridLayout_5.addWidget(self.spin_delay, 2, 1, 1, 2)

        self.label_16 = QLabel(self.groupBox_6)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_5.addWidget(self.label_16, 3, 0, 1, 1)

        self.spin_pitch = QSpinBox(self.groupBox_6)
        self.spin_pitch.setObjectName(u"spin_pitch")

        self.gridLayout_5.addWidget(self.spin_pitch, 3, 1, 1, 2)

        self.label_21 = QLabel(self.groupBox_6)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_5.addWidget(self.label_21, 4, 0, 1, 1)

        self.spin_speed = QSpinBox(self.groupBox_6)
        self.spin_speed.setObjectName(u"spin_speed")

        self.gridLayout_5.addWidget(self.spin_speed, 4, 1, 1, 2)


        self.horizontalLayout_17.addLayout(self.gridLayout_5)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setSpacing(2)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalSpacer_3 = QSpacerItem(20, 3, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_3)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_29 = QLabel(self.groupBox_6)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_34.addWidget(self.label_29)

        self.btn_apf_on = QPushButton(self.groupBox_6)
        self.btn_apf_on.setObjectName(u"btn_apf_on")
        self.btn_apf_on.setMinimumSize(QSize(50, 0))
        self.btn_apf_on.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_34.addWidget(self.btn_apf_on)

        self.btn_apf_off = QPushButton(self.groupBox_6)
        self.btn_apf_off.setObjectName(u"btn_apf_off")
        self.btn_apf_off.setMinimumSize(QSize(50, 0))
        self.btn_apf_off.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_34.addWidget(self.btn_apf_off)


        self.verticalLayout_26.addLayout(self.horizontalLayout_34)

        self.dial_apf = QDial(self.groupBox_6)
        self.dial_apf.setObjectName(u"dial_apf")

        self.verticalLayout_26.addWidget(self.dial_apf)

        self.spin_apf = QSpinBox(self.groupBox_6)
        self.spin_apf.setObjectName(u"spin_apf")

        self.verticalLayout_26.addWidget(self.spin_apf)

        self.verticalSpacer_2 = QSpacerItem(20, 3, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_2)

        self.verticalLayout_26.setStretch(2, 6)
        self.verticalLayout_26.setStretch(3, 1)

        self.horizontalLayout_17.addLayout(self.verticalLayout_26)


        self.horizontalLayout_23.addWidget(self.groupBox_6)

        self.groupBox_4 = QGroupBox(self.tab_cd)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setSpacing(2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(2, 2, 2, 2)
        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.list_ft8 = QComboBox(self.groupBox_4)
        self.list_ft8.setObjectName(u"list_ft8")
        self.list_ft8.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_4.addWidget(self.list_ft8, 0, 1, 1, 2)

        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)

        self.list_ft4 = QComboBox(self.groupBox_4)
        self.list_ft4.setObjectName(u"list_ft4")
        self.list_ft4.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_4.addWidget(self.list_ft4, 1, 1, 1, 2)

        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 2, 0, 1, 1)

        self.btn_bfo_lsb = QPushButton(self.groupBox_4)
        self.btn_bfo_lsb.setObjectName(u"btn_bfo_lsb")
        self.btn_bfo_lsb.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_4.addWidget(self.btn_bfo_lsb, 2, 1, 1, 1)

        self.btn_bfo_usb = QPushButton(self.groupBox_4)
        self.btn_bfo_usb.setObjectName(u"btn_bfo_usb")
        self.btn_bfo_usb.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_4.addWidget(self.btn_bfo_usb, 2, 2, 1, 1)

        self.label_10 = QLabel(self.groupBox_4)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 3, 0, 1, 1)

        self.btn_mic_front = QPushButton(self.groupBox_4)
        self.btn_mic_front.setObjectName(u"btn_mic_front")
        self.btn_mic_front.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_4.addWidget(self.btn_mic_front, 3, 1, 1, 1)

        self.btn_mic_rear = QPushButton(self.groupBox_4)
        self.btn_mic_rear.setObjectName(u"btn_mic_rear")
        self.btn_mic_rear.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_4.addWidget(self.btn_mic_rear, 3, 2, 1, 1)

        self.btn_data_resume = QPushButton(self.groupBox_4)
        self.btn_data_resume.setObjectName(u"btn_data_resume")

        self.gridLayout_4.addWidget(self.btn_data_resume, 4, 1, 1, 2)


        self.horizontalLayout_23.addWidget(self.groupBox_4)

        self.horizontalLayout_23.setStretch(0, 2)
        self.horizontalLayout_23.setStretch(1, 1)
        self.tab_main.addTab(self.tab_cd, "")
        self.tab_stat = QWidget()
        self.tab_stat.setObjectName(u"tab_stat")
        self.tab_main.addTab(self.tab_stat, "")
        self.tab_sys = QWidget()
        self.tab_sys.setObjectName(u"tab_sys")
        self.horizontalLayout_18 = QHBoxLayout(self.tab_sys)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.groupBox_2 = QGroupBox(self.tab_sys)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.list_serial_port = QComboBox(self.groupBox_2)
        self.list_serial_port.setObjectName(u"list_serial_port")

        self.gridLayout.addWidget(self.list_serial_port, 0, 1, 1, 1)

        self.btn_serial_refresh = QPushButton(self.groupBox_2)
        self.btn_serial_refresh.setObjectName(u"btn_serial_refresh")
        self.btn_serial_refresh.setMinimumSize(QSize(60, 0))

        self.gridLayout.addWidget(self.btn_serial_refresh, 0, 2, 1, 1)

        self.btn_serial_save = QPushButton(self.groupBox_2)
        self.btn_serial_save.setObjectName(u"btn_serial_save")
        self.btn_serial_save.setMinimumSize(QSize(60, 0))

        self.gridLayout.addWidget(self.btn_serial_save, 0, 3, 1, 1)

        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 1, 0, 1, 1)

        self.list_serial_baudrate = QComboBox(self.groupBox_2)
        self.list_serial_baudrate.addItem("")
        self.list_serial_baudrate.addItem("")
        self.list_serial_baudrate.addItem("")
        self.list_serial_baudrate.addItem("")
        self.list_serial_baudrate.addItem("")
        self.list_serial_baudrate.setObjectName(u"list_serial_baudrate")

        self.gridLayout.addWidget(self.list_serial_baudrate, 1, 1, 1, 1)

        self.btn_serial_connect = QPushButton(self.groupBox_2)
        self.btn_serial_connect.setObjectName(u"btn_serial_connect")
        self.btn_serial_connect.setMinimumSize(QSize(60, 0))

        self.gridLayout.addWidget(self.btn_serial_connect, 1, 2, 1, 1)

        self.btn_serial_break = QPushButton(self.groupBox_2)
        self.btn_serial_break.setObjectName(u"btn_serial_break")
        self.btn_serial_break.setMinimumSize(QSize(60, 0))

        self.gridLayout.addWidget(self.btn_serial_break, 1, 3, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)

        self.verticalLayout_10.addWidget(self.groupBox_2)

        self.groupBox_13 = QGroupBox(self.tab_sys)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.gridLayout_8 = QGridLayout(self.groupBox_13)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.btn_rig_poweron = QPushButton(self.groupBox_13)
        self.btn_rig_poweron.setObjectName(u"btn_rig_poweron")

        self.gridLayout_8.addWidget(self.btn_rig_poweron, 0, 0, 1, 1)

        self.btn_rig_dial1_down = QPushButton(self.groupBox_13)
        self.btn_rig_dial1_down.setObjectName(u"btn_rig_dial1_down")

        self.gridLayout_8.addWidget(self.btn_rig_dial1_down, 0, 3, 1, 1)

        self.btn_rig_lock = QPushButton(self.groupBox_13)
        self.btn_rig_lock.setObjectName(u"btn_rig_lock")

        self.gridLayout_8.addWidget(self.btn_rig_lock, 1, 0, 1, 1)

        self.btn_rig_dial2_down = QPushButton(self.groupBox_13)
        self.btn_rig_dial2_down.setObjectName(u"btn_rig_dial2_down")

        self.gridLayout_8.addWidget(self.btn_rig_dial2_down, 1, 3, 1, 1)

        self.btn_rig_poweroff = QPushButton(self.groupBox_13)
        self.btn_rig_poweroff.setObjectName(u"btn_rig_poweroff")

        self.gridLayout_8.addWidget(self.btn_rig_poweroff, 0, 1, 1, 1)

        self.btn_rig_dial2_up = QPushButton(self.groupBox_13)
        self.btn_rig_dial2_up.setObjectName(u"btn_rig_dial2_up")

        self.gridLayout_8.addWidget(self.btn_rig_dial2_up, 1, 2, 1, 1)

        self.btn_rig_fast = QPushButton(self.groupBox_13)
        self.btn_rig_fast.setObjectName(u"btn_rig_fast")

        self.gridLayout_8.addWidget(self.btn_rig_fast, 1, 1, 1, 1)

        self.btn_rig_dial1_up = QPushButton(self.groupBox_13)
        self.btn_rig_dial1_up.setObjectName(u"btn_rig_dial1_up")

        self.gridLayout_8.addWidget(self.btn_rig_dial1_up, 0, 2, 1, 1)

        self.btn_rig_fast_2 = QPushButton(self.groupBox_13)
        self.btn_rig_fast_2.setObjectName(u"btn_rig_fast_2")

        self.gridLayout_8.addWidget(self.btn_rig_fast_2, 0, 4, 1, 1)

        self.btn_rig_vm = QPushButton(self.groupBox_13)
        self.btn_rig_vm.setObjectName(u"btn_rig_vm")

        self.gridLayout_8.addWidget(self.btn_rig_vm, 1, 4, 1, 1)


        self.verticalLayout_10.addWidget(self.groupBox_13)


        self.horizontalLayout_18.addLayout(self.verticalLayout_10)

        self.groupBox_3 = QGroupBox(self.tab_sys)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.spin_refresh = QSpinBox(self.groupBox_3)
        self.spin_refresh.setObjectName(u"spin_refresh")

        self.verticalLayout_4.addWidget(self.spin_refresh)

        self.verticalSpacer = QSpacerItem(20, 58, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.btn_exit = QPushButton(self.groupBox_3)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setMinimumSize(QSize(0, 49))

        self.verticalLayout_4.addWidget(self.btn_exit)


        self.horizontalLayout_18.addWidget(self.groupBox_3)

        self.tab_main.addTab(self.tab_sys, "")

        self.verticalLayout_3.addWidget(self.tab_main)


        self.retranslateUi(Form)
        self.btn_exit.clicked.connect(Form.close)

        self.tab_main.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u7535\u53f0\u8f85\u52a9\u63a7\u5236", None))
        self.group_rig_lcd.setTitle(QCoreApplication.translate("Form", u"RigName", None))
        self.lbl_background.setText("")
        self.lbl_mode.setText(QCoreApplication.translate("Form", u"\u6a21\u5f0f", None))
        self.btn_mode_lsb.setText(QCoreApplication.translate("Form", u"LSB", None))
        self.btn_mode_usb.setText(QCoreApplication.translate("Form", u"USB", None))
        self.btn_mode_am.setText(QCoreApplication.translate("Form", u"AM", None))
        self.btn_mode_cwl.setText(QCoreApplication.translate("Form", u"CW-L", None))
        self.btn_mode_cwu.setText(QCoreApplication.translate("Form", u"CW-U", None))
        self.btn_mode_fm.setText(QCoreApplication.translate("Form", u"FM", None))
        self.btn_mode_rttyl.setText(QCoreApplication.translate("Form", u"RTTY-L", None))
        self.btn_mode_rttyu.setText(QCoreApplication.translate("Form", u"RTTY-U", None))
        self.btn_mode_c4fm.setText(QCoreApplication.translate("Form", u"C4FM", None))
        self.btn_mode_datal.setText(QCoreApplication.translate("Form", u"DATA-L", None))
        self.btn_mode_datau.setText(QCoreApplication.translate("Form", u"DATA-U", None))
        self.btn_mode_datafm.setText(QCoreApplication.translate("Form", u"DATA-F", None))
        self.lbl_band.setText(QCoreApplication.translate("Form", u"\u6ce2\u6bb5", None))
        self.btn_band_430.setText(QCoreApplication.translate("Form", u"430", None))
        self.btn_band_mw.setText(QCoreApplication.translate("Form", u"MW", None))
        self.btn_band_10.setText(QCoreApplication.translate("Form", u"10", None))
        self.btn_band_18.setText(QCoreApplication.translate("Form", u"18", None))
        self.btn_band_21.setText(QCoreApplication.translate("Form", u"21", None))
        self.btn_band_3_5.setText(QCoreApplication.translate("Form", u"3.5", None))
        self.btn_band_air.setText(QCoreApplication.translate("Form", u"AIR", None))
        self.btn_band_24.setText(QCoreApplication.translate("Form", u"24", None))
        self.btn_band_7_0.setText(QCoreApplication.translate("Form", u"7.0", None))
        self.btn_band_144.setText(QCoreApplication.translate("Form", u"144", None))
        self.btn_band_14.setText(QCoreApplication.translate("Form", u"14", None))
        self.btn_band_28.setText(QCoreApplication.translate("Form", u"28", None))
        self.btn_band_1_8.setText(QCoreApplication.translate("Form", u"1.8", None))
        self.btn_band_50.setText(QCoreApplication.translate("Form", u"50", None))
        self.btn_band_gen.setText(QCoreApplication.translate("Form", u"GEN", None))
        self.btn_band_5_0.setText(QCoreApplication.translate("Form", u"5.0", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_basic), QCoreApplication.translate("Form", u"\u5e38\u7528", None))
        self.btn_vfo_num2.setText(QCoreApplication.translate("Form", u"2", None))
        self.btn_vfo_num3.setText(QCoreApplication.translate("Form", u"3", None))
        self.btn_vfo_num9.setText(QCoreApplication.translate("Form", u"9", None))
        self.btn_vfo_qmb_recall.setText(QCoreApplication.translate("Form", u"QMB\u53d6", None))
        self.btn_vfo_am.setText(QCoreApplication.translate("Form", u"A->M", None))
        self.btn_vfo_mem_up.setText(QCoreApplication.translate("Form", u"\u9891\u9053-", None))
        self.btn_vfo_num4.setText(QCoreApplication.translate("Form", u"4", None))
        self.btn_vfo_set_b.setText(QCoreApplication.translate("Form", u"B", None))
        self.btn_vfo_ba.setText(QCoreApplication.translate("Form", u"B->A", None))
        self.text_vfo.setInputMask("")
        self.btn_vfo_num0.setText(QCoreApplication.translate("Form", u"0", None))
        self.btn_vfo_num7.setText(QCoreApplication.translate("Form", u"7", None))
        self.btn_vfo_num1.setText(QCoreApplication.translate("Form", u"1", None))
        self.btn_vfo_num6.setText(QCoreApplication.translate("Form", u"6", None))
        self.btn_vfo_qmb_save.setText(QCoreApplication.translate("Form", u"QMB\u5b58", None))
        self.btn_vfo_ab.setText(QCoreApplication.translate("Form", u"A->B", None))
        self.btn_vfo_num8.setText(QCoreApplication.translate("Form", u"8", None))
        self.btn_vfo_ma.setText(QCoreApplication.translate("Form", u"M->A", None))
        self.btn_vfo_mem_down.setText(QCoreApplication.translate("Form", u"\u9891\u9053+", None))
        self.btn_vfo_num5.setText(QCoreApplication.translate("Form", u"5", None))
        self.btn_vfo_clear.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a", None))
        self.btn_vfo_swap.setText(QCoreApplication.translate("Form", u"A<>B", None))
        self.btn_vfo_set_a.setText(QCoreApplication.translate("Form", u"A", None))
        ___qtablewidgetitem = self.table_mem.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u5e8f\u53f7", None));
        ___qtablewidgetitem1 = self.table_mem.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u6a21\u5f0f", None));
        ___qtablewidgetitem2 = self.table_mem.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u9891\u7387", None));
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_vfo), QCoreApplication.translate("Form", u"\u9891\u7387", None))
        self.lbl_rf.setText(QCoreApplication.translate("Form", u"\u63a5\u6536\u589e\u76ca", None))
        self.lbl_af.setText(QCoreApplication.translate("Form", u"\u97f3\u91cf", None))
        self.lbl_sql.setText(QCoreApplication.translate("Form", u"\u9759\u566a", None))
        self.lbl_width.setText(QCoreApplication.translate("Form", u"\u5e26\u5bbd", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"IPO", None))
        self.btn_ipo_on.setText(QCoreApplication.translate("Form", u"\u5f00", None))
        self.btn_ipo_off.setText(QCoreApplication.translate("Form", u"\u5173", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"ATT", None))
        self.btn_att_on.setText(QCoreApplication.translate("Form", u"\u5f00", None))
        self.btn_att_off.setText(QCoreApplication.translate("Form", u"\u5173", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"\u7a84\u5e26", None))
        self.btn_nar_on.setText(QCoreApplication.translate("Form", u"\u5f00", None))
        self.btn_nar_off.setText(QCoreApplication.translate("Form", u"\u5173", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"\u5f02\u9891", None))
        self.btn_shift_on.setText(QCoreApplication.translate("Form", u"\u5f00", None))
        self.btn_shift_off.setText(QCoreApplication.translate("Form", u"\u5173", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"AGC", None))
        self.btn_agc_off.setText(QCoreApplication.translate("Form", u"\u5173\u95ed", None))
        self.btn_agc_fast.setText(QCoreApplication.translate("Form", u"\u5feb", None))
        self.btn_agc_mid.setText(QCoreApplication.translate("Form", u"\u4e2d", None))
        self.btn_agc_slow.setText(QCoreApplication.translate("Form", u"\u6162", None))
        self.btn_agc_auto.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u626b\u63cf", None))
        self.btn_scan_up.setText(QCoreApplication.translate("Form", u"+", None))
        self.btn_scan_stop.setText(QCoreApplication.translate("Form", u"\u505c", None))
        self.btn_scan_down.setText(QCoreApplication.translate("Form", u"-", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_rx), QCoreApplication.translate("Form", u"\u63a5\u6536", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"\u529f\u7387", None))
        self.spin_power.setSuffix(QCoreApplication.translate("Form", u" W", None))
        self.label_35.setText(QCoreApplication.translate("Form", u"\u58f0\u63a7\u589e\u76ca", None))
        self.spin_vox.setSuffix(QCoreApplication.translate("Form", u" %", None))
        self.label_37.setText(QCoreApplication.translate("Form", u"\u9ea6\u514b\u98ce", None))
        self.spin_mic.setSuffix(QCoreApplication.translate("Form", u" %", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"\u58f0\u63a7", None))
        self.btn_vox_on.setText(QCoreApplication.translate("Form", u"\u5f00", None))
        self.btn_vox_off.setText(QCoreApplication.translate("Form", u"\u5173", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"\u76d1\u542c", None))
        self.btn_moni_on.setText(QCoreApplication.translate("Form", u"\u5f00", None))
        self.btn_moni_off.setText(QCoreApplication.translate("Form", u"\u5173", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"\u5929\u8c03", None))
        self.btn_atu_on.setText(QCoreApplication.translate("Form", u"\u5f00\u542f", None))
        self.btn_atu_off.setText(QCoreApplication.translate("Form", u"\u5173\u95ed", None))
        self.btn_atu_tune.setText(QCoreApplication.translate("Form", u"\u8c03\u8282", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_tx), QCoreApplication.translate("Form", u"\u53d1\u5c04", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"NB", None))
        self.btn_nb_on.setText(QCoreApplication.translate("Form", u"\u5f00", None))
        self.btn_nb_off.setText(QCoreApplication.translate("Form", u"\u5173", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"NR", None))
        self.btn_nr_on.setText(QCoreApplication.translate("Form", u"\u5f00", None))
        self.btn_nr_off.setText(QCoreApplication.translate("Form", u"\u5173", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"CONTOUR", None))
        self.btn_contour_on.setText(QCoreApplication.translate("Form", u"\u5f00", None))
        self.btn_contour_off.setText(QCoreApplication.translate("Form", u"\u5173", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"NOTCH", None))
        self.btn_notch_on.setText(QCoreApplication.translate("Form", u"\u5f00", None))
        self.btn_notch_off.setText(QCoreApplication.translate("Form", u"\u5173", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_dsp), QCoreApplication.translate("Form", u"\u964d\u566a", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Form", u"CW", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u4fa7\u97f3", None))
        self.btn_bk_on.setText(QCoreApplication.translate("Form", u"\u5f00", None))
        self.btn_bk_off.setText(QCoreApplication.translate("Form", u"\u5173", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u952e", None))
        self.btn_keyer_on.setText(QCoreApplication.translate("Form", u"\u5f00", None))
        self.btn_keyer_off.setText(QCoreApplication.translate("Form", u"\u5173", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"\u5ef6\u8fdf", None))
        self.spin_delay.setSuffix(QCoreApplication.translate("Form", u" ms", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"\u97f3\u8c03", None))
        self.spin_pitch.setSuffix(QCoreApplication.translate("Form", u" Hz", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"\u952e\u901f", None))
        self.spin_speed.setSuffix(QCoreApplication.translate("Form", u" wpm", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"APF", None))
        self.btn_apf_on.setText(QCoreApplication.translate("Form", u"\u5f00", None))
        self.btn_apf_off.setText(QCoreApplication.translate("Form", u"\u5173", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"DATA", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"FT8\u9891\u7387", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"FT4\u9891\u7387", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"BFO", None))
        self.btn_bfo_lsb.setText(QCoreApplication.translate("Form", u"LSB", None))
        self.btn_bfo_usb.setText(QCoreApplication.translate("Form", u"USB", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u9ea6\u514b\u98ce", None))
        self.btn_mic_front.setText(QCoreApplication.translate("Form", u"\u524d", None))
        self.btn_mic_rear.setText(QCoreApplication.translate("Form", u"\u540e", None))
        self.btn_data_resume.setText(QCoreApplication.translate("Form", u"\u590d\u539f", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_cd), QCoreApplication.translate("Form", u"CW", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_stat), QCoreApplication.translate("Form", u"\u72b6\u6001", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
        self.label_6.setText(QCoreApplication.translate("Form", u" \u4e32  \u53e3", None))
        self.btn_serial_refresh.setText(QCoreApplication.translate("Form", u"\u5237\u65b0", None))
        self.btn_serial_save.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58", None))
        self.label_12.setText(QCoreApplication.translate("Form", u" \u6ce2\u7279\u7387", None))
        self.list_serial_baudrate.setItemText(0, QCoreApplication.translate("Form", u"4800", None))
        self.list_serial_baudrate.setItemText(1, QCoreApplication.translate("Form", u"9600", None))
        self.list_serial_baudrate.setItemText(2, QCoreApplication.translate("Form", u"14400", None))
        self.list_serial_baudrate.setItemText(3, QCoreApplication.translate("Form", u"19200", None))
        self.list_serial_baudrate.setItemText(4, QCoreApplication.translate("Form", u"38400", None))

        self.btn_serial_connect.setText(QCoreApplication.translate("Form", u"\u8fde\u63a5", None))
        self.btn_serial_break.setText(QCoreApplication.translate("Form", u"\u65ad\u5f00", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("Form", u"\u6309\u952e\u6a21\u62df", None))
        self.btn_rig_poweron.setText(QCoreApplication.translate("Form", u"\u7535\u6e90\u5f00", None))
        self.btn_rig_dial1_down.setText(QCoreApplication.translate("Form", u"\u4e3b\u65cb\u94ae-", None))
        self.btn_rig_lock.setText(QCoreApplication.translate("Form", u"LOCK", None))
        self.btn_rig_dial2_down.setText(QCoreApplication.translate("Form", u"\u526f\u65cb\u94ae-", None))
        self.btn_rig_poweroff.setText(QCoreApplication.translate("Form", u"\u7535\u6e90\u5173", None))
        self.btn_rig_dial2_up.setText(QCoreApplication.translate("Form", u"\u526f\u65cb\u94ae+", None))
        self.btn_rig_fast.setText(QCoreApplication.translate("Form", u"FAST", None))
        self.btn_rig_dial1_up.setText(QCoreApplication.translate("Form", u"\u4e3b\u65cb\u94ae+", None))
        self.btn_rig_fast_2.setText(QCoreApplication.translate("Form", u"FAST", None))
        self.btn_rig_vm.setText(QCoreApplication.translate("Form", u"V/M", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u7cfb\u7edf", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5237\u65b0\u9891\u7387", None))
        self.spin_refresh.setSuffix(QCoreApplication.translate("Form", u" ms", None))
        self.btn_exit.setText(QCoreApplication.translate("Form", u"\u9000\u51fa", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_sys), QCoreApplication.translate("Form", u"\u7cfb\u7edf", None))
    # retranslateUi

