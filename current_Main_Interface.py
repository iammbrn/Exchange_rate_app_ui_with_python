import sys


from PyQt5 import QtWidgets,QtGui

from PyQt5.QtWidgets import QStackedWidget,QMainWindow,QApplication

from user_signup_ui import *

from user_login_ui import *

from main_page_project import *

from update_User_Informations import *

from login import *



class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.window=SignupPage()

        self.stackedWidget=QStackedWidget()

        self.setCentralWidget(self.stackedWidget)


        self.stackedWidget.addWidget(self.window)

        self.stackedWidget.setCurrentWidget(self.window)

        self.window.pushButton_login.clicked.connect(self.openLoginPage)

        self.setGeometry(100,100,640,480)
        self.setStyleSheet("background-color: rgb(173, 216, 230);")
        self.setWindowTitle("Üye Ol")


    def openLoginPage(self):

        self.open_login=LoginPage()

        self.stackedWidget.addWidget(self.open_login)
        self.stackedWidget.setCurrentWidget(self.open_login)
        self.setWindowTitle("Giriş Yap")


        self.open_login.pushButton_login.clicked.connect(self.login)

        self.open_login.pushButton_signup.clicked.connect(self.return_Signup)



    def login(self):
        username = self.open_login.lineEdit_username.text()
        password = self.open_login.lineEdit_password.text()
        self.control = LogIn()

        result = self.control.logIn(username, password)

        if result == "Eksik bilgi!, lütfen bilgilerinizi tekrar kontrol edin.":

            QMessageBox.information(self, "Uyarı!", result)

        elif result == "Yanlış Kullanıcı Adı veya Şifre, lütfen bilgilerinizi tekrar kontrol edin.":

            QMessageBox.information(self, "Uyarı!", result)

        elif result == f"Hoşgeldiniz, {username}":

            self.userMainPage(username, result)



    def userMainPage(self,username,result):

        self.menu = Menu(username)

        self.stackedWidget.addWidget(self.menu)

        self.stackedWidget.setCurrentWidget(self.menu)

        QMessageBox.information(self, "Bilgi", result)

        self.setWindowTitle("ALDEBARAN Döviz")




    def return_Signup(self):
        self.stackedWidget.setCurrentWidget(self.window)
        self.setWindowTitle("Üye Ol")






if __name__ == "__main__":

    app=QApplication(sys.argv)

    window=MainWindow()

    window.show()

    sys.exit(app.exec_())