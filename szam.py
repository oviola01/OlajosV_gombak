"""A.	Generálj egy véletlen egész  számot az [1, 50] zárt intervallumban!  (2p)
B.	A program írja ki a következők egyikét: (a mintának megfelelően - 1p):
•	Amennyiben a szám 5-tel osztható:
“A szám öttel osztható!”,
•	Amennyiben a szám 3-mal osztható:
“A szám hárommal  osztható!”,
•	Amennyiben a szám 5-tel és 3 - mal is osztható:
“A szám öttel és hárommal is osztható!”,
"""

import random

def generalas():
    szam = int(random.random()*51)+1
    #feladat nem tér ki rá, mi van, ha egyikkel sem osztható, ezért ezt kiküszöbölöm
    while szam % 5 != 0 and szam % 3 != 0:
       szam = int(random.random()*51)+1
    print(f"I/A:\n\tA generált szám: {szam}")
    return szam    

def oszthatosag():
    szam = generalas()
    print(f"I/B:")
    if szam % 5 == 0 and szam % 3 != 0:
        print(f"\tA szám öttel osztható!")
    elif szam % 3 == 0 and szam % 5 != 0:
        print(f"\tA szám hárommal osztható!")
    elif szam % 3 == 0 and szam % 5 == 0:
        print(f"\tA szám hárommal és öttel is osztható!")
