#inizio codice
#utilizzo la libreia  numpy e pandas

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#attraverso python e con l'aiuto di excel documento i miei progressi in palestra

print(" settimana di ferragosto")
x = np.array(["lunedi","martedi","mercoledi","giovedi","venerdi","sabato","domenica"])
y = np.array([75.6,75.20,75.20,74.85,74.35,74.35,75.20])

plt.plot(x, y)

plt.xlabel("giorni")
plt.ylabel("peso")


plt.show()


print("settimana dopo ferragosto")
x = np.array(["lunedi","martedi","mercoledi","giovedi","venerdi","sabato","domenica"])
y = np.array([74.35,74,74.30,74,74.35,74.32,73.90])

plt.plot(x, y)

plt.xlabel("giorni")
plt.ylabel("peso")


plt.show()

#documento gli ultimi giorni di agosto

print("ultimi giorni di agosto")
x = np.array(["lunedi","martedi","mercoledi"])
y = np.array([74.35,73.9,74.35])

plt.plot(x, y)

plt.xlabel("giorni")
plt.ylabel("peso")


plt.show()

#calcolo medie carico esercizi
try:

    esercizio=input("inserisci il nome  dell'esercizio: ")
    print(esercizio)

    serie=int(input("inserisci quante serie fai: "))
    
    kg1=float(input("inserisci i kili: "))
    kg2=float(input("inserisci i kili: "))
    kg3=float(input("inserisci i kili: "))
    
    if serie == 2:
        
        media=(kg1+kg2)/2
        print("la media dell'esercizio "+str(media))
    elif serie > 2:
        media=(kg1+kg2+kg3)/3
        print("la media è"+str(media))
    else:
        print("dati inseriti non corretti")


except:
    print("dati inseriti non corretti")



try:
    bike=float(input("inserisci quanti kilometri fai con la bici: "))
    ciclette=float(input("inserisci quanti km fai con la cyclette: "))
    tappeto=float(input("inserisci quanti km fai con il tappeto: "))
    media=(bike+ciclette+tappeto)/3
    print("la media dei km è:"+str(media))
except:
    print("dati inseriti non corretti")

#do il comando di aprire un file in jsonata

print("confronto peso e altezza con i famigliari")

df = pd.read_json('famiglia.json')

print(df.to_string()) 


        
#fine codice


print("****** THE AND *********")