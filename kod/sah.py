import imageio as imo
import numpy as np
import os
from PIL import Image

def W_sah(matrica,i,j,sah1):
    sah = sah1
    if matrica[i][j] == "k":
        i1, j1 = i, j
        z = 0
        while (matrica[i1][j1] == "0" or z == 0):
            z = 1
            i1 = i1 - 1
            if (i1 < 0):
                break
            if (matrica[i1][j1] == "R" or matrica[i1][j1] == "Q"):
                sah = "W"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
                break
            if (matrica[i1][j1] == "K" or matrica[i1][j1] == "r" or matrica[i1][j1] == "n" or matrica[i1][j1] == "b" or
                    matrica[i1][j1] == "q" or matrica[i1][j1] == "p"):
                break
        i1, j1 = i, j
        z = 0
        while (matrica[i1][j1] == "0" or z == 0):
            z = 1
            i1 = i1 + 1
            if (i1 >= 8):
                break
            if (matrica[i1][j1] == "R" or matrica[i1][j1] == "Q"):
                sah = "W"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
                break
            if (matrica[i1][j1] == "K" or matrica[i1][j1] == "r" or matrica[i1][j1] == "n" or matrica[i1][j1] == "b" or
                    matrica[i1][j1] == "q" or matrica[i1][j1] == "p"):
                break
        i1, j1 = i, j
        z = 0
        while (matrica[i1][j1] == "0" or z == 0):
            z = 1
            j1 = j1 - 1
            if (j1 < 0):
                break
            if (matrica[i1][j1] == "R" or matrica[i1][j1] == "Q"):
                sah = "W"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
                break
            if (matrica[i1][j1] == "K" or matrica[i1][j1] == "r" or matrica[i1][j1] == "n" or matrica[i1][j1] == "b" or
                    matrica[i1][j1] == "q" or matrica[i1][j1] == "p"):
                break
        i1, j1 = i, j
        z = 0
        while (matrica[i1][j1] == "0" or z == 0):
            z = 1
            j1 = j1 + 1
            if (j1 >= 8):
                break
            if (matrica[i1][j1] == "R" or matrica[i1][j1] == "Q"):
                sah = "W"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
                break
            if (matrica[i1][j1] == "K" or matrica[i1][j1] == "r" or matrica[i1][j1] == "n" or matrica[i1][j1] == "b" or
                    matrica[i1][j1] == "q" or matrica[i1][j1] == "p"):
                break

        i1, j1 = i, j
        z = 0
        while (matrica[i1][j1] == "0" or z == 0):
            z = 1
            j1 = j1 - 1
            i1 = i1 - 1
            if (j1 < 0 or i1 < 0):
                break
            if (matrica[i1][j1] == "B" or matrica[i1][j1] == "Q"):
                sah = "W"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
                break
            if (matrica[i1][j1] == "K" or matrica[i1][j1] == "r" or matrica[i1][j1] == "n" or matrica[i1][j1] == "b" or
                    matrica[i1][j1] == "q" or matrica[i1][j1] == "p"):
                break
        i1, j1 = i, j
        z = 0
        while (matrica[i1][j1] == "0" or z == 0):
            z = 1
            j1 = j1 + 1
            i1 = i1 + 1
            if (j1 >= 8 or i1 >= 8):
                break
            if (matrica[i1][j1] == "B" or matrica[i1][j1] == "Q"):
                sah = "W"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
                break
            if (matrica[i1][j1] == "K" or matrica[i1][j1] == "r" or matrica[i1][j1] == "n" or matrica[i1][j1] == "b" or
                    matrica[i1][j1] == "q" or matrica[i1][j1] == "p"):
                break
        i1, j1 = i, j
        z = 0
        while (matrica[i1][j1] == "0" or z == 0):
            z = 1
            j1 = j1 - 1
            i1 = i1 + 1
            if (j1 < 0 or i1 >= 8):
                break
            if (matrica[i1][j1] == "B" or matrica[i1][j1] == "Q"):
                sah = "W"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
                break
            if (matrica[i1][j1] == "K" or matrica[i1][j1] == "r" or matrica[i1][j1] == "n" or matrica[i1][j1] == "b" or
                    matrica[i1][j1] == "q" or matrica[i1][j1] == "p"):
                break
        i1, j1 = i, j
        z = 0
        while (matrica[i1][j1] == "0" or z == 0):
            z = 1
            j1 = j1 + 1
            i1 = i1 - 1
            if (j1 >= 8 or i1 < 0):
                break
            if (matrica[i1][j1] == "B" or matrica[i1][j1] == "Q"):
                sah = "W"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
                break
            if (matrica[i1][j1] == "K" or matrica[i1][j1] == "r" or matrica[i1][j1] == "n" or matrica[i1][j1] == "b" or
                    matrica[i1][j1] == "q" or matrica[i1][j1] == "p"):
                break

        i1, j1 = i - 2, j - 1
        if (j1 >= 8 or i1 < 0 or i1 >= 8 or j1 < 0):
            brojac1 = 0
        else:
            if (matrica[i1][j1] == "N"):
                sah = "W"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
        i1, j1 = i - 1, j - 2
        if (j1 >= 8 or i1 < 0 or i1 >= 8 or j1 < 0):
            brojac1 = 0
        else:
            if (matrica[i1][j1] == "N"):
                sah = "W"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
        i1, j1 = i - 2, j + 1
        if (j1 >= 8 or i1 < 0 or i1 >= 8 or j1 < 0):
            brojac1 = 0
        else:
            if (matrica[i1][j1] == "N"):
                sah = "W"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
        i1, j1 = i - 1, j + 2
        if (j1 >= 8 or i1 < 0 or i1 >= 8 or j1 < 0):
            brojac1 = 0
        else:
            if (matrica[i1][j1] == "N"):
                sah = "W"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
        i1, j1 = i + 1, j - 2
        if (j1 >= 8 or i1 < 0 or i1 >= 8 or j1 < 0):
            brojac1 = 0
        else:
            if (matrica[i1][j1] == "N"):
                sah = "W"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
        i1, j1 = i + 2, j - 1
        if (j1 >= 8 or i1 < 0 or i1 >= 8 or j1 < 0):
            brojac1 = 0
        else:
            if (matrica[i1][j1] == "N"):
                sah = "W"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
        i1, j1 = i + 2, j + 1
        if (j1 >= 8 or i1 < 0 or i1 >= 8 or j1 < 0):
            brojac1 = 0
        else:
            if (matrica[i1][j1] == "N"):
                sah = "W"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
        i1, j1 = i + 1, j + 2
        if (j1 >= 8 or i1 < 0 or i1 >= 8 or j1 < 0):
            brojac1 = 0
        else:
            if (matrica[i1][j1] == "N"):
                sah = "W"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)


        i1, j1 = i - 1, j - 1
        if (j1 >= 8 or i1 < 0 or i1 >= 8 or j1 < 0):
            brojac1 = 0
        else:
            if (matrica[i1][j1] == "P" or matrica[i1][j1] == "K"):
                sah = "W"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
        i1, j1 = i + 1, j + 1
        if (j1 >= 8 or i1 < 0 or i1 >= 8 or j1 < 0):
            brojac1 = 0
        else:
            if (matrica[i1][j1] == "P" or matrica[i1][j1] == "K"):
                sah = "W"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
        i1, j1 = i - 1, j + 1
        if (j1 >= 8 or i1 < 0 or i1 >= 8 or j1 < 0):
            brojac1 = 0
        else:
            if (matrica[i1][j1] == "P" or matrica[i1][j1] == "K"):
                sah = "W"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
        i1, j1 = i + 1, j - 1
        if (j1 >= 8 or i1 < 0 or i1 >= 8 or j1 < 0):
            brojac1 = 0
        else:
            if (matrica[i1][j1] == "P" or matrica[i1][j1] == "K"):
                sah = "W"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)

        i1, j1 = i, j - 1
        if (j1 >= 8 or i1 < 0 or i1 >= 8 or j1 < 0):
            brojac1 = 0
        else:
            if (matrica[i1][j1] == "K"):
                sah = "W"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
        i1, j1 = i+1, j
        if (j1 >= 8 or i1 < 0 or i1 >= 8 or j1 < 0):
            brojac1 = 0
        else:
            if (matrica[i1][j1] == "K"):
                sah = "W"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
        i1, j1 = i-1, j
        if (j1 >= 8 or i1 < 0 or i1 >= 8 or j1 < 0):
            brojac1 = 0
        else:
            if (matrica[i1][j1] == "K"):
                sah = "W"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
        i1, j1 = i, j + 1
        if (j1 >= 8 or i1 < 0 or i1 >= 8 or j1 < 0):
            brojac1 = 0
        else:
            if (matrica[i1][j1] == "K"):
                sah = "W"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)

    return sah

