import requests
import time

from bs4 import BeautifulSoup


url="https://kur.doviz.com/serbest-piyasa/?=user_currency"

response=requests.get(url) # Web sitesine bir istek gönderilir.

html_content=response.content # cevap içindeki içerik html_content değikenine atanır.

soup=BeautifulSoup(html_content,"html.parser") # html_content içeriğini ayrıştırıp soup nesnesine atar.

currencies=soup.find_all("div",{"class":"currency-details"}) #html içeriği içindeki aynı etiket ve sınıfa ait verilerin hepsini currencies atar.

exchange_values=soup.find_all("td",{"data-socket-attr":"bid"}) #html içeriği içindeki aynı etiket ve sınıfa ait verilerin hepsini exchange_values atar.


#print(currencies)
#print(exchange_values)


currencies2=list()
exchange_values2=list()
for currency,value in zip(currencies,exchange_values): #zip fonksiyonu kullanrak iki listedeki verilere eriştik.
    currency=currency.text # currency indeksinde bulunan html verisinin text kısmını alır.
    value=value.text       # value indeksinde bulunan html verisinin text kısmını alır.
    currency = currency.strip()
    value = value.strip()
    currency=currency.strip("\n") # strip fonksiyonu kullanarak içeriğin sonundaki ve başındaki \n çıkarıldı
    value=value.strip("\n")
    currency=currency.split("\n")  # split fonksiyonu kullanarak içeriğin içindeki \n göre içeriği ayırarak listeler.
    value=value.strip("'")
    value=value.replace(",",".") # replace fonksiyonu kullanarak içeriğin içindeki değer sayısal değer olduğu için virgül noktaya dönüştürüldü.
    currencies2.append(currency)   # append fonksiyonu kullanılarak içerikler listeye eklenir.
    exchange_values2.append(value)


"""print(currencies2)
print(exchange_values2)"""


class Currency_Convert():


    def first_Second_Convert(self,amount,first_Currency,second_Currency):

        amount = float(amount)

        for i in range(len(currencies2)):

            for j in range(len(currencies2)):
                if first_Currency==second_Currency:
                    result=amount
                    break

                elif(first_Currency=="TRY" and second_Currency==currencies2[i][0]):
                    result=amount/float(exchange_values2[i])
                    break

                elif(first_Currency==currencies2[i][0] and second_Currency=="TRY"):
                    result=amount*float(exchange_values2[i])
                    break

                elif(first_Currency==currencies2[i][0] and second_Currency==currencies2[j][0]):
                    result=amount*(float(exchange_values2[i])/float(exchange_values2[j]))
                    break



        return result

    def first_All_Convert(self,amount,firstCurrecy,secondCurrecy):

        if (firstCurrecy and secondCurrecy) or (firstCurrecy) or (secondCurrecy):
            response=[]
            amount = float(amount)

            if(firstCurrecy=="TRY" ):
                for i in range(len(currencies2)):
                    response.append([(currencies2)[i][0],(currencies2[i][1]),(amount/float(exchange_values2[i]))])

                    response.append(["********************","**********************","*********************************"])

                for i in range(len(currencies2)):
                    if(secondCurrecy==currencies2[i][0]):
                        for j in range(len(currencies2)):
                            value1=amount*(float(exchange_values2[i]))/(float(exchange_values2[j]))
                            response.append([currencies2[j][0],(currencies2[j][1]),value1])
                            response.append(["********************", "**********************", "*********************************"])

            elif (secondCurrecy == "TRY"):
                for i in range(len(currencies2)):
                    response.append([(currencies2)[i][0], (currencies2[i][1]), (amount / float(exchange_values2[i]))])
                    response.append(["********************","**********************","*********************************"])

                for i in range(len(currencies2)):
                    if (firstCurrecy == currencies2[i][0]):
                        for j in range(len(currencies2)):
                            value1 = amount * (float(exchange_values2[i])) / (float(exchange_values2[j]))
                            response.append([currencies2[j][0], (currencies2[j][1]), value1])
                            response.append(["********************", "**********************", "*********************************"])

            else:
                for i in range(len(currencies2)):
                    if(firstCurrecy==currencies2[i][0]):
                        for j in range(len(currencies2)):
                            value1=amount*(float(exchange_values2[i]))/(float(exchange_values2[j]))
                            response.append([currencies2[j][0],(currencies2[j][1]),value1])
                            response.append(["********************","**********************","*********************************"])

                for i in range(len(currencies2)):
                    if(secondCurrecy==currencies2[i][0]):
                        for j in range(len(currencies2)):
                            value1=amount*(float(exchange_values2[i]))/(float(exchange_values2[j]))
                            response.append([currencies2[j][0],(currencies2[j][1]),value1])
                            response.append(["********************", "**********************", "*********************************"])



        return response

