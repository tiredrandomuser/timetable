# -*- coding: utf-8 -*-
#
# Form implementation generated from reading ui file 'trialwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import ui_stylesheet

class Ui_trialwindow(object):
    def setupUi(self, trialwindow):
        trialwindow.setObjectName("trialwindow")
        trialwindow.resize(920, 500)
        trialwindow.setStyleSheet(ui_stylesheet.css)
        self.labelTitle = QtWidgets.QLabel(trialwindow)
        self.labelTitle.setGeometry(QtCore.QRect(390, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(14)
        self.labelTitle.setFont(font)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.label = QtWidgets.QLabel(trialwindow)
        self.label.setGeometry(QtCore.QRect(20, 90, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.inputType_combobox = QtWidgets.QComboBox(trialwindow)
        self.inputType_combobox.setGeometry(QtCore.QRect(100, 90, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        self.inputType_combobox.setFont(font)
        self.inputType_combobox.setObjectName("inputType_combobox")
        self.input_list = QtWidgets.QListWidget(trialwindow)
        self.input_list.setGeometry(QtCore.QRect(520, 50, 391, 371))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        self.input_list.setFont(font)
        self.input_list.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.input_list.setAlternatingRowColors(False)
        self.input_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.input_list.setMovement(QtWidgets.QListView.Static)
        self.input_list.setResizeMode(QtWidgets.QListView.Adjust)
        self.input_list.setObjectName("input_list")
        self.semester_label = QtWidgets.QLabel(trialwindow)
        self.semester_label.setGeometry(QtCore.QRect(20, 190, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(9)
        self.semester_label.setFont(font)
        self.semester_label.setObjectName("semester_label")
        self.semester_combobox = QtWidgets.QComboBox(trialwindow)
        self.semester_combobox.setGeometry(QtCore.QRect(100, 190, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        self.semester_combobox.setFont(font)
        self.semester_combobox.setObjectName("semester_combobox")
        self.line = QtWidgets.QFrame(trialwindow)
        self.line.setGeometry(QtCore.QRect(10, 150, 491, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.noofsections_label = QtWidgets.QLabel(trialwindow)
        self.noofsections_label.setGeometry(QtCore.QRect(270, 190, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(9)
        self.noofsections_label.setFont(font)
        self.noofsections_label.setObjectName("noofsections_label")
        self.sections_spinbox = QtWidgets.QSpinBox(trialwindow)
        self.sections_spinbox.setGeometry(QtCore.QRect(400, 190, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sections_spinbox.setFont(font)
        self.sections_spinbox.setObjectName("sections_spinbox")
        self.line_2 = QtWidgets.QFrame(trialwindow)
        self.line_2.setGeometry(QtCore.QRect(10, 240, 491, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_4 = QtWidgets.QLabel(trialwindow)
        self.label_4.setGeometry(QtCore.QRect(120, 290, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.input_textbox = QtWidgets.QLineEdit(trialwindow)
        self.input_textbox.setGeometry(QtCore.QRect(110, 320, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(9)
        self.input_textbox.setFont(font)
        self.input_textbox.setObjectName("input_textbox")
        self.addBtn = QtWidgets.QPushButton(trialwindow)
        self.addBtn.setGeometry(QtCore.QRect(20, 440, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(11)
        self.addBtn.setFont(font)
        self.addBtn.setObjectName("addBtn")
        self.removeBtn = QtWidgets.QPushButton(trialwindow)
        self.removeBtn.setGeometry(QtCore.QRect(180, 440, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(11)
        self.removeBtn.setFont(font)
        self.removeBtn.setObjectName("removeBtn")
        self.nextBtn = QtWidgets.QPushButton(trialwindow)
        self.nextBtn.setGeometry(QtCore.QRect(770, 440, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(11)
        self.nextBtn.setFont(font)
        self.nextBtn.setObjectName("nextBtn")
        self.title_combobox = QtWidgets.QComboBox(trialwindow)
        self.title_combobox.setGeometry(QtCore.QRect(20, 320, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.title_combobox.setFont(font)
        self.title_combobox.setObjectName("title_combobox")
        self.subject_short_input = QtWidgets.QLineEdit(trialwindow)
        self.subject_short_input.setGeometry(QtCore.QRect(390, 320, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.subject_short_input.setFont(font)
        self.subject_short_input.setObjectName("subject_short_input")
        self.label_2 = QtWidgets.QLabel(trialwindow)
        self.label_2.setGeometry(QtCore.QRect(390, 290, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(trialwindow)
        QtCore.QMetaObject.connectSlotsByName(trialwindow)

    def retranslateUi(self, trialwindow):
        _translate = QtCore.QCoreApplication.translate
        trialwindow.setWindowTitle(_translate("trialwindow", "TrialWindow"))
        self.labelTitle.setText(_translate("trialwindow", "List Entry"))
        self.label.setText(_translate("trialwindow", "Input Type :"))
        self.input_list.setSortingEnabled(True)
        self.semester_label.setText(_translate("trialwindow", "Semester :"))
        self.noofsections_label.setText(_translate("trialwindow", "Number of Sections :"))
        self.label_4.setText(_translate("trialwindow", "Name :"))
        self.addBtn.setText(_translate("trialwindow", "Add"))
        self.removeBtn.setText(_translate("trialwindow", "Remove"))
        self.nextBtn.setText(_translate("trialwindow", "Next >"))
        self.label_2.setText(_translate("trialwindow", "Subject short form:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    trialwindow = QtWidgets.QWidget()
    ui = Ui_trialwindow()
    ui.setupUi(trialwindow)
    trialwindow.show()
    sys.exit(app.exec_())