def B_sah(matrica,i,j,sah1):

    sah = sah1
    if matrica[i][j] == "K":
        i1, j1 = i, j
        z = 0
        while (matrica[i1][j1] == "0" or z == 0):
            z = 1
            i1 = i1 - 1
            if (i1 < 0):
                break
            if (matrica[i1][j1] == "r" or matrica[i1][j1] == "q"):
                sah = "B"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
                break
            if (matrica[i1][j1] == "k" or matrica[i1][j1] == "R" or matrica[i1][j1] == "N" or matrica[i1][j1] == "B" or
                    matrica[i1][j1] == "Q" or matrica[i1][j1] == "P"):
                break
        i1, j1 = i, j
        z = 0
        while (matrica[i1][j1] == "0" or z == 0):
            z = 1
            i1 = i1 + 1
            if (i1 >= 8):
                break
            if (matrica[i1][j1] == "r" or matrica[i1][j1] == "q"):
                sah = "B"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
                break
            if (matrica[i1][j1] == "k" or matrica[i1][j1] == "R" or matrica[i1][j1] == "N" or matrica[i1][j1] == "B" or
                    matrica[i1][j1] == "Q" or matrica[i1][j1] == "P"):
                break
        i1, j1 = i, j
        z = 0
        while (matrica[i1][j1] == "0" or z == 0):
            z = 1
            j1 = j1 - 1
            if (j1 < 0):
                break
            if (matrica[i1][j1] == "r" or matrica[i1][j1] == "q"):
                sah = "B"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
                break
            if (matrica[i1][j1] == "k" or matrica[i1][j1] == "R" or matrica[i1][j1] == "N" or matrica[i1][j1] == "B" or
                    matrica[i1][j1] == "Q" or matrica[i1][j1] == "P"):
                break
        i1, j1 = i, j
        z = 0
        while (matrica[i1][j1] == "0" or z == 0):
            z = 1
            j1 = j1 + 1
            if (j1 >= 8):
                break
            if (matrica[i1][j1] == "r" or matrica[i1][j1] == "q"):
                sah = "B"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
                break
            if (matrica[i1][j1] == "k" or matrica[i1][j1] == "R" or matrica[i1][j1] == "N" or matrica[i1][j1] == "B" or
                    matrica[i1][j1] == "Q" or matrica[i1][j1] == "P"):
                break

        i1, j1 = i, j
        z = 0
        while (matrica[i1][j1] == "0" or z == 0):
            z = 1
            j1 = j1 - 1
            i1 = i1 - 1
            if (j1 < 0 or i1 < 0):
                break
            if (matrica[i1][j1] == "b" or matrica[i1][j1] == "q"):
                sah = "B"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
                break
            if (matrica[i1][j1] == "k" or matrica[i1][j1] == "R" or matrica[i1][j1] == "N" or matrica[i1][j1] == "B" or
                    matrica[i1][j1] == "Q" or matrica[i1][j1] == "P"):
                break
        i1, j1 = i, j
        z = 0
        while (matrica[i1][j1] == "0" or z == 0):
            z = 1
            j1 = j1 + 1
            i1 = i1 + 1
            if (j1 >= 8 or i1 >= 8):
                break
            if (matrica[i1][j1] == "b" or matrica[i1][j1] == "q"):
                sah = "B"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
                break
            if (matrica[i1][j1] == "k" or matrica[i1][j1] == "R" or matrica[i1][j1] == "N" or matrica[i1][j1] == "B" or
                    matrica[i1][j1] == "Q" or matrica[i1][j1] == "P"):
                break
        i1, j1 = i, j
        z = 0
        while (matrica[i1][j1] == "0" or z == 0):
            z = 1
            j1 = j1 - 1
            i1 = i1 + 1
            if (j1 < 0 or i1 >= 8):
                break
            if (matrica[i1][j1] == "b" or matrica[i1][j1] == "q"):
                sah = "B"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
                break
            if (matrica[i1][j1] == "k" or matrica[i1][j1] == "R" or matrica[i1][j1] == "N" or matrica[i1][j1] == "B" or
                    matrica[i1][j1] == "Q" or matrica[i1][j1] == "P"):
                break
        i1, j1 = i, j
        z = 0
        while (matrica[i1][j1] == "0" or z == 0):
            z = 1
            j1 = j1 + 1
            i1 = i1 - 1
            if (j1 >= 8 or i1 < 0):
                break
            if (matrica[i1][j1] == "b" or matrica[i1][j1] == "q"):
                sah = "B"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
                break
            if (matrica[i1][j1] == "k" or matrica[i1][j1] == "R" or matrica[i1][j1] == "N" or matrica[i1][j1] == "B" or
                    matrica[i1][j1] == "Q" or matrica[i1][j1] == "P"):
                break

        i1, j1 = i - 2, j - 1
        if (j1 >= 8 or i1 < 0 or i1 >= 8 or j1 < 0):
            brojac1 = 0
        else:
            if (matrica[i1][j1] == "n"):
                sah = "B"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
        i1, j1 = i - 1, j - 2
        if (j1 >= 8 or i1 < 0 or i1 >= 8 or j1 < 0):
            brojac1 = 0
        else:
            if (matrica[i1][j1] == "n"):
                sah = "B"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
        i1, j1 = i - 2, j + 1
        if (j1 >= 8 or i1 < 0 or i1 >= 8 or j1 < 0):
            brojac1 = 0
        else:
            if (matrica[i1][j1] == "n"):
                sah = "B"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
        i1, j1 = i - 1, j + 2
        if (j1 >= 8 or i1 < 0 or i1 >= 8 or j1 < 0):
            brojac1 = 0
        else:
            if (matrica[i1][j1] == "n"):
                sah = "B"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
        i1, j1 = i + 1, j - 2
        if (j1 >= 8 or i1 < 0 or i1 >= 8 or j1 < 0):
            brojac1 = 0
        else:
            if (matrica[i1][j1] == "n"):
                sah = "B"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
        i1, j1 = i + 2, j - 1
        if (j1 >= 8 or i1 < 0 or i1 >= 8 or j1 < 0):
            brojac1 = 0
        else:
            if (matrica[i1][j1] == "n"):
                sah = "B"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
        i1, j1 = i + 2, j + 1
        if (j1 >= 8 or i1 < 0 or i1 >= 8 or j1 < 0):
            brojac1 = 0
        else:
            if (matrica[i1][j1] == "n"):
                sah = "B"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
        i1, j1 = i + 1, j + 2
        if (j1 >= 8 or i1 < 0 or i1 >= 8 or j1 < 0):
            brojac1 = 0
        else:
            if (matrica[i1][j1] == "n"):
                sah = "B"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)


        i1, j1 = i - 1, j - 1
        if (j1 >= 8 or i1 < 0 or i1 >= 8 or j1 < 0):
            brojac1 = 0
        else:
            if (matrica[i1][j1] == "p" or matrica[i1][j1] == "k"):
                sah = "B"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
        i1, j1 = i + 1, j + 1
        if (j1 >= 8 or i1 < 0 or i1 >= 8 or j1 < 0):
            brojac1 = 0
        else:
            if (matrica[i1][j1] == "p" or matrica[i1][j1] == "k"):
                sah = "B"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
        i1, j1 = i - 1, j + 1
        if (j1 >= 8 or i1 < 0 or i1 >= 8 or j1 < 0):
            brojac1 = 0
        else:
            if (matrica[i1][j1] == "p" or matrica[i1][j1] == "k"):
                sah = "B"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
        i1, j1 = i + 1, j - 1
        if (j1 >= 8 or i1 < 0 or i1 >= 8 or j1 < 0):
            brojac1 = 0
        else:
            if (matrica[i1][j1] == "p" or matrica[i1][j1] == "k"):
                sah = "B"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)

        i1, j1 = i, j - 1
        if (j1 >= 8 or i1 < 0 or i1 >= 8 or j1 < 0):
            brojac1 = 0
        else:
            if (matrica[i1][j1] == "k"):
                sah = "B"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
        i1, j1 = i + 1, j
        if (j1 >= 8 or i1 < 0 or i1 >= 8 or j1 < 0):
            brojac1 = 0
        else:
            if (matrica[i1][j1] == "k"):
                sah = "B"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
        i1, j1 = i - 1, j
        if (j1 >= 8 or i1 < 0 or i1 >= 8 or j1 < 0):
            brojac1 = 0
        else:
            if (matrica[i1][j1] == "k"):
                sah = "B"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)
        i1, j1 = i, j + 1
        if (j1 >= 8 or i1 < 0 or i1 >= 8 or j1 < 0):
            brojac1 = 0
        else:
            if (matrica[i1][j1] == "k"):
                sah = "B"
                lista1 = []
                lista1.append(i1)
                lista1.append(j1)
                lista_napadaca.append(lista1)

    return sah


