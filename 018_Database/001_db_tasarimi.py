'''

one to one                   
--- normal tablolar >>> biri ürün bir detay ile bir detay da bir ürünü işaret edebilir
product                     produc_detail
id  name         price      id  renk     ebat
1   samsung s6   2000       1   kırmızı  5inc
2   samsung s7   3000       2   mavi     6inc
3   dell laptop  5000       3   beyaz    4.8inc


one to many ## her bir ürün sadece bir categoriye air tersten bakarsak her bir kategoriginin birden fazla ürüne karşılığı vardır
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
many to many            ### bir ürün birden fazla kategoriye ait olabilir her bir kategori de birden fazla ürünü işaret edebilir
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
### bu tablolarda id olamaz  (bu satırı- bence yanlış) çünkü her tablonun id si vardır
## her ikisi de bvirincil anahtar olmalı
## tabloda değişmez bir alan varsa o başka. o zaman id kullanılır    >>>>> rol permission ve role_permissipon daki gibi
### bir ürünün birden fazla kategorisi olablir ve diğer yandan da bir kategorinin de birden fazla ürünü işaret edebilir
## many to many tablolarında ayrı yapılmalı çünkü one yo many de category kolonuna 1,4 şeklidne ilişkili olduğu kategoriler yazılmaz
ProductCategroy
urunid    categoryid
1         1
2         1
1         3
2         3

'''
