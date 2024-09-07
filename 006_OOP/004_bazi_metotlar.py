class Movie :
    def __init__(self, title, director, duration) :
        self.title = title
        self.director = director
        self.duration = duration
        print("movie oluşturuldu")
    
    # bir tane movie objesi yazıdırılınca çalışır
    def __str__(self):
        return f"{self.title} by {self.director}"
    
    def __len__(self):
        return self.duration
    
    # mevcut bir obje silinince çalışır
    def __del__(self) :
        print("obje silindi")

m = Movie("rezervuar köpekleri","tarantino", 140)
# print(m)
# print(str(m))
print(len(m))  ## normalde class'da çalışmaz
# print(m.__len__())
# del m