from math import *
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

def is_year_leap(year: int):
    """Liigaasta leidmine (Високосный год ищем)
    Tagastab true kui aasta on liigaasta ja False kui ei ole
    :param int aasta: Aasata number
    :rtype bool: Funktsioni vvastus loogilises formaadis
    """
    if year%4==0:
        vastus=True
    else:
        vastus=False
    return vastus 
def square(s1;float):
    p=s1*4
    s=s1*s1
    d=(s1**2) + (s1**2)
    print("P=",p \n "S=", s\n"D=" , d )

def season(seson: int):
    """otsime, millele see kuu kuulub 봄여름가을겨울 그리고 봄 
    """

    if a=="12" or "1" or "2":
        r="talv"
    elif a=="3" or "4" or "5":
        r="kevad"
    elif a=="6" or "7" or "8":
        r="suvi"
    else:
        r="sügis"
    return r