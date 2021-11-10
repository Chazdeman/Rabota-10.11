from module1 import *
from keyboard import *
from math import *

while True:
    print("Funktsioonid" .center(50, " ") )
    v=input("arithmetic - A\n is_year_leap Y\n Season C\n Mida sa tahad?")
    
    if v.upper()=="A":
        arv1=float(input("Esimene arv =>"))
        arv2=float(input("Teine arv =>"))
        sym=input("Aritmeetiline Tehing =>")
        rezult=arithmetic(arv1,arv2,sym)
        print(rezult)

    elif is_year_leap()=="Y":
         rezult=is_year_leap(int(input("Sisesta aasta")))
         print(rezult)
    elif square()=="B":
         rezult=square(int(input("Sisesta number")))
         print(rezult)
    elif season()=="C":
        l=int(input("kuu =>")) 
        otvet=season(l)
        print(otvet)