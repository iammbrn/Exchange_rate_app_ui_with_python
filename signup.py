import sqlite3


class SignUp():

    def __init__(self):

        self.create_Connect()


    def create_Connect(self):

        self.connect = sqlite3.connect("Database.db")
        self.cursor = self.connect.cursor()

        self.cursor.execute("Create Table If Not Exists UserData(ad TEXT, soyad TEXT, kullaniciAdi TEXT, email TEXT, sifre TEXT)")

        self.connect.commit()


    def signUp(self,name,surname,username,email,password):

        self.cursor.execute("Select * From UserData where kullaniciAdi=? or email=?",(username,email))
        user_data = self.cursor.fetchall()

        if len(user_data)==0:
            if name and surname and  username and email and password:

                if len(password)>=8 and ("@" in email):
                    self.cursor.execute("Insert Into UserData Values(?,?,?,?,?)",(name,surname,username,email,password))
                    self.connect.commit()
                    return "İşlem Başarılı"

                else:
                    if len(password)<8:
                        return "Sevgili kullanıcı, şifreniz en az 8 karakter olmalıdır."

                    elif ("@" in email)==False:
                        return "Sevgili kullanıcı lütfen e-posta (@) adresinizi kontrol edin."

            else:
                return "Lütfen bilgilerinizi kontrol edin!"

        elif username == user_data[0][2]:
            return "Bu Kullanıcı Adı mevcut, lütfen başka bir Kullanıcı Adı deneyin!"

        elif email == user_data[0][3]:
            return "Bu Email hesabı mevcut, lütfen başka bir Email deneyin!"

        else:
            return "Lütfen bilgilerinizi kontrol edin!"

    def __del__(self):
        self.connect.close()














