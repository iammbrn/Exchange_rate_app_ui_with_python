
import os

import sqlite3

import sys

from update_User_Informations import *

from web_currents_data import Currency_Convert

from delete_my_account import *

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, \
    QMainWindow, QAction, QLabel, QComboBox,QRadioButton, QFileDialog,qApp,QMenu,QMessageBox,QCheckBox


class MainPage(QWidget):

    def __init__(self):

        super().__init__()

        self.setupMainPage()
    def setupMainPage(self):

        self.verticalLayout_Main = QVBoxLayout()
        self.verticalLayout_Main.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_Main.setSpacing(10)
        self.verticalLayout_Main.setObjectName("verticalLayout_Main")

        self.horizontalLayout_amount = QHBoxLayout()
        self.horizontalLayout_amount.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_amount.setSpacing(10)
        self.horizontalLayout_amount.setObjectName("horizontalLayout_amount")

        self.label_amount = QLabel("Dönüştürmek istediğiniz miktarı girin:")
        self.label_amount.setStyleSheet("background-color: rgb(169, 169, 169);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_amount.setObjectName("label_amount")
        self.horizontalLayout_amount.addWidget(self.label_amount)

        self.lineEdit_amount = QLineEdit()
        self.lineEdit_amount.setStyleSheet("background-color: rgb(169, 169, 169);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.lineEdit_amount.setObjectName("lineEdit_amount")
        self.horizontalLayout_amount.addWidget(self.lineEdit_amount)

        self.verticalLayout_Main.addLayout(self.horizontalLayout_amount)

        self.horizontalLayout_Fist_Currency = QHBoxLayout()
        self.horizontalLayout_Fist_Currency.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_Fist_Currency.setSpacing(10)
        self.horizontalLayout_Fist_Currency.setObjectName("horizontalLayout_Fist_Currency")

        self.label_First_Currency = QLabel("Dönüştürülecek para birimini girin:")
        self.label_First_Currency.setStyleSheet("background-color: rgb(169, 169, 169);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_First_Currency.setObjectName("label_First_Currency")

        self.horizontalLayout_Fist_Currency.addWidget(self.label_First_Currency)

        self.comboBox_First_Currency = QComboBox()
        self.comboBox_First_Currency.setStyleSheet("background-color: rgb(47, 79, 79);\n""color:rgb(255,255,255);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.comboBox_First_Currency.setObjectName("comboBox_First_Currency")
        self.comboBox_First_Currency.addItem("TRY", "Turk Lirasi")
        self.comboBox_First_Currency.addItem("GBP", "Ingiliz Sterlini")
        self.comboBox_First_Currency.addItem("EUR", "Euro")
        self.comboBox_First_Currency.addItem("USD", "Amerikan Dolari")


        self.horizontalLayout_Fist_Currency.addWidget(self.comboBox_First_Currency)

        self.lineEdit_First_Currency = QLineEdit()
        self.lineEdit_First_Currency.setStyleSheet("background-color: rgb(169, 169, 169);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.lineEdit_First_Currency.setObjectName("lineEdit_First_Currency")

        self.horizontalLayout_Fist_Currency.addWidget(self.lineEdit_First_Currency)
        self.verticalLayout_Main.addLayout(self.horizontalLayout_Fist_Currency)

        self.horizontalLayout_Second_Currency = QHBoxLayout()
        self.horizontalLayout_Second_Currency.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_Second_Currency.setSpacing(10)
        self.horizontalLayout_Second_Currency.setObjectName("horizontalLayout_Second_Currency")

        self.label_Second_Currency = QLabel("Dönüştürülecek para birimini girin:")
        self.label_Second_Currency.setStyleSheet("background-color: rgb(169, 169, 169);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_Second_Currency.setObjectName("label_Second_Currency")

        self.horizontalLayout_Second_Currency.addWidget(self.label_Second_Currency)

        self.comboBox_Second_Currency = QComboBox()
        self.comboBox_Second_Currency.setStyleSheet("background-color: rgb(47, 79, 79);\n""color:rgb(255,255,255);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.comboBox_Second_Currency.setObjectName("comboBox_Second_Currency")
        self.comboBox_Second_Currency.addItem("EUR", "Euro")
        self.comboBox_Second_Currency.addItem("TRY", "Turk Lirasi")
        self.comboBox_Second_Currency.addItem("GBP", "Ingiliz Sterlini")
        self.comboBox_Second_Currency.addItem("USD", "Amerikan Dolari")



        self.horizontalLayout_Second_Currency.addWidget(self.comboBox_Second_Currency)

        self.lineEdit_Second_Currency = QLineEdit()
        self.lineEdit_Second_Currency.setStyleSheet("background-color: rgb(169, 169, 169);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.lineEdit_Second_Currency.setObjectName("lineEdit_Second_Currency")

        self.horizontalLayout_Second_Currency.addWidget(self.lineEdit_Second_Currency)
        self.verticalLayout_Main.addLayout(self.horizontalLayout_Second_Currency)

        self.pushButton_Convert = QPushButton("Dönüştür")
        self.pushButton_Convert.setStyleSheet("background-color: rgb(47, 79, 79);\n""color:rgb(255,255,255);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.pushButton_Convert.setObjectName("pushButton_Convert")

        self.verticalLayout_Main.addWidget(self.pushButton_Convert)

        self.label_Select = QLabel("Aşağıdaki veilen butonlara tıklayarak seçtiğiniz döviz kurunun diğer dövizlere karşı değerini bulabilirsiniz.")
        self.label_Select.setStyleSheet("background-color: rgb(169, 169, 169);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_Select.setObjectName("label")

        self.verticalLayout_Main.addWidget(self.label_Select)

        self.checkBox_First_Currency = QCheckBox( "1. Döviz ")
        self.checkBox_First_Currency.setStyleSheet("background-color: rgb(169, 169, 169);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.checkBox_First_Currency.setObjectName("checkBox_First_Currency")

        self.verticalLayout_Main.addWidget(self.checkBox_First_Currency)

        self.checkBox_Second_Currency =QCheckBox("2. Döviz")
        self.checkBox_Second_Currency.setStyleSheet("background-color: rgb(169, 169, 169);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.checkBox_Second_Currency.setObjectName("checkBox_Second_Currency")

        self.verticalLayout_Main.addWidget(self.checkBox_Second_Currency)

        self.pushButton_All_Convert = QPushButton("Tüm Döviz Değerlerini Bul")
        self.pushButton_All_Convert.setStyleSheet("background-color: rgb(47, 79, 79);\n""color:rgb(255,255,255);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.pushButton_All_Convert.setObjectName("pushButton_All_Convert")

        self.verticalLayout_Main.addWidget(self.pushButton_All_Convert)

        self.textEdit_All_Currenies = QTextEdit()
        self.textEdit_All_Currenies.setStyleSheet("background-color: rgb(169, 169, 169);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.textEdit_All_Currenies.setObjectName("textEdit_All_Currenies")

        self.verticalLayout_Main.addWidget(self.textEdit_All_Currenies)



        self.setLayout(self.verticalLayout_Main)

        self.pushButton_Convert.clicked.connect(lambda : self.convert(self.lineEdit_amount.text(),self.lineEdit_First_Currency.text(),self.lineEdit_Second_Currency.text(),self.textEdit_All_Currenies))

        self.pushButton_All_Convert.clicked.connect(lambda : self.convertAll(self.lineEdit_amount.text(),self.lineEdit_First_Currency.text(),self.lineEdit_Second_Currency.text(),self.checkBox_First_Currency.isChecked(),self.checkBox_Second_Currency.isChecked(),self.textEdit_All_Currenies))

        self.comboBox_First_Currency.currentTextChanged.connect(self.selectCombo_box1)
        self.comboBox_Second_Currency.currentTextChanged.connect(self.selectCombo_box2)

        self.setGeometry(100,100,640,480)


    def convert(self,amount,firstCurrency,secondCurrency,answer):
        calculate = Currency_Convert()

        if amount and firstCurrency and secondCurrency:
            result=calculate.first_Second_Convert(amount, firstCurrency, secondCurrency)
            answer.setText(f"{result}")

        elif not amount:
            QMessageBox.information(self,"Uyarı!","Lütfen miktar bilgisini girin.")
        elif not firstCurrency:
            QMessageBox.information(self,"Uyarı!","Lütfen ilk para birimi bilgisini girin.")
        elif not secondCurrency:
            QMessageBox.information(self,"Uyarı!","Lütfen ikinci para birimi bilgisini girin.")
        else:
            QMessageBox.information(self,"Uyarı!","Birden fazla eksik bilgi, lütfen eksik bilgileri girin.")
    def convertAll(self,amount,first_currency,second_currency,first_curr_Checkbox,second_curr_Checkbox,answer):
        calculate = Currency_Convert()
        answer.clear()
        if first_curr_Checkbox and second_curr_Checkbox:
            for values in calculate.first_All_Convert(amount, first_currency,second_currency):

                answer.append(f"{values[0]}, {values[1]} ={values[2]}\n")

        elif first_curr_Checkbox:

            for values in calculate.first_All_Convert(amount,first_currency,None):

                answer.append(f"{values[0]}, {values[1]} ={values[2]}\n")

        elif second_curr_Checkbox:

            for values in calculate.first_All_Convert(amount,None,second_currency):

                answer.append(f"{values[0]}, {values[1]} ={values[2]}\n")
        else:
            QMessageBox.information(self,"Uyarı!","Lütfen yukarıda verilen kutucuklarda, hangi döviz kurunu dönüştürmek istediğinizi seçin.")

    def open_file(self):
        file_name,_=QFileDialog.getOpenFileName(self,"Open File",os.getenv("Desktop"))

        if file_name:
            with open(file_name,"r",encoding="utf-8") as file:
                self.textEdit_All_Currenies.setText(file.read())

    def save_file(self):
        file_name, _= QFileDialog.getSaveFileName(self, "Save File", os.getenv("HOME"))

        if file_name:
            with open(file_name, "w", encoding="utf-8") as file1:
                file1.write(self.textEdit_All_Currenies.toPlainText())

    def clean_file(self):
        self.textEdit_All_Currenies.setText("")


    def help_window(self,help_action):
        dictionary={
            'user_guide': "Döviz Arayüzü Kullanım Kılavuzu \n\n\
            Döviz Kuru Görüntüleme:\n\
            Uygulamayı başlattığınızda, güncel döviz kurları ana ekranda otomatik olarak görüntülenir.\n\
            Ana ekranda, belirli bir para biriminin alış ve satış fiyatlarını görmek için ilgili para birimine tıklayabilirsiniz.\n\
            Döviz Dönüştürme:\n\
            Döviz dönüştürme işlemi yapmak için, sol üst köşedeki 'Dönüştür' butonuna tıklayın.\n\
            Açılan pencerede, dönüştürmek istediğiniz miktarı girin ve dönüştürmek istediğiniz para birimlerini seçin.\n\
            'Dönüştür' butonuna tıkladıktan sonra, dönüştürülmüş miktar hemen altında görüntülenir.\n\
            Tüm Döviz Değerlerini Görüntüleme:\n\
            Tüm döviz değerlerini görmek için, 'Tüm Döviz Değerlerini Bul' butonuna tıklayın.\n\
            Açılan pencerede, dönüştürmek istediğiniz miktarı ve dönüştürme yapmak istediğiniz para birimini seçin.\n\
            'Tamam' butonuna tıkladıktan sonra, seçilen para birimlerinin diğer tüm dövizlere karşı değerleri görüntülenir.\n\
            Mod Seçenekleri:\n\
            Sağ üst köşedeki 'Ayarlar' menüsünden farklı modları seçebilirsiniz:\n\
            'Normal Mod': Arayüzü varsayılan temaya geri döndürür.\n\
            'Gece Modu': Arayüzü karanlık bir temaya dönüştürür.\n\
            'Okuma Modu': Arayüzü okuma dostu bir tema ile görüntüler.\n\
            Profil Ayarları:\n\
            Sağ üst köşedeki kullanıcı adınıza tıklayarak profil ayarlarına erişebilirsiniz.\n\
            Profil bilgilerinizi güncellemek veya hesabınızı silmek için uygun menü seçeneklerini kullanın.\n\
            Uygulamayı kullanırken herhangi bir sorunla karşılaşırsanız veya daha fazla yardıma ihtiyacınız olursa, 'Yardım' menüsündeki seçenekleri kullanarak destek alabilirsiniz.",

            'about' : "Hakkında \n\n\
            Döviz Arayüzü, kullanıcıların anlık döviz kurlarını izlemelerine ve dönüştürmelerine olanak tanıyan kullanıcı dostu bir uygulamadır. Bu uygulama, güncel döviz kurlarını çevrimiçi olarak alır ve kullanıcıların seçtikleri para birimleri arasında dönüşümler yapmalarını sağlar.\n\
            Uygulama, kolay kullanılabilir arayüzü sayesinde hızlı bir şekilde döviz kurlarını görmek ve istenen döviz miktarlarını dönüştürmek için tasarlanmıştır. Ayrıca, kullanıcıların tercihlerine göre farklı döviz kurları arasında dönüşümler yapmalarını sağlayan özelleştirilebilir seçenekler sunar.\n\
            Döviz Arayüzü, güncel ve doğru döviz kuru bilgilerine erişim sağlayarak kullanıcıların döviz işlemlerini kolaylaştırır. Hızlı, güvenilir ve kullanıcı odaklı bir deneyim sunar.",

            'frequently_asked_questions': "Sıkça Sorulan Sorular \n\n\
            Döviz Kurları Nasıl Güncellenir?\n\
            Döviz kurları otomatik olarak güncellenir ve her açılışta en son verileri görüntüler. Ancak, güncellemeyi manuel olarak yapmak için 'Güncelle' veya benzeri bir butona tıklayabilirsiniz.\n\
            Döviz Dönüştürme İşlemi Nasıl Yapılır?\n\
            Döviz dönüştürme işlemi yapmak için, ana ekranda bulunan 'Dönüştür' butonuna tıklayın. Ardından, miktarı ve dönüştürmek istediğiniz para birimlerini seçin ve 'Dönüştür'e tıklayın.\n\
            Tüm Döviz Değerlerini Nasıl Görebilirim?\n\
            Tüm döviz değerlerini görmek için, 'Tüm Döviz Değerlerini Bul' butonuna tıklayın. Daha sonra, dönüştürmek istediğiniz miktarı ve para birimini seçin ve 'Tamam'ı tıklayın.\n\
            Modları Nasıl Değiştirebilirim?\n\
            Sağ üst köşedeki 'Ayarlar' menüsünden farklı modları seçebilirsiniz. 'Normal Mod', 'Gece Modu' ve 'Okuma Modu' arasında geçiş yapabilirsiniz.\n\
            Profil Bilgilerimi Nasıl Güncellerim?\n\
            Sağ üst köşedeki kullanıcı adınıza tıklayarak profil ayarlarına erişebilirsiniz. Profil bilgilerinizi güncellemek veya hesabınızı silmek için uygun menü seçeneklerini kullanın.\n\
            Yardım ve Destek İçin Nereye Başvurabilirim?\n\
            Herhangi bir sorunuz veya sorununuz varsa, 'Yardım' menüsündeki seçenekleri kullanarak destek alabilirsiniz."}

        if help_action.text() == "Kullanım Kılavuzu":
            self.textEdit_All_Currenies.setText(f"{dictionary['user_guide']}")

        elif help_action.text() == "Hakkında":
            self.textEdit_All_Currenies.setText(f"{dictionary['about']}")
        elif help_action.text() == "Sıkça Sorulan Sorular":
            self.textEdit_All_Currenies.setText(f"{dictionary['frequently_asked_questions']}")

    def selectCombo_box1(self,text):

        self.lineEdit_First_Currency.setText(text)

    def selectCombo_box2(self,text):

        self.lineEdit_Second_Currency.setText(text)






class Menu(QMainWindow):

    def __init__(self,username):

        super().__init__()

        self.window= MainPage()

        self.setCentralWidget(self.window)

        self.setWindowTitle("ALDEBARAN Döviz")
        self.setStyleSheet("background-color: rgb(173, 216, 230);")

        self.createMenu(username)
        self.username=username

    def createMenu(self,username):

        self.menubar = self.menuBar()

        self.menubar.setStyleSheet("background-color: rgb(173, 216, 230);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.menubar.setObjectName("menubar")


        self.menuName = self.menubar.addMenu(f"{username}")
        self.menuName.setStyleSheet("background-color: rgb(255, 255, 255);\n""font: 75 10pt \"MS Shell Dlg 2\";")
        self.menuName.setObjectName("menuName")

        self.menuSettings = self.menubar.addMenu("Ayarlar")
        self.menuSettings.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.menuSettings.setObjectName("menuSettings")

        self.menuFile = self.menubar.addMenu("Dosya")
        self.menuFile.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.menuFile.setObjectName("menuFile")

        self.menuView = self.menubar.addMenu("Görünüm")
        self.menuView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.menuView.setObjectName("menuView")

        self.menuTheme = QMenu("Tema") # Alt menu oluşturduk.
        self.menuTheme.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.menuTheme.setObjectName("menuTheme")

        self.menuHelp = self.menubar.addMenu("Yardım")
        self.menuHelp.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.menuHelp.setObjectName("menuHelp")


        self.actionUpdate_Profile_Information=QAction("Profil Bilgilerini Güncelle",self)
        self.actionUpdate_Profile_Information.setObjectName("actionUpdate_Profile_Information")

        self.actionView_Profile_Information=QAction("Profil Bilgilerini Görüntüle",self)
        self.actionView_Profile_Information.setObjectName("actionView_Profile_Information")

        self.actionDelete_My_Account =QAction("Hesabımı Sil",self)
        self.actionDelete_My_Account.setObjectName("actionDelete_My_Account")

        self.actionLogOut = QAction("Çıkış Yap",self)
        self.actionLogOut.setObjectName("actionLogOut")
        self.grabShortcut("Ctrl+Q")

        self.actionSave_File = QAction("Dosya Kaydet",self)
        self.actionSave_File.setObjectName("actionSave_File")
        self.actionSave_File.setShortcut("Ctrl+S")

        self.actionOpen_File = QAction("Dosya Aç",self)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionOpen_File.setShortcut("Ctrl+O")

        self.actionReading_Mode = QAction("Okuma Modu",self)
        self.actionReading_Mode.setObjectName("actionReading_Mode")
        self.actionReading_Mode.setShortcut("Ctrl+R")

        self.actionNight_Mode = QAction("Gece Modu",self)
        self.actionNight_Mode.setObjectName("actionNight_Mode")
        self.actionNight_Mode.setShortcut("Ctrl+N")

        self.actionNormal_Mode = QAction("Normal Mod",self)
        self.actionNormal_Mode.setShortcut("Ctrl+N+N")
        self.actionNormal_Mode.setObjectName("actionNormal_Mode")

        self.actionUser_Guide = QAction("Kullanım Kılavuzu",self)
        self.actionUser_Guide.setObjectName("actionUser_Guide")

        self.actionAbout = QAction("Hakkında",self)
        self.actionAbout.setObjectName("actionAbout")

        self.actionFrequently_Asked_Questions = QAction("Sıkça Sorulan Sorular",self)
        self.actionFrequently_Asked_Questions.setObjectName("actionFrequently_Asked_Questions")

        self.actionClean = QAction("Temizle",self)
        self.actionClean.setObjectName("actionClean")
        self.actionClean.setShortcut("Ctrl+D")

        self.menuSettings.addAction(self.actionUpdate_Profile_Information)
        self.menuSettings.addAction(self.actionView_Profile_Information)
        self.menuSettings.addAction(self.actionDelete_My_Account)
        self.menuSettings.addAction(self.actionLogOut)

        self.menuFile.addAction(self.actionSave_File)
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionClean)

        self.menuTheme.addAction(self.actionNormal_Mode)
        self.menuTheme.addAction(self.actionNight_Mode)
        self.menuTheme.addAction(self.actionReading_Mode)

        self.menuView.addAction(self.menuTheme.menuAction())

        self.menuHelp.addAction(self.actionUser_Guide)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionFrequently_Asked_Questions)

        self.menuFile.triggered.connect(self.file)

        self.actionNormal_Mode.triggered.connect(self.view)
        self.actionNight_Mode.triggered.connect(self.view)
        self.actionReading_Mode.triggered.connect(self.view)

        self.actionUpdate_Profile_Information.triggered.connect(self.updateUser)
        self.actionView_Profile_Information.triggered.connect(self.settings)
        self.actionDelete_My_Account.triggered.connect(self.settings)
        self.actionLogOut.triggered.connect(self.settings)

        self.menuHelp.triggered.connect(self.help)




    def file(self,action):

        if(action.text()=="Dosya Aç"):
            self.window.open_file()

        elif(action.text()=="Dosya Kaydet"):

            self.window.save_file()

        elif(action.text()=="Temizle"):

            self.window.clean_file()

    def updateUser(self):

        action=self.sender()

        if action.text() == "Profil Bilgilerini Güncelle":
            self.update=UpdatePage()
            self.setCentralWidget(self.update)

            self.update.pushButton_cancel.clicked.connect(self.returnmainpage)

            self.update.pushButton_update.clicked.connect(self.update_user)

    def update_user(self):

        update = UpdateUserInformations()

        result = update.update_User_Informations(self.username,self.update.lineEdit_name.text(), self.update.lineEdit_surname.text(),self.update.lineEdit_username.text(), self.update.lineEdit_useremail.text(),self.update.lineEdit_password.text())

        if self.update.lineEdit_username.text()!="":
            self.username=self.update.lineEdit_username.text()


        self.menubar.clear()
        self.window=Menu(self.username)
        self.setCentralWidget(self.window)
        QMessageBox.information(self, "Bilgi", result)
    def returnmainpage(self):
        self.menubar.clear()
        self.window=Menu(self.username)
        self.setCentralWidget(self.window)






    def settings(self):

        action=self.sender()

        connect=sqlite3.connect("Database.db")

        cursor=connect.cursor()

        if action.text()=="Profil Bilgilerini Görüntüle":
            connect=sqlite3.connect("Database.db")
            cursor=connect.cursor()

            cursor.execute("Select * From UserData where kullaniciAdi=?",(self.username,))
            user_data=cursor.fetchall()

            if len(user_data)!=0:

                user_data_list = ["Ad:", "Soyad:", "Kullanıcı Adı:", "Email:", "Şifre:"]
                for key,value in zip(user_data_list,user_data[0]):
                    self.window.textEdit_All_Currenies.append(key+str(value))


        elif action.text()=="Hesabımı Sil":
            delete=DeleteAccount()
            delete.delete_My_Account(self.username)
            qApp.quit()

        elif action.text()=="Çıkış Yap":
            qApp.quit()

    def view(self):

        action=self.sender()
        if action.text()=="Normal Mod":
            self.setStyleSheet("background-color: rgb(173, 216, 230);")

        elif action.text()=="Gece Modu":
            self.setStyleSheet("background-color: rgb(0, 0, 0);")

        elif action.text() == "Okuma Modu":
            self.setStyleSheet("background-color: rgb(245,245,220 );")


    def help(self,action):
        self.window.help_window(action)


if __name__ == "__main__":

    app=QApplication(sys.argv)

    window=Menu("Four")

    window.show()

    sys.exit(app.exec_())

