'''

Öğrenci
id  ad     soyad   numara  tc_no   cinsiyet  dogum_tarihi  sube_id
1   ahmet  yılmaz  100     111111  Erkek     01.01.2005    1
2   sena   turan   100     222222  Kız       08.11.2008    2
3   çınar  bilgin  100     333333  Erkek     01.01.2005    1

Öğretmen
id  ad     soyad   tc_no   cinsiyet  dogum_tarihi  sube_id  branş
1   ahmet  yılmaz  111111  Erkek     01.01.1980    1        1
2   sena   turan   222222  Kız       08.11.1975    1        3
3   çınar  bilgin  333333  Erkek     01.01.1990    2        4

Şube
id  sube_ad     
1   10/A 
2   10/B   
3   10/C 
4   11/A
5   11/B

Branş
id  brans_ad     
1   matematik 
2   fizik  
3   kimya 
4   resim
5   müzik

Ders
id   ders_adi
1    progralama dersi
2    matematik
3    fizik
4    beden


### many to many 
### bu tablolarda id olamaz
## her ikisi de bvirincil anahtar olmalı
## tabloda değişmez bir alan varsa o başka. o zaman id kullanılır
Şube_Öğretmen
sube_id  öğretmen_id  ders_id
1        1            1
1        1            2
1        2            2
2        1            1




'''
#####################################################################

'''

##### one to many
Film
id  Film_adı   açıklama  süre  yayın_tarihi  resim_url   tanıtım  yönetmen_id
1   film_1     açıklama  124   2020          1.jpg       1.mp4    1
2   film_2     açıklama  93    2011          2.jpg       2.mp4    2
3   film_3     açıklama  105   2019          3.jpg       3.mp4    1

Kategory
id  kategory_adı  açıklama
1   macera        açıklama  
2   komedi        açıklama  
3   bilim kurgu   açıklama  


### many to many 
### bu tablolarda id olamaz
## her ikisi de bvirincil anahtar olmalı
Film_Kategory
film_id  cat_id
1        2
1        3
2        3

### many to many 
### bu tablolarda id olamaz
## her ikisi de bvirincil anahtar olmalı
## tabloda değişmez bir alan varsa o başka. o zaman id kullanılır
Film_oyuncu
film_id  oyuncu_id
1          2
2          3
2          2

Yönetmen 
id  adı    soyadı   doğum_tarihi  cinsiyet  ülke
1   ali    yılmaz   1980          Erkek     Türkiye          
2   ahmet  yılamz   1975          Erkek     Türkiye 
3   çınar  turan    1980          Erkek     Türkiye 

Oyuncu 
id  adı    soyadı   doğum_tarihi  cinsiyet  ülke
1   ali    yılmaz   1980          Erkek     Türkiye          
2   ahmet  yılamz   1975          Erkek     Türkiye 
3   çınar  turan    1980          Erkek     Türkiye 





'''