# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 411)
        self.saveBtn = QtWidgets.QPushButton(Form)
        self.saveBtn.setGeometry(QtCore.QRect(160, 340, 93, 28))
        self.saveBtn.setObjectName("saveBtn")
        self.cancelBtn = QtWidgets.QPushButton(Form)
        self.cancelBtn.setGeometry(QtCore.QRect(260, 340, 93, 28))
        self.cancelBtn.setObjectName("cancelBtn")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 10, 321, 311))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.widget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.inputName = QtWidgets.QLineEdit(self.splitter)
        self.inputName.setMaximumSize(QtCore.QSize(16777215, 24))
        self.inputName.setObjectName("inputName")
        self.verticalLayout.addWidget(self.splitter)
        self.splitter_3 = QtWidgets.QSplitter(self.widget)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_3 = QtWidgets.QLabel(self.splitter_3)
        self.label_3.setObjectName("label_3")
        self.inputPosition = QtWidgets.QLineEdit(self.splitter_3)
        self.inputPosition.setMaximumSize(QtCore.QSize(16777215, 24))
        self.inputPosition.setObjectName("inputPosition")
        self.verticalLayout.addWidget(self.splitter_3)
        self.splitter_6 = QtWidgets.QSplitter(self.widget)
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName("splitter_6")
        self.label_6 = QtWidgets.QLabel(self.splitter_6)
        self.label_6.setObjectName("label_6")
        self.dateOfHiring = QtWidgets.QDateEdit(self.splitter_6)
        self.dateOfHiring.setMaximumSize(QtCore.QSize(16777215, 24))
        self.dateOfHiring.setObjectName("dateOfHiring")
        self.verticalLayout.addWidget(self.splitter_6)
        self.splitter_4 = QtWidgets.QSplitter(self.widget)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.label_4 = QtWidgets.QLabel(self.splitter_4)
        self.label_4.setObjectName("label_4")
        self.dateOfBirth = QtWidgets.QDateEdit(self.splitter_4)
        self.dateOfBirth.setMaximumSize(QtCore.QSize(16777215, 24))
        self.dateOfBirth.setObjectName("dateOfBirth")
        self.verticalLayout.addWidget(self.splitter_4)
        self.splitter_2 = QtWidgets.QSplitter(self.widget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        self.label_2.setObjectName("label_2")
        self.comboBoxSex = QtWidgets.QComboBox(self.splitter_2)
        self.comboBoxSex.setMaximumSize(QtCore.QSize(16777215, 24))
        self.comboBoxSex.setObjectName("comboBoxSex")
        self.verticalLayout.addWidget(self.splitter_2)
        self.splitter_5 = QtWidgets.QSplitter(self.widget)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.label_5 = QtWidgets.QLabel(self.splitter_5)
        self.label_5.setObjectName("label_5")
        self.comboBoxDepartment = QtWidgets.QComboBox(self.splitter_5)
        self.comboBoxDepartment.setMaximumSize(QtCore.QSize(16777215, 24))
        self.comboBoxDepartment.setObjectName("comboBoxDepartment")
        self.verticalLayout.addWidget(self.splitter_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Dialog"))
        self.saveBtn.setText(_translate("Form", "??????????????????"))
        self.cancelBtn.setText(_translate("Form", "????????????"))
        self.label.setText(_translate("Form", "?????? ????????????????????:"))
        self.label_3.setText(_translate("Form", "??????????????????"))
        self.label_6.setText(_translate("Form", "???????? ??????????????????????????????"))
        self.label_4.setText(_translate("Form", "???????? ????????????????"))
        self.label_2.setText(_translate("Form", "??????"))
        self.label_5.setText(_translate("Form", "??????????"))
