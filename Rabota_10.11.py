from module1 import *
from keyboard import *
from math import *

while True:
    print("Funktsioonid" .center(50, "+") )
    v=input("arithmetic - A\n Yearleep Y\nSeason C\nSquare B\nBank K\nis_prime U\n=>")
    
    if v.upper()=="A":
        arv1=float(input("Esimene arv =>"))
        arv2=float(input("Teine arv =>"))
        sym=input("Aritmeetiline Tehing =>")
        rezult=arithmetic(arv1,arv2,sym)
        print(rezult)
    if v.upper()=="Y":
         rezult=Yearleep(int(input("Sisesta aasta")))
         print(rezult)
    
    if v.upper()=="B":
         rezult=square(int(input("Sisesta number")))
         print(rezult)
    
    if v.upper()=="C":
        otvet=season(int(input("kuu =>"))) 
        print(otvet)
        
    if v.upper()=="K":
        rezult=Bank(float(input("money =>"))) 
        a=years(int(input("year =>")))
        print(f"Вы заработаете {rezult} за {year} лет.")
    
    if v.upper()=="U":
         rezult=is_prime(int(input("Sisesta number")))
         print(rezult)