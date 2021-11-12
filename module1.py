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
            r="Div0"
            r=0.0
    else:
        r="Viga"
        r=0.0
    return r

def Yearleep(aasta: int):

    #Liigaasta leidmine
    #Tagastab True kui on liigaasta ja False kui ei ole
    #:param int aasta:Asta number
    #:rtype bool:Funktsioni vastus logilises formatis
   
   if aasta % 4 != 0:
       vastus=True
   else:
        vastus=False
   return vastus

def square(j:float):
    #leidmine P S D
    #:Param float number: P S D
    #:rtype int: int int int
    if j!=0:
        p=j*4
        s=j*j
        d=sqrt(j*j*j*j)
        r=(("P="),p)
        k=(("S="),s)
        o=(("D="),d)

    return r,k,o

def season(a: int):
    #otsime, millele see kuu kuulub 봄여름가을겨울 그리고 봄
    #:param int seson: kuu järjekordne number
    #:rtype str: hooaja nimetus
    #Tagastab season talv või kevad või suvi või sügis 
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

def is_prime(a: int):
    #algarve leidmine
    #:param int number : True or False
    #:rtype str: Funktsiooni vastus 1 or 2
    #Tagastab True kui on algarve ja False kui on midagi muu
    if a % 2 == 0 and a != 2:
        return False
    if a == 0 or a == 1:
        return False
    for n in range(3, int(sqrt(a).real) + 1, 2):
        if a % n == 0:  
            return False
    else:
        return True  

def Bank(a: float , years: int):
    #otsime, milline on panus
    #:param float money , years: money
    #:rtyoe bool: Funktisooni vastus money
    if a>=0:
        k=years*1.1
        b=a*k
    return b 

def xor_cipher(string: str , key: str)->str:
    """Tavaline sõna kodeeritakse
    param: str sõna : str key
    ord - десятичное число,которое кодирует букву
    """
    result = ''
    temp = int()
    for i in range(len(string)):
        temp = ord(string[i]) #näitab sümboli kood
        for j in range(len(key)):
            temp ^=ord(key[j])
        result +=chr(temp)
    return result

def xor_uncipher(string:str , key: str) -> str:
    """
    param str
    chr - наоборот берёт число и возвращает букву.
    """
    result = ''
    temp=[]
    for i in range(len(string)):
        temp.append(string[i])
        for j in reversed(range(len(key))):
            temp[i]= chr(ord(key[j]) ^ ord(temp[i]))
        result +=temp[i]
    return result

def date(day: int ,month: int , year: int):
    """otsime, kas on see data või Ei
    :param int day, int month , int years : True or False
    :rtype bool:
    """
    if((month==1 or month>=1)and (month<=12 or month==12)) and ((day==1 or day>=1) and (day==31 or day<=31)) and year>=0:
        if month==2 and day<=30:
            if year%4==0 and day==29:
                otv="True"
            else:
                otv="False"
        elif(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12) and (day==31 or day<=31):
               otv="True"
        else:
                otv="False"
    return otv