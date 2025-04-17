# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(490, 331)
        Dialog.setStyleSheet("background-color: #2e2e2e; color: #ffffff;")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 40, 431, 80))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet("background-color: #444444; color: #ffffff;")

        slider_style = """
        QSlider::groove:horizontal {
            border: 1px solid #bbb;
            background: white;
            height: 6px;
            border-radius: 3px;
        }
        QSlider::handle:horizontal {
            background: #00aced;
            border: 1px solid #5c5c5c;
            width: 12px;
            margin: -5px 0;
            border-radius: 6px;
        }
        """

        self.horizontalSlider = QtWidgets.QSlider(Dialog)
        self.horizontalSlider.setGeometry(QtCore.QRect(140, 150, 321, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setMinimum(8)
        self.horizontalSlider.setMaximum(40)
        self.horizontalSlider.setValue(22)
        self.horizontalSlider.setStyleSheet(slider_style)
        self.horizontalSlider.setObjectName("horizontalSlider")

        self.horizontalSlider_2 = QtWidgets.QSlider(Dialog)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(140, 200, 321, 22))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setMinimum(0)
        self.horizontalSlider_2.setMaximum(255)
        self.horizontalSlider_2.setValue(74)
        self.horizontalSlider_2.setStyleSheet(slider_style)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")

        self.horizontalSlider_3 = QtWidgets.QSlider(Dialog)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(140, 250, 321, 22))
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setMinimum(0)
        self.horizontalSlider_3.setMaximum(255)
        self.horizontalSlider_3.setValue(243)
        self.horizontalSlider_3.setStyleSheet(slider_style)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 150, 100, 21))
        self.label_2.setText("Font Size")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 200, 100, 21))
        self.label_3.setText("Background Color")

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 250, 100, 21))
        self.label_4.setText("Font Color")

        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 290, 431, 41))
        font.setPointSize(7)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setText("Rizki Rahman Maulana | F1D022093")
        self.label_5.setStyleSheet("color: #bbbbbb;")

        self.connectSignals()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def connectSignals(self):
        self.horizontalSlider.valueChanged.connect(self.changeFontSize)
        self.horizontalSlider_2.valueChanged.connect(self.changeBackgroundColor)
        self.horizontalSlider_3.valueChanged.connect(self.changeFontColor)

    def changeFontSize(self, value):
        font = self.label.font()
        font.setPointSize(value)
        self.label.setFont(font)

    def changeBackgroundColor(self, value):
        hex_value = "#{0:02x}{0:02x}{0:02x}".format(value)
        font_color = self.horizontalSlider_3.value()
        font_hex = "#{0:02x}{0:02x}{0:02x}".format(font_color)
        self.label.setStyleSheet(f"background-color: {hex_value}; color: {font_hex};")


    def changeFontColor(self, value):
        hex_value = "#{0:02x}{0:02x}{0:02x}".format(value)
        self.label.setStyleSheet(f"color: {hex_value}; background-color: #444444;")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Font Settings"))
        self.label.setText(_translate("Dialog", "F1D022093"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
