x = "global x"
y = "global y"

def function() :
    x = "local x"
    print(x)  # local değeri alır
    print(y)  # localde olamadığı için globalden alır değeri


function()
print(x)
print(y)

##################################################################

sayi = 50
def test(sayi) :
    print(f"sayi : {sayi}")
    sayi = 100
    print(f"sayi : {sayi}")

test(sayi)
print(sayi)  # global değeri alır


###################################################################

num = 50
def test2() :
    global num
    print(f"num : {num}")
    num = 100
    print(f"num : {num}")

test2()
print(num)  #  değiştirlen değeri alır değeri alır