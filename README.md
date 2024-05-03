# Aldebaran Döviz Uygulaması Açıklama

## 1. **Web Sitesi Üzerinden Veri Çekilmesi:** <br/>
  * Bu işlem için **requests ve (from bs4 import BeautifulSoup)** modülleri [web_currents_data.py](https://github.com/iammbrn/Exchange_rate_app_ui_with_python/blob/master/web_currents_data.py) dosyasına dahil edildi.
  * Web sitesi url' si kullanılarak `response=requests.get(url)` komutu ile web sitesine veri çekme isteği gönderildi gelen veri **response** değişkenine atandı.
  * `html_content=response.content` komutu gelen ve gelen içeriğin içindeki içerik **html_content** değişkenine atandı.
  * `soup=BeautifulSoup(html_content,"html.parser")` komutu ile html_content içeriği ayrıştırılıp **soup** değişkenine atandı.
  * `currencies=soup.find_all("div",{"class":"currency-details"})` komutu ile belirtilen etiketlere sahip veriler yani para birimleri **currencies** değişkenine atandı.
  * `exchange_values=soup.find_all("td",{"data-socket-attr":"bid"})` komutu ile belirtilen etiketlere sahip veriler yani para birimi değerleri **exchange_values** değişkenine atandı.
  * `class Currency_Convert():` sınıfı oluşturulup bu sınıf içinde iki para birimini dönüştürmek için `def first_Second_Convert(self,amount,first_Currency,second_Currency):` fonksiyonu, bir para birimine karşılık diğer para birimlerini değerlerini bulmak için `def first_All_Convert(self,amount,firstCurrecy,secondCurrecy):` fonksiyonu oluşturuldu.


## 2. **Kullanıcı Üye Ol Sayfası için Veritabanı Bağlantısı Oluşturma:** <br/>
 * Bu işlem için **sqlite3** modülü [signup.py](https://github.com/iammbrn/Exchange_rate_app_ui_with_python/blob/master/signup.py) dosyasına dahil edildi.
 * `class SignUp():` sınıfı oluşturulup, eğer varsa veri tabanıyla direk bağlantı kurulup, yoksa veritabanını oluşturup bağlantı kurmak ve veri tabanı üzerinde imleç oluşturmak için yapıcı fonksiyon **__init__** içinde **self.createConnect()** fonksiyonu oluşturuldu.
 * Daha sonra sınıf içinde `def signUp(self,name,surname,username,email,password):` fonksyionu oluşturulur.
 * **signUp** fonksiyonu verilen parametre değerlerini **veritabanı** üzerinde kontrol ederek return ile sonuç döndürür.
 * Son olarak **Veritabanı** bağlantısını kesmek için `def __del__(self):` fonksiyonu oluşturularak, bu fonksiyon içinde `self.connect.close()` komutu ile veritabanı bağlantısı kesilir.
   

## 3. **Kullanıcı Üye Ol Arayüzü Oluşturma:** <br/>
 * Bu işlem için **sys, pyqt5 ve (from signup import * )** modülleri [user_signup_ui.py](https://github.com/iammbrn/Exchange_rate_app_ui_with_python/blob/master/user_signup_ui.py) dosyasına dahil edildi.
 * `class SignupPage(QWidget):` QWidget sınıfını miras alan bir sınıf oluşturuldu.
 * Sınıfın yapıcı fonksiyonu __init__ içinde `super().__init__()` komutu ile üst sınıfa ait özellik ve işlevler bu sınıfa dahil edildi böylece pencere oluşturuldu ve __init__ içinde **self.setupSignupPage()** fonksiyonu oluşturuldu.
 * `def setupSignupPage(self):` fonksiyonu ile pencereye label, buton, ve renk vb. özellikler eklendi.
 * `self.pushButton_signup.clicked.connect(self.signup)` komutu Pencere üzerinde bulunan **self.pushButton_signup** butonuna tıklandığında onu **self.signup** fonksiyonuna bağlar.
 * `def signup(self):` fonksiyonu `self.createuser=SignUp()` komutu ile **SignUp** sınıfına ait bir nesne oluşturark `self.createuser.signUp(name, surname, username, email, password)` komutu ile bu nesne üzerinden pencere üzerine kullanıcının girmiş olduğu verileri kullanarak üye kaydı gerçekleştirilir.

## 4. **Kullanıcı Giriş Yap Sayfası için Veritabanı Bağlantısı Oluşturma:** <br/>
  * Bu işlem için **sqlite3** modülü [login.py](https://github.com/iammbrn/Exchange_rate_app_ui_with_python/blob/master/login.py) dosyasına dahil edildi.
 * `class LogIn():` sınıfı oluşturulup, eğer varsa veri tabanıyla direk bağlantı kurulup, yoksa veritabanını oluşturup bağlantı kurmak ve veri tabanı üzerinde imleç oluşturmak için yapıcı fonksiyon **__init__** içinde **self.createConnect()** fonksiyonu oluşturuldu.
 * Daha sonra sınıf içinde `def logIn(self,username,password):` fonksyionu oluşturuldu. Bu fonksiyon verilien parametre değerlerini **veritabanı** üzerinde kontrol ederek return ile sonuç döndürür.
 * Son olarak **Veritabanı** bağlantısını kesmek için `def __del__(self):` fonksiyonu oluşturularak, bu fonksiyon içinde `self.connect.close()` komutu ile veritabanı bağlantısı kesilir.

## 5. **Kullanıcı Giriş Yap Sayfası Arayüzü Oluşturulması:** <br/>
  * Bu işlem için **sys ve pyqt5** modülleri [user_login_ui.py](https://github.com/iammbrn/Exchange_rate_app_ui_with_python/blob/master/user_login_ui.py) dosyasına dahil edildi.
 * `class LoginPage(QWidget):` QWidget sınıfını miras alan bir sınıf oluşturuldu.
 * Sınıfın yapıcı fonksiyonu __init__ içinde `super().__init__()` komutu ile üst sınıfa ait özellik ve işlevler bu sınıfa dahil edildi böylece pencere oluşturuldu ve __init__ içinde **self.setupLoginPage()** fonksiyonu oluşturuldu.
 * `def setupLoginPage(self):` fonksiyonu ile pencereye label, buton, ve renk vb. özellikler eklendi.

## 6. **Kullanıcı Ana Sayfa Arayüzü Oluşturma:** <br/>
 * Bu işlem için gerekli modüller [main_page_project.py](https://github.com/iammbrn/Exchange_rate_app_ui_with_python/blob/master/main_page_project.py) dosyasına dahil edildi.
 * `class MainPage(QWidget):` QWidget sınıfını miras alan bir sınıf oluşturuldu.
 * Sınıfın yapıcı fonksiyonu __init__ içinde `super().__init__()` komutu ile üst sınıfa ait özellik ve işlevler bu sınıfa dahil edildi böylece pencere oluşturuldu ve __init__ içinde **self.setupMainPage()** fonksiyonu oluşturuldu.
 * `def setupMainPage(self):` fonksiyonu ile pencereye label, buton, ve renk vb. özellikler eklendi.
 * `self.pushButton_Convert.clicked.connect(lambda : self.convert(self.lineEdit_amount.text(),self.lineEdit_First_Currency.text(),self.lineEdit_Second_Currency.text(),self.textEdit_All_Currenies))` komutu **self.pushButton_Convert** butonuna tıklandığında onu **self.convert** fonksiyonuna bağlar.
 * `def convert(self,amount,firstCurrency,secondCurrency,answer):` fonksiyonu `calculate = Currency_Convert()` komutu ile bir nesne oluşturur. Bu nesne üzerinden döviz kuru dönüşüm fonksiyonunu `calculate.first_Second_Convert(amount, firstCurrency, secondCurrency)` kullanır.
* `self.comboBox_First_Currency.currentTextChanged.connect(self.selectCombo_box1)` komutu kombobox üzerindeki text değeri değişince **self.selectCombo_box1** fonksiyonuna bağlanır. `def selectCombo_box1(self,text):` fonksiyonuna parametre olarak yeni text değeri gelir ve bu text değeri istenilen yere eklenir.
 * `class Menu(QMainWindow):` QMainWindow sınıfını miras alan bir sınıf oluşturuldu.
 * Sınıfın yapıcı fonksiyonu __init__ içinde `super().__init__()` komutu ile üst sınıfa ait özellik ve işlevler bu sınıfa dahil edildi böylece **Ana Pencere** oluşturuldu.
 * __init__ içinde `self.window= MainPage()` ve `self.setCentralWidget(self.window)` komutları ile önce **MainPage** sınıfından QWidget nesnesi(penceresi) oluşturuldu sonra bu pencere Ana pencerenin merkezine konuldu.
 * __init__ içinde self.createMenu(username) fonksiyonu oluşturuldu. Bu fonksiyon içinde Ana Pencere üzerine **Menubar** eklenip bu menubara menüler ve actionlar eklendi.
 * Menubar üzerindeki actionlara tıklandığında; <br/>
   **İsim menüsünde:** herhangi bir işlem gerçekleşmez, bu menüde sadece isim tutulur. <br/>
   **Ayarlar menüsünde:** *Profil Bilgileri Güncellenebilir, Profil Bilgileri Görüntülenebilir, Hesap Silinebilir ve Çıkış Yapılabilir.* <br/>
   **Dosya menüsünde:** *Dosya kaydetme, Dosya Açma ve Temizleme işlemleri yapılabilir.* <br/>
   **Görünüm menüsünde:** *Tema* kısmıda ekran görünümü *Normal Mod, Gece Modu ve Okuma Moduna geçirilebilir.* <br/>
   **Yardım menüsünde:** *Kullanım kılavuzuna, Hakkında kısmına ve Sıkça Sorulan Sorulara* ulaşıbilir. 

## 7. **Kullanıcı Profil Bilgileri Güncelleme Arayüzü:** <br/>
 *  Bu işlem için gerekli modüller [update_User_Informations.py](https://github.com/iammbrn/Exchange_rate_app_ui_with_python/blob/master/update_User_Informations.py) dosyasına dahil edildi.
 *  `class UpdateUserInformations()`sınıfı oluşturulup, eğer varsa veri tabanıyla direk bağlantı kurulup, yoksa veritabanını oluşturup bağlantı kurmak ve veri tabanı üzerinde imleç oluşturmak için yapıcı fonksiyon **__init__** içinde **self.createConnect()** fonksiyonu oluşturuldu.
 *  Daha sonra Veritabanına bağlanıp verileri güncellemek için `def update_User_Informations(self,username,name,surname,newusername,email,password):` fonksiyonu oluşturuldu.
 * Son olarak **Veritabanı** bağlantısını kesmek için `def __del__(self):` fonksiyonu oluşturularak, bu fonksiyon içinde `self.connect.close()` komutu ile veritabanı bağlantısı kesilir.
 * `class UpdatePage(QWidget):` QWidget sınıfını miras alan bir sınıf oluşturuldu.
 * Sınıfın yapıcı fonksiyonu __init__ içinde `super().__init__()` komutu ile üst sınıfa ait özellik ve işlevler bu sınıfa dahil edildi böylece pencere oluşturuldu ve __init__ içinde **self.setupUpdatePage()** fonksiyonu oluşturuldu.
 * `def setupUpdatePage(self):` fonksiyonu ile pencereye label, buton, ve renk vb. özellikler eklendi.

## 8. **Hesabımı Sil Sınıfı Oluşturma:** <br/>
 * Bu işlem için gerekli modüller [delete_my_account.py](https://github.com/iammbrn/Exchange_rate_app_ui_with_python/blob/master/delete_my_account.py) dosyasına dahil edildi.
 *  `class DeleteAccount()`sınıfı oluşturulup, eğer varsa veri tabanıyla direk bağlantı kurulup, yoksa veritabanını oluşturup bağlantı kurmak ve veri tabanı üzerinde imleç oluşturmak için yapıcı fonksiyon **__init__** içinde **self.createConnect()** fonksiyonu oluşturuldu.
 * Daha sonra veritabanına bağlanıp parametre olarak verilen kullanıcı adına sahip kişinin hesabını silmek için `def delete_My_Account(self,username):` fonksiyonu oluşturuldu.
 *  Son olarak **Veritabanı** bağlantısını kesmek için `def __del__(self):` fonksiyonu oluşturularak, bu fonksiyon içinde `self.connect.close()` komutu ile veritabanı bağlantısı kesilir.

## 9. **Arayüzler Arası Geçiş Ana Penceresi Oluşturma:**
 * Bu işlem için gerekli modüller [current_Main_Interface.py](https://github.com/iammbrn/Exchange_rate_app_ui_with_python/blob/master/current_Main_Interface.py) dosyasına dahil edildi.
 * `class MainWindow(QMainWindow):` QMainWindow sınıfını miras alan bir sınıf oluşturuldu.
 * Sınıfın yapıcı fonksiyonu __init__ içinde `super().__init__()` komutu ile üst sınıfa ait özellik ve işlevler bu sınıfa dahil edildi böylece **Ana Pencere** oluşturuldu.
 * `self.window=SignupPage()`: komutu ile bir nesne oluşturuldu.
 * `self.stackedWidget=QStackedWidget()`: komutu ile bir **stackedWidget** oluşturuldu.
 * `self.setCentralWidget(self.stackedWidget)`: Oluşturulan stackedWidget Ana pencerenin merkezine konuldu.
 * `self.stackedWidget.addWidget(self.window)`: stackedWidget' a QWidget nesnesi eklendi.
 * `self.stackedWidget.setCurrentWidget(self.window)` stackedWidget' a self.window görüntülenmesi sağlanır.
 * `self.window.pushButton_login.clicked.connect(self.openLoginPage)` komutu **self.window.pushButton_login** butonuna tıklandığında *self.openLoginPage* fonksiyonuna bağlanır. self.openLoginPage fonksiyonu `self.open_login=LoginPage()`, `self.stackedWidget.addWidget(self.open_login)` ve `self.stackedWidget.setCurrentWidget(self.open_login)` komutlarıyla yeni bir LoginPage nesnesi oluşturup, stackedWidget'e ekleyip sonrada stackedWidget' bu nesnenin görüntülenmesi sağlanır.
 * `self.open_login.pushButton_login.clicked.connect(self.login)` komutu **self.open_login.pushButton_login** butonuna tıklandığında *self.login* fonksiyonuna bağlanır. self.login fonksiyonu `self.control = LogIn()` komutu ile bir nesne oluşturup, `self.control.logIn(username, password)` komutuyla kullanıcının bilgilerini kontrol edip sistme giriş yapmasını veya bilgiler hatalıysa hata almasını sağlar. Bilgiler doğru ise `self.userMainPage(username, result)` komutu çalışır, buda bir fonksiyona bağlanır, bu fonksiyon `self.menu = Menu(username)` komutu ile bir nesne oluşturup stackedWidget'e ekleyip sonrada stackedWidget'a bu nesnenin görüntülenmesi sağlanır.
 * `self.open_login.pushButton_signup.clicked.connect(self.return_Signup)` komutu Giriş Yap penceresi üzerinde  **self.open_login.pushButton_signup** bu butona tıklandığında *self.return_Signup* fonksiyonuna bağlanır. Bu fonksiyon `self.stackedWidget.setCurrentWidget(self.window)` komutu ile self.window nesnesi yani Üye Ol penceresi stackedWidget'e tekrar görüntülenir.

  
