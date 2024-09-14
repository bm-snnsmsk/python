import os
import datetime

# result = dir(os)
# result = os.name    # nt = windows
# result = os.getcwd()  # etkin dizin


# ## dizin değiştirme
# os.chdir("..")   # bir üst dizinine git
# os.chdir("../..")   # iki üst dizinine git
# os.chdir("C:\\")   # C dizinine git
# os.mkdir("newdirectory")   # belirtilen dizinde yeni bir klasör oluştur
# os.mkdirs("newdirectory/yenibir klasor")   # belirtilen dizinde iç içe  klasör oluştur

# os.rename("newdirectory", "newname")
# os.rmdir("newdirectory") ## boş dizin silme
# os.removedirs("newdirectory") ## dolu dizin silme

# result = os.listdir()  ## mevcut dizini listele
# result = os.listdir("C:\\")  ## belirtilen dizini listele

## sadece .py dosyaları listele
# for i in os.listdir() :
#     if i.endswith(".py") :
#         print(i)

# result = os.stat("deneme_1.py")
# result = os.stat("deneme_1.py").st_size/1024
# result = datetime.datetime.fromtimestamp(os.stat("deneme_1.py").st_ctime)  # create time
# result = datetime.datetime.fromtimestamp(os.stat("deneme_1.py").st_atime)  # son erişim time
# result = datetime.datetime.fromtimestamp(os.stat("deneme_1.py").st_mtime)  # değiştirme time


# os.system("deneme_1.py")   ## programı veya çalıştırma
  # tam yol C:\Users\bm_snnsmsk\Desktop\python_sadik_turan_05.09.2024\deneme_1.py


# result = os.path.dirname("C:/Users/bm_snnsmsk/Desktop/python_sadik_turan_05.09.2024/deneme_1.py")  # directory path  -- C:\Users\bm_snnsmsk\Desktop\python_sadik_turan_05.09.2024\
# result = os.path.dirname(os.path.abspath("deneme_1.py"))  # directory path  -- C:\Users\bm_snnsmsk\Desktop\python_sadik_turan_05.09.2024\

# result = os.path.exists("deneme_1.py") # dosya veya klasör sorulama # True
# result = os.path.isdir("C:/Users/bm_snnsmsk/Desktop/python_sadik_turan_05.09.2024/deneme_1.py") # klasör yolu mu sorulama # False
# result = os.path.isdir("C:/Users/bm_snnsmsk/Desktop/python_sadik_turan_05.09.2024") # klasör yolu mu sorulama # True

# result = os.path.isfile("C:/Users/bm_snnsmsk/Desktop/python_sadik_turan_05.09.2024/deneme_1.py") # dosya yolu mu sorulama # True
# result = os.path.isfile("C:/Users/bm_snnsmsk/Desktop/python_sadik_turan_05.09.2024") # dosya yolu mu sorulama # True

# result = os.path.join("C:\\", "deneme", "deneme1") # belirtilen dizinde dizin oluşturma

# result = os.path.split("C:\\deneme") # dizinleri parçalama
result = os.path.splitext("deneme_1.py") # dosya isim ve uzantıya çevirme
result = result[1]  ## .py

print(result)