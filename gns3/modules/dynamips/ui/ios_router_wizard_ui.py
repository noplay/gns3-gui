# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/grossmj/PycharmProjects/gns3-gui/gns3/modules/dynamips/ui/ios_router_wizard.ui'
#
# Created: Wed Oct 22 16:46:37 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_IOSRouterWizard(object):
    def setupUi(self, IOSRouterWizard):
        IOSRouterWizard.setObjectName(_fromUtf8("IOSRouterWizard"))
        IOSRouterWizard.resize(517, 398)
        IOSRouterWizard.setModal(True)
        self.uiServerWizardPage = QtGui.QWizardPage()
        self.uiServerWizardPage.setObjectName(_fromUtf8("uiServerWizardPage"))
        self.verticalLayout = QtGui.QVBoxLayout(self.uiServerWizardPage)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.uiServerTypeGroupBox = QtGui.QGroupBox(self.uiServerWizardPage)
        self.uiServerTypeGroupBox.setObjectName(_fromUtf8("uiServerTypeGroupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.uiServerTypeGroupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.uiRemoteRadioButton = QtGui.QRadioButton(self.uiServerTypeGroupBox)
        self.uiRemoteRadioButton.setChecked(True)
        self.uiRemoteRadioButton.setObjectName(_fromUtf8("uiRemoteRadioButton"))
        self.horizontalLayout.addWidget(self.uiRemoteRadioButton)
        self.uiCloudRadioButton = QtGui.QRadioButton(self.uiServerTypeGroupBox)
        self.uiCloudRadioButton.setObjectName(_fromUtf8("uiCloudRadioButton"))
        self.horizontalLayout.addWidget(self.uiCloudRadioButton)
        self.uiLocalRadioButton = QtGui.QRadioButton(self.uiServerTypeGroupBox)
        self.uiLocalRadioButton.setObjectName(_fromUtf8("uiLocalRadioButton"))
        self.horizontalLayout.addWidget(self.uiLocalRadioButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.uiServerTypeGroupBox)
        self.uiRemoteServersGroupBox = QtGui.QGroupBox(self.uiServerWizardPage)
        self.uiRemoteServersGroupBox.setObjectName(_fromUtf8("uiRemoteServersGroupBox"))
        self.gridLayout_7 = QtGui.QGridLayout(self.uiRemoteServersGroupBox)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.uiLoadBalanceCheckBox = QtGui.QCheckBox(self.uiRemoteServersGroupBox)
        self.uiLoadBalanceCheckBox.setChecked(True)
        self.uiLoadBalanceCheckBox.setObjectName(_fromUtf8("uiLoadBalanceCheckBox"))
        self.gridLayout_7.addWidget(self.uiLoadBalanceCheckBox, 0, 0, 1, 2)
        self.uiRemoteServersLabel = QtGui.QLabel(self.uiRemoteServersGroupBox)
        self.uiRemoteServersLabel.setObjectName(_fromUtf8("uiRemoteServersLabel"))
        self.gridLayout_7.addWidget(self.uiRemoteServersLabel, 1, 0, 1, 1)
        self.uiRemoteServersComboBox = QtGui.QComboBox(self.uiRemoteServersGroupBox)
        self.uiRemoteServersComboBox.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteServersComboBox.sizePolicy().hasHeightForWidth())
        self.uiRemoteServersComboBox.setSizePolicy(sizePolicy)
        self.uiRemoteServersComboBox.setObjectName(_fromUtf8("uiRemoteServersComboBox"))
        self.gridLayout_7.addWidget(self.uiRemoteServersComboBox, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.uiRemoteServersGroupBox)
        IOSRouterWizard.addPage(self.uiServerWizardPage)
        self.uiIOSImageWizardPage = QtGui.QWizardPage()
        self.uiIOSImageWizardPage.setObjectName(_fromUtf8("uiIOSImageWizardPage"))
        self.gridLayout_6 = QtGui.QGridLayout(self.uiIOSImageWizardPage)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.uiIOSImageLineEdit = QtGui.QLineEdit(self.uiIOSImageWizardPage)
        self.uiIOSImageLineEdit.setObjectName(_fromUtf8("uiIOSImageLineEdit"))
        self.horizontalLayout_5.addWidget(self.uiIOSImageLineEdit)
        self.uiIOSImageToolButton = QtGui.QToolButton(self.uiIOSImageWizardPage)
        self.uiIOSImageToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiIOSImageToolButton.setObjectName(_fromUtf8("uiIOSImageToolButton"))
        self.horizontalLayout_5.addWidget(self.uiIOSImageToolButton)
        self.gridLayout_6.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)
        self.uiIOSImageLabel = QtGui.QLabel(self.uiIOSImageWizardPage)
        self.uiIOSImageLabel.setObjectName(_fromUtf8("uiIOSImageLabel"))
        self.gridLayout_6.addWidget(self.uiIOSImageLabel, 1, 0, 1, 1)
        IOSRouterWizard.addPage(self.uiIOSImageWizardPage)
        self.uiNamePlatformWizardPage = QtGui.QWizardPage()
        self.uiNamePlatformWizardPage.setObjectName(_fromUtf8("uiNamePlatformWizardPage"))
        self.gridLayout = QtGui.QGridLayout(self.uiNamePlatformWizardPage)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.uiNameLineEdit = QtGui.QLineEdit(self.uiNamePlatformWizardPage)
        self.uiNameLineEdit.setObjectName(_fromUtf8("uiNameLineEdit"))
        self.gridLayout.addWidget(self.uiNameLineEdit, 0, 1, 1, 1)
        self.uiChassisComboBox = QtGui.QComboBox(self.uiNamePlatformWizardPage)
        self.uiChassisComboBox.setObjectName(_fromUtf8("uiChassisComboBox"))
        self.gridLayout.addWidget(self.uiChassisComboBox, 2, 1, 1, 1)
        self.uiTypeLabel = QtGui.QLabel(self.uiNamePlatformWizardPage)
        self.uiTypeLabel.setObjectName(_fromUtf8("uiTypeLabel"))
        self.gridLayout.addWidget(self.uiTypeLabel, 1, 0, 1, 1)
        self.uiNameLabel = QtGui.QLabel(self.uiNamePlatformWizardPage)
        self.uiNameLabel.setObjectName(_fromUtf8("uiNameLabel"))
        self.gridLayout.addWidget(self.uiNameLabel, 0, 0, 1, 1)
        self.uiPlatformComboBox = QtGui.QComboBox(self.uiNamePlatformWizardPage)
        self.uiPlatformComboBox.setObjectName(_fromUtf8("uiPlatformComboBox"))
        self.gridLayout.addWidget(self.uiPlatformComboBox, 1, 1, 1, 1)
        self.uiChassisLabel = QtGui.QLabel(self.uiNamePlatformWizardPage)
        self.uiChassisLabel.setObjectName(_fromUtf8("uiChassisLabel"))
        self.gridLayout.addWidget(self.uiChassisLabel, 2, 0, 1, 1)
        IOSRouterWizard.addPage(self.uiNamePlatformWizardPage)
        self.uiMemoryWizardPage = QtGui.QWizardPage()
        self.uiMemoryWizardPage.setObjectName(_fromUtf8("uiMemoryWizardPage"))
        self.gridLayout_2 = QtGui.QGridLayout(self.uiMemoryWizardPage)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.uiRamLabel = QtGui.QLabel(self.uiMemoryWizardPage)
        self.uiRamLabel.setObjectName(_fromUtf8("uiRamLabel"))
        self.gridLayout_2.addWidget(self.uiRamLabel, 0, 0, 1, 1)
        self.uiRamSpinBox = QtGui.QSpinBox(self.uiMemoryWizardPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRamSpinBox.sizePolicy().hasHeightForWidth())
        self.uiRamSpinBox.setSizePolicy(sizePolicy)
        self.uiRamSpinBox.setMinimum(32)
        self.uiRamSpinBox.setMaximum(65535)
        self.uiRamSpinBox.setSingleStep(32)
        self.uiRamSpinBox.setProperty("value", 128)
        self.uiRamSpinBox.setObjectName(_fromUtf8("uiRamSpinBox"))
        self.gridLayout_2.addWidget(self.uiRamSpinBox, 0, 1, 1, 1)
        self.uiTestIOSImagePushButton = QtGui.QPushButton(self.uiMemoryWizardPage)
        self.uiTestIOSImagePushButton.setObjectName(_fromUtf8("uiTestIOSImagePushButton"))
        self.gridLayout_2.addWidget(self.uiTestIOSImagePushButton, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.uiMemoryWizardPage)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 2)
        IOSRouterWizard.addPage(self.uiMemoryWizardPage)
        self.uiNetworkAdaptersWizardPage = QtGui.QWizardPage()
        self.uiNetworkAdaptersWizardPage.setObjectName(_fromUtf8("uiNetworkAdaptersWizardPage"))
        self.gridLayout_4 = QtGui.QGridLayout(self.uiNetworkAdaptersWizardPage)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.uiSlot0Label = QtGui.QLabel(self.uiNetworkAdaptersWizardPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiSlot0Label.sizePolicy().hasHeightForWidth())
        self.uiSlot0Label.setSizePolicy(sizePolicy)
        self.uiSlot0Label.setObjectName(_fromUtf8("uiSlot0Label"))
        self.gridLayout_4.addWidget(self.uiSlot0Label, 0, 0, 1, 1)
        self.uiSlot0comboBox = QtGui.QComboBox(self.uiNetworkAdaptersWizardPage)
        self.uiSlot0comboBox.setObjectName(_fromUtf8("uiSlot0comboBox"))
        self.gridLayout_4.addWidget(self.uiSlot0comboBox, 0, 1, 1, 1)
        self.uiSlot1Label = QtGui.QLabel(self.uiNetworkAdaptersWizardPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiSlot1Label.sizePolicy().hasHeightForWidth())
        self.uiSlot1Label.setSizePolicy(sizePolicy)
        self.uiSlot1Label.setObjectName(_fromUtf8("uiSlot1Label"))
        self.gridLayout_4.addWidget(self.uiSlot1Label, 1, 0, 1, 1)
        self.uiSlot1comboBox = QtGui.QComboBox(self.uiNetworkAdaptersWizardPage)
        self.uiSlot1comboBox.setObjectName(_fromUtf8("uiSlot1comboBox"))
        self.gridLayout_4.addWidget(self.uiSlot1comboBox, 1, 1, 1, 1)
        self.uiSlot2Label = QtGui.QLabel(self.uiNetworkAdaptersWizardPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiSlot2Label.sizePolicy().hasHeightForWidth())
        self.uiSlot2Label.setSizePolicy(sizePolicy)
        self.uiSlot2Label.setObjectName(_fromUtf8("uiSlot2Label"))
        self.gridLayout_4.addWidget(self.uiSlot2Label, 2, 0, 1, 1)
        self.uiSlot2comboBox = QtGui.QComboBox(self.uiNetworkAdaptersWizardPage)
        self.uiSlot2comboBox.setObjectName(_fromUtf8("uiSlot2comboBox"))
        self.gridLayout_4.addWidget(self.uiSlot2comboBox, 2, 1, 1, 1)
        self.uiSlot3Label = QtGui.QLabel(self.uiNetworkAdaptersWizardPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiSlot3Label.sizePolicy().hasHeightForWidth())
        self.uiSlot3Label.setSizePolicy(sizePolicy)
        self.uiSlot3Label.setObjectName(_fromUtf8("uiSlot3Label"))
        self.gridLayout_4.addWidget(self.uiSlot3Label, 3, 0, 1, 1)
        self.uiSlot3comboBox = QtGui.QComboBox(self.uiNetworkAdaptersWizardPage)
        self.uiSlot3comboBox.setObjectName(_fromUtf8("uiSlot3comboBox"))
        self.gridLayout_4.addWidget(self.uiSlot3comboBox, 3, 1, 1, 1)
        self.uiSlot4Label = QtGui.QLabel(self.uiNetworkAdaptersWizardPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiSlot4Label.sizePolicy().hasHeightForWidth())
        self.uiSlot4Label.setSizePolicy(sizePolicy)
        self.uiSlot4Label.setObjectName(_fromUtf8("uiSlot4Label"))
        self.gridLayout_4.addWidget(self.uiSlot4Label, 4, 0, 1, 1)
        self.uiSlot4comboBox = QtGui.QComboBox(self.uiNetworkAdaptersWizardPage)
        self.uiSlot4comboBox.setObjectName(_fromUtf8("uiSlot4comboBox"))
        self.gridLayout_4.addWidget(self.uiSlot4comboBox, 4, 1, 1, 1)
        self.uiSlot5Label = QtGui.QLabel(self.uiNetworkAdaptersWizardPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiSlot5Label.sizePolicy().hasHeightForWidth())
        self.uiSlot5Label.setSizePolicy(sizePolicy)
        self.uiSlot5Label.setObjectName(_fromUtf8("uiSlot5Label"))
        self.gridLayout_4.addWidget(self.uiSlot5Label, 5, 0, 1, 1)
        self.uiSlot5comboBox = QtGui.QComboBox(self.uiNetworkAdaptersWizardPage)
        self.uiSlot5comboBox.setObjectName(_fromUtf8("uiSlot5comboBox"))
        self.gridLayout_4.addWidget(self.uiSlot5comboBox, 5, 1, 1, 1)
        self.uiSlot6Label = QtGui.QLabel(self.uiNetworkAdaptersWizardPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiSlot6Label.sizePolicy().hasHeightForWidth())
        self.uiSlot6Label.setSizePolicy(sizePolicy)
        self.uiSlot6Label.setObjectName(_fromUtf8("uiSlot6Label"))
        self.gridLayout_4.addWidget(self.uiSlot6Label, 6, 0, 1, 1)
        self.uiSlot6comboBox = QtGui.QComboBox(self.uiNetworkAdaptersWizardPage)
        self.uiSlot6comboBox.setObjectName(_fromUtf8("uiSlot6comboBox"))
        self.gridLayout_4.addWidget(self.uiSlot6comboBox, 6, 1, 1, 1)
        IOSRouterWizard.addPage(self.uiNetworkAdaptersWizardPage)
        self.uiWicWizardPage = QtGui.QWizardPage()
        self.uiWicWizardPage.setObjectName(_fromUtf8("uiWicWizardPage"))
        self.gridLayout_5 = QtGui.QGridLayout(self.uiWicWizardPage)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.uiWic0Label = QtGui.QLabel(self.uiWicWizardPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiWic0Label.sizePolicy().hasHeightForWidth())
        self.uiWic0Label.setSizePolicy(sizePolicy)
        self.uiWic0Label.setObjectName(_fromUtf8("uiWic0Label"))
        self.gridLayout_5.addWidget(self.uiWic0Label, 0, 0, 1, 1)
        self.uiWic0comboBox = QtGui.QComboBox(self.uiWicWizardPage)
        self.uiWic0comboBox.setObjectName(_fromUtf8("uiWic0comboBox"))
        self.gridLayout_5.addWidget(self.uiWic0comboBox, 0, 1, 1, 1)
        self.uiWic1Label = QtGui.QLabel(self.uiWicWizardPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiWic1Label.sizePolicy().hasHeightForWidth())
        self.uiWic1Label.setSizePolicy(sizePolicy)
        self.uiWic1Label.setObjectName(_fromUtf8("uiWic1Label"))
        self.gridLayout_5.addWidget(self.uiWic1Label, 1, 0, 1, 1)
        self.uiWic1comboBox = QtGui.QComboBox(self.uiWicWizardPage)
        self.uiWic1comboBox.setObjectName(_fromUtf8("uiWic1comboBox"))
        self.gridLayout_5.addWidget(self.uiWic1comboBox, 1, 1, 1, 1)
        self.uiWic2Label = QtGui.QLabel(self.uiWicWizardPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiWic2Label.sizePolicy().hasHeightForWidth())
        self.uiWic2Label.setSizePolicy(sizePolicy)
        self.uiWic2Label.setObjectName(_fromUtf8("uiWic2Label"))
        self.gridLayout_5.addWidget(self.uiWic2Label, 2, 0, 1, 1)
        self.uiWic2comboBox = QtGui.QComboBox(self.uiWicWizardPage)
        self.uiWic2comboBox.setObjectName(_fromUtf8("uiWic2comboBox"))
        self.gridLayout_5.addWidget(self.uiWic2comboBox, 2, 1, 1, 1)
        IOSRouterWizard.addPage(self.uiWicWizardPage)
        self.uiIdlePCWizardPage = QtGui.QWizardPage()
        self.uiIdlePCWizardPage.setObjectName(_fromUtf8("uiIdlePCWizardPage"))
        self.gridLayout_3 = QtGui.QGridLayout(self.uiIdlePCWizardPage)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.uiIdlepcLabel = QtGui.QLabel(self.uiIdlePCWizardPage)
        self.uiIdlepcLabel.setObjectName(_fromUtf8("uiIdlepcLabel"))
        self.gridLayout_3.addWidget(self.uiIdlepcLabel, 0, 0, 1, 1)
        self.uiIdlepcLineEdit = QtGui.QLineEdit(self.uiIdlePCWizardPage)
        self.uiIdlepcLineEdit.setObjectName(_fromUtf8("uiIdlepcLineEdit"))
        self.gridLayout_3.addWidget(self.uiIdlepcLineEdit, 0, 1, 1, 1)
        self.uiIdlePCFinderPushButton = QtGui.QPushButton(self.uiIdlePCWizardPage)
        self.uiIdlePCFinderPushButton.setObjectName(_fromUtf8("uiIdlePCFinderPushButton"))
        self.gridLayout_3.addWidget(self.uiIdlePCFinderPushButton, 0, 2, 1, 1)
        IOSRouterWizard.addPage(self.uiIdlePCWizardPage)

        self.retranslateUi(IOSRouterWizard)
        QtCore.QMetaObject.connectSlotsByName(IOSRouterWizard)
        IOSRouterWizard.setTabOrder(self.uiNameLineEdit, self.uiPlatformComboBox)

    def retranslateUi(self, IOSRouterWizard):
        IOSRouterWizard.setWindowTitle(_translate("IOSRouterWizard", "New IOS router", None))
        self.uiServerWizardPage.setTitle(_translate("IOSRouterWizard", "Server", None))
        self.uiServerWizardPage.setSubTitle(_translate("IOSRouterWizard", "Please choose a server type to run your new IOS router.", None))
        self.uiServerTypeGroupBox.setTitle(_translate("IOSRouterWizard", "Server type", None))
        self.uiRemoteRadioButton.setText(_translate("IOSRouterWizard", "Remote", None))
        self.uiCloudRadioButton.setText(_translate("IOSRouterWizard", "Cloud", None))
        self.uiLocalRadioButton.setText(_translate("IOSRouterWizard", "Local", None))
        self.uiRemoteServersGroupBox.setTitle(_translate("IOSRouterWizard", "Remote servers", None))
        self.uiLoadBalanceCheckBox.setText(_translate("IOSRouterWizard", "Load balance across all available remote servers", None))
        self.uiRemoteServersLabel.setText(_translate("IOSRouterWizard", "Run on server:", None))
        self.uiIOSImageWizardPage.setTitle(_translate("IOSRouterWizard", "IOS image", None))
        self.uiIOSImageWizardPage.setSubTitle(_translate("IOSRouterWizard", "Please choose an IOS image.", None))
        self.uiIOSImageToolButton.setText(_translate("IOSRouterWizard", "&Browse...", None))
        self.uiIOSImageLabel.setText(_translate("IOSRouterWizard", "IOS image:", None))
        self.uiNamePlatformWizardPage.setTitle(_translate("IOSRouterWizard", "Name and platform", None))
        self.uiNamePlatformWizardPage.setSubTitle(_translate("IOSRouterWizard", "Please choose a descriptive name for this new IOS router and verify the platform and chassis.", None))
        self.uiTypeLabel.setText(_translate("IOSRouterWizard", "Platform:", None))
        self.uiNameLabel.setText(_translate("IOSRouterWizard", "Name:", None))
        self.uiChassisLabel.setText(_translate("IOSRouterWizard", "Chassis:", None))
        self.uiMemoryWizardPage.setTitle(_translate("IOSRouterWizard", "Memory", None))
        self.uiMemoryWizardPage.setSubTitle(_translate("IOSRouterWizard", "Please check the amount of memory (RAM) that you allocate to IOS. Not enough RAM could prevent IOS to start.", None))
        self.uiRamLabel.setText(_translate("IOSRouterWizard", "Default RAM:", None))
        self.uiRamSpinBox.setSuffix(_translate("IOSRouterWizard", " MiB", None))
        self.uiTestIOSImagePushButton.setText(_translate("IOSRouterWizard", "&Test IOS image", None))
        self.label.setText(_translate("IOSRouterWizard", "<html><head/><body><p><a href=\"http://tools.cisco.com/ITDIT/CFN/jsp/SearchBySoftware.jsp\"><span style=\" text-decoration: underline; color:#0000ff;\">Check for minimum RAM requirement</span></a></p></body></html>", None))
        self.uiNetworkAdaptersWizardPage.setTitle(_translate("IOSRouterWizard", "Network adapters", None))
        self.uiNetworkAdaptersWizardPage.setSubTitle(_translate("IOSRouterWizard", "Please choose the default network adapters that should be inserted into every new instance of this router.", None))
        self.uiSlot0Label.setText(_translate("IOSRouterWizard", "slot 0:", None))
        self.uiSlot1Label.setText(_translate("IOSRouterWizard", "slot 1:", None))
        self.uiSlot2Label.setText(_translate("IOSRouterWizard", "slot 2:", None))
        self.uiSlot3Label.setText(_translate("IOSRouterWizard", "slot 3:", None))
        self.uiSlot4Label.setText(_translate("IOSRouterWizard", "slot 4:", None))
        self.uiSlot5Label.setText(_translate("IOSRouterWizard", "slot 5:", None))
        self.uiSlot6Label.setText(_translate("IOSRouterWizard", "slot 6:", None))
        self.uiWicWizardPage.setTitle(_translate("IOSRouterWizard", "WIC modules", None))
        self.uiWicWizardPage.setSubTitle(_translate("IOSRouterWizard", "Please choose the default WIC modules that should be inserted into every new instance of this router.", None))
        self.uiWic0Label.setText(_translate("IOSRouterWizard", "wic 0:", None))
        self.uiWic1Label.setText(_translate("IOSRouterWizard", "wic 1:", None))
        self.uiWic2Label.setText(_translate("IOSRouterWizard", "wic 2:", None))
        self.uiIdlePCWizardPage.setTitle(_translate("IOSRouterWizard", "Idle-PC", None))
        self.uiIdlePCWizardPage.setSubTitle(_translate("IOSRouterWizard", "An Idle-PC value is necessary to prevent IOS to use 100% of your processor or one of its core.", None))
        self.uiIdlepcLabel.setText(_translate("IOSRouterWizard", "Idle-PC:", None))
        self.uiIdlePCFinderPushButton.setText(_translate("IOSRouterWizard", "Idle-PC finder", None))

