# Aldebaran Döviz Uygulaması Açıklama

## 1. **Web Sitesi Üzerinden Veri Çekilmesi:** <br/>
  * Bu işlem için **requests ve (from bs4 import BeautifulSoup)** modülleri [web_currents_data.py](https://github.com/iammbrn/Exchange_rate_app_ui_with_python/blob/master/web_currents_data.py) dosyasına dahil edildi.
  * Web sitesi url' si kullanılarak `response=requests.get(url)` komutu ile web sitesine veri çekme isteği gönderildi gelen veri **response** değişkenine atandı.
  * `html_content=response.content` komutu gelen ve gelen içeriğin içindeki içerik **html_content** değişkenine atandı.
  * `soup=BeautifulSoup(html_content,"html.parser")` komutu ile html_content içeriği ayrıştırılıp **soup** değişkenine atandı.
  * `currencies=soup.find_all("div",{"class":"currency-details"})` komutu ile belirtilen etiketlere sahip veriler yani para birimleri **currencies** değişkenine atandı.
  * `exchange_values=soup.find_all("td",{"data-socket-attr":"bid"})` komutu ile belirtilen etiketlere sahip veriler yani para birimi değerleri **exchange_values** değişkenine atandı.
  * `class Currency_Convert():` sınıfı oluşturulup bu sınıf içinde iki para birimini dönüştürmek için `def first_Second_Convert(self,amount,first_Currency,second_Currency):` fonksiyonu, bir para birimine karşılık diğer para birimleri değerlerini bulmak için `def first_All_Convert(self,amount,firstCurrecy,secondCurrecy):` fonksiyonu oluşturuldu.


## 2. ** Kullanıcı Üye Ol Sayfası için Veritabanı Bağlantısı Oluşturma:** <br/>
 * Bu işlem için **sqlite3** modülü [signup.py](https://github.com/iammbrn/Exchange_rate_app_ui_with_python/blob/master/signup.py) dosyasına dahil edildi.
 * `class SignUp():` sınıfı oluşturulup eğer varsa veri tabanıyla direk bağlantı kurup yoksa o veritabanını oluşturup bağlantı kurup ve veri tabanı üzerinde imleç oluşturmak için yapıcı fonksiyon **__init__** içinde **self.createConnect()** fonksiyonu oluşturuşlur.
 * Daha sonra sınıf içinde `def signUp(self,name,surname,username,email,password):` fonksyionu oluşturulur.
 * **signUp** fonksiyonu verilen parametre değerlerini kontrol ederek return ile sonuç döndürür.

## 3. **Kullanıcı Üye Ol Arayüzü Oluşturma:** <br/>
 * Bu işlem için **sys, pyqt5 ve (from signup import * )** modülleri [user_signup_ui.py](https://github.com/iammbrn/Exchange_rate_app_ui_with_python/blob/master/user_signup_ui.py) dosyasına dahil edildi.
 * `class SignupPage(QWidget):` QWidget sınıfını miras alan bir sınıf oluşturuldu.
 * Sınıfın yapıcı fonksiyonu __init__ içinde `super().__init__()` komutu ile üst sınıfa ait özellik ve işlevler bu sınıfa dahil edildi böylece pencere oluşturuldu ve __init__ içinde **self.setupSignupPage()** fonksiyonu oluşturuldu.
 * `def setupSignupPage(self):` fonksiyonu ile pencereye label, buton vb. eklendi.
 * `self.pushButton_signup.clicked.connect(self.signup)` komutu Pencere üzerinde bulunan **self.pushButton_signup** butonuna tıklandığında onu **self.signup** fonksiyonuna bağlar.
 * `def signup(self):` fonksiyonu `self.createuser=SignUp()` komutu ile **SignUp** sınıfına ait bir nesne oluşturark `self.createuser.signUp(name, surname, username, email, password)` komutu ile bu nesne üzerinden pencere üzerine kullanıcının girmiş olduğu verileri kullanarak üye kaydı gerçekleştirilir.
 


    
  
