# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'symmGui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!


import numpy as np
import matplotlib.pyplot as plt

import gsyIO
import gsyTransforms as trf

from PyQt5 import QtCore, QtGui, QtWidgets
from asteval import Interpreter
from numbers import Number


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(536, 421)
        MainWindow.setMinimumSize(QtCore.QSize(493, 404))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 1000))
        MainWindow.setBaseSize(QtCore.QSize(493, 404))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_equations = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setBold(True)
        font.setWeight(75)
        self.lbl_equations.setFont(font)
        self.lbl_equations.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lbl_equations.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_equations.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_equations.setObjectName("lbl_equations")
        self.verticalLayout_2.addWidget(self.lbl_equations)
        self.lbl_units = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_units.setFont(font)
        self.lbl_units.setObjectName("lbl_units")
        self.verticalLayout_2.addWidget(self.lbl_units)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_phaseBMag = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_phaseBMag.setFont(font)
        self.lbl_phaseBMag.setObjectName("lbl_phaseBMag")
        self.gridLayout.addWidget(self.lbl_phaseBMag, 1, 0, 1, 1)
        self.ledt_phaseAOmega = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_phaseAOmega.setObjectName("ledt_phaseAOmega")
        self.gridLayout.addWidget(self.ledt_phaseAOmega, 0, 3, 1, 1)
        self.lbl_phaseAPhi = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_phaseAPhi.setFont(font)
        self.lbl_phaseAPhi.setObjectName("lbl_phaseAPhi")
        self.gridLayout.addWidget(self.lbl_phaseAPhi, 0, 4, 1, 1)
        self.lbl_phaseAMag = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_phaseAMag.setFont(font)
        self.lbl_phaseAMag.setObjectName("lbl_phaseAMag")
        self.gridLayout.addWidget(self.lbl_phaseAMag, 0, 0, 1, 1)
        self.ledt_phaseAMag = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_phaseAMag.setObjectName("ledt_phaseAMag")
        self.gridLayout.addWidget(self.ledt_phaseAMag, 0, 1, 1, 1)
        self.ledt_phaseAPhi = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_phaseAPhi.setObjectName("ledt_phaseAPhi")
        self.gridLayout.addWidget(self.ledt_phaseAPhi, 0, 5, 1, 1)
        self.ledt_phaseCMag = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_phaseCMag.setObjectName("ledt_phaseCMag")
        self.gridLayout.addWidget(self.ledt_phaseCMag, 2, 1, 1, 1)
        self.ledt_phaseBPhi = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_phaseBPhi.setObjectName("ledt_phaseBPhi")
        self.gridLayout.addWidget(self.ledt_phaseBPhi, 1, 5, 1, 1)
        self.lbl_phaseCMag = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_phaseCMag.setFont(font)
        self.lbl_phaseCMag.setObjectName("lbl_phaseCMag")
        self.gridLayout.addWidget(self.lbl_phaseCMag, 2, 0, 1, 1)
        self.ledt_phaseCOmega = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_phaseCOmega.setObjectName("ledt_phaseCOmega")
        self.gridLayout.addWidget(self.ledt_phaseCOmega, 2, 3, 1, 1)
        self.lbl_phaseCOmega = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_phaseCOmega.setFont(font)
        self.lbl_phaseCOmega.setObjectName("lbl_phaseCOmega")
        self.gridLayout.addWidget(self.lbl_phaseCOmega, 2, 2, 1, 1)
        self.ledt_pllOmega = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_pllOmega.setObjectName("ledt_pllOmega")
        self.gridLayout.addWidget(self.ledt_pllOmega, 3, 1, 1, 1)
        self.lbl_pllOmega = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_pllOmega.setFont(font)
        self.lbl_pllOmega.setObjectName("lbl_pllOmega")
        self.gridLayout.addWidget(self.lbl_pllOmega, 3, 0, 1, 1)
        self.ledt_phaseCPhi = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_phaseCPhi.setObjectName("ledt_phaseCPhi")
        self.gridLayout.addWidget(self.ledt_phaseCPhi, 2, 5, 1, 1)
        self.lbl_phaseCPhi = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_phaseCPhi.setFont(font)
        self.lbl_phaseCPhi.setObjectName("lbl_phaseCPhi")
        self.gridLayout.addWidget(self.lbl_phaseCPhi, 2, 4, 1, 1)
        self.ledt_pllPhi = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_pllPhi.setObjectName("ledt_pllPhi")
        self.gridLayout.addWidget(self.ledt_pllPhi, 3, 3, 1, 1)
        self.ledt_time = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_time.setObjectName("ledt_time")
        self.gridLayout.addWidget(self.ledt_time, 4, 1, 1, 1)
        self.lbl_time = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_time.setFont(font)
        self.lbl_time.setObjectName("lbl_time")
        self.gridLayout.addWidget(self.lbl_time, 4, 0, 1, 1)
        self.ledt_phaseBOmega = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_phaseBOmega.setObjectName("ledt_phaseBOmega")
        self.gridLayout.addWidget(self.ledt_phaseBOmega, 1, 3, 1, 1)
        self.lbl_phaseBPhi = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_phaseBPhi.setFont(font)
        self.lbl_phaseBPhi.setObjectName("lbl_phaseBPhi")
        self.gridLayout.addWidget(self.lbl_phaseBPhi, 1, 4, 1, 1)
        self.lbl_pllPhase = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_pllPhase.setFont(font)
        self.lbl_pllPhase.setObjectName("lbl_pllPhase")
        self.gridLayout.addWidget(self.lbl_pllPhase, 3, 2, 1, 1)
        self.lbl_phaseBOmega = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_phaseBOmega.setFont(font)
        self.lbl_phaseBOmega.setObjectName("lbl_phaseBOmega")
        self.gridLayout.addWidget(self.lbl_phaseBOmega, 1, 2, 1, 1)
        self.ledt_phaseBMag = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_phaseBMag.setObjectName("ledt_phaseBMag")
        self.gridLayout.addWidget(self.ledt_phaseBMag, 1, 1, 1, 1)
        self.lbl_phaseAOmega = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_phaseAOmega.setFont(font)
        self.lbl_phaseAOmega.setObjectName("lbl_phaseAOmega")
        self.gridLayout.addWidget(self.lbl_phaseAOmega, 0, 2, 1, 1)
        self.btn_update = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setBold(True)
        font.setWeight(75)
        self.btn_update.setFont(font)
        self.btn_update.setObjectName("btn_update")
        self.gridLayout.addWidget(self.btn_update, 4, 5, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 536, 26))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.file_saveData = QtWidgets.QAction(MainWindow)
        self.file_saveData.setObjectName("file_saveData")
        self.help_Documentation = QtWidgets.QAction(MainWindow)
        self.help_Documentation.setObjectName("help_Documentation")
        self.help_About = QtWidgets.QAction(MainWindow)
        self.help_About.setObjectName("help_About")
        self.file_saveSetting = QtWidgets.QAction(MainWindow)
        self.file_saveSetting.setObjectName("file_saveSetting")
        self.file_Exit = QtWidgets.QAction(MainWindow)
        self.file_Exit.setObjectName("file_Exit")
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.file_saveData)
        self.menu_file.addAction(self.file_saveSetting)
        self.menu_file.addAction(self.file_Exit)
        self.menu_help.addAction(self.help_Documentation)
        self.menu_help.addSeparator()
        self.menu_help.addAction(self.help_About)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)

        self.file_Exit.triggered.connect(MainWindow.close)

