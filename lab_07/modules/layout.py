# Form implementation generated from reading ui file 'design/lab_07.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1389, 771)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1381, 761))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.main_tab = QtWidgets.QWidget()
        self.main_tab.setObjectName("main_tab")
        self.mainFrame = QtWidgets.QFrame(self.main_tab)
        self.mainFrame.setGeometry(QtCore.QRect(0, 0, 1011, 741))
        self.mainFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.graphicsView = GraphicsView(self.mainFrame)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1011, 731))
        self.graphicsView.setObjectName("graphicsView")
        self.frame_5 = QtWidgets.QFrame(self.main_tab)
        self.frame_5.setGeometry(QtCore.QRect(1150, 660, 221, 61))
        self.frame_5.setAutoFillBackground(True)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.exitButton = QtWidgets.QPushButton(self.frame_5)
        self.exitButton.setGeometry(QtCore.QRect(130, 10, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.exitButton.setFont(font)
        self.exitButton.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.exitButton.setObjectName("exitButton")
        self.resetButton = QtWidgets.QPushButton(self.frame_5)
        self.resetButton.setGeometry(QtCore.QRect(10, 10, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.resetButton.setFont(font)
        self.resetButton.setObjectName("resetButton")
        self.frame_9 = QtWidgets.QFrame(self.main_tab)
        self.frame_9.setGeometry(QtCore.QRect(1020, 290, 351, 211))
        self.frame_9.setAutoFillBackground(True)
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setLineWidth(5)
        self.frame_9.setObjectName("frame_9")
        self.label_23 = QtWidgets.QLabel(self.frame_9)
        self.label_23.setGeometry(QtCore.QRect(0, 0, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_23.setWordWrap(True)
        self.label_23.setObjectName("label_23")
        self.lineColorButton = QtWidgets.QPushButton(self.frame_9)
        self.lineColorButton.setGeometry(QtCore.QRect(260, 50, 80, 31))
        self.lineColorButton.setObjectName("lineColorButton")
        self.lineColorLabel = QtWidgets.QLabel(self.frame_9)
        self.lineColorLabel.setGeometry(QtCore.QRect(40, 50, 201, 31))
        self.lineColorLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineColorLabel.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.lineColorLabel.setText("")
        self.lineColorLabel.setObjectName("lineColorLabel")
        self.cutterColorLabel = QtWidgets.QLabel(self.frame_9)
        self.cutterColorLabel.setGeometry(QtCore.QRect(40, 110, 201, 31))
        self.cutterColorLabel.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.cutterColorLabel.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.cutterColorLabel.setText("")
        self.cutterColorLabel.setObjectName("cutterColorLabel")
        self.cutterColorButton = QtWidgets.QPushButton(self.frame_9)
        self.cutterColorButton.setGeometry(QtCore.QRect(260, 110, 80, 31))
        self.cutterColorButton.setObjectName("cutterColorButton")
        self.label_24 = QtWidgets.QLabel(self.frame_9)
        self.label_24.setGeometry(QtCore.QRect(0, 20, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_24.setWordWrap(True)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame_9)
        self.label_25.setGeometry(QtCore.QRect(0, 80, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_25.setWordWrap(True)
        self.label_25.setObjectName("label_25")
        self.resultColorButton = QtWidgets.QPushButton(self.frame_9)
        self.resultColorButton.setGeometry(QtCore.QRect(260, 170, 80, 31))
        self.resultColorButton.setObjectName("resultColorButton")
        self.resultColorLabel = QtWidgets.QLabel(self.frame_9)
        self.resultColorLabel.setGeometry(QtCore.QRect(40, 170, 201, 31))
        self.resultColorLabel.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.resultColorLabel.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.resultColorLabel.setText("")
        self.resultColorLabel.setObjectName("resultColorLabel")
        self.label_27 = QtWidgets.QLabel(self.frame_9)
        self.label_27.setGeometry(QtCore.QRect(0, 140, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_27.setFont(font)
        self.label_27.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_27.setWordWrap(True)
        self.label_27.setObjectName("label_27")
        self.lineFrame = QtWidgets.QFrame(self.main_tab)
        self.lineFrame.setGeometry(QtCore.QRect(1020, 140, 351, 141))
        self.lineFrame.setAutoFillBackground(True)
        self.lineFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.lineFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.lineFrame.setLineWidth(5)
        self.lineFrame.setObjectName("lineFrame")
        self.lineXAForm = QtWidgets.QLineEdit(self.lineFrame)
        self.lineXAForm.setGeometry(QtCore.QRect(60, 30, 111, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineXAForm.setFont(font)
        self.lineXAForm.setObjectName("lineXAForm")
        self.label_15 = QtWidgets.QLabel(self.lineFrame)
        self.label_15.setGeometry(QtCore.QRect(10, 30, 41, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_15.setFont(font)
        self.label_15.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_15.setScaledContents(False)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.lineFrame)
        self.label_16.setGeometry(QtCore.QRect(0, 0, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.lineFrame)
        self.label_17.setGeometry(QtCore.QRect(180, 30, 41, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_17.setFont(font)
        self.label_17.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_17.setScaledContents(False)
        self.label_17.setObjectName("label_17")
        self.lineYAForm = QtWidgets.QLineEdit(self.lineFrame)
        self.lineYAForm.setGeometry(QtCore.QRect(220, 30, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineYAForm.setFont(font)
        self.lineYAForm.setObjectName("lineYAForm")
        self.addLineButton = QtWidgets.QPushButton(self.lineFrame)
        self.addLineButton.setGeometry(QtCore.QRect(10, 100, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.addLineButton.setFont(font)
        self.addLineButton.setStyleSheet("")
        self.addLineButton.setObjectName("addLineButton")
        self.lineXBForm = QtWidgets.QLineEdit(self.lineFrame)
        self.lineXBForm.setGeometry(QtCore.QRect(60, 60, 111, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineXBForm.setFont(font)
        self.lineXBForm.setObjectName("lineXBForm")
        self.label_26 = QtWidgets.QLabel(self.lineFrame)
        self.label_26.setGeometry(QtCore.QRect(10, 60, 41, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_26.setFont(font)
        self.label_26.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_26.setScaledContents(False)
        self.label_26.setObjectName("label_26")
        self.label_28 = QtWidgets.QLabel(self.lineFrame)
        self.label_28.setGeometry(QtCore.QRect(180, 60, 41, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        self.label_28.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_28.setFont(font)
        self.label_28.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_28.setScaledContents(False)
        self.label_28.setObjectName("label_28")
        self.lineYBForm = QtWidgets.QLineEdit(self.lineFrame)
        self.lineYBForm.setGeometry(QtCore.QRect(220, 60, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineYBForm.setFont(font)
        self.lineYBForm.setObjectName("lineYBForm")
        self.cutterFrame = QtWidgets.QFrame(self.main_tab)
        self.cutterFrame.setGeometry(QtCore.QRect(1020, 0, 351, 131))
        self.cutterFrame.setAutoFillBackground(True)
        self.cutterFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.cutterFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.cutterFrame.setLineWidth(5)
        self.cutterFrame.setObjectName("cutterFrame")
        self.addCutterButton = QtWidgets.QPushButton(self.cutterFrame)
        self.addCutterButton.setGeometry(QtCore.QRect(10, 90, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.addCutterButton.setFont(font)
        self.addCutterButton.setStyleSheet("")
        self.addCutterButton.setObjectName("addCutterButton")
        self.cutterXAForm = QtWidgets.QLineEdit(self.cutterFrame)
        self.cutterXAForm.setGeometry(QtCore.QRect(50, 30, 111, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cutterXAForm.setFont(font)
        self.cutterXAForm.setObjectName("cutterXAForm")
        self.label_18 = QtWidgets.QLabel(self.cutterFrame)
        self.label_18.setGeometry(QtCore.QRect(180, 30, 41, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_18.setFont(font)
        self.label_18.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_18.setScaledContents(False)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.cutterFrame)
        self.label_19.setGeometry(QtCore.QRect(10, 30, 41, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_19.setFont(font)
        self.label_19.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_19.setScaledContents(False)
        self.label_19.setObjectName("label_19")
        self.cutterYAForm = QtWidgets.QLineEdit(self.cutterFrame)
        self.cutterYAForm.setGeometry(QtCore.QRect(220, 30, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cutterYAForm.setFont(font)
        self.cutterYAForm.setObjectName("cutterYAForm")
        self.label_20 = QtWidgets.QLabel(self.cutterFrame)
        self.label_20.setGeometry(QtCore.QRect(0, 0, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_20.setWordWrap(True)
        self.label_20.setObjectName("label_20")
        self.cutterYBForm = QtWidgets.QLineEdit(self.cutterFrame)
        self.cutterYBForm.setGeometry(QtCore.QRect(220, 60, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cutterYBForm.setFont(font)
        self.cutterYBForm.setObjectName("cutterYBForm")
        self.cutterXBForm = QtWidgets.QLineEdit(self.cutterFrame)
        self.cutterXBForm.setGeometry(QtCore.QRect(50, 60, 111, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cutterXBForm.setFont(font)
        self.cutterXBForm.setObjectName("cutterXBForm")
        self.label_21 = QtWidgets.QLabel(self.cutterFrame)
        self.label_21.setGeometry(QtCore.QRect(10, 60, 41, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_21.setFont(font)
        self.label_21.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_21.setScaledContents(False)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.cutterFrame)
        self.label_22.setGeometry(QtCore.QRect(180, 60, 41, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_22.setFont(font)
        self.label_22.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_22.setScaledContents(False)
        self.label_22.setObjectName("label_22")
        self.loggerFrame = QtWidgets.QFrame(self.main_tab)
        self.loggerFrame.setGeometry(QtCore.QRect(1020, 590, 351, 61))
        self.loggerFrame.setAutoFillBackground(True)
        self.loggerFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.loggerFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.loggerFrame.setObjectName("loggerFrame")
        self.loggerLabel = QtWidgets.QLabel(self.loggerFrame)
        self.loggerLabel.setGeometry(QtCore.QRect(10, 0, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loggerLabel.setFont(font)
        self.loggerLabel.setWordWrap(True)
        self.loggerLabel.setObjectName("loggerLabel")
        self.frame_7 = QtWidgets.QFrame(self.main_tab)
        self.frame_7.setGeometry(QtCore.QRect(1020, 510, 351, 61))
        self.frame_7.setAutoFillBackground(True)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.cutButton = QtWidgets.QPushButton(self.frame_7)
        self.cutButton.setGeometry(QtCore.QRect(10, 10, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cutButton.setFont(font)
        self.cutButton.setObjectName("cutButton")
        self.tabWidget.addTab(self.main_tab, "")
        self.actionabc = QtGui.QAction(Dialog)
        self.actionabc.setObjectName("actionabc")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineXAForm, self.lineYAForm)
        Dialog.setTabOrder(self.lineYAForm, self.addLineButton)
        Dialog.setTabOrder(self.addLineButton, self.resetButton)
        Dialog.setTabOrder(self.resetButton, self.exitButton)
        Dialog.setTabOrder(self.exitButton, self.graphicsView)
        Dialog.setTabOrder(self.graphicsView, self.tabWidget)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.exitButton.setText(_translate("Dialog", "Выход"))
        self.resetButton.setText(_translate("Dialog", "Сброс"))
        self.label_23.setText(_translate("Dialog", "Цвет"))
        self.lineColorButton.setText(_translate("Dialog", "Выбрать"))
        self.cutterColorButton.setText(_translate("Dialog", "Выбрать"))
        self.label_24.setText(_translate("Dialog", "Цвет Отрезков"))
        self.label_25.setText(_translate("Dialog", "Цвет Отсекателя"))
        self.resultColorButton.setText(_translate("Dialog", "Выбрать"))
        self.label_27.setText(_translate("Dialog", "Цвет Результата"))
        self.lineXAForm.setText(_translate("Dialog", "300"))
        self.label_15.setText(_translate("Dialog", "X1 ="))
        self.label_16.setText(_translate("Dialog", "Добавить отрезок"))
        self.label_17.setText(_translate("Dialog", "Y1 ="))
        self.lineYAForm.setText(_translate("Dialog", "400"))
        self.addLineButton.setText(_translate("Dialog", "Добавить"))
        self.lineXBForm.setText(_translate("Dialog", "500"))
        self.label_26.setText(_translate("Dialog", "X2 ="))
        self.label_28.setText(_translate("Dialog", "Y2 ="))
        self.lineYBForm.setText(_translate("Dialog", "600"))
        self.addCutterButton.setText(_translate("Dialog", "Добавить"))
        self.cutterXAForm.setText(_translate("Dialog", "300"))
        self.label_18.setText(_translate("Dialog", "Y1 ="))
        self.label_19.setText(_translate("Dialog", "X1 ="))
        self.cutterYAForm.setText(_translate("Dialog", "400"))
        self.label_20.setText(_translate("Dialog", "Добавить Отсекатель"))
        self.cutterYBForm.setText(_translate("Dialog", "600"))
        self.cutterXBForm.setText(_translate("Dialog", "500"))
        self.label_21.setText(_translate("Dialog", "X2 ="))
        self.label_22.setText(_translate("Dialog", "Y2 ="))
        self.loggerLabel.setText(_translate("Dialog", "App started..."))
        self.cutButton.setText(_translate("Dialog", "Выполнить отсечение"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main_tab), _translate("Dialog", "Main Tab"))
        self.actionabc.setText(_translate("Dialog", "abc"))
from .graphicsView import GraphicsView