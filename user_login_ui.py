import sys


from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget, QLayout, QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, \
    QMessageBox,QMainWindow,QStackedWidget


class LoginPage(QWidget):

    def __init__(self):
        super().__init__()

        self.setupLoginPage()

    def setupLoginPage(self):
        self.verticalLayoutLogin = QVBoxLayout()
        self.verticalLayoutLogin.addStretch(100)
        self.verticalLayoutLogin.setContentsMargins(10, 10, 10, 10)
        self.verticalLayoutLogin.setSpacing(10)
        self.verticalLayoutLogin.setObjectName("verticalLayoutLogin")


        self.horizontalLayout_username = QHBoxLayout()
        self.horizontalLayout_username.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_username.setSpacing(10)
        self.horizontalLayout_username.setObjectName("horizontalLayout_username")
        self.horizontalLayout_username.addStretch(100)

        self.label_username_or_email = QLabel("Kullanıcı Adı veya Email:")
        self.label_username_or_email.setStyleSheet("background-color: rgb(169, 169, 169);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_username_or_email.setObjectName("label_username_or_email")

        self.horizontalLayout_username.addWidget(self.label_username_or_email)

        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setStyleSheet(
            "background-color: rgb(169, 169, 169);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.lineEdit_username.setObjectName("lineEdit_username")

        self.horizontalLayout_username.addWidget(self.lineEdit_username)
        self.horizontalLayout_username.addStretch(100)

        self.verticalLayoutLogin.addLayout(self.horizontalLayout_username)



        self.horizontalLayout_password = QHBoxLayout()
        self.horizontalLayout_password.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_password.setSpacing(10)
        self.horizontalLayout_password.setObjectName("horizontalLayout_password")
        self.horizontalLayout_password.addStretch(100)

        self.label_password = QLabel("Şifre:")
        self.label_password.setStyleSheet("background-color: rgb(169, 169, 169);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_password.setObjectName("label_password")

        self.horizontalLayout_password.addWidget(self.label_password)

        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setStyleSheet(
            "background-color: rgb(169, 169, 169);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_password.setObjectName("label_password")

        self.horizontalLayout_password.addWidget(self.lineEdit_password)
        self.horizontalLayout_password.addStretch(100)

        self.verticalLayoutLogin.addLayout(self.horizontalLayout_password)

        self.horizontalLayout_login_signup = QHBoxLayout()
        self.horizontalLayout_login_signup.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_login_signup.setSpacing(10)
        self.horizontalLayout_login_signup.setObjectName("horizontalLayout_login_signin")
        self.horizontalLayout_login_signup.addStretch(100)

        self.pushButton_login = QPushButton("Giriş Yap")
        self.pushButton_login.setStyleSheet(
            "background-color: rgb(47, 79, 79);\n""color:rgb(255,255,255);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.pushButton_login.setObjectName("pushButton_login")

        self.horizontalLayout_login_signup.addWidget(self.pushButton_login)

        self.pushButton_signup = QPushButton("Üye Ol")
        self.pushButton_signup.setStyleSheet(
            "background-color: rgb(47, 79, 79);\n""color:rgb(255,255,255);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.pushButton_signup.setObjectName("pushButton_signup")

        self.horizontalLayout_login_signup.addWidget(self.pushButton_signup)
        self.horizontalLayout_login_signup.addStretch(100)

        self.verticalLayoutLogin.addLayout(self.horizontalLayout_login_signup)
        self.verticalLayoutLogin.addStretch(100)

        self.setLayout(self.verticalLayoutLogin)
        




if __name__=="__main__":

    app=QApplication(sys.argv)

    window=LoginPage()

    window.show()

    sys.exit(app.exec_())