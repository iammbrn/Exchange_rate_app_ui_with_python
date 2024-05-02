import sqlite3


class DeleteAccount():

    def __init__(self):

        self.create_Connect()


    def create_Connect(self):

        self.connect=sqlite3.connect("Database.db")

        self.cursor=self.connect.cursor()

    def delete_My_Account(self,username):

        self.cursor.execute("Delete From UserData where kullaniciAdi=?",(username))
        self.connect.commit()

    def __del__(self):
        self.connect.close()