def slika(putanja):
    filelist=os.listdir(putanja)
    for fichier in filelist[:]:
        if not(fichier.endswith(".png")):
            filelist.remove(fichier)
    return filelist

def sumpi(slika, d):
    sumpix = 0
    suma_belih = 0
    suma_crnih = 0
    for x in range(d):
        for y in range(d):
            r,g,b = slika.load()[x,y]
            if(r!=240 or g!=217 or b!=183) and (r != 180 or g != 136 or b != 102):
                sumpix += 1
            if (r == 255 and g == 255 and b == 255):
                suma_belih += 1
            if (r == 0 and g == 0 and b == 0):
                suma_crnih += 1
    return sumpix, suma_belih, suma_crnih

def suma1(slika, d):
    sump = 0
    suma_belih = 0
    for x in range(d):
        r,g,b = slika.load()[x,15]
        if (r == 0 and g == 0 and b == 0):
            sump += 1
        if (r == 255 and g == 255 and b == 255):
            suma_belih += 1
    return sump, suma_belih

putanja = input()
slika_table = slika(putanja)
putanja1 = putanja +'/' + slika_table[0]
img = imo.imread(putanja1)

not_black = np.array(np.where(img != 0))
koordinate = not_black[:,0]
x, y = koordinate[0], koordinate[1]
koordinate_str = str(x) + "," + str(y)
print(koordinate_str)

