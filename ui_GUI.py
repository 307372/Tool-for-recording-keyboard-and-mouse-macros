# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUIdacMXt.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(792, 584)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.tabs = QTabWidget(self.centralwidget)
        self.tabs.setObjectName(u"tabs")
        self.tabs.setGeometry(QRect(10, 0, 781, 561))
        self.tabs.setFocusPolicy(Qt.ClickFocus)
        self.macroTab = QWidget()
        self.macroTab.setObjectName(u"macroTab")
        self.macroDelete = QPushButton(self.macroTab)
        self.macroDelete.setObjectName(u"macroDelete")
        self.macroDelete.setGeometry(QRect(690, 500, 75, 23))
        self.macroEdit = QPushButton(self.macroTab)
        self.macroEdit.setObjectName(u"macroEdit")
        self.macroEdit.setGeometry(QRect(20, 500, 91, 23))
        self.macroNew = QPushButton(self.macroTab)
        self.macroNew.setObjectName(u"macroNew")
        self.macroNew.setGeometry(QRect(130, 500, 97, 23))
        self.macroTreeView = QTreeView(self.macroTab)
        self.macroTreeView.setObjectName(u"macroTreeView")
        self.macroTreeView.setGeometry(QRect(10, 10, 751, 481))
        self.macroTestButton = QPushButton(self.macroTab)
        self.macroTestButton.setObjectName(u"macroTestButton")
        self.macroTestButton.setGeometry(QRect(260, 500, 75, 23))
        self.macroWhatIsThisButton = QPushButton(self.macroTab)
        self.macroWhatIsThisButton.setObjectName(u"macroWhatIsThisButton")
        self.macroWhatIsThisButton.setGeometry(QRect(360, 500, 75, 23))
        self.tabs.addTab(self.macroTab, "")
        self.creatorTab = QWidget()
        self.creatorTab.setObjectName(u"creatorTab")
        self.creatorEditorGroup = QGroupBox(self.creatorTab)
        self.creatorEditorGroup.setObjectName(u"creatorEditorGroup")
        self.creatorEditorGroup.setGeometry(QRect(10, 10, 761, 521))
        self.creatorEditorDeleteFromMacro = QPushButton(self.creatorEditorGroup)
        self.creatorEditorDeleteFromMacro.setObjectName(u"creatorEditorDeleteFromMacro")
        self.creatorEditorDeleteFromMacro.setGeometry(QRect(130, 480, 101, 23))
        self.creatorEditorActions = QTreeWidget(self.creatorEditorGroup)
        __qtreewidgetitem = QTreeWidgetItem(self.creatorEditorActions)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem1 = QTreeWidgetItem(self.creatorEditorActions)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2 = QTreeWidgetItem(self.creatorEditorActions)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(self.creatorEditorActions)
        QTreeWidgetItem(self.creatorEditorActions)
        self.creatorEditorActions.setObjectName(u"creatorEditorActions")
        self.creatorEditorActions.setGeometry(QRect(20, 30, 211, 411))
        self.creatorEditorActions.setFrameShadow(QFrame.Sunken)
        self.creatorEditorActions.setAlternatingRowColors(True)
        self.creatorEditorAddToMacro = QPushButton(self.creatorEditorGroup)
        self.creatorEditorAddToMacro.setObjectName(u"creatorEditorAddToMacro")
        self.creatorEditorAddToMacro.setGeometry(QRect(130, 450, 101, 23))
        self.creatorEditorMoveUp = QPushButton(self.creatorEditorGroup)
        self.creatorEditorMoveUp.setObjectName(u"creatorEditorMoveUp")
        self.creatorEditorMoveUp.setGeometry(QRect(270, 450, 75, 23))
        self.creatorEditorMoveDown = QPushButton(self.creatorEditorGroup)
        self.creatorEditorMoveDown.setObjectName(u"creatorEditorMoveDown")
        self.creatorEditorMoveDown.setGeometry(QRect(270, 480, 75, 23))
        self.creatorEditorSave = QPushButton(self.creatorEditorGroup)
        self.creatorEditorSave.setObjectName(u"creatorEditorSave")
        self.creatorEditorSave.setGeometry(QRect(440, 480, 101, 23))
        self.creatorEditorName = QLineEdit(self.creatorEditorGroup)
        self.creatorEditorName.setObjectName(u"creatorEditorName")
        self.creatorEditorName.setGeometry(QRect(440, 450, 301, 20))
        self.label_9 = QLabel(self.creatorEditorGroup)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(360, 450, 71, 20))
        self.testSaveButton = QPushButton(self.creatorEditorGroup)
        self.testSaveButton.setObjectName(u"testSaveButton")
        self.testSaveButton.setGeometry(QRect(210, 260, 75, 23))
        self.creatorEditorClear = QPushButton(self.creatorEditorGroup)
        self.creatorEditorClear.setObjectName(u"creatorEditorClear")
        self.creatorEditorClear.setGeometry(QRect(640, 480, 101, 23))
        self.creatorEditorDeleteFromActions = QPushButton(self.creatorEditorGroup)
        self.creatorEditorDeleteFromActions.setObjectName(u"creatorEditorDeleteFromActions")
        self.creatorEditorDeleteFromActions.setGeometry(QRect(20, 480, 103, 23))
        self.creatorEditorNewRecording = QPushButton(self.creatorEditorGroup)
        self.creatorEditorNewRecording.setObjectName(u"creatorEditorNewRecording")
        self.creatorEditorNewRecording.setGeometry(QRect(20, 450, 101, 23))
        self.label_8 = QLabel(self.creatorEditorGroup)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(270, 10, 152, 13))
        self.creatorEditorEdit = QPushButton(self.creatorEditorGroup)
        self.creatorEditorEdit.setObjectName(u"creatorEditorEdit")
        self.creatorEditorEdit.setGeometry(QRect(350, 480, 81, 23))
        self.testLoadButton = QPushButton(self.creatorEditorGroup)
        self.testLoadButton.setObjectName(u"testLoadButton")
        self.testLoadButton.setGeometry(QRect(210, 300, 75, 23))
        self.testButton = QPushButton(self.creatorEditorGroup)
        self.testButton.setObjectName(u"testButton")
        self.testButton.setGeometry(QRect(210, 340, 75, 23))
        self.creatorEditorTreeView = QTreeView(self.creatorEditorGroup)
        self.creatorEditorTreeView.setObjectName(u"creatorEditorTreeView")
        self.creatorEditorTreeView.setGeometry(QRect(270, 30, 471, 411))
        self.creatorEditorTreeView.setAlternatingRowColors(True)
        self.creatorEditorTreeView.setTextElideMode(Qt.ElideMiddle)
        self.creatorEditorTreeView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.creatorEditorTreeView.setWordWrap(True)
        self.creatorEditorTreeView.header().setDefaultSectionSize(200)
        self.testButton_2 = QPushButton(self.creatorEditorGroup)
        self.testButton_2.setObjectName(u"testButton_2")
        self.testButton_2.setGeometry(QRect(210, 370, 75, 23))
        self.WhatIsThisButton = QPushButton(self.creatorEditorGroup)
        self.WhatIsThisButton.setObjectName(u"WhatIsThisButton")
        self.WhatIsThisButton.setGeometry(QRect(210, 400, 75, 23))
        self.previewButton = QPushButton(self.creatorEditorGroup)
        self.previewButton.setObjectName(u"previewButton")
        self.previewButton.setGeometry(QRect(550, 480, 75, 23))
        self.testButton_3 = QPushButton(self.creatorEditorGroup)
        self.testButton_3.setObjectName(u"testButton_3")
        self.testButton_3.setGeometry(QRect(210, 430, 75, 23))
        self.label_10 = QLabel(self.creatorEditorGroup)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(200, 240, 90, 13))
        self.creatorEditorDeleteFromMacro.raise_()
        self.creatorEditorActions.raise_()
        self.creatorEditorAddToMacro.raise_()
        self.creatorEditorMoveUp.raise_()
        self.creatorEditorMoveDown.raise_()
        self.creatorEditorSave.raise_()
        self.creatorEditorName.raise_()
        self.label_9.raise_()
        self.creatorEditorClear.raise_()
        self.creatorEditorDeleteFromActions.raise_()
        self.creatorEditorNewRecording.raise_()
        self.label_8.raise_()
        self.creatorEditorEdit.raise_()
        self.creatorEditorTreeView.raise_()
        self.testSaveButton.raise_()
        self.testLoadButton.raise_()
        self.testButton.raise_()
        self.testButton_2.raise_()
        self.WhatIsThisButton.raise_()
        self.previewButton.raise_()
        self.testButton_3.raise_()
        self.label_10.raise_()
        self.tabs.addTab(self.creatorTab, "")
        self.autoclickerTab = QWidget()
        self.autoclickerTab.setObjectName(u"autoclickerTab")
        self.AC_Time = QGroupBox(self.autoclickerTab)
        self.AC_Time.setObjectName(u"AC_Time")
        self.AC_Time.setGeometry(QRect(20, 20, 321, 80))
        self.AC_Hours = QSpinBox(self.AC_Time)
        self.AC_Hours.setObjectName(u"AC_Hours")
        self.AC_Hours.setGeometry(QRect(20, 30, 42, 22))
        self.AC_Hours.setMaximum(999)
        self.AC_Minutes = QSpinBox(self.AC_Time)
        self.AC_Minutes.setObjectName(u"AC_Minutes")
        self.AC_Minutes.setGeometry(QRect(100, 30, 42, 22))
        self.AC_Minutes.setMaximum(999)
        self.AC_Seconds = QSpinBox(self.AC_Time)
        self.AC_Seconds.setObjectName(u"AC_Seconds")
        self.AC_Seconds.setGeometry(QRect(180, 30, 42, 22))
        self.AC_Seconds.setMaximum(999)
        self.AC_Miliseconds = QSpinBox(self.AC_Time)
        self.AC_Miliseconds.setObjectName(u"AC_Miliseconds")
        self.AC_Miliseconds.setGeometry(QRect(260, 30, 42, 22))
        self.AC_Miliseconds.setMinimum(1)
        self.AC_Miliseconds.setMaximum(999)
        self.AC_Miliseconds.setValue(100)
        self.label = QLabel(self.AC_Time)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 50, 54, 20))
        self.label_2 = QLabel(self.AC_Time)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 53, 41, 20))
        self.label_3 = QLabel(self.AC_Time)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 51, 41, 20))
        self.label_4 = QLabel(self.AC_Time)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 53, 38, 20))
        self.AC_Start = QPushButton(self.autoclickerTab)
        self.AC_Start.setObjectName(u"AC_Start")
        self.AC_Start.setGeometry(QRect(30, 270, 131, 23))
        self.AC_Stop = QPushButton(self.autoclickerTab)
        self.AC_Stop.setObjectName(u"AC_Stop")
        self.AC_Stop.setGeometry(QRect(194, 270, 141, 23))
        self.AC_ClickHowManyTimesGroup = QGroupBox(self.autoclickerTab)
        self.AC_ClickHowManyTimesGroup.setObjectName(u"AC_ClickHowManyTimesGroup")
        self.AC_ClickHowManyTimesGroup.setGeometry(QRect(180, 110, 161, 151))
        self.AC_ClickNTimes = QRadioButton(self.AC_ClickHowManyTimesGroup)
        self.AC_ClickNTimes.setObjectName(u"AC_ClickNTimes")
        self.AC_ClickNTimes.setGeometry(QRect(10, 60, 47, 21))
        self.AC_ClickNTimesN = QSpinBox(self.AC_ClickHowManyTimesGroup)
        self.AC_ClickNTimesN.setObjectName(u"AC_ClickNTimesN")
        self.AC_ClickNTimesN.setGeometry(QRect(60, 60, 61, 22))
        self.AC_ClickNTimesN.setMinimum(1)
        self.AC_ClickNTimesN.setMaximum(9999999)
        self.AC_ClickNTimesN.setValue(1)
        self.label_7 = QLabel(self.AC_ClickHowManyTimesGroup)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(130, 60, 21, 21))
        self.AC_ClickUntilStopped = QRadioButton(self.AC_ClickHowManyTimesGroup)
        self.AC_ClickUntilStopped.setObjectName(u"AC_ClickUntilStopped")
        self.AC_ClickUntilStopped.setGeometry(QRect(10, 90, 123, 17))
        self.AC_ClickUntilStopped.setChecked(True)
        self.groupBox = QGroupBox(self.autoclickerTab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 110, 151, 151))
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 30, 113, 13))
        self.AC_WhichButton = QComboBox(self.groupBox)
        self.AC_WhichButton.addItem("")
        self.AC_WhichButton.addItem("")
        self.AC_WhichButton.addItem("")
        self.AC_WhichButton.setObjectName(u"AC_WhichButton")
        self.AC_WhichButton.setGeometry(QRect(20, 50, 71, 22))
        self.AC_Hotkey = QKeySequenceEdit(self.groupBox)
        self.AC_Hotkey.setObjectName(u"AC_Hotkey")
        self.AC_Hotkey.setGeometry(QRect(20, 110, 113, 20))
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 90, 81, 16))
        self.tabs.addTab(self.autoclickerTab, "")
        self.settingsTab = QWidget()
        self.settingsTab.setObjectName(u"settingsTab")
        self.settingsAutosave = QCheckBox(self.settingsTab)
        self.settingsAutosave.setObjectName(u"settingsAutosave")
        self.settingsAutosave.setGeometry(QRect(10, 30, 157, 17))
        self.settingsAutosave.setChecked(True)
        self.settingsDefault = QPushButton(self.settingsTab)
        self.settingsDefault.setObjectName(u"settingsDefault")
        self.settingsDefault.setGeometry(QRect(10, 480, 171, 41))
        self.forceSave = QPushButton(self.settingsTab)
        self.forceSave.setObjectName(u"forceSave")
        self.forceSave.setGeometry(QRect(10, 440, 81, 23))
        self.forceLoad = QPushButton(self.settingsTab)
        self.forceLoad.setObjectName(u"forceLoad")
        self.forceLoad.setGeometry(QRect(100, 440, 81, 23))
        self.tabs.addTab(self.settingsTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 792, 21))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.creatorEditorActions.itemDoubleClicked.connect(self.creatorEditorAddToMacro.click)
        self.creatorEditorTreeView.clicked.connect(self.creatorEditorEdit.click)

        self.tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Rzeczy w miejscach 0.5", None))
        self.macroDelete.setText(QCoreApplication.translate("MainWindow", u"Usu\u0144", None))
        self.macroEdit.setText(QCoreApplication.translate("MainWindow", u"Edytuj", None))
        self.macroNew.setText(QCoreApplication.translate("MainWindow", u"Dodaj nowe makro", None))
        self.macroTestButton.setText(QCoreApplication.translate("MainWindow", u"testImport", None))
        self.macroWhatIsThisButton.setText(QCoreApplication.translate("MainWindow", u"Inspect", None))
        self.tabs.setTabText(self.tabs.indexOf(self.macroTab), QCoreApplication.translate("MainWindow", u"Makra", None))
        self.creatorEditorGroup.setTitle(QCoreApplication.translate("MainWindow", u"Edytor", None))
        self.creatorEditorDeleteFromMacro.setText(QCoreApplication.translate("MainWindow", u"Usu\u0144 z makro", None))
        ___qtreewidgetitem = self.creatorEditorActions.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Czynno\u015bci", None));

        __sortingEnabled = self.creatorEditorActions.isSortingEnabled()
        self.creatorEditorActions.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.creatorEditorActions.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Akcje myszki", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"Przemie\u015b\u0107 kursor", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"Klikni\u0119cie", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem1.child(2)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"Podw\u00f3jne klikni\u0119cie", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem1.child(3)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"Przytrzymaj przycisk myszy", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem1.child(4)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"Pu\u015b\u0107 przycisk myszy", None));
        ___qtreewidgetitem7 = ___qtreewidgetitem1.child(5)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"Ruch k\u00f3\u0142ka myszy", None));
        ___qtreewidgetitem8 = self.creatorEditorActions.topLevelItem(1)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"Akcje klawiatury", None));
        ___qtreewidgetitem9 = ___qtreewidgetitem8.child(0)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"Kliknij klawisz", None));
        ___qtreewidgetitem10 = ___qtreewidgetitem8.child(1)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainWindow", u"U\u017cyj skr\u00f3tu klawiszowego", None));
        ___qtreewidgetitem11 = ___qtreewidgetitem8.child(2)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("MainWindow", u"Przytrzymaj klawisz", None));
        ___qtreewidgetitem12 = ___qtreewidgetitem8.child(3)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("MainWindow", u"Pu\u015b\u0107 klawisz", None));
        ___qtreewidgetitem13 = ___qtreewidgetitem8.child(4)
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("MainWindow", u"Wypisz tekst", None));
        ___qtreewidgetitem14 = ___qtreewidgetitem8.child(5)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("MainWindow", u"Pu\u015b\u0107 wszystkie klawisze", None));
        ___qtreewidgetitem15 = self.creatorEditorActions.topLevelItem(2)
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("MainWindow", u"Logika", None));
        ___qtreewidgetitem16 = ___qtreewidgetitem15.child(0)
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("MainWindow", u"Czekaj na akcj\u0119 myszy", None));
        ___qtreewidgetitem17 = ___qtreewidgetitem15.child(1)
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("MainWindow", u"Czekaj na akcj\u0119 klawiatury", None));
        ___qtreewidgetitem18 = ___qtreewidgetitem15.child(2)
        ___qtreewidgetitem18.setText(0, QCoreApplication.translate("MainWindow", u"Czekaj N sekund", None));
        ___qtreewidgetitem19 = ___qtreewidgetitem15.child(3)
        ___qtreewidgetitem19.setText(0, QCoreApplication.translate("MainWindow", u"Wykonaj N razy", None));
        ___qtreewidgetitem20 = self.creatorEditorActions.topLevelItem(3)
        ___qtreewidgetitem20.setText(0, QCoreApplication.translate("MainWindow", u"Nagrane", None));
        ___qtreewidgetitem21 = self.creatorEditorActions.topLevelItem(4)
        ___qtreewidgetitem21.setText(0, QCoreApplication.translate("MainWindow", u"Makra", None));
        self.creatorEditorActions.setSortingEnabled(__sortingEnabled)

        self.creatorEditorAddToMacro.setText(QCoreApplication.translate("MainWindow", u"Dodaj do makro", None))
        self.creatorEditorMoveUp.setText(QCoreApplication.translate("MainWindow", u"\u25b2", None))
        self.creatorEditorMoveDown.setText(QCoreApplication.translate("MainWindow", u"\u25bc", None))
        self.creatorEditorSave.setText(QCoreApplication.translate("MainWindow", u"Zapisz makro", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Nazwa makra", None))
        self.testSaveButton.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.creatorEditorClear.setText(QCoreApplication.translate("MainWindow", u"Wyczy\u015b\u0107 edytor", None))
        self.creatorEditorDeleteFromActions.setText(QCoreApplication.translate("MainWindow", u"Usu\u0144 nagranie", None))
        self.creatorEditorNewRecording.setText(QCoreApplication.translate("MainWindow", u"Nowe nagranie", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Lista komend tworz\u0105cych makro", None))
        self.creatorEditorEdit.setText(QCoreApplication.translate("MainWindow", u"Edytuj", None))
        self.testLoadButton.setText(QCoreApplication.translate("MainWindow", u"Wczytaj", None))
        self.testButton.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.testButton_2.setText(QCoreApplication.translate("MainWindow", u"timeTest", None))
        self.WhatIsThisButton.setText(QCoreApplication.translate("MainWindow", u"Co to jest?", None))
        self.previewButton.setText(QCoreApplication.translate("MainWindow", u"Odtw\u00f3rz", None))
        self.testButton_3.setText(QCoreApplication.translate("MainWindow", u"SelectionTest", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"(przyciski testowe)", None))
        self.tabs.setTabText(self.tabs.indexOf(self.creatorTab), QCoreApplication.translate("MainWindow", u"Kreator", None))
        self.AC_Time.setTitle(QCoreApplication.translate("MainWindow", u"Odst\u0119p czasowy mi\u0119dzy klikni\u0119ciami", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Milisekundy", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sekundy", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Minuty", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Godziny", None))
        self.AC_Start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.AC_Stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.AC_ClickHowManyTimesGroup.setTitle(QCoreApplication.translate("MainWindow", u"Ile razy ma klika\u0107", None))
        self.AC_ClickNTimes.setText(QCoreApplication.translate("MainWindow", u"Klikaj", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"razy", None))
        self.AC_ClickUntilStopped.setText(QCoreApplication.translate("MainWindow", u"Klikaj do zatrzymania", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Opcje", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Wybierz przycisk myszy", None))
        self.AC_WhichButton.setItemText(0, QCoreApplication.translate("MainWindow", u"Lewy", None))
        self.AC_WhichButton.setItemText(1, QCoreApplication.translate("MainWindow", u"\u015arodkowy", None))
        self.AC_WhichButton.setItemText(2, QCoreApplication.translate("MainWindow", u"Prawy", None))

        self.AC_Hotkey.setKeySequence(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Skr\u00f3t klawiszowy", None))
        self.tabs.setTabText(self.tabs.indexOf(self.autoclickerTab), QCoreApplication.translate("MainWindow", u"Autoclicker", None))
        self.settingsAutosave.setText(QCoreApplication.translate("MainWindow", u"Autozapis po ka\u017cdej zmianie", None))
        self.settingsDefault.setText(QCoreApplication.translate("MainWindow", u"Przywr\u00f3\u0107 domy\u015blne ustawienia", None))
        self.forceSave.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.forceLoad.setText(QCoreApplication.translate("MainWindow", u"Wczytaj", None))
        self.tabs.setTabText(self.tabs.indexOf(self.settingsTab), QCoreApplication.translate("MainWindow", u"Ustawienia", None))
    # retranslateUi

