import math
import numpy as np

def vreme(matrix1):
    suma1 = float(0)
    for i in matrix1:
        x = float(i[0])
        y = float(i[1])
        suma1 = suma1 + math.sqrt(x * x + y * y)
        i[0] = x - float(i[2])
        i[1] = y - float(i[3])
    t = -1
    suma=0
    k=0
    while(suma < suma1):
        if(t!=-1):
            suma1=suma
            suma=0
        t += 1
        for i in matrix1:
            x = float(i[0])
            y = float(i[1])
            suma = suma + math.sqrt(x * x + y * y)
            i[0] = x - float(i[2])
            i[1] = y - float(i[3])
    return t
def vreme1(matrix1):
    suma1 = float(0)
    for i in matrix1:
        i[0] = float(i[0]) - float(i[2])*float(200)
        i[1] = float(i[1]) - float(i[3])*float(200)
        suma1 = suma1 + math.sqrt(float(i[0])*float(i[0]) + float(i[1])*float(i[1]))
        i[0] = float(i[0]) - float(i[2])
        i[1] = float(i[1]) - float(i[3])
    suma = 0
    k = 0
    t=200
    while (suma < suma1):
        if (t != 200):
            suma1 = suma
            suma = 0
        t += 1
        for i in matrix1:
            x = float(i[0])
            y = float(i[1])
            suma = suma + math.sqrt(x * x + y * y)
            i[0] = x - float(i[2])
            i[1] = y - float(i[3])
    t=t-1
    return t
def odbijanje(matrix, s, t1, n, p):
    niz = np.zeros(n)
    s1 = -1*s
    broj_sudara = 0
    while (t1 > 0):
        a = 0
        for i in matrix:
            x = float(i[0])
            y = float(i[1])
            i[0] = x + float(i[2])
            i[1] = y + float(i[3])
            if(i[0]>=s):
                broj_sudara += 1
                i[0] =  s - (i[0] - s)
                i[2] = -1 * float(i[2])
                niz[a] += 1
            if (i[0] <= s1):
                broj_sudara += 1
                i[0] = s1 - (i[0] + s)
                i[2] = -1 * float(i[2])
                niz[a] += 1
            if (i[1] >= s):
                broj_sudara += 1
                i[1] = s - (i[1] - s)
                i[3] = -1 * float(i[3])
                niz[a] += 1
            if (i[1] <= s1):
                broj_sudara += 1
                i[1] = s1 - (i[1] + s)
                i[3] = -1 * float(i[3])
                niz[a] += 1
            a += 1
        t1 = t1 - 1
    verovatnoca = 0
    for i in niz:
        verovatnoca += p**i
    return broj_sudara, verovatnoca


linija = input().split()
n = int(linija[0])
matrix = []
for i in range(n):
    line = input().split()
    matrix.append(line)

matrix1 = np.array(matrix)
t = 0

if(n<1000):
    t = vreme(matrix1)
else:
    t = vreme1(matrix1)

broj_sudara, verovatnoca = odbijanje(matrix, float(linija[1]), int(linija[2]), int(linija[0]), float(linija[3]))
print(t,broj_sudara,verovatnoca)
