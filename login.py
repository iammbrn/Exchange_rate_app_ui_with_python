import sqlite3

class LogIn():

    def __init__(self):

        self.create_Connect()

    def create_Connect(self):

        self.connect=sqlite3.connect("Database.db")

        self.cursor=self.connect.cursor()

    def logIn(self,username,password):

        self.cursor.execute("Select kullaniciAdi,sifre From UserData where (kullaniciAdi=? or email=?) and sifre=?",(username,username,password))
        user_data=self.cursor.fetchall()

        if username and password:
            if len(user_data)==0:
                return "Yanlış Kullanıcı Adı veya Şifre, lütfen bilgilerinizi tekrar kontrol edin."
            else:
                return f"Hoşgeldiniz, {username}"

        else:
            return "Eksik bilgi!, lütfen bilgilerinizi tekrar kontrol edin."


    def __del__(self):
        self.connect.close()


