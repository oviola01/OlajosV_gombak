"""A.	Kérj be 5 egész számot a felhasználótól, melyek az egyes személyek korát jelentik! [0,120] (4p)
B.	A bekért  értékeket tárolja lista adatszerkezetben! (1p)
C.	Írasd ki a képernyőre a számokat : -tal (kettősponttal) elválasztva. A : jel csak az értékek között szerepeljen (a végén, elején ne)! (2p)
D.	Írj függvényt elso_idos néven, ami megkeresi az első  70 év feletti kort. A visszatérési érték legyen egy egész szám, melynek a kornak az INDEX-ét tartalmazza, a függvény bemenete a lista! (3p)
E.	Az elso_idos függvény eredményét írasd ki a mintának megfelelően a konzolra, amit konzolra_ir nevű metódusban fogalmazz meg! (2p)
F.	Az elso_idos függvény eredményét írasd ki a mintának megfelelően a oreg.txt nevű fájlba, amit fajl_ir nevű metódusban fogalmazzon meg! (2p)
"""

def bekeres(lista):
    i = 1
    while len(lista) < 5:
        ember_kor = int(input(f"Kérlek add meg az {i}. ember korát! "))
        if ember_kor < 0 or ember_kor > 120:
            ember_kor = int(input(f"Kérlek 0 és 120 közötti számot adj meg! "))
        lista.append(ember_kor)
        i += 1

def elvalasztas(lista):
    kiiras = ""
    i = 0
    while i < len(lista):
        kiiras += str(lista[i])
        if i < len(lista)-1:
            kiiras += ":"
        i+= 1
    print(f"II/A, B, C:\n\t{kiiras}")

def elso_idos(lista):
    i = 0
    while i < len(lista)-1 and lista[i] < 70:
        i += 1
    return i

def konzolra_ir(lista, index):
    eredmeny = ""
    if lista[index] < 70:
        eredmeny = str(f"II/D, E:\n\tSajnos nincs olyan személy a listában, aki már betöltötte a a hetvenet.")
    else:
        eredmeny = str(f"II/D, E:\n\tElső idős ember korának helye a listában: {index}")
    print(eredmeny)
    return eredmeny

def fajl_ir(szoveg):
    fajlom = open("oreg.txt","w",encoding="UTF-8")
    fajlom.write(szoveg)
    fajlom.close
    fajlom = open("oreg.txt","r",encoding="UTF-8")
    tartalom = fajlom.read()
    fajlom.close
    print(f"oreg.txt tartalma:\n{tartalom}")
            