# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server_preferences_page.ui'
#
# Created: Wed May  6 16:12:08 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

import gns3.qt
from gns3.qt import QtCore, QtGui, QtWidgets

class Ui_ServerPreferencesPageWidget(object):
    def setupUi(self, ServerPreferencesPageWidget):
        ServerPreferencesPageWidget.setObjectName("ServerPreferencesPageWidget")
        ServerPreferencesPageWidget.resize(460, 536)
        self.gridLayout = QtWidgets.QGridLayout(ServerPreferencesPageWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(164, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.uiRestoreDefaultsPushButton = QtWidgets.QPushButton(ServerPreferencesPageWidget)
        self.uiRestoreDefaultsPushButton.setObjectName("uiRestoreDefaultsPushButton")
        self.horizontalLayout_2.addWidget(self.uiRestoreDefaultsPushButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.uiTabWidget = QtWidgets.QTabWidget(ServerPreferencesPageWidget)
        self.uiTabWidget.setObjectName("uiTabWidget")
        self.uiLocalTabWidget = QtWidgets.QWidget()
        self.uiLocalTabWidget.setObjectName("uiLocalTabWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.uiLocalTabWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.uiLocalServerAutoStartCheckBox = QtWidgets.QCheckBox(self.uiLocalTabWidget)
        self.uiLocalServerAutoStartCheckBox.setChecked(True)
        self.uiLocalServerAutoStartCheckBox.setObjectName("uiLocalServerAutoStartCheckBox")
        self.verticalLayout_2.addWidget(self.uiLocalServerAutoStartCheckBox)
        self.uiGeneralSettingsGroupBox = QtWidgets.QGroupBox(self.uiLocalTabWidget)
        self.uiGeneralSettingsGroupBox.setObjectName("uiGeneralSettingsGroupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.uiGeneralSettingsGroupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.uiLocalServerPathLabel = QtWidgets.QLabel(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerPathLabel.setObjectName("uiLocalServerPathLabel")
        self.gridLayout_3.addWidget(self.uiLocalServerPathLabel, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiLocalServerPathLineEdit = QtWidgets.QLineEdit(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerPathLineEdit.setObjectName("uiLocalServerPathLineEdit")
        self.horizontalLayout.addWidget(self.uiLocalServerPathLineEdit)
        self.uiLocalServerToolButton = QtWidgets.QToolButton(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiLocalServerToolButton.setObjectName("uiLocalServerToolButton")
        self.horizontalLayout.addWidget(self.uiLocalServerToolButton)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.uiLocalServerHostLabel = QtWidgets.QLabel(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerHostLabel.setObjectName("uiLocalServerHostLabel")
        self.gridLayout_3.addWidget(self.uiLocalServerHostLabel, 2, 0, 1, 1)
        self.uiLocalServerHostComboBox = QtWidgets.QComboBox(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerHostComboBox.setObjectName("uiLocalServerHostComboBox")
        self.gridLayout_3.addWidget(self.uiLocalServerHostComboBox, 3, 0, 1, 1)
        self.uiLocalServerPortLabel = QtWidgets.QLabel(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerPortLabel.setObjectName("uiLocalServerPortLabel")
        self.gridLayout_3.addWidget(self.uiLocalServerPortLabel, 4, 0, 1, 1)
        self.uiLocalServerPortSpinBox = QtWidgets.QSpinBox(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerPortSpinBox.setSuffix(" TCP")
        self.uiLocalServerPortSpinBox.setMaximum(65535)
        self.uiLocalServerPortSpinBox.setProperty("value", 8000)
        self.uiLocalServerPortSpinBox.setObjectName("uiLocalServerPortSpinBox")
        self.gridLayout_3.addWidget(self.uiLocalServerPortSpinBox, 5, 0, 1, 1)
        self.uiConsoleConnectionsToAnyIPCheckBox = QtWidgets.QCheckBox(self.uiGeneralSettingsGroupBox)
        self.uiConsoleConnectionsToAnyIPCheckBox.setObjectName("uiConsoleConnectionsToAnyIPCheckBox")
        self.gridLayout_3.addWidget(self.uiConsoleConnectionsToAnyIPCheckBox, 7, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.uiGeneralSettingsGroupBox)
        self.uiConsolePortRangeGroupBox = QtWidgets.QGroupBox(self.uiLocalTabWidget)
        self.uiConsolePortRangeGroupBox.setObjectName("uiConsolePortRangeGroupBox")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.uiConsolePortRangeGroupBox)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.uiConsoleStartPortSpinBox = QtWidgets.QSpinBox(self.uiConsolePortRangeGroupBox)
        self.uiConsoleStartPortSpinBox.setSuffix(" TCP")
        self.uiConsoleStartPortSpinBox.setMaximum(65535)
        self.uiConsoleStartPortSpinBox.setProperty("value", 2000)
        self.uiConsoleStartPortSpinBox.setObjectName("uiConsoleStartPortSpinBox")
        self.horizontalLayout_7.addWidget(self.uiConsoleStartPortSpinBox)
        self.uiConsolePortRangeLabel = QtWidgets.QLabel(self.uiConsolePortRangeGroupBox)
        self.uiConsolePortRangeLabel.setObjectName("uiConsolePortRangeLabel")
        self.horizontalLayout_7.addWidget(self.uiConsolePortRangeLabel)
        self.uiConsoleEndPortSpinBox = QtWidgets.QSpinBox(self.uiConsolePortRangeGroupBox)
        self.uiConsoleEndPortSpinBox.setSuffix(" TCP")
        self.uiConsoleEndPortSpinBox.setMaximum(65535)
        self.uiConsoleEndPortSpinBox.setProperty("value", 5000)
        self.uiConsoleEndPortSpinBox.setObjectName("uiConsoleEndPortSpinBox")
        self.horizontalLayout_7.addWidget(self.uiConsoleEndPortSpinBox)
        spacerItem1 = QtWidgets.QSpacerItem(363, 22, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.uiConsolePortRangeGroupBox)
        self.uiUDPPortRangeGroupBox = QtWidgets.QGroupBox(self.uiLocalTabWidget)
        self.uiUDPPortRangeGroupBox.setObjectName("uiUDPPortRangeGroupBox")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.uiUDPPortRangeGroupBox)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.uiUDPStartPortSpinBox = QtWidgets.QSpinBox(self.uiUDPPortRangeGroupBox)
        self.uiUDPStartPortSpinBox.setSuffix(" UDP")
        self.uiUDPStartPortSpinBox.setMaximum(65535)
        self.uiUDPStartPortSpinBox.setProperty("value", 10000)
        self.uiUDPStartPortSpinBox.setObjectName("uiUDPStartPortSpinBox")
        self.horizontalLayout_8.addWidget(self.uiUDPStartPortSpinBox)
        self.uiUDPPortRangeLabel = QtWidgets.QLabel(self.uiUDPPortRangeGroupBox)
        self.uiUDPPortRangeLabel.setObjectName("uiUDPPortRangeLabel")
        self.horizontalLayout_8.addWidget(self.uiUDPPortRangeLabel)
        self.uiUDPEndPortSpinBox = QtWidgets.QSpinBox(self.uiUDPPortRangeGroupBox)
        self.uiUDPEndPortSpinBox.setSuffix(" UDP")
        self.uiUDPEndPortSpinBox.setMaximum(65535)
        self.uiUDPEndPortSpinBox.setProperty("value", 20000)
        self.uiUDPEndPortSpinBox.setObjectName("uiUDPEndPortSpinBox")
        self.horizontalLayout_8.addWidget(self.uiUDPEndPortSpinBox)
        spacerItem2 = QtWidgets.QSpacerItem(363, 22, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.uiUDPPortRangeGroupBox)
        spacerItem3 = QtWidgets.QSpacerItem(390, 193, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.uiTabWidget.addTab(self.uiLocalTabWidget, "")
        self.uiRemoteTabWidget = QtWidgets.QWidget()
        self.uiRemoteTabWidget.setObjectName("uiRemoteTabWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.uiRemoteTabWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiRemoteServersTreeWidget = QtWidgets.QTreeWidget(self.uiRemoteTabWidget)
        self.uiRemoteServersTreeWidget.setColumnCount(4)
        self.uiRemoteServersTreeWidget.setObjectName("uiRemoteServersTreeWidget")
        self.uiRemoteServersTreeWidget.headerItem().setText(0, "Protocol")
        self.uiRemoteServersTreeWidget.headerItem().setText(1, "Host")
        self.uiRemoteServersTreeWidget.headerItem().setText(2, "Port")
        self.verticalLayout.addWidget(self.uiRemoteServersTreeWidget)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.uiRemoteServerProtocolLabel = QtWidgets.QLabel(self.uiRemoteTabWidget)
        self.uiRemoteServerProtocolLabel.setObjectName("uiRemoteServerProtocolLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.uiRemoteServerProtocolLabel)
        self.uiRemoteServerProtocolComboBox = QtWidgets.QComboBox(self.uiRemoteTabWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteServerProtocolComboBox.sizePolicy().hasHeightForWidth())
        self.uiRemoteServerProtocolComboBox.setSizePolicy(sizePolicy)
        self.uiRemoteServerProtocolComboBox.setObjectName("uiRemoteServerProtocolComboBox")
        self.uiRemoteServerProtocolComboBox.addItem("")
        self.uiRemoteServerProtocolComboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.uiRemoteServerProtocolComboBox)
        self.uiRemoteServerHostLabel = QtWidgets.QLabel(self.uiRemoteTabWidget)
        self.uiRemoteServerHostLabel.setObjectName("uiRemoteServerHostLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.uiRemoteServerHostLabel)
        self.uiRemoteServerPortLineEdit = QtWidgets.QLineEdit(self.uiRemoteTabWidget)
        self.uiRemoteServerPortLineEdit.setObjectName("uiRemoteServerPortLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.uiRemoteServerPortLineEdit)
        self.uiRemoteServerPortLabel = QtWidgets.QLabel(self.uiRemoteTabWidget)
        self.uiRemoteServerPortLabel.setObjectName("uiRemoteServerPortLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.uiRemoteServerPortLabel)
        self.uiRemoteServerPortSpinBox = QtWidgets.QSpinBox(self.uiRemoteTabWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteServerPortSpinBox.sizePolicy().hasHeightForWidth())
        self.uiRemoteServerPortSpinBox.setSizePolicy(sizePolicy)
        self.uiRemoteServerPortSpinBox.setSuffix(" TCP")
        self.uiRemoteServerPortSpinBox.setMaximum(65535)
        self.uiRemoteServerPortSpinBox.setProperty("value", 8000)
        self.uiRemoteServerPortSpinBox.setObjectName("uiRemoteServerPortSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.uiRemoteServerPortSpinBox)
        self.uiRemoteServerUserLabel = QtWidgets.QLabel(self.uiRemoteTabWidget)
        self.uiRemoteServerUserLabel.setObjectName("uiRemoteServerUserLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.uiRemoteServerUserLabel)
        self.uiRemoteServerUserLineEdit = QtWidgets.QLineEdit(self.uiRemoteTabWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteServerUserLineEdit.sizePolicy().hasHeightForWidth())
        self.uiRemoteServerUserLineEdit.setSizePolicy(sizePolicy)
        self.uiRemoteServerUserLineEdit.setObjectName("uiRemoteServerUserLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.uiRemoteServerUserLineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.uiAddRemoteServerPushButton = QtWidgets.QPushButton(self.uiRemoteTabWidget)
        self.uiAddRemoteServerPushButton.setObjectName("uiAddRemoteServerPushButton")
        self.horizontalLayout_3.addWidget(self.uiAddRemoteServerPushButton)
        self.uiDeleteRemoteServerPushButton = QtWidgets.QPushButton(self.uiRemoteTabWidget)
        self.uiDeleteRemoteServerPushButton.setEnabled(False)
        self.uiDeleteRemoteServerPushButton.setObjectName("uiDeleteRemoteServerPushButton")
        self.horizontalLayout_3.addWidget(self.uiDeleteRemoteServerPushButton)
        spacerItem4 = QtWidgets.QSpacerItem(206, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(390, 12, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.uiTabWidget.addTab(self.uiRemoteTabWidget, "")
        self.gridLayout.addWidget(self.uiTabWidget, 0, 0, 1, 1)

        self.retranslateUi(ServerPreferencesPageWidget)
        self.uiTabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(ServerPreferencesPageWidget)
        ServerPreferencesPageWidget.setTabOrder(self.uiTabWidget, self.uiLocalServerAutoStartCheckBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiLocalServerAutoStartCheckBox, self.uiLocalServerToolButton)
        ServerPreferencesPageWidget.setTabOrder(self.uiLocalServerToolButton, self.uiLocalServerHostComboBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiLocalServerHostComboBox, self.uiLocalServerPortSpinBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiLocalServerPortSpinBox, self.uiConsoleConnectionsToAnyIPCheckBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiConsoleConnectionsToAnyIPCheckBox, self.uiConsoleStartPortSpinBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiConsoleStartPortSpinBox, self.uiConsoleEndPortSpinBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiConsoleEndPortSpinBox, self.uiUDPStartPortSpinBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiUDPStartPortSpinBox, self.uiUDPEndPortSpinBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiUDPEndPortSpinBox, self.uiLocalServerPathLineEdit)
        ServerPreferencesPageWidget.setTabOrder(self.uiLocalServerPathLineEdit, self.uiRemoteServersTreeWidget)
        ServerPreferencesPageWidget.setTabOrder(self.uiRemoteServersTreeWidget, self.uiRemoteServerProtocolComboBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiRemoteServerProtocolComboBox, self.uiRemoteServerPortLineEdit)
        ServerPreferencesPageWidget.setTabOrder(self.uiRemoteServerPortLineEdit, self.uiRemoteServerPortSpinBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiRemoteServerPortSpinBox, self.uiRemoteServerUserLineEdit)
        ServerPreferencesPageWidget.setTabOrder(self.uiRemoteServerUserLineEdit, self.uiAddRemoteServerPushButton)
        ServerPreferencesPageWidget.setTabOrder(self.uiAddRemoteServerPushButton, self.uiDeleteRemoteServerPushButton)
        ServerPreferencesPageWidget.setTabOrder(self.uiDeleteRemoteServerPushButton, self.uiRestoreDefaultsPushButton)

    def retranslateUi(self, ServerPreferencesPageWidget):
        _translate = gns3.qt.translate
        ServerPreferencesPageWidget.setWindowTitle(_translate("ServerPreferencesPageWidget", "Server"))
        self.uiRestoreDefaultsPushButton.setText(_translate("ServerPreferencesPageWidget", "Restore defaults"))
        self.uiLocalServerAutoStartCheckBox.setText(_translate("ServerPreferencesPageWidget", "Enable local server"))
        self.uiGeneralSettingsGroupBox.setTitle(_translate("ServerPreferencesPageWidget", "General settings"))
        self.uiLocalServerPathLabel.setText(_translate("ServerPreferencesPageWidget", "Path:"))
        self.uiLocalServerToolButton.setText(_translate("ServerPreferencesPageWidget", "&Browse..."))
        self.uiLocalServerHostLabel.setText(_translate("ServerPreferencesPageWidget", "Host binding:"))
        self.uiLocalServerPortLabel.setText(_translate("ServerPreferencesPageWidget", "Port:"))
        self.uiConsoleConnectionsToAnyIPCheckBox.setText(_translate("ServerPreferencesPageWidget", "Allow console connections to any local IP address"))
        self.uiConsolePortRangeGroupBox.setTitle(_translate("ServerPreferencesPageWidget", "Console port range"))
        self.uiConsolePortRangeLabel.setText(_translate("ServerPreferencesPageWidget", "to"))
        self.uiUDPPortRangeGroupBox.setTitle(_translate("ServerPreferencesPageWidget", "UDP tunneling port range"))
        self.uiUDPPortRangeLabel.setText(_translate("ServerPreferencesPageWidget", "to"))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.uiLocalTabWidget), _translate("ServerPreferencesPageWidget", "Local server"))
        self.uiRemoteServersTreeWidget.headerItem().setText(3, _translate("ServerPreferencesPageWidget", "User"))
        self.uiRemoteServerProtocolLabel.setText(_translate("ServerPreferencesPageWidget", "Protocol:"))
        self.uiRemoteServerProtocolComboBox.setCurrentText(_translate("ServerPreferencesPageWidget", "HTTP"))
        self.uiRemoteServerProtocolComboBox.setItemText(0, _translate("ServerPreferencesPageWidget", "HTTP"))
        self.uiRemoteServerProtocolComboBox.setItemText(1, _translate("ServerPreferencesPageWidget", "SSH"))
        self.uiRemoteServerHostLabel.setText(_translate("ServerPreferencesPageWidget", "Host:"))
        self.uiRemoteServerPortLineEdit.setText(_translate("ServerPreferencesPageWidget", "192.168.56.101"))
        self.uiRemoteServerPortLabel.setText(_translate("ServerPreferencesPageWidget", "Port:"))
        self.uiRemoteServerUserLabel.setText(_translate("ServerPreferencesPageWidget", "User (only for SSH):"))
        self.uiAddRemoteServerPushButton.setText(_translate("ServerPreferencesPageWidget", "&Add"))
        self.uiDeleteRemoteServerPushButton.setText(_translate("ServerPreferencesPageWidget", "&Delete"))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.uiRemoteTabWidget), _translate("ServerPreferencesPageWidget", "Remote servers"))

