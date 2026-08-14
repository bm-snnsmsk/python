def tambolenler(sayi) :
    tambolenler = []
    for i in range(2, sayi + i):
        if sayi % i == 0 :
            tambolenler.append(i)
    return tambolenler

print(tambolenler(20))


"""
def bolenler(sayi) :
    tambolenler = []
    for i in range(1, sayi + 1) :
        if sayi % i == 0 :
            tambolenler.append(i)
            print(f"{sayi}, {i}'ye tam bölünüyor...")
        else :
            print(f"{sayi}, {i}'ye bölünmüyor...")
    return tambolenler
"""
