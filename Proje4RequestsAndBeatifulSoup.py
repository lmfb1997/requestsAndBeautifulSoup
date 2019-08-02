import requests
from bs4 import BeautifulSoup

import sys

from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QHBoxLayout

"""
****************************************************************************
r = requests.get("https://store.steampowered.com/search/?specials=1")
#print(r.status_code) # sayfa durumunun kodunu öğrenme
#print(r.content) # sayfa kaynağına erişme


soup = BeautifulSoup(r.content,"html.parser")#neyi parçalayacağız --> r.content 2.parametre ise hangi kütüphane ile parçalayacağımız.


basliklar=soup.find_all("div",{"class":"responsive_search_name_combined"})
oyunAdlari=soup.find_all("span",{"class":"title"})
indirimYuzdeleri = soup.find_all("div",{"class":"col search_discount responsive_secondrow"})
oyunFiyatlari = soup.find_all("div",{"class":"col search_price discounted responsive_secondrow"})
for game in basliklar:
    print("{} oyununun {} indirimli, fiyat:{}".format(
        game.find("span", {"class": "title"}).text.strip(),
        game.find("div",{"class":"col search_discount responsive_secondrow"}).text.strip(),
        game.find("div",{"class":"col search_price discounted responsive_secondrow"}).text.strip()
    )) # .text dersek sadece içeriğin isimlerini getirir.
****************************************************************************


url = "https://boxofficeturkiye.com/hafta/?yil=2019&hafta=29"
headers_param = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36 OPR/62.0.3331.99 (Edition Campaign 34)"}

r = requests.get(url,headers=headers_param)

soup = BeautifulSoup(r.content,"html.parser")

#print(soup.prettify()) # içeriği düzgün bir şekilde gösterir.

filmTablosu = soup.find("table",{"class":"ustcizgi"}).select("tr:nth-of-type(2) > td > table:nth-of-type(3) > tr") #select kelimesi bizim gitmek istediğimiz elementlere gitmemizi sağlar örneğin 2. tr nin altındaki td nin altındaki 3. tablenin tr sine git dedik.

for i in range(1,21):
    filmAdi=filmTablosu[i].find("a",{"class":"film"}).get("title")#a etiketinin içindeki title ın içindeki degeri getir.
    toplamSeyirci = filmTablosu[i].select("td:nth-of-type(10) > font")[0].text
    hasilat = filmTablosu[i].select("td:nth-of-type(9) > font")[0].text
    print("Film Adı: {} \n Hasılat : {} \n Toplam Seyirci : {}".format(filmAdi,hasilat,toplamSeyirci))
    print("-"*30)
****************************************************************************    
    


url = "https://www.python.org/jobs/"

r = requests.get(url)

soup = BeautifulSoup(r.content,"html.parser")

pages=len(soup.find_all("ul",{"class":"pagination"})[0].find_all("li")) -2 #sayfa sayısından previous ve next i çıkarıyoruz
totalJobs=0
for pageNumber in range(1,pages +1): # her bir sayfayı dön.
    pageRequest = requests.get("https://www.python.org/jobs/?page="+str(pageNumber))
    print(pageRequest.url)
    pageSource = BeautifulSoup(pageRequest.content,"html.parser")
    jobs = pageSource.find("div",{"class":"row"}).ol.find_all("li")# "." demek onun altındaki bir element anlamında
    #Tüm işleri çektik, döngü ile ilan detaylarını alalım.
    for job in jobs:
        name = job.h2.find("a").text
        location = job.find("span",{"class":"listing-location"}).text
        company = job.find("span",{"class","listing-company-name"}).br.next.strip()
        publish_time = job.find("time").text
        totalJobs+=1
        print(name,company,location,publish_time,sep="\n")
        print("-"*60)


print(totalJobs)
****************************************************************************
"""

url = "https://www.imdb.com/chart/top"
response = requests.get(url)
soup = BeautifulSoup(response.content,"html.parser")


class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.filmIsmi = QPushButton("Film İsimlerini Getir")
        self.filmRating = QPushButton("Film Ratinglerini Getir")
        self.yazi_alani = QTextEdit()



        h_box = QHBoxLayout()

        h_box.addWidget(self.filmIsmi)
        h_box.addWidget(self.filmRating)

        v_box = QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addStretch()
        v_box.addWidget(self.yazi_alani)

        self.setWindowTitle("Filmler")
        self.setLayout(v_box)

        self.filmIsmi.clicked.connect(self.filmIsmiClick)
        self.filmRating.clicked.connect(self.filmRatingClick)

        self.show()

    def filmIsmiClick(self):
        self.yazi_alani.clear()
        filmIsimleri = soup.find_all("td",{"class":"titleColumn"})
        for i in filmIsimleri:
            film_Isimleri = i.find("a").text
            self.yazi_alani.insertPlainText(film_Isimleri+"\n")
    def filmRatingClick(self):
        self.yazi_alani.clear()
        filmRatingleri = soup.find_all("td",{"class","ratingColumn imdbRating"})
        for i in filmRatingleri:
            i = i.text
            i= i.strip()
            self.yazi_alani.insertPlainText(i+"\n")

app = QApplication(sys.argv)
pencere = Pencere()


sys.exit(app.exec_())
























