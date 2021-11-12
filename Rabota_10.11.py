from module1 import *
from keyboard import *
from math import *

while True:
    print("Funktsioonid" .center(50, "+") )
    v=input("arithmetic - A\n Yearleep Y\nSeason C\nSquare B\nBank K\nis_prime U\nxor_cipher J\ndate X \n=>")
    
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
        otvet=season(int(input("Sisesta kuu =>"))) 
        print(otvet)
        
    if v.upper()=="K":
        money=(float(input("Sisesta money =>")))
        years=(int(input("year =>")))
        rezult=Bank(money,years)
        print(f"Вы заработаете {rezult} за {years} years.")
    
    if v.upper()=="U":
         rezult=is_prime(int(input("Sisesta number")))
         print(rezult)
    
    if v.upper()=="J":
        print("Kodeerimine".center(60,"+"))
        rezult=xor_cipher(input("Sisesta text=>"), input("Sisesta võti=>"))
        print(rezult)
        print("Dekodeerimine".center(60,"+"))
        de_rezult=xor_uncipher(rezult, input("Sisesta võti =>"))
        print(de_rezult)

    if v.upper()=="X":
         day=(int(input("Sisesta day=>")))
         month=(int(input("Sisesta month=>")))
         year=(int(input("Sisesta year=>")))
         rezult=date(day,month,year)
         print(rezult)