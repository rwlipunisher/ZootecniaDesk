from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtCore import Qt
import sqlite3

class MainWindowApp():

    
    def setupUi(self, MainWindow: QMainWindow, mainDatabasePath: str):
        self.mainDatabasePath = mainDatabasePath
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1012, 692)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(25, 25, 25);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_header = QtWidgets.QFrame(parent=self.centralwidget)
        self.main_header.setMaximumSize(QtCore.QSize(16777215, 50))
        self.main_header.setStyleSheet("QFrame{\n"
"    border-bottom: 1px solid #000;\n"
"    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.main_header.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.main_header.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main_header.setObjectName("main_header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.main_header)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tittle_bar_container = QtWidgets.QFrame(parent=self.main_header)
        self.tittle_bar_container.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.tittle_bar_container.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.tittle_bar_container.setObjectName("tittle_bar_container")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tittle_bar_container)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.left_menu_toggle = QtWidgets.QFrame(parent=self.tittle_bar_container)
        self.left_menu_toggle.setMinimumSize(QtCore.QSize(50, 0))
        self.left_menu_toggle.setMaximumSize(QtCore.QSize(50, 16777215))
        self.left_menu_toggle.setStyleSheet("QFrame{\n"
"    background-color: #000;\n"
"}\n"
"QPushButton{\n"
"    padding: 5px 10px;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    background-color: #000;\n"
"    color: #fff;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"}")
        self.left_menu_toggle.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.left_menu_toggle.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.left_menu_toggle.setObjectName("left_menu_toggle")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.left_menu_toggle)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_5.addWidget(self.left_menu_toggle)
        self.tittle_bar = QtWidgets.QFrame(parent=self.tittle_bar_container)
        self.tittle_bar.setStyleSheet("QLabel{\n"
"    color: #fff;\n"
"}")
        self.tittle_bar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.tittle_bar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.tittle_bar.setObjectName("tittle_bar")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tittle_bar)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_6 = QtWidgets.QLabel(parent=self.tittle_bar)
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_9.addWidget(self.label_6)
        self.horizontalLayout_5.addWidget(self.tittle_bar)
        self.horizontalLayout_2.addWidget(self.tittle_bar_container)
        self.top_right_btns = QtWidgets.QFrame(parent=self.main_header)
        self.top_right_btns.setMaximumSize(QtCore.QSize(100, 16777215))
        self.top_right_btns.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"}")
        self.top_right_btns.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.top_right_btns.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.top_right_btns.setObjectName("top_right_btns")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.top_right_btns)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.restoreButton = QtWidgets.QPushButton(parent=self.top_right_btns)
        self.restoreButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.restoreButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/cil-window-maximize.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.restoreButton.setIcon(icon)
        self.restoreButton.setIconSize(QtCore.QSize(24, 24))
        self.restoreButton.setObjectName("restoreButton")
        self.horizontalLayout_3.addWidget(self.restoreButton)
        self.minimizeButton = QtWidgets.QPushButton(parent=self.top_right_btns)
        self.minimizeButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.minimizeButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/cil-minus.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.minimizeButton.setIcon(icon1)
        self.minimizeButton.setIconSize(QtCore.QSize(24, 24))
        self.minimizeButton.setObjectName("minimizeButton")
        self.horizontalLayout_3.addWidget(self.minimizeButton)
        self.closeButton = QtWidgets.QPushButton(parent=self.top_right_btns)
        self.closeButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.closeButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/cil-x.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.closeButton.setIcon(icon2)
        self.closeButton.setIconSize(QtCore.QSize(24, 24))
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_3.addWidget(self.closeButton)
        self.horizontalLayout_2.addWidget(self.top_right_btns)
        self.verticalLayout.addWidget(self.main_header)
        self.main_body = QtWidgets.QFrame(parent=self.centralwidget)
        self.main_body.setStyleSheet("")
        self.main_body.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main_body.setObjectName("main_body")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_body)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_side_menu = QtWidgets.QFrame(parent=self.main_body)
        self.left_side_menu.setMaximumSize(QtCore.QSize(50, 16777215))
        self.left_side_menu.setStyleSheet("QFrame{\n"
"    background-color: #000;\n"
"}\n"
"QPushButton{\n"
"    padding: 20px 10px;\n"
"    border: none;\n"
"    border-left: 2px solid transparent;\n"
"    border-bottom: 2px solid transparent;\n"
"    border-radius: 5px;\n"
"    background-color: #000;\n"
"    color: #fff;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(0, 92, 157);\n"
"    border-bottom: 2px solid rgb(255, 165, 24);\n"
"}")
        self.left_side_menu.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.left_side_menu.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.left_side_menu.setObjectName("left_side_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.left_side_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.left_menu_top_buttons = QtWidgets.QFrame(parent=self.left_side_menu)
        self.left_menu_top_buttons.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.left_menu_top_buttons.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.left_menu_top_buttons.setObjectName("left_menu_top_buttons")
        self.formLayout = QtWidgets.QFormLayout(self.left_menu_top_buttons)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.Terceiros = QtWidgets.QPushButton(parent=self.left_menu_top_buttons)
        self.Terceiros.setMaximumSize(QtCore.QSize(40, 60))
        self.Terceiros.setStyleSheet("background-image: url(:/icons/icons/cil-user.png);\n"
"background-repeat: none;\n"
"padding-left: 50px;\n"
"background-position: center left;")
        self.Terceiros.setText("")
        self.Terceiros.setObjectName("Terceiros")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Terceiros)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.left_menu_top_buttons)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.left_menu_top_buttons)
        self.pushButton_3.setObjectName("pushButton_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.pushButton_3)
        self.verticalLayout_3.addWidget(self.left_menu_top_buttons)
        self.horizontalLayout.addWidget(self.left_side_menu)
        self.center_main_items = QtWidgets.QFrame(parent=self.main_body)
        self.center_main_items.setStyleSheet("")
        self.center_main_items.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.center_main_items.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.center_main_items.setObjectName("center_main_items")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.center_main_items)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.center_main_items)
        self.stackedWidget.setMidLineWidth(0)
        self.stackedWidget.setObjectName("stackedWidget")
        self.accounts_page = QtWidgets.QWidget()
        self.accounts_page.setStyleSheet("")
        self.accounts_page.setObjectName("accounts_page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.accounts_page)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.login_response_frame = QtWidgets.QFrame(parent=self.accounts_page)
        self.login_response_frame.setMinimumSize(QtCore.QSize(400, 100))
        self.login_response_frame.setMaximumSize(QtCore.QSize(600, 300))
        self.login_response_frame.setStyleSheet("QFrame{    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    border: 2px solid rgb(0, 69, 116);\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton{    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 69, 116);\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"QLabel{\n"
"    padding: 10px;\n"
"    border: none;\n"
"}")
        self.login_response_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.login_response_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.login_response_frame.setObjectName("login_response_frame")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.login_response_frame)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.login_response_msg = QtWidgets.QLabel(parent=self.login_response_frame)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.login_response_msg.setFont(font)
        self.login_response_msg.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.login_response_msg.setObjectName("login_response_msg")
        self.verticalLayout_11.addWidget(self.login_response_msg)
        self.login_res_ok_btn = QtWidgets.QPushButton(parent=self.login_response_frame)
        self.login_res_ok_btn.setMinimumSize(QtCore.QSize(80, 50))
        self.login_res_ok_btn.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setBold(True)
        self.login_res_ok_btn.setFont(font)
        self.login_res_ok_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.login_res_ok_btn.setObjectName("login_res_ok_btn")
        self.verticalLayout_11.addWidget(self.login_res_ok_btn, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_6.addWidget(self.login_response_frame, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.login_form_frame = QtWidgets.QFrame(parent=self.accounts_page)
        self.login_form_frame.setMinimumSize(QtCore.QSize(450, 350))
        self.login_form_frame.setMaximumSize(QtCore.QSize(450, 350))
        self.login_form_frame.setStyleSheet("border-radius: 20px;\n"
"")
        self.login_form_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.login_form_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.login_form_frame.setObjectName("login_form_frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.login_form_frame)
        self.verticalLayout_8.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.input_fileds_frame = QtWidgets.QFrame(parent=self.login_form_frame)
        self.input_fileds_frame.setStyleSheet("QFrame{\n"
"    background-color: rgb(34, 34, 34);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid rgb(1, 90, 153);\n"
"}\n"
"QLineEdit {\n"
"    border: 2px solid rgb(0, 93, 159);\n"
"    border-radius: 10px;\n"
"    padding: 15px;\n"
"    background-color: rgb(0, 69, 116);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(0, 66, 124);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(206, 206, 206);\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 10px;\n"
"    padding: 15px;\n"
"    background-color:rgb(14, 13, 24);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(0, 66, 124);\n"
"}\n"
"QLabel{\n"
"    border:3px solid  rgb(45, 45, 45);\n"
"    border-radius: 10px;\n"
"    \n"
"    background-color: rgb(6, 63, 104);\n"
"}\n"
"QCheckBox{\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 10px;\n"
"}\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(0, 93, 159);\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius: 10px;\n"
"    background:rgb(0, 0, 0);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(255, 255, 255);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(34, 34, 34);\n"
"    background-image: url(:/icons/icons/cil-check.png);\n"
"}")
        self.input_fileds_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.input_fileds_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.input_fileds_frame.setObjectName("input_fileds_frame")
        self.formLayout_2 = QtWidgets.QFormLayout(self.input_fileds_frame)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.input_fileds_frame)
        self.label_2.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.username = QtWidgets.QLineEdit(parent=self.input_fileds_frame)
        self.username.setMinimumSize(QtCore.QSize(200, 50))
        self.username.setMaximumSize(QtCore.QSize(200, 16777215))
        self.username.setStyleSheet("border:3px solid  rgb(43, 31, 91);\n"
"border-radius: 10px;")
        self.username.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.username.setObjectName("username")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.username)
        self.label_5 = QtWidgets.QLabel(parent=self.input_fileds_frame)
        self.label_5.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.password = QtWidgets.QLineEdit(parent=self.input_fileds_frame)
        self.password.setMinimumSize(QtCore.QSize(200, 50))
        self.password.setMaximumSize(QtCore.QSize(200, 16777215))
        self.password.setStyleSheet("border:3px solid  rgb(43, 31, 91);\n"
"border-radius: 10px;")
        self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.password.setObjectName("password")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.password)
        self.keep_me_logged = QtWidgets.QCheckBox(parent=self.input_fileds_frame)
        self.keep_me_logged.setObjectName("keep_me_logged")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.keep_me_logged)
        self.login_btn = QtWidgets.QPushButton(parent=self.input_fileds_frame)
        self.login_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.login_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        self.login_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.login_btn.setObjectName("login_btn")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.login_btn)
        self.profile_icon_frame = QtWidgets.QFrame(parent=self.input_fileds_frame)
        self.profile_icon_frame.setMinimumSize(QtCore.QSize(50, 50))
        self.profile_icon_frame.setMaximumSize(QtCore.QSize(50, 50))
        self.profile_icon_frame.setStyleSheet("image: url(:/icons/icons/cil-user-follow.png);\n"
"background-color: rgb(34, 34, 34);\n"
"border-radius: 25px;\n"
"border: 3px solid rgb(0, 93, 159);")
        self.profile_icon_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.profile_icon_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.profile_icon_frame.setObjectName("profile_icon_frame")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.profile_icon_frame)
        self.verticalLayout_8.addWidget(self.input_fileds_frame, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_6.addWidget(self.login_form_frame, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.stackedWidget.addWidget(self.accounts_page)
        self.settings_page = QtWidgets.QWidget()
        self.settings_page.setStyleSheet("")
        self.settings_page.setObjectName("settings_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.settings_page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_2 = QtWidgets.QFrame(parent=self.settings_page)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_3 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setObjectName("gridLayout")
        self.codChipEdit = QtWidgets.QLineEdit(parent=self.frame_3)
        self.codChipEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.codChipEdit.setObjectName("codChipEdit")
        self.gridLayout.addWidget(self.codChipEdit, 1, 0, 1, 1)
        self.cpfProprietario = QtWidgets.QLineEdit(parent=self.frame_3)
        self.cpfProprietario.setStyleSheet("color: rgb(255, 255, 255);")
        self.cpfProprietario.setObjectName("cpfProprietario")
        self.gridLayout.addWidget(self.cpfProprietario, 6, 1, 1, 1)
        self.tipoSangueEdit = QtWidgets.QLineEdit(parent=self.frame_3)
        self.tipoSangueEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.tipoSangueEdit.setObjectName("tipoSangueEdit")
        self.gridLayout.addWidget(self.tipoSangueEdit, 5, 0, 1, 1)
        self.sexoBox = QtWidgets.QComboBox(parent=self.frame_3)
        self.sexoBox.setObjectName("sexoBox")
        self.gridLayout.addWidget(self.sexoBox, 2, 1, 1, 1)
        self.codChipMaeEdit = QtWidgets.QLineEdit(parent=self.frame_3)
        self.codChipMaeEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.codChipMaeEdit.setObjectName("codChipMaeEdit")
        self.gridLayout.addWidget(self.codChipMaeEdit, 3, 0, 1, 1)
        self.nomeEdit = QtWidgets.QLineEdit(parent=self.frame_3)
        self.nomeEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.nomeEdit.setObjectName("nomeEdit")
        self.gridLayout.addWidget(self.nomeEdit, 1, 1, 1, 1)
        self.nascimentoEdit = QtWidgets.QLineEdit(parent=self.frame_3)
        self.nascimentoEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.nascimentoEdit.setObjectName("nascimentoEdit")
        self.gridLayout.addWidget(self.nascimentoEdit, 2, 0, 1, 1)
        self.precoVendaEdit = QtWidgets.QLineEdit(parent=self.frame_3)
        self.precoVendaEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.precoVendaEdit.setObjectName("precoVendaEdit")
        self.gridLayout.addWidget(self.precoVendaEdit, 5, 1, 1, 1)
        self.codChipPaiEdit = QtWidgets.QLineEdit(parent=self.frame_3)
        self.codChipPaiEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.codChipPaiEdit.setObjectName("codChipPaiEdit")
        self.gridLayout.addWidget(self.codChipPaiEdit, 4, 0, 1, 1)
        self.cpfCriadorEdit = QtWidgets.QLineEdit(parent=self.frame_3)
        self.cpfCriadorEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.cpfCriadorEdit.setObjectName("cpfCriadorEdit")
        self.gridLayout.addWidget(self.cpfCriadorEdit, 6, 0, 1, 1)
        self.precoCompraEdit = QtWidgets.QLineEdit(parent=self.frame_3)
        self.precoCompraEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.precoCompraEdit.setObjectName("precoCompraEdit")
        self.gridLayout.addWidget(self.precoCompraEdit, 4, 1, 1, 1)
        self.frame_5 = QtWidgets.QFrame(parent=self.frame_3)
        self.frame_5.setMaximumSize(QtCore.QSize(500, 50))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_5, 0, 0, 1, 2)
        self.pelagemEdit = QtWidgets.QLineEdit(parent=self.frame_3)
        self.pelagemEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.pelagemEdit.setObjectName("pelagemEdit")
        self.gridLayout.addWidget(self.pelagemEdit, 3, 1, 1, 1)
        self.salvarAnimalpushButton = QtWidgets.QPushButton(parent=self.frame_3)
        self.salvarAnimalpushButton.setObjectName("salvarAnimalpushButton")
        self.gridLayout.addWidget(self.salvarAnimalpushButton, 7, 0, 1, 2)
        self.horizontalLayout_7.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_4.setMinimumSize(QtCore.QSize(250, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_8 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_10.addWidget(self.label_8)
        self.nomeTerceiroEdit = QtWidgets.QLineEdit(parent=self.frame_4)
        self.nomeTerceiroEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.nomeTerceiroEdit.setObjectName("nomeTerceiroEdit")
        self.verticalLayout_10.addWidget(self.nomeTerceiroEdit)
        self.contatoTerceiroEdit = QtWidgets.QLineEdit(parent=self.frame_4)
        self.contatoTerceiroEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.contatoTerceiroEdit.setObjectName("contatoTerceiroEdit")
        self.verticalLayout_10.addWidget(self.contatoTerceiroEdit)
        self.cidadeTerceiroEdit = QtWidgets.QLineEdit(parent=self.frame_4)
        self.cidadeTerceiroEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.cidadeTerceiroEdit.setObjectName("cidadeTerceiroEdit")
        self.verticalLayout_10.addWidget(self.cidadeTerceiroEdit)
        self.cpfTerceiro = QtWidgets.QLineEdit(parent=self.frame_4)
        self.cpfTerceiro.setStyleSheet("color: rgb(255, 255, 255);")
        self.cpfTerceiro.setObjectName("cpfTerceiro")
        self.verticalLayout_10.addWidget(self.cpfTerceiro)
        self.observacoesTerceiroEdit = QtWidgets.QTextEdit(parent=self.frame_4)
        self.observacoesTerceiroEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.observacoesTerceiroEdit.setObjectName("observacoesTerceiroEdit")
        self.verticalLayout_10.addWidget(self.observacoesTerceiroEdit)
        self.SalvarTerceiropushButton = QtWidgets.QPushButton(parent=self.frame_4)
        self.SalvarTerceiropushButton.setObjectName("SalvarTerceiropushButton")
        self.verticalLayout_10.addWidget(self.SalvarTerceiropushButton)
        self.horizontalLayout_7.addWidget(self.frame_4)
        self.verticalLayout_5.addWidget(self.frame_2)
        self.stackedWidget.addWidget(self.settings_page)
        self.busca = QtWidgets.QWidget()
        self.busca.setObjectName("busca")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.busca)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_6 = QtWidgets.QFrame(parent=self.busca)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame = QtWidgets.QFrame(parent=self.frame_6)
        self.frame.setGeometry(QtCore.QRect(90, 80, 415, 252))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.criterioDeBuscaComboBox = QtWidgets.QComboBox(parent=self.frame)
        self.criterioDeBuscaComboBox.setObjectName("criterioDeBuscaComboBox")
        self.gridLayout_3.addWidget(self.criterioDeBuscaComboBox, 0, 0, 1, 1)
        self.buscaDeAnimallineEdit = QtWidgets.QLineEdit(parent=self.frame)
        self.buscaDeAnimallineEdit.setObjectName("buscaDeAnimallineEdit")
        self.gridLayout_3.addWidget(self.buscaDeAnimallineEdit, 0, 1, 1, 1)
        self.buscarAnimalpushButton = QtWidgets.QPushButton(parent=self.frame)
        self.buscarAnimalpushButton.setObjectName("buscarAnimalpushButton")
        self.gridLayout_3.addWidget(self.buscarAnimalpushButton, 0, 2, 1, 1)
        self.buscaDeAnimaltableWidget = QtWidgets.QTableWidget(parent=self.frame)
        self.buscaDeAnimaltableWidget.setStyleSheet("color: rgb(255, 255, 255);")
        self.buscaDeAnimaltableWidget.setObjectName("buscaDeAnimaltableWidget")
        self.buscaDeAnimaltableWidget.setColumnCount(0)
        self.buscaDeAnimaltableWidget.setRowCount(0)
        self.gridLayout_3.addWidget(self.buscaDeAnimaltableWidget, 1, 0, 1, 3)
        self.frame_7 = QtWidgets.QFrame(parent=self.frame_6)
        self.frame_7.setGeometry(QtCore.QRect(520, 50, 371, 441))
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.frame_7)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 340, 105, 34))
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_12.addWidget(self.frame_6)
        self.stackedWidget.addWidget(self.busca)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.center_main_items)
        self.verticalLayout.addWidget(self.main_body)
        self.main_footer = QtWidgets.QFrame(parent=self.centralwidget)
        self.main_footer.setMinimumSize(QtCore.QSize(0, 50))
        self.main_footer.setMaximumSize(QtCore.QSize(16777215, 30))
        self.main_footer.setStyleSheet("QFrame{\n"
"    background-color: rgb(0, 0, 0);\n"
"    border-top-color: solid 1px  rgb(0, 0, 0);\n"
"}\n"
"QLabel{\n"
"    color: #fff;\n"
"}")
        self.main_footer.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.main_footer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main_footer.setObjectName("main_footer")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.main_footer)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(parent=self.main_footer)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.size_grip = QtWidgets.QFrame(parent=self.main_footer)
        self.size_grip.setMinimumSize(QtCore.QSize(20, 20))
        self.size_grip.setMaximumSize(QtCore.QSize(20, 20))
        self.size_grip.setStyleSheet("")
        self.size_grip.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.size_grip.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.size_grip.setObjectName("size_grip")
        self.horizontalLayout_6.addWidget(self.size_grip, 0, QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignBottom)
        self.verticalLayout.addWidget(self.main_footer)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "Sistema Gerenciador"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.login_response_msg.setText(_translate("MainWindow", "Login Response Msg"))
        self.login_res_ok_btn.setText(_translate("MainWindow", "Ok"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.label_5.setText(_translate("MainWindow", "Password"))
        self.password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.keep_me_logged.setText(_translate("MainWindow", "Keep me logged in"))
        self.login_btn.setText(_translate("MainWindow", "Login"))
        self.codChipEdit.setPlaceholderText(_translate("MainWindow", "Codigo do Chip"))
        self.cpfProprietario.setPlaceholderText(_translate("MainWindow", "CPF do Criador"))
        self.tipoSangueEdit.setPlaceholderText(_translate("MainWindow", "Tipo Sanguineo"))
        self.codChipMaeEdit.setPlaceholderText(_translate("MainWindow", "Codigo do Chip Mae"))
        self.nomeEdit.setPlaceholderText(_translate("MainWindow", "Nome do Animal"))
        self.nascimentoEdit.setPlaceholderText(_translate("MainWindow", "Nascimento"))
        self.precoVendaEdit.setPlaceholderText(_translate("MainWindow", "Preço de Venda"))
        self.codChipPaiEdit.setPlaceholderText(_translate("MainWindow", "Codigo do Chip Pai"))
        self.cpfCriadorEdit.setPlaceholderText(_translate("MainWindow", "CPF do Criador"))
        self.precoCompraEdit.setPlaceholderText(_translate("MainWindow", "Preço de Compra"))
        self.label_3.setText(_translate("MainWindow", "Cadastrar Novo Animal"))
        self.pelagemEdit.setPlaceholderText(_translate("MainWindow", "Pelagem"))
        self.salvarAnimalpushButton.setText(_translate("MainWindow", "PushButton"))
        self.label_8.setText(_translate("MainWindow", "Cadastrar Novo Terceiro"))
        self.nomeTerceiroEdit.setPlaceholderText(_translate("MainWindow", "Nome Completo"))
        self.contatoTerceiroEdit.setPlaceholderText(_translate("MainWindow", "Contatos"))
        self.cidadeTerceiroEdit.setPlaceholderText(_translate("MainWindow", "Cidade"))
        self.cpfTerceiro.setPlaceholderText(_translate("MainWindow", "CPF "))
        self.observacoesTerceiroEdit.setPlaceholderText(_translate("MainWindow", "Observações Gerais"))
        self.SalvarTerceiropushButton.setText(_translate("MainWindow", "PushButton"))
        self.criterioDeBuscaComboBox.setPlaceholderText(_translate("MainWindow", "Criterio"))
        self.buscarAnimalpushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.label_7.setText(_translate("MainWindow", "v 1.0"))
        
        
        self.salvarAnimalpushButton.clicked.connect(self.salvarAnimais)
        self.SalvarTerceiropushButton.clicked.connect(self.salvarTerceiro)
        self.buscarAnimalpushButton.clicked.connect(self.resultadoBuscaAnimais)
        self.buscaDeAnimaltableWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.buscaDeAnimaltableWidget.customContextMenuRequested.connect(self.rigthClickBuscaAnimais)

    def goToAnimaisCadastro(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def goToRelatorios(self):
        self.stackedWidget.setCurrentIndex(3)

    def goToConfiguracoes(self):
        self.stackedWidget.setCurrentIndex(1)

    def salvarAnimais(self):
        print("Salvando novo Animal")

        saveCommandSql =f'''INSERT INTO animais_data (codChip, nomeAnimal, nascimento, CodChipMae, codChipPai, pelagem, preco_compra, preco_venda, cpfProprietario, cpfCriador, tipoSanquineo ) VALUES ( '{self.codChipEdit.text()}' , '{self.nomeEdit.text()}', '{self.nascimentoEdit.text()}', '{self.codChipMaeEdit.text()}, {self.codChipPaiEdit.text()}, {self.pelagemEdit.text()}, {self.precoCompraEdit.text()}, {self.precoVendaEdit.text()}', '{self.cpfProprietario.text()}', '{self.cpfCriadorEdit.text()}', '{self.tipoSangueEdit.text()}')'''
        print(( {self.codChipEdit.text()} , {self.nomeEdit.text()}, {self.nascimentoEdit.text()}, {self.codChipMaeEdit.text()}, {self.codChipPaiEdit.text()}, {self.pelagemEdit.text()}, {self.precoCompraEdit.text()}, {self.precoVendaEdit.text()}, {self.cpfProprietario.text()}, {self.cpfCriadorEdit.text()}, {self.tipoSangueEdit.text()}))
        try:
            print(self.mainDatabasePath)
            connection = sqlite3.connect(self.mainDatabasePath)
            cursor = connection.cursor()
            cursor.execute(saveCommandSql)
            connection.commit()
            connection.close()
            
        except sqlite3.Error as e:
            print(str(e))
    
    def salvarTerceiro(self):
        print("Salvando Terceiro")
        saveCommandSql =f'''INSERT INTO terceiros_data (cpfTerceiro, nomeTerceiro, contatoTerceiro, cidadeTerceiro, observacaoTerceiro ) VALUES ('{self.cpfTerceiroEdit.text()}', '{self.nomeTerceiroEdit.text()}', '{self.contatoTerceiroEdit.text()}','{self.cidadeTerceiroEdit.text()}', '{self.observacoesTerceiroEdit.toPlainText()}')'''
        print({self.cpfTerceiroEdit.text()}, {self.nomeTerceiroEdit.text()}, {self.contatoTerceiroEdit.text()}, {self.cidadeTerceiroEdit.text()}, {self.observacoesTerceiroEdit.toPlainText()})
        try:
            print(self.mainDatabasePath)
            connection = sqlite3.connect(self.mainDatabasePath)
            cursor = connection.cursor()
            cursor.execute(saveCommandSql)
            connection.commit()
            connection.close()
            
        except sqlite3.Error as e:
            print(str(e))

    def resultadoBuscaAnimais(self):
        termo = self.buscaDeAnimallineEdit.text()
        buscasql =f'''SELECT codChip, nomeAnimal FROM animais_data WHERE  cpfProprietario ="{termo}"'''
        try:
            connection = sqlite3.connect(self.mainDatabasePath)
            cursor = connection.cursor()
            cursor.execute(buscasql)
            connection.commit()
            rows = cursor.fetchall()
            connection.close()
            self.buscaDeAnimaltableWidget.setRowCount(10)  # Set the number of rows as needed
            self.buscaDeAnimaltableWidget.setColumnCount(2)

            # Set the column headers (optional)
            self.buscaDeAnimaltableWidget.setHorizontalHeaderLabels(["codChip", "Nome"])
            # Populate the QTableWidget with data
            for row_number, row_data in enumerate(rows):
                self.buscaDeAnimaltableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    item = QtWidgets.QTableWidgetItem(str(data))
                    self.buscaDeAnimaltableWidget.setItem(row_number, column_number, item)
        except sqlite3.Error as e:
            print(str(e))

        
    def rigthClickBuscaAnimais(self, event):
        contextMenu = QtWidgets.QMenu(self.buscaDeAnimaltableWidget)
        actionExcluir = QtGui.QAction("Excluir")
        actionAlterar = QtGui.QAction("Alterar")

        actionExcluir.triggered.connect(self.actionExcluir)
        actionAlterar.triggered.connect(self.actionAlterar)

        contextMenu.addAction(actionExcluir)
        contextMenu.addAction(actionAlterar)

        contextMenu.exec(self.buscaDeAnimaltableWidget.mapToGlobal(QtCore.QPoint(event.x(), event.y())))

    def actionExcluir(self):
        selected_item = self.buscaDeAnimaltableWidget.selectedItems()
        if selected_item:
            row = selected_item[0].row()
            chipCodeAnimal = self.buscaDeAnimaltableWidget.item(row, 1).text()
            #colocar mensage box para que usuario confire a exclusão do animal
            connection = sqlite3.connect(self.mainDatabasePath)
            cursor = connection.cursor()
            sqlcommand = f'''DELETE FROM animais_data WHERE codChip = "{chipCodeAnimal}"'''
            cursor.execute(sqlcommand)
            connection.close()
            print("Animal excluido permanetemente!")

        print("Exclui dado")

    def actionAlterar(self):
        print("Vai para alterar Dado")
    

