## any  ## en az bir tane 
# all   ## hepsi 

sonuc  = any([True, True, False])  ## True
sonuc  = any([True, True, True])  ## True
sonuc  = any([True, False, False])  ## True
sonuc  = any([False, False, False])  ## False

sonuc  = all([False, False, False])  ## False
sonuc  = all([True, False, False])  ## False
sonuc  = all([True, True, False])  ## False
sonuc  = all([True, True, True])  ## True

print(sonuc)

#####################################################
sayilar = [1, 6, 9, 11, -2, 0]

sonuc = all([bool(i) for i in sayilar])  ## T, T, T, T, T, F
sonuc = any([bool(i) for i in sayilar])  ## True
print(sonuc)

#####################################################

sonuc = [i % 2 == 0 for i in sayilar]  ## [False, True, False, False, True, True]
sonuc = any([i % 2 == 0 for i in sayilar])  ## True
sonuc = all([i % 2 == 0 for i in sayilar])  ## False
print(sonuc)
