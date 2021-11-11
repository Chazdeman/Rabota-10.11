from math import*

def arithmetic(a: float, b: float,c: str):
#Lihtne kalkulaator - простой калькулятор
#+ - liitmine(сложение)
#- - Lahutamine(разложение)
#* - Korrutamine (умножение)
#/ - jagamine (деление)
#:param float a: Esimene arv
#:param float b: Teine arv
#:param str c: Aritmeetiline Tehing
#:rtype float:
    if c=="+":
        r=a+b
    elif c=="-":
        r=a-b
    elif c=="*":
        r=a*b
    elif c=="/":
        if b!=0:
            r=a/b
        else:
            print("Div0")
            r=0.0
    else:
        print("Viga")
        r=0.0
    return r

def Yearleep(aasta: int):

    #Liigaasta leidmine
    #Tagastab True kui on liigaasta ja False kui ei ole
    #:param int aasta:Asta number
    #:rtype bool:Funktsioni vastus logilises formatis
   
    if aasta%4==0:
        vastus=True
    else:
        vastus=False
    return vastus

def square(j:float):
    if j!=0:
        pop=""
        p=j*4
        s=j*j
        d=sqrt(j*j*j*j)
        print("P=",p)
        print("S=", s)
        print("D=" , d)

    return pop

def season(a: int):
    #otsime, millele see kuu kuulub 봄여름가을겨울 그리고 봄
    #:param int seson: seson
    #:rtype bool: Funktsiooni vastus seson
    if a==12 or 1 <= a <= 2:
        r="See on talv"
    elif 3 <= a <= 5:
        r="See on kevad"
    elif 6 <= a <= 8:
        r="See on suvi"
    elif 9 <= a <= 11:
        r="See on sügis"
    else:
        r="Ma ei tea see kuu"
    return r

def Bank(a: float , years: int):
    #otsime, milline on panus
    #:param float money , years: money
    #:rtyoe bool: Funktisooni vastus money

    if a>=0:
        k=years*1.1
        b=a*k
    return b


