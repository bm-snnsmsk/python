def ustel(a, b) :
  if b == 0 :
    return 1
  else :
    return a * ustel(a, b - 1)



print(ustel(5,2)
