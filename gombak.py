"""A.	Olvassa be osztály segítségével (utóbbit hozza létre külön modulban) a gombák.txt fájlból a játékosok adatait, és tárolja el összetett adatszerkezetben, ami elősegíti a további feladatok könnyű megoldását! Ügyeljen arra, hogy az állomány első sora az adatok fejlécét tartalmazza! (7p)
B.	Írassa ki a gombák számát a mintának megfelelően a konzolra! A metódus neve legyen gombak_szama! (2p)
C.	Határozza meg és írassa ki a konzolra a minta szerint, hogy a melyik a papsapkagombák nemzettségben melyik az első gomba, amelyik szerepel a listában?  A metódus neve legyen papsapka! (4p)
D.	Írassa ki konzolra a mintának megfelelően a tinóru nemzettséghez tartozó gombák számát! A metódus neve tinoru legyen  (4p)
"""

from Gombaosztaly import Gombaosztaly
gomba_lista = []

def fajl_beolv():
    gombafajl = open("gombak_jav.txt","r",encoding="UTF-8")
    fejlec = gombafajl.readline()
    tartalom = gombafajl.readlines()
    gombafajl.close
    i = 0
    while i < len(tartalom):
        sor = tartalom[i].strip().split("@")
        gomba_lista.append(Gombaosztaly(sor))
        i += 1

def gombak_szama():
    print(f"III/A, B:\n\tA gombák száma: {len(gomba_lista)}")

def papsapka():
    i = 0
    while i < len(gomba_lista)-1 and gomba_lista[i].nemzettseg != "papsapkagombák ":
        i += 1
    if gomba_lista[i].nemzettseg == "papsapkagombák ":
        print(f"III/C:\n\tAz első papsapkagomba neve: {gomba_lista[i].gombaneve}")
    else:
        print(f"III/C:\n\tSajnos egyetlen papsapkagomba sincs a listában.")
        
def tinoru():
    ossz_tinoru = 0
    i = 0
    while i < len(gomba_lista)-1:
        if gomba_lista[i].nemzettseg == "tinóru":
            ossz_tinoru += 1
        i += 1
    print(f"III/D:\n\tA tinóru gombák száma: {ossz_tinoru}")



