import os
from nltk import SnowballStemmer
import math
from nltk import word_tokenize
import sys

def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            r.append(os.path.join(root, name))
    return r

def reci_za_txt(document):
    bagOfWordsA = []

    s = SnowballStemmer("english")

    with open(document, "r", encoding="utf-8") as documentAs:
        lines = documentAs.read()
        a = word_tokenize(lines)
        for i in a:
            if (i.isalnum()):
                e = s.stem(i)
                bagOfWordsA.append(e)
    return bagOfWordsA

def numOfWords(bagOfWordsA1):
    uniqueWords = set(bagOfWordsA1)
    numOfWordsA = dict.fromkeys(uniqueWords, 0)
    for word in bagOfWordsA1:
        numOfWordsA[word] += 1
    return numOfWordsA

def computeIDF(documents, bagOfWordsA1):
    N = len(documents)
    idfDict = dict.fromkeys(bagOfWordsA1, 0)

    for document1 in documents:
        for word in bagOfWordsA1:
            if word in document1:
                idfDict[word] += 1
    for word, val in idfDict.items():
        idfDict[word] = math.log(N / float(val))
    return idfDict

def computeTFIDF(tfA, idfs):
    tfidf = {}
    for word, val in tfA.items():
        tfidf[word] = val * idfs[word]
    return tfidf

#dokumenti i podela reci
folder = input()
document = input()
files = list_files(folder)

bagOfWordsA1 = reci_za_txt(document)

#kreiranje recnika sa recima i njihovim ponavljanjem u datom fajlu
tfA = numOfWords(bagOfWordsA1)

# racunanje IDF za sve dokumente
niz=[]
for d in files:
    bagOfWordsB1 = reci_za_txt(d)
    tfB = set(bagOfWordsB1)
    niz.append(tfB)

idfs = computeIDF(niz, tfA)

# racunanje TF-IDF skora za sve reci u korpusu
tfidfA = computeTFIDF(tfA, idfs)
p = sorted(tfidfA, key=lambda x: (-tfidfA.get(x), x))

if(len(p)<10):
    kraj1=p[:]
else:
    kraj1=p[0:10]
kraj =""
for i in kraj1:
    kraj = kraj + i + "," + " "
kraj = kraj[0:-2]

from nltk.tokenize import sent_tokenize

def sve_recenice(fajl):
    gfg = open(fajl, "r", encoding="utf-8")
    lista = sent_tokenize(gfg.read())
    gfg.close()
    return lista

def reci_u_recenici(recenica):
    bagOfWordsA=[]
    s = SnowballStemmer("english")
    a=word_tokenize(recenica)
    for i in a:
        if (i.isalnum()):
            e = s.stem(i)
            bagOfWordsA.append(e)
    skup = set(bagOfWordsA)

    return bagOfWordsA, skup

recenice = {}
sveRecenice = sve_recenice(document)
recenice1={}
recenice2={}
br=0
for i in sveRecenice:
    recenice2[br] = i
    recenice1[i]=br
    br+=1
br=0
for i in sveRecenice:
    a, skup = reci_u_recenici(i)
    skup1=numOfWords(a)
    tfidfk = {}
    for j in skup:
        tfidfk[j]=tfidfA[j]
    t = sorted(tfidfk, key=lambda x: (-tfidfk.get(x), x))
    p=[]
    s1=0
    br1=[]
    for ll in t:
        p.append(ll)
        kkk=10-s1
        s1=s1+skup1[ll]
        if(s1>=10):
            br1.append(kkk)
            break
        br1.append(skup1[ll])

    p1 = {}
    brt={}
    s1=0
    for j in p:
        brt[j]=br1[s1]
        s1=s1+1
        p1[j] = tfidfk[j]

    suma=0
    for j in p:
        suma=suma+brt[j]*p1[j]
    recenice[br]=suma
    br+=1

kuk = sorted(recenice.items(), key=lambda x: (x[1],x[0]), reverse=True)

krajnje=[]

br=0
for i,j in kuk:
    for i in recenice:
        if(recenice[i]==j):
            if(br<5):
                krajnje.append(i)
                recenice[i]=0
                br=br+1

krajnje1=[]
for i in krajnje:
    krajnje1.append(recenice2[i])

strr=""
for i in sveRecenice:
    if i in krajnje1:
        strr = strr + i + " "

strr=strr[0:-1]
sys.stdout.reconfigure(encoding='utf-8')
print(kraj)
print(strr)