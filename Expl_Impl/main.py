import method
import matplotlib.pyplot as plt
from json import load
from matplotlib import use
use("TkAgg")

def read():
    with open("output.json", "r") as file:
        info = load(file)
        return info["xvector"], info["yvector"]

with open("input.json", "r") as file:
    info = load(file)

h = info["h"]
y0 = info["y0"]
x0 = info["x0"]
A = info["A"]
x_final = info["x_final"]

example = method.Method(A, h, y0, x0, x_final)
print('\n'+example.eiginNumb())
# example.explMeth()
# xExpl, ynExpl = read()
# yExpl = [i[1] for i in ynExpl]
# plt.plot(xExpl, yExpl, color = 'green', label='expl')

example.implMeth()
xImpl, ynImpl = read()
yImpl = [i[1] for i in ynImpl]
plt.plot(xImpl, yImpl, color = 'yellow', label='impl')

y = [method.fy(i) for i in  xImpl]
z = [method.fz(i) for i in  xImpl]
plt.plot(xImpl, y, '--b', label = 'yx')
plt.plot(xImpl, z, '--r', label = 'zx')
plt.suptitle('Численная траектория')
plt.legend(loc='upper right')
plt.grid()
plt.show()