#        self.file_saveData.triggered.connect(self.file_save_data)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.ledt_phaseAMag, self.ledt_phaseAOmega)
        MainWindow.setTabOrder(self.ledt_phaseAOmega, self.ledt_phaseAPhi)
        MainWindow.setTabOrder(self.ledt_phaseAPhi, self.ledt_phaseBMag)
        MainWindow.setTabOrder(self.ledt_phaseBMag, self.ledt_phaseBOmega)
        MainWindow.setTabOrder(self.ledt_phaseBOmega, self.ledt_phaseBPhi)
        MainWindow.setTabOrder(self.ledt_phaseBPhi, self.ledt_phaseCMag)
        MainWindow.setTabOrder(self.ledt_phaseCMag, self.ledt_phaseCOmega)
        MainWindow.setTabOrder(self.ledt_phaseCOmega, self.ledt_phaseCPhi)
        MainWindow.setTabOrder(self.ledt_phaseCPhi, self.ledt_pllOmega)
        MainWindow.setTabOrder(self.ledt_pllOmega, self.ledt_pllPhi)
        
        self.phaseAMag      = None
        self.phaseAOmega    = None
        self.phaseAPhi      = None
        
        self.phaseBMag      = None
        self.phaseBOmega    = None
        self.phaseBPhi      = None
        
        self.phaseCMag      = None
        self.phaseCOmega    = None
        self.phaseCPhi      = None
        
        self.pllOmega       = None
        self.pllPhi         = None
        
        self.timeEnd        = None

        self.time_samples   = None

        self.phaseAdata = None
        self.phaseAdata_real = None
        self.phaseAdata_imag = None

        self.phaseBdata = None
        self.phaseBdata_real = None
        self.phaseBdata_imag = None

        self.phaseCdata = None
        self.phaseCdata_real = None
        self.phaseCdata_imag = None

        # self.
        
        self.btn_update.clicked.connect(self.update)
        self.file_saveData.triggered.connect(self.save_data)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_equations.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Equations:</span></p><p><img src=\":/equations_/equations_all_inputs_150.png\"/></p></body></html>"))
        self.lbl_units.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">Units : angular freq. are in rad/s; phases are in rad, time in seconds</span></p></body></html>"))
        self.lbl_phaseBMag.setText(_translate("MainWindow", "<html><head/><body><p>Mag<span style=\" vertical-align:sub;\">b</span><span style=\" font-style:normal;\"> : </span></p></body></html>"))
        self.ledt_phaseAOmega.setToolTip(_translate("MainWindow", "The angular frequency of Phase-A input"))
        self.lbl_phaseAPhi.setText(_translate("MainWindow", "<html><head/><body><p>&phi;<span style=\" vertical-align:sub;\">a</span><span style=\" font-style:normal;\"> :</span></p></body></html>"))
        self.lbl_phaseAMag.setText(_translate("MainWindow", "<html><head/><body><p>Mag<span style=\" vertical-align:sub;\">a</span><span style=\" font-style:normal;\"> : </span></p></body></html>"))
        self.ledt_phaseAMag.setToolTip(_translate("MainWindow", "The magnitude of Phase-A input"))
        self.ledt_phaseAPhi.setToolTip(_translate("MainWindow", "The initial phase of Phase-A input"))
        self.ledt_phaseCMag.setToolTip(_translate("MainWindow", "The magnitude of Phase-C input"))
        self.ledt_phaseBPhi.setToolTip(_translate("MainWindow", "The initial phase of Phase-B input"))
        self.lbl_phaseCMag.setText(_translate("MainWindow", "<html><head/><body><p>Mag<span style=\" vertical-align:sub;\">c</span><span style=\" font-style:normal;\"> : </span></p></body></html>"))
        self.ledt_phaseCOmega.setToolTip(_translate("MainWindow", "The angular frequency of Phase-C input"))
        self.lbl_phaseCOmega.setText(_translate("MainWindow", "<html><head/><body><p>ω<span style=\" vertical-align:sub;\">c</span><span style=\" font-style:normal;\"> :</span></p></body></html>"))
        self.ledt_pllOmega.setToolTip(_translate("MainWindow", "The angular frequency of the PLL"))
        self.lbl_pllOmega.setText(_translate("MainWindow", "<html><head/><body><p>ω<span style=\" vertical-align:sub;\">PLL</span><span style=\" font-style:normal;\"> :</span></p></body></html>"))
        self.ledt_phaseCPhi.setToolTip(_translate("MainWindow", "The initial phase of Phase-C input"))
        self.lbl_phaseCPhi.setText(_translate("MainWindow", "<html><head/><body><p>&phi;<span style=\" vertical-align:sub;\">c</span><span style=\" font-style:normal;\"> :</span></p></body></html>"))
        self.ledt_pllPhi.setToolTip(_translate("MainWindow", "The initial phase of the PLL"))
        self.ledt_time.setToolTip(_translate("MainWindow", "The total time"))
        self.lbl_time.setText(_translate("MainWindow", "<html><head/><body><p>t<span style=\" font-style:normal;\"> : </span></p></body></html>"))
        self.ledt_phaseBOmega.setToolTip(_translate("MainWindow", "The angular frequency of Phase-B input"))
        self.lbl_phaseBPhi.setText(_translate("MainWindow", "<html><head/><body><p>&phi;<span style=\" vertical-align:sub;\">b</span><span style=\" font-style:normal;\"> :</span></p></body></html>"))
        self.lbl_pllPhase.setText(_translate("MainWindow", "<html><head/><body><p>&phi;<span style=\" vertical-align:sub;\">PLL</span><span style=\" font-style:normal;\"> :</span></p></body></html>"))
        self.lbl_phaseBOmega.setText(_translate("MainWindow", "<html><head/><body><p>ω<span style=\" vertical-align:sub;\">b</span><span style=\" font-style:normal;\"> :</span></p></body></html>"))
        self.ledt_phaseBMag.setToolTip(_translate("MainWindow", "The magnitude of Phase-B input"))
        self.lbl_phaseAOmega.setText(_translate("MainWindow", "<html><head/><body><p>ω<span style=\" vertical-align:sub;\">a</span><span style=\" font-style:normal;\"> :</span></p></body></html>"))
        self.btn_update.setText(_translate("MainWindow", "Update"))
        self.menu_file.setTitle(_translate("MainWindow", "File"))
        self.menu_help.setTitle(_translate("MainWindow", "Help"))
        self.file_saveData.setText(_translate("MainWindow", "Save Data"))
        self.help_Documentation.setText(_translate("MainWindow", "Documentation"))
        self.help_About.setText(_translate("MainWindow", "About"))
        self.file_saveSetting.setText(_translate("MainWindow", "Save Setting"))
        self.file_Exit.setText(_translate("MainWindow", "Exit"))

    def update(self):
        
        plt.close('all')

        print(gsyIO.date_time_now() + 'Updating')

        list_temp = []
        
        self.phaseAMag      = self.to_numeric(self.ledt_phaseAMag.text())
        self.phaseAOmega    = self.to_numeric(self.ledt_phaseAOmega.text())
        self.phaseAPhi      = self.to_numeric(self.ledt_phaseAPhi.text())
        
        list_temp.append(['Phase-A Mag = ', self.phaseAMag])
        list_temp.append(['Phase-A Omega = ', self.phaseAOmega])
        list_temp.append(['Phase-A Phi = ', self.phaseAPhi])

        self.phaseBMag      = self.to_numeric(self.ledt_phaseBMag.text())
        self.phaseBOmega    = self.to_numeric(self.ledt_phaseBOmega.text())
        self.phaseBPhi      = self.to_numeric(self.ledt_phaseBPhi.text())

        list_temp.append(['Phase-B Mag = ', self.phaseBMag])
        list_temp.append(['Phase-B Omega = ', self.phaseBOmega])
        list_temp.append(['Phase-B Phi = ', self.phaseBPhi])

        self.phaseCMag      = self.to_numeric(self.ledt_phaseCMag.text())
        self.phaseCOmega    = self.to_numeric(self.ledt_phaseCOmega.text())
        self.phaseCPhi      = self.to_numeric(self.ledt_phaseCPhi.text())

        list_temp.append(['Phase-C Mag = ', self.phaseCMag])
        list_temp.append(['Phase-C Omega = ', self.phaseCOmega])
        list_temp.append(['Phase-C Phi = ', self.phaseCPhi])

        self.pllOmega       = self.to_numeric(self.ledt_pllOmega.text())
        self.pllPhi         = self.to_numeric(self.ledt_pllPhi.text())

        list_temp.append(['PLL Omega = ', self.pllOmega])
        list_temp.append(['PLL Phi = ', self.pllPhi])
        
        self.timeEnd        = self.to_numeric(self.ledt_time.text())

        list_temp.append(['Time = ', self.timeEnd])

        for item in list_temp:

            print(gsyIO.date_time_now() + str(item[0]) +str(item[1]))

        self.phaseAdata, self.time_samples  = self.make_data(self.phaseAMag, self.phaseAOmega, self.phaseAPhi)
        self.phaseAdata_real = self.phaseAdata.real
        self.phaseAdata_imag = self.phaseAdata.imag

        self.phaseBdata, _ = self.make_data(self.phaseBMag, self.phaseBOmega, self.phaseBPhi)
        self.phaseBdata_real = self.phaseBdata.real
        self.phaseBdata_imag = self.phaseBdata.imag

        self.phaseCdata, _ = self.make_data(self.phaseCMag, self.phaseCOmega, self.phaseCPhi)
        self.phaseCdata_real = self.phaseCdata.real
        self.phaseCdata_imag = self.phaseCdata.imag

        plt.plot(self.time_samples, self.phaseAdata, self.time_samples, self.phaseBdata, self.time_samples, self.phaseCdata)

        plt.show()

        print(self.phaseAdata.real)
        
    def to_numeric(self, str_input):

        aeval = Interpreter()

        if len(str_input) == 0:

            return 0

        else:

            temp = aeval(str_input)

            if ( isinstance(temp, Number) == True ) and ( type(temp) != bool ):

                return temp

            else:
                
                return 0

    def cal_samples(self):

        max_omega = max(abs(self.phaseAOmega), 
                        abs(self.phaseBOmega),
                        abs(self.phaseCOmega))

        max_freq = max_omega / (2 * np.pi)
        
        if self.timeEnd == 0:

            raise ValueError('Time is zero. No data.')

        elif max_freq == 0:

            samples = 1e6

            return samples

        else:

            samples = max_freq * 6

            return samples

    def make_data(self, mag, omega, phi):

        samples = self.cal_samples()

        array_time = np.linspace(0, self.timeEnd, samples)

        x = omega * array_time + phi

        return trf.to_complex(mag, x), array_time

    def save_data(self):

        header = ['time', 
                  'Phase-A Omega', 'Phase-A Phi', 'Phase-A Real', 'Phase-A Imag',
                  'Phase-B Omega', 'Phase-B Phi', 'Phase-B Real', 'Phase-B Imag',
                  'Phase-C Omega', 'Phase-C Phi', 'Phase-C Real', 'Phase-C Imag']

        phase_a_omaga   = [self.phaseAOmega] * len(self.time_samples)
        phase_a_phi     = [self.phaseAPhi] * len(self.time_samples)

        phase_b_omaga   = [self.phaseBOmega] * len(self.time_samples)
        phase_b_phi     = [self.phaseBPhi] * len(self.time_samples)

        phase_c_omaga   = [self.phaseCOmega] * len(self.time_samples)
        phase_c_phi     = [self.phaseCPhi] * len(self.time_samples)

        data_sets = [self.time_samples, 
                     phase_a_omaga, phase_a_phi, self.phaseAdata_real, self.phaseAdata_imag,
                     phase_b_omaga, phase_b_phi, self.phaseBdata_real, self.phaseBdata_imag,
                     phase_c_omaga, phase_c_phi, self.phaseCdata_real, self.phaseCdata_imag]

        gsyIO.save_csv_gui(header, data_sets)




import equations

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

