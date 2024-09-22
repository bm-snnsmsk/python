'''

one to one                   
--- normal tablolar
product                     produc_detail
id  name         price      id  renk     ebat
1   samsung s6   2000       1   kırmızı  5inc
2   samsung s7   3000       2   mavi     6inc
3   dell laptop  5000       3   beyaz    4.8inc


one to many
---  
product                          category
id  name         price  catid    id  name
1   samsung s6   2000   1        1   telefon
2   samsung s7   3000   1        2   bilgisayar
3   dell laptop  5000   2        3   tablet


many to many
---  ## bir numaralı hem telefon hem elektronik
product                     category             ProductCategory
id  name         price      id  name             productid   categoryid
1   samsung s6   2000       1   telefon          1           1            
2   samsung s7   3000       2   bilgisayar       1           3
3   dell laptop  5000       3   tablet           2           1

'''

''' 
database tasarımı 
## tekrarlara yer vermemesi için tasarım iyi oluşturulmalı

one to many 

müşteri                kategory
id  müşteri_adı        id  kategory_adı
1   ahmet              1   telefon
2   ali                2   bilgisayar
3   zeynep             3   elektronik


ürünler                                      
id   ürün_adı       fiyat  açıklama     kategory_id
1    samsung s5     6000   iyi          1
2    samsung s6     3000   kötü         1
3    lenovo laptop  12000  idare eder   2


siparişler
id    ürün_id     müsteri  sipariş_tarihi
2     2           2        1.01.2020
3     3           3        1.11.2020
4     1           1        1.01.2020
1     1           1        1.01.2019

############################################################
many to many
müşteri                kategory
id  müşteri_adı        id  kategory_adı
1   ahmet              1   telefon
2   ali                2   bilgisayar
3   zeynep             3   elektronik


ürünler                                      
id   ürün_adı       fiyat  açıklama    
1    samsung s5     6000   iyi         
2    samsung s6     3000   kötü         
3    lenovo laptop  12000  idare eder   


siparişler
id    ürün_id     müsteri  sipariş_tarihi
2     2           2        1.01.2020
3     3           3        1.11.2020
4     1           1        1.01.2020
1     1           1        1.01.2019


### many to many 
### bu tablolarda id olamaz
## her ikisi de bvirincil anahtar olmalı
## tabloda değişmez bir alan varsa o başka. o zaman id kullanılır
ProductCategroy
urunid    categoryid
1         1
2         1
1         3
2         3

'''