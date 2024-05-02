import sys
from signup import *

from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QWidget,QLayout,QApplication,QVBoxLayout,QHBoxLayout,QPushButton,QLabel,QLineEdit, QMessageBox,QStackedWidget,QMainWindow


class SignupPage(QWidget):

    def __init__(self):

        super().__init__()

        self.setupSignupPage()


    def setupSignupPage(self):

        self.verticalLayoutLogin = QVBoxLayout()
        self.verticalLayoutLogin.addStretch(100)
        self.verticalLayoutLogin.setContentsMargins(10,10,10,10 )
        self.verticalLayoutLogin.setSpacing(10)
        self.verticalLayoutLogin.setObjectName("verticalLayoutLogin")

        self.horizontalLayout_name = QHBoxLayout()
        self.horizontalLayout_name.setContentsMargins(10,10,10,10)
        self.horizontalLayout_name.setSpacing(10)
        self.horizontalLayout_name.setObjectName("horizontalLayout_name")
        self.horizontalLayout_name.addStretch(100)

        self.label_name = QLabel("Ad:")
        self.label_name.setStyleSheet("background-color: rgb(169, 169, 169);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_name.setObjectName("label_name")

        self.horizontalLayout_name.addWidget(self.label_name)

        self.lineEdit_name = QLineEdit()
        self.lineEdit_name.setStyleSheet("background-color: rgb(169, 169, 169);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.lineEdit_name.setObjectName("lineEdit_name")


        self.horizontalLayout_name.addWidget(self.lineEdit_name)
        self.horizontalLayout_name.addStretch(100)


        self.verticalLayoutLogin.addLayout(self.horizontalLayout_name)

        self.horizontalLayout_surname = QHBoxLayout()
        self.horizontalLayout_surname.setContentsMargins(10,10,10,10)
        self.horizontalLayout_surname.setSpacing(10)
        self.horizontalLayout_surname.setObjectName("horizontalLayout_surname")
        self.horizontalLayout_surname.addStretch(100)

        self.label_surname = QLabel("Soyad:")
        self.label_surname.setStyleSheet("background-color: rgb(169, 169, 169);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_surname.setObjectName("label_surname")

        self.horizontalLayout_surname.addWidget(self.label_surname)

        self.lineEdit_surname = QLineEdit()
        self.lineEdit_surname.setStyleSheet("background-color: rgb(169, 169, 169);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.lineEdit_surname.setObjectName("lineEdit_surname")

        self.horizontalLayout_surname.addWidget(self.lineEdit_surname)
        self.horizontalLayout_surname.addStretch(100)


        self.verticalLayoutLogin.addLayout(self.horizontalLayout_surname)

        self.horizontalLayout_username = QHBoxLayout()
        self.horizontalLayout_username.setContentsMargins(10,10,10,10)
        self.horizontalLayout_username.setSpacing(10)
        self.horizontalLayout_username.setObjectName("horizontalLayout_username")
        self.horizontalLayout_username.addStretch(100)


        self.label_username = QLabel("Kullanıcı Adı:")
        self.label_username.setStyleSheet("background-color: rgb(169, 169, 169);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_username.setObjectName("label_username")

        self.horizontalLayout_username.addWidget(self.label_username)

        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setStyleSheet("background-color: rgb(169, 169, 169);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.lineEdit_username.setObjectName("lineEdit_username")

        self.horizontalLayout_username.addWidget(self.lineEdit_username)
        self.horizontalLayout_username.addStretch(100)


        self.verticalLayoutLogin.addLayout(self.horizontalLayout_username)

        self.horizontalLayout_useremail = QHBoxLayout()
        self.horizontalLayout_useremail.setContentsMargins(10,10,10,10)
        self.horizontalLayout_useremail.setSpacing(10)
        self.horizontalLayout_useremail.setObjectName("horizontalLayout_useremail")
        self.horizontalLayout_useremail.addStretch(100)

        self.label_useremail = QLabel("E-mail:")
        self.label_useremail.setStyleSheet("background-color: rgb(169, 169, 169);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_useremail.setObjectName("label_useremail")

        self.horizontalLayout_useremail.addWidget(self.label_useremail)

        self.lineEdit_useremail = QLineEdit()
        self.lineEdit_useremail.setStyleSheet("background-color: rgb(169, 169, 169);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.lineEdit_useremail.setObjectName("lineEdit_useremail")

        self.horizontalLayout_useremail.addWidget(self.lineEdit_useremail)
        self.horizontalLayout_useremail.addStretch(100)


        self.verticalLayoutLogin.addLayout(self.horizontalLayout_useremail)

        self.horizontalLayout_password=QHBoxLayout()
        self.horizontalLayout_password.setContentsMargins(10,10,10,10)
        self.horizontalLayout_password.setSpacing(10)
        self.horizontalLayout_password.setObjectName("horizontalLayout_password")
        self.horizontalLayout_password.addStretch(100)

        self.label_password=QLabel("Şifre:")
        self.label_password.setStyleSheet("background-color: rgb(169, 169, 169);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_password.setObjectName("label_password")

        self.horizontalLayout_password.addWidget(self.label_password)

        self.lineEdit_password=QLineEdit()
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setStyleSheet("background-color: rgb(169, 169, 169);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_password.setObjectName("label_password")

        self.horizontalLayout_password.addWidget(self.lineEdit_password)
        self.horizontalLayout_password.addStretch(100)


        self.verticalLayoutLogin.addLayout(self.horizontalLayout_password)

        self.horizontalLayout_login_signup = QHBoxLayout()
        self.horizontalLayout_login_signup.setContentsMargins(10,10,10,10)
        self.horizontalLayout_login_signup.setSpacing(10)
        self.horizontalLayout_login_signup.setObjectName("horizontalLayout_login_signin")
        self.horizontalLayout_login_signup.addStretch(100)

        self.pushButton_login = QPushButton("Giriş Yap")
        self.pushButton_login.setStyleSheet("background-color: rgb(47, 79, 79);\n""color:rgb(255,255,255);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.pushButton_login.setObjectName("pushButton_login")

        self.horizontalLayout_login_signup.addWidget(self.pushButton_login)

        self.pushButton_signup = QPushButton("Üye Ol")
        self.pushButton_signup.setStyleSheet("background-color: rgb(47, 79, 79);\n""color:rgb(255,255,255);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.pushButton_signup.setObjectName("pushButton_signup")


        self.horizontalLayout_login_signup.addWidget(self.pushButton_signup)
        self.horizontalLayout_login_signup.addStretch(100)


        self.verticalLayoutLogin.addLayout(self.horizontalLayout_login_signup)
        self.verticalLayoutLogin.addStretch(100)


        self.setLayout(self.verticalLayoutLogin)

        self.pushButton_signup.clicked.connect(self.signup)

        self.setGeometry(100,100,640,480)
        self.setWindowTitle("Üye Ol ")
        self.setStyleSheet("background-color: rgb(173, 216, 230);")



    def signup(self):
        name=self.lineEdit_name.text()
        surname=self.lineEdit_surname.text()
        username=self.lineEdit_username.text()
        email=self.lineEdit_useremail.text()
        password=self.lineEdit_password.text()

        self.createuser=SignUp()

        result=self.createuser.signUp(name, surname, username, email, password)

        QMessageBox.information(self,"Bilgi",result)




if __name__ == "__main__":
    app=QApplication(sys.argv)

    window=SignupPage()

    window.show()

    sys.exit(app.exec_())
