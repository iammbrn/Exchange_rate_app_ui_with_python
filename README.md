# Aldebaran Döviz Uygulaması Açıklama

## 1. **Web Sitesi Üzerinden Veri Çekilmesi:** <br/>
  * Bu işlem için **requests ve (from bs4 import BeautifulSoup)** modülleri [web_currents_data.py](https://github.com/iammbrn/Exchange_rate_app_ui_with_python/blob/master/web_currents_data.py) dosyasına dahil edildi.
  * Web sitesi url' si kullanılarak `response=requests.get(url)` komutu ile web sitesine veri çekme isteği gönderildi gelen veri **response** değişkenine atandı.
  * `html_content=response.content` komutu gelen ve gelen içeriğin içindeki içerik **html_content** değişkenine atandı.
  * `soup=BeautifulSoup(html_content,"html.parser")` komutu ile html_content içeriği ayrıştırılıp **soup** değişkenine atandı.
  * `currencies=soup.find_all("div",{"class":"currency-details"})` komutu ile belirtilen etiketlere sahip veriler yani para birimleri **currencies** değişkenine atandı.
  * `exchange_values=soup.find_all("td",{"data-socket-attr":"bid"})` komutu ile belirtilen etiketlere sahip veriler yani para birimi değerleri **exchange_values** değişkenine atandı.
  * `class Currency_Convert():` sınıfı oluşturulup bu sınıf içinde iki para birimini dönüştürmek için `def first_Second_Convert(self,amount,first_Currency,second_Currency):` fonksiyonu, bir para birimine karşılık diğer para birimleri değerlerini bulmak için `def first_All_Convert(self,amount,firstCurrecy,secondCurrecy):` fonksiyonu oluşturuldu.


    
  
