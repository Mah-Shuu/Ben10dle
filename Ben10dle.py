# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ben10dle.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
# https://videos.openai.com/vg-assets/assets%2Ftask_01jrmxs10vet68rf2g2dyfs8qy%2Fimg_0.webp?st=2025-04-12T16%3A40%3A46Z&se=2025-04-18T17%3A40%3A46Z&sks=b&skt=2025-04-12T16%3A40%3A46Z&ske=2025-04-18T17%3A40%3A46Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ebb0df1-a278-4e2e-9c20-f2d373479b3a&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=2h46AoAjKbkXETr0d%2Bbp9Xeztj9966lEr6V7CZS86Vc%3D&az=oaivgprodscus

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1331, 833)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1331, 811))
        self.label.setMinimumSize(QtCore.QSize(1331, 0))
        self.label.setMaximumSize(QtCore.QSize(1331, 811))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Ben10/photoshopmaster.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(590, 70, 171, 161))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Ben10/Logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(534, 250, 261, 101))
        self.label_3.setStyleSheet("QLabel{\n"
"    background-color: #D9D9D9;\n"
"    border: 6px solid #000000;\n"
"}")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(564, 276, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(724, 268, 41, 41))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Ben10/Logo.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(561, 310, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(440, 653, 451, 101))
        self.label_7.setStyleSheet("QLabel{\n"
"    background-color: #D9D9D9;\n"
"    border: 6px solid #000000;\n"
"}")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(512, 367, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    background-color: #D9D9D9;\n"
"    border: 5px solid #000000;\n"
"border-right: 0px;\n"
"}")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_omnitrix = QtWidgets.QLabel(self.centralwidget)
        self.label_omnitrix.setGeometry(QtCore.QRect(769, 352, 71, 71))
        self.label_omnitrix.setStyleSheet("QLabel:hover{\n"
"    color: red;\n"
"}")
        self.label_omnitrix.setText("")
        self.label_omnitrix.setPixmap(QtGui.QPixmap("Ben10/omnitrix.png"))
        self.label_omnitrix.setScaledContents(True)
        self.label_omnitrix.setObjectName("label_omnitrix")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(512, 367, 261, 41))
        self.label_9.setStyleSheet("")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("Ben10/edit.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(404, 770, 521, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("QLabel{\n"
"color: white;\n"
"}")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(620, 663, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(457, 680, 182, 62))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(636, 701, 41, 41))
        self.label_15.setStyleSheet("QLabel{\n"
"    background-color: #78E750;\n"
"    border: 4px solid #000000;\n"
"}78E750")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(686, 701, 41, 41))
        self.label_16.setStyleSheet("QLabel{\n"
"    background-color: #FFD633;\n"
"    border: 4px solid #000000;\n"
"}78E750")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(736, 701, 41, 41))
        self.label_17.setStyleSheet("QLabel{\n"
"    background-color: #FF2D2D;\n"
"    border: 4px solid #000000;\n"
"}78E750")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(786, 701, 41, 41))
        self.label_18.setStyleSheet("QLabel{\n"
"    background-color: #FF2D2D;\n"
"    border: 4px solid #000000;\n"
"}78E750")
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("Ben10/baixo.png"))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(836, 701, 41, 41))
        self.label_19.setStyleSheet("QLabel{\n"
"    background-color: #FF2D2D;\n"
"    border: 4px solid #000000;\n"
"}78E750")
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("Ben10/cima.png"))
        self.label_19.setScaledContents(True)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(636, 685, 40, 16))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(687, 685, 40, 16))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(736, 685, 40, 16))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(786, 685, 40, 16))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(836, 685, 40, 16))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.label_39 = QtWidgets.QLabel(self.centralwidget)
        self.label_39.setGeometry(QtCore.QRect(30, 0, 1271, 791))
        self.label_39.setText("")
        self.label_39.setPixmap(QtGui.QPixmap("Ben10/blur.png"))
        self.label_39.setScaledContents(True)
        self.label_39.setObjectName("label_39")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(420, 420, 491, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_26 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_26.setMinimumSize(QtCore.QSize(61, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_3.addWidget(self.label_26)
        self.label_25 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_25.setMinimumSize(QtCore.QSize(61, 61))
        self.label_25.setStyleSheet("QLabel{\n"
"    background-color: #D9D9D9;\n"
"    border: 4px solid #000000;\n"
"}78E750")
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.verticalLayout_3.addWidget(self.label_25)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_40 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_40.setMinimumSize(QtCore.QSize(61, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.verticalLayout_4.addWidget(self.label_40)
        self.label_41 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_41.setMinimumSize(QtCore.QSize(61, 61))
        self.label_41.setStyleSheet("QLabel{\n"
"    background-color: #D9D9D9;\n"
"    border: 4px solid #000000;\n"
"}78E750")
        self.label_41.setText("")
        self.label_41.setObjectName("label_41")
        self.verticalLayout_4.addWidget(self.label_41)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_42 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_42.setMinimumSize(QtCore.QSize(61, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.verticalLayout_5.addWidget(self.label_42)
        self.label_43 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_43.setMinimumSize(QtCore.QSize(61, 61))
        self.label_43.setStyleSheet("QLabel{\n"
"    background-color: #D9D9D9;\n"
"    border: 4px solid #000000;\n"
"}78E750")
        self.label_43.setText("")
        self.label_43.setObjectName("label_43")
        self.verticalLayout_5.addWidget(self.label_43)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_44 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_44.setMinimumSize(QtCore.QSize(61, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.verticalLayout_6.addWidget(self.label_44)
        self.label_45 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_45.setMinimumSize(QtCore.QSize(61, 61))
        self.label_45.setStyleSheet("QLabel{\n"
"    background-color: #D9D9D9;\n"
"    border: 4px solid #000000;\n"
"}78E750")
        self.label_45.setText("")
        self.label_45.setObjectName("label_45")
        self.verticalLayout_6.addWidget(self.label_45)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_50 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_50.setMinimumSize(QtCore.QSize(61, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_50.setFont(font)
        self.label_50.setAlignment(QtCore.Qt.AlignCenter)
        self.label_50.setObjectName("label_50")
        self.verticalLayout_9.addWidget(self.label_50)
        self.label_51 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_51.setMinimumSize(QtCore.QSize(61, 61))
        self.label_51.setStyleSheet("QLabel{\n"
"    background-color: #D9D9D9;\n"
"    border: 4px solid #000000;\n"
"}78E750")
        self.label_51.setText("")
        self.label_51.setObjectName("label_51")
        self.verticalLayout_9.addWidget(self.label_51)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_52 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_52.setMinimumSize(QtCore.QSize(61, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_52.setFont(font)
        self.label_52.setAlignment(QtCore.Qt.AlignCenter)
        self.label_52.setObjectName("label_52")
        self.verticalLayout_10.addWidget(self.label_52)
        self.label_53 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_53.setMinimumSize(QtCore.QSize(61, 61))
        self.label_53.setStyleSheet("QLabel{\n"
"    background-color: #D9D9D9;\n"
"    border: 4px solid #000000;\n"
"}78E750")
        self.label_53.setText("")
        self.label_53.setObjectName("label_53")
        self.verticalLayout_10.addWidget(self.label_53)
        self.horizontalLayout.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_54 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_54.setMinimumSize(QtCore.QSize(61, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_54.setFont(font)
        self.label_54.setAlignment(QtCore.Qt.AlignCenter)
        self.label_54.setWordWrap(True)
        self.label_54.setObjectName("label_54")
        self.verticalLayout_11.addWidget(self.label_54)
        self.label_55 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_55.setMinimumSize(QtCore.QSize(61, 61))
        self.label_55.setStyleSheet("QLabel{\n"
"    background-color: #D9D9D9;\n"
"    border: 4px solid #000000;\n"
"}78E750")
        self.label_55.setText("")
        self.label_55.setObjectName("label_55")
        self.verticalLayout_11.addWidget(self.label_55)
        self.horizontalLayout.addLayout(self.verticalLayout_11)
        self.pushButton_omnitrix = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_omnitrix.setGeometry(QtCore.QRect(770, 350, 71, 71))
        self.pushButton_omnitrix.setStyleSheet("QPushButton{\n"
"    border: 0;\n"
"border-radius: 35px;\n"
"}")
        self.pushButton_omnitrix.setText("")
        self.pushButton_omnitrix.setFlat(True)
        self.pushButton_omnitrix.setObjectName("pushButton_omnitrix")
        self.label.raise_()
        self.label_39.raise_()
        self.label_9.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.lineEdit.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.verticalLayoutWidget.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.horizontalLayoutWidget.raise_()
        self.label_omnitrix.raise_()
        self.pushButton_omnitrix.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1331, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Adivinhe o alien de"))
        self.label_6.setText(_translate("MainWindow", "Digite um nome para começar"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Nome do alien ..."))
        self.label_10.setText(_translate("MainWindow", "Ben 10 é uma marca registrada de Cartoon Network, Turner Broadcasting (dissolvido), WarnerMedia (mesclada com Discovery), e Warner Bros. Discovery."))
        self.label_11.setText(_translate("MainWindow", "Definições:"))
        self.label_12.setText(_translate("MainWindow", "FA = Força Alienígena"))
        self.label_13.setText(_translate("MainWindow", "SA = Supremacia Alienígena"))
        self.label_14.setText(_translate("MainWindow", "OV = Omniverse"))
        self.label_20.setText(_translate("MainWindow", "Correto"))
        self.label_21.setText(_translate("MainWindow", "Parcial"))
        self.label_22.setText(_translate("MainWindow", "Errado"))
        self.label_23.setText(_translate("MainWindow", "Menor"))
        self.label_24.setText(_translate("MainWindow", "Maior"))
        self.label_26.setText(_translate("MainWindow", "Alien"))
        self.label_40.setText(_translate("MainWindow", "Gênero"))
        self.label_42.setText(_translate("MainWindow", "Poder"))
        self.label_44.setText(_translate("MainWindow", "Cores"))
        self.label_50.setText(_translate("MainWindow", "Altura"))
        self.label_52.setText(_translate("MainWindow", "Origem"))
        self.label_54.setText(_translate("MainWindow", "Primeira Aparição"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