d = x
r, g, b = img[x,y]
xa = x
while(r==240 and g==217 and b==183):
    xa = xa+1
    r, g, b = img[xa, y]
d = xa - d

putanja_polja = putanja +'/' + "tiles"
putanja_figure_bele = putanja + '/' + "pieces" + '/' + "white"
putanja_figure_crne = putanja + '/' + "pieces" + '/' + "black"
img_polja, img_figure_bele, img_figure_crne = slika(putanja_polja), slika(putanja_figure_bele), slika(putanja_figure_crne)


tabla = np.zeros((8,8))
image = Image.open(putanja1)
lista = []

br=0
matrica=[]
for x1 in range(8):
    matrica1=[]
    for y1 in range(8):
        polozaj_x, polozaj_y = x+x1*d, y+y1*d
        cropped_image = image.crop((polozaj_y, polozaj_x, polozaj_y + d, polozaj_x + d))
        suma_piksela, suma_belih_piksela, suma_crnih_piksela = sumpi(cropped_image, d)
        if(suma_piksela==0):
            matrica1.append("0")
            br+=1
        if(suma_piksela==314):
            if(br!=0):
                lista.append(br)
                br=0
            if(suma_belih_piksela>suma_crnih_piksela):
                lista.append("R")
                matrica1.append("R")
            else:
                lista.append("r")
                matrica1.append("r")
        if (suma_piksela == 364):
            if (br != 0):
                lista.append(br)
                br = 0
            if (suma_belih_piksela > suma_crnih_piksela):
                lista.append("N")
                matrica1.append("N")
            else:
                c, b = suma1(cropped_image,d)
                if(c>b):
                    lista.append("n")
                    matrica1.append("n")
                else:
                    lista.append("Q")
                    matrica1.append("Q")
        if (suma_piksela == 252):
            if (br != 0):
                lista.append(br)
                br = 0
            if (suma_belih_piksela > suma_crnih_piksela):
                lista.append("B")
                matrica1.append("B")
            else:
                lista.append("b")
                matrica1.append("b")
        if (suma_piksela == 372):
            if (br != 0):
                lista.append(br)
                br = 0
            lista.append("q")
            matrica1.append("q")
        if (suma_piksela == 324):
            if (br != 0):
                lista.append(br)
                br = 0
            if (suma_belih_piksela > suma_crnih_piksela):
                lista.append("K")
                matrica1.append("K")
            else:
                lista.append("k")
                matrica1.append("k")
        if (suma_piksela == 230):
            if (br != 0):
                lista.append(br)
                br = 0
            if (suma_belih_piksela > suma_crnih_piksela):
                lista.append("P")
                matrica1.append("P")
            else:
                lista.append("p")
                matrica1.append("p")
        if(y1==7 and br!=0):
            lista.append(br)
            br=0
    lista.append("/")
    matrica.append(matrica1)

