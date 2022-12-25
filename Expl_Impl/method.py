from numpy import linalg, array
from matplotlib import pyplot as plt
from json import dump
from math import exp

class Method:
    def __init__(subj, A, h, y0, x0, x_final):
        subj.initState = (x0, y0)

        subj.h = h
        subj.x = x0
        subj.yn = y0
        subj.b = x_final
        subj.A = array(A)
        subj.E = array(identityMatrix(len(A)))
        subj.explK = subj.explicitK()
        subj.implK = subj.implicitK()

    def explicitK(subj):
        A = subj.A.dot(subj.A)
        k = subj.E + subj.h * subj.A + (0.5 * subj.h**2) * A
        return k
    
    def implicitK(subj):
        invMatrix = linalg.inv(subj.E - subj.h * 0.25 * subj.A)
        k1 = invMatrix.dot(subj.A)
        k2 = subj.E + subj.h * 2 * k1 + (0.75 * subj.h ** 2) * (k1.dot(k1))
        return k2

    def explMeth(subj):
        n = int((subj.b - subj.x)/subj.h)
        xvector = [subj.x]
        yvector = [subj.yn]
        for _ in range (1, int(n+1)):
            subj.x += subj.h
            xvector.append(subj.x)
            subj.yn = subj.explK.dot(subj.yn)
            yvector.append(list(subj.yn))
        write(xvector, yvector)
        subj.x, subj.yn = subj.initState

    def implMeth(subj):
        n = int((subj.b - subj.x)/subj.h)
        xvector = [subj.x]
        yvector = [subj.yn]
        for _ in range (1, int(n+1)):
            subj.x += subj.h
            xvector.append(subj.x)
            subj.yn = subj.implK.dot(subj.yn)
            yvector.append(list(subj.yn))
        write(xvector, yvector)
        subj.x, subj.yn = subj.initState

    def eiginNumb(subj):
        numbList = linalg.eigvals(subj.A)
        S = min(numbList)/max(numbList)
        return f'Собственные числа = {numbList}, Коэффициент жесткости системы = {S}'

def write(xvector, yvector):
    with open("output.json", "w") as file:
        dump({"xvector": xvector, "yvector": yvector}, file)

def fy(x):
    return 4*exp(-x)-3*exp(-1000*x)

def fz(x):
    return 3*exp(-1000*x)-2*exp(-x)

def identityMatrix(m):
    return [[1 if i == j else 0 for j in range(m)] for i in range(m)]

