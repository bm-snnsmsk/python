import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,9,20)
y = x ** 3
z = x ** 2


# figure = plt.figure()



## graik içine grafik ekleme

# axes_cube = figure.add_axes([0.1,0.1,0.8,0.8]) ## figure yerleşme oranları
# axes_cube.plot(x,y,'b')
# axes_cube.set_xlabel("X Axis")
# axes_cube.set_ylabel("Y Axis")
# axes_cube.set_title("Cube")

# axes_square = figure.add_axes([0.15,0.6,0.25,0.25])
# axes_square.plot(x,z,'r')
# axes_square.set_xlabel("X Axis")
# axes_square.set_ylabel("Y Axis")
# axes_square.set_title("Square")



### graik içine fsarklı plot ekleme
# axes = figure.add_axes([0,0,1,1])

# axes.plot(x,z,label="Square")
# axes.plot(x,y,label="Cube")
# axes.legend(loc=4)  ## bilgileri sağ-alt köşe


# fig,(axes1, axes2) = plt.subplots(nrows=2,ncols=1)
fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(8,8)) ## figure boyutlandırma

axes[0].plot(x,y)
axes[0].set_title("Cube")
axes[1].plot(x,z)
axes[1].set_title("Square")

plt.tight_layout() ## grikler birbirine karışmasın
# fig.savefig("figure2.png")
fig.savefig("figure2.pdf")

plt.show()