string=""
for brojac in lista:
    string=string+str(brojac)
string=string[0:-1]
print(string)

sah="-"

lista_napadaca = []

for i in range(8):
    for j in range(8):
        sah = W_sah(matrica, i, j, sah)
        sah = B_sah(matrica, i, j, sah)

lista_napadaca1 = lista_napadaca[:]
print(sah)

mat = 1
if(sah == "-"):
    mat = 0
else:
    for i in range(8):
        for j in range(8):
            if(sah == "W" and matrica[i][j] == "k"):
                i1, j1 = i - 1, j - 1
                if(i1 >= 0 and j1 >= 0 and i1 < 8 and j1 < 8):
                    element1 = matrica[i1][j1]
                    if(element1 == "r" or element1 == "n" or element1 == "b" or element1 == "q" or element1 == "p"):
                        brojac1=0
                    else:
                        matrica[i1][j1] = "k"
                        matrica[i][j] = "0"
                        sah1 = "-"
                        a = W_sah(matrica, i1, j1, sah1)
                        if(a == "-"):
                            mat = 0
                        matrica[i1][j1] = element1
                        matrica[i][j] = "k"

                i1, j1 = i, j - 1
                if (i1 >= 0 and j1 >= 0 and i1 < 8 and j1 < 8):
                    element1 = matrica[i1][j1]
                    if (element1 == "r" or element1 == "n" or element1 == "b" or element1 == "q" or element1 == "p"):
                        brojac1 = 0
                    else:
                        matrica[i1][j1] = "k"
                        matrica[i][j] = "0"
                        sah1 = "-"
                        a = W_sah(matrica, i1, j1, sah1)
                        if (a == "-"):
                            mat = 0
                        matrica[i1][j1] = element1
                        matrica[i][j] = "k"

                i1, j1 = i + 1, j - 1
                if (i1 >= 0 and j1 >= 0 and i1 < 8 and j1 < 8):
                    element1 = matrica[i1][j1]
                    if (element1 == "r" or element1 == "n" or element1 == "b" or element1 == "q" or element1 == "p"):
                        brojac1 = 0
                    else:
                        matrica[i1][j1] = "k"
                        matrica[i][j] = "0"
                        sah1 = "-"
                        a = W_sah(matrica, i1, j1, sah1)
                        if (a == "-"):
                            mat = 0
                        matrica[i1][j1] = element1
                        matrica[i][j] = "k"

                i1, j1 = i - 1, j
                if (i1 >= 0 and j1 >= 0 and i1 < 8 and j1 < 8):
                    element1 = matrica[i1][j1]
                    if (element1 == "r" or element1 == "n" or element1 == "b" or element1 == "q" or element1 == "p"):
                        brojac1 = 0
                    else:
                        matrica[i1][j1] = "k"
                        matrica[i][j] = "0"
                        sah1 = "-"
                        a = W_sah(matrica, i1, j1, sah1)
                        if (a == "-"):
                            mat = 0
                        matrica[i1][j1] = element1
                        matrica[i][j] = "k"

                i1, j1 = i +1, j
                if (i1 >= 0 and j1 >= 0 and i1 < 8 and j1 < 8):
                    element1 = matrica[i1][j1]
                    if (element1 == "r" or element1 == "n" or element1 == "b" or element1 == "q" or element1 == "p"):
                        brojac1 = 0
                    else:
                        matrica[i1][j1] = "k"
                        matrica[i][j] = "0"
                        sah1 = "-"
                        a = W_sah(matrica, i1, j1, sah1)
                        if (a == "-"):
                            mat = 0
                        matrica[i1][j1] = element1
                        matrica[i][j] = "k"

                i1, j1 = i - 1, j + 1
                if (i1 >= 0 and j1 >= 0 and i1 < 8 and j1 < 8):
                    element1 = matrica[i1][j1]
                    if (element1 == "r" or element1 == "n" or element1 == "b" or element1 == "q" or element1 == "p"):
                        brojac1 = 0
                    else:
                        matrica[i1][j1] = "k"
                        matrica[i][j] = "0"
                        sah1 = "-"
                        a = W_sah(matrica, i1, j1, sah1)
                        if (a == "-"):
                            mat = 0
                        matrica[i1][j1] = element1
                        matrica[i][j] = "k"

                i1, j1 = i, j + 1
                if (i1 >= 0 and j1 >= 0 and i1 < 8 and j1 < 8):
                    element1 = matrica[i1][j1]
                    if (element1 == "r" or element1 == "n" or element1 == "b" or element1 == "q" or element1 == "p"):
                        brojac1 = 0
                    else:
                        matrica[i1][j1] = "k"
                        matrica[i][j] = "0"
                        sah1 = "-"
                        a = W_sah(matrica, i1, j1, sah1)
                        if (a == "-"):
                            mat = 0
                        matrica[i1][j1] = element1
                        matrica[i][j] = "k"

                i1, j1 = i + 1, j + 1
                if (i1 >= 0 and j1 >= 0 and i1 < 8 and j1 < 8):
                    element1 = matrica[i1][j1]
                    if (element1 == "r" or element1 == "n" or element1 == "b" or element1 == "q" or element1 == "p"):
                        brojac1 = 0
                    else:
                        matrica[i1][j1] = "k"
                        matrica[i][j] = "0"
                        sah1 = "-"
                        a = W_sah(matrica, i1, j1, sah1)
                        if (a == "-"):
                            mat = 0
                        matrica[i1][j1] = element1
                        matrica[i][j] = "k"
            if (sah == "B" and matrica[i][j] == "K"):

                i1, j1 = i - 1, j - 1
                if (i1 >= 0 and j1 >= 0 and i1 < 8 and j1 < 8):
                    element1 = matrica[i1][j1]
                    if (element1 == "R" or element1 == "N" or element1 == "B" or element1 == "Q" or element1 == "P"):
                        brojac1 = 0
                    else:
                        matrica[i1][j1] = "K"
                        matrica[i][j] = "0"
                        sah1 = "-"
                        a = B_sah(matrica, i1, j1, sah1)
                        if (a == "-"):
                            mat = 0
                        matrica[i1][j1] = element1
                        matrica[i][j] = "K"

                i1, j1 = i, j - 1
                if (i1 >= 0 and j1 >= 0 and i1 < 8 and j1 < 8):
                    element1 = matrica[i1][j1]
                    if (element1 == "R" or element1 == "N" or element1 == "B" or element1 == "Q" or element1 == "P"):
                        brojac1 = 0
                    else:
                        matrica[i1][j1] = "K"
                        matrica[i][j] = "0"
                        sah1 = "-"
                        a = B_sah(matrica, i1, j1, sah1)
                        if (a == "-"):
                            mat = 0
                        matrica[i1][j1] = element1
                        matrica[i][j] = "K"

                i1, j1 = i + 1, j - 1
                if (i1 >= 0 and j1 >= 0 and i1 < 8 and j1 < 8):
                    element1 = matrica[i1][j1]
                    if (element1 == "R" or element1 == "N" or element1 == "B" or element1 == "Q" or element1 == "P"):
                        brojac1 = 0
                    else:
                        matrica[i1][j1] = "K"
                        matrica[i][j] = "0"
                        sah1 = "-"
                        a = B_sah(matrica, i1, j1, sah1)
                        if (a == "-"):
                            mat = 0
                        matrica[i1][j1] = element1
                        matrica[i][j] = "K"

                i1, j1 = i - 1, j
                if (i1 >= 0 and j1 >= 0 and i1 < 8 and j1 < 8):
                    element1 = matrica[i1][j1]
                    if (element1 == "R" or element1 == "N" or element1 == "B" or element1 == "Q" or element1 == "P"):
                        brojac1 = 0
                    else:
                        matrica[i1][j1] = "K"
                        matrica[i][j] = "0"
                        sah1 = "-"
                        a = B_sah(matrica, i1, j1, sah1)
                        if (a == "-"):
                            mat = 0
                        matrica[i1][j1] = element1
                        matrica[i][j] = "K"

                i1, j1 = i + 1, j
                if (i1 >= 0 and j1 >= 0 and i1 < 8 and j1 < 8):
                    element1 = matrica[i1][j1]
                    if (element1 == "R" or element1 == "N" or element1 == "B" or element1 == "Q" or element1 == "P"):
                        brojac1 = 0
                    else:
                        matrica[i1][j1] = "K"
                        matrica[i][j] = "0"
                        sah1 = "-"
                        a = B_sah(matrica, i1, j1, sah1)
                        if (a == "-"):
                            mat = 0
                        matrica[i1][j1] = element1
                        matrica[i][j] = "K"

                i1, j1 = i - 1, j + 1
                if (i1 >= 0 and j1 >= 0 and i1 < 8 and j1 < 8):
                    element1 = matrica[i1][j1]
                    if (element1 == "R" or element1 == "N" or element1 == "B" or element1 == "Q" or element1 == "P"):
                        brojac1 = 0
                    else:
                        matrica[i1][j1] = "K"
                        matrica[i][j] = "0"
                        sah1 = "-"
                        a = B_sah(matrica, i1, j1, sah1)
                        if (a == "-"):
                            mat = 0
                        matrica[i1][j1] = element1
                        matrica[i][j] = "K"

                i1, j1 = i, j + 1
                if (i1 >= 0 and j1 >= 0 and i1 < 8 and j1 < 8):
                    element1 = matrica[i1][j1]
                    if (element1 == "R" or element1 == "N" or element1 == "B" or element1 == "Q" or element1 == "P"):
                        brojac1 = 0
                    else:
                        matrica[i1][j1] = "K"
                        matrica[i][j] = "0"
                        sah1 = "-"
                        a = B_sah(matrica, i1, j1, sah1)
                        if (a == "-"):
                            mat = 0
                        matrica[i1][j1] = element1
                        matrica[i][j] = "K"

                i1, j1 = i + 1, j + 1
                if (i1 >= 0 and j1 >= 0 and i1 < 8 and j1 < 8):
                    element1 = matrica[i1][j1]
                    if (element1 == "R" or element1 == "N" or element1 == "B" or element1 == "Q" or element1 == "P"):
                        brojac1 = 0
                    else:
                        matrica[i1][j1] = "K"
                        matrica[i][j] = "0"
                        sah1 = "-"
                        a = B_sah(matrica, i1, j1, sah1)
                        if (a == "-"):
                            mat = 0
                        matrica[i1][j1] = element1
                        matrica[i][j] = "K"

    if(mat == 1):
        if(len(lista_napadaca1)>1):
            brojac1 = 0
        elif len(lista_napadaca1)==0:
            mat = 0
        else:
            napadac = matrica[lista_napadaca1[0][0]][lista_napadaca1[0][1]]
            if(napadac == "r" or napadac == "n" or napadac == "b" or napadac == "q" or napadac == "k" or napadac == "p"):
                for i in range(8):
                    for j in range(8):
                        if(matrica[i][j]=="K"):
                            matrica[i][j] = "0"
                matrica[lista_napadaca1[0][0]][lista_napadaca1[0][1]] = "k"
                sah1 = "-"
                a = W_sah(matrica, lista_napadaca1[0][0], lista_napadaca1[0][1], sah1)
                br = 0
                for i in range(8):
                    for j in range(8):
                        if (matrica[i][j] == "R" or matrica[i][j] == "N" or matrica[i][j] == "B" or matrica[i][
                            j] == "Q" or matrica[i][j] == "K" or matrica[i][j] == "P"):
                            br += 1
                if (br == 0):
                    a = "-"
                if(a == "W"):
                    mat = 0

            if (napadac == "R" or napadac == "N" or napadac == "B" or napadac == "Q" or napadac == "K" or napadac == "P"):
                for i in range(8):
                    for j in range(8):
                        if(matrica[i][j]=="k"):
                            matrica[i][j] = "0"

                matrica[lista_napadaca1[0][0]][lista_napadaca1[0][1]] = "K"
                sah1 = "-"
                a = B_sah(matrica, lista_napadaca1[0][0],lista_napadaca1[0][1], sah1)
                br = 0
                for i in range(8):
                    for j in range(8):
                        if (matrica[i][j] == "r" or matrica[i][j] == "n" or matrica[i][j] == "b" or matrica[i][
                            j] == "q" or matrica[i][j] == "k" or matrica[i][j] == "p"):
                            br += 1
                if (br == 0):
                    a = "-"
                if (a == "B"):
                    mat = 0

print(mat)
