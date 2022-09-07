#najwyższy wspólny dzielnik
def nwd(a,b):
    while a != b:
        if a > b:
            a = a -b
        elif b > a:
            b = b - a
    return a
# najwyższa wspólna wielokrotność

def nww(a, b):
    return (a * b)/nwd(a,b)
# palidrom, wyraz czytany od tyłu jest taki sam

def is_palindrom(a):
    b = "".join(reversed(a))
    if a == b:
        return True
    else:
        return False
#anagram - wyraz czytany od tyłu taki sam
def is_anagram(a,b):
    if sorted(a) == sorted(b):
        return True
    else:
        return False

def silnia(a):
    if a == 0:
        return 1
    else:
        return a * silnia(a-1)
#od 0 = 0, 1 = 1, suma 2 poprzednich wyrazów ciągu 
def fib(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        return fib(a-1) + fib(a-2)

#liczba doskonała to liczba ktora jest sumą wszystkkich swouch dzielników właściwych
from math import sqrt
from re import I
def liczba_doskonala(a):
    suma = 0
    for i in range(1, int(sqrt(a))+1):
        if a%i == 0:
            suma+=i
            if a/i != a and a/i != i:
                suma += a/i
    return suma == a

def czy_pierwsza(a):
    if a == 1:
        return False
    if a == 2:
        return True
    if a % 2 == 0:
        return False
    for i in range(3, int(a/2)+1,2):
        if a % i == 0:
            return False
    return True 
def dzielniki(a):
    pass


#suma dzielników    maj 2016, z1.2 Liczby skojarzone
def suma_dzielników(a):
    suma = 0
    i = 1
    while i*i <=a:   #i <=sqrt(a)
        if a % i == 0: # jezeli to jest dzielnik
            suma +=i
            if i*i != a:
                suma += a/i
        i+=1
    return suma

#int -> bin 

def to_bin(a):
    bin = []
    while a != 0:
        if a%2 == 0:
            bin.append("0")
            a=a//2
        if a%2 ==1:
            bin.append("1")
            a=a//2
    bin.reverse()
    return "".join(bin)

#konwertowanie dowolnej liczby do dowolnego systemu liczbowego

#to_base(16, 8)
#reszta = 16%8 = 0
#a = 16//8    = 2 

def to_base(a, b):
    base = []
    while a != 0:
        reszta = a%b
        if 0 <= reszta <=9:
            base.append(chr(48+reszta))
        else:
            base.append(chr(97 +(reszta-10)))
        a //= b
    base.reverse()
    return "".join(base)

# konwertowanie z bin do inta
#
def to_int(bin):
    potega = 0
    suma = 0
    for c in reversed(bin):
        suma += int(c) * 2 **potega
        potega+=1
    return suma
'''
Napisz funkcję zwracającą listę wszystkich liczb pierwszych mniejszych lub równych N. 
Implementację należy wykonać za pomocą algorytmu sita Eratostenesa.
'''

def sito(n): #n =10 len=11
    a = [True for i in range(1,n+1)]
    a[0] = None
    a[1] = None
    for k in range(2, int(sqrt(len(a)))):
        if a[k]!=None:
            for j in range(2*k,len(a),k):
                a[j]=None
    b= [idx for idx, el in enumerate(a)if el!=None]    
    print(b)
'''
Napisz funkcję zwracającą w postaci listy rozkład liczby N na czynniki pierwsze.
'''
def czyn_pierwsze(n):
    tab = []
    orig_n = n
    while n > 1:
        i=2
        while i*i <= orig_n:
            while n % i == 0:
                tab.append(i)
                n = int(n/i)
            i+=1
    if n > 1:
        tab.append(n)
    print(tab)


'''
Napisz funkcję, która odczyta i przekonwertuje na liczbę (int) przekazany w parametrze napis reprezentujący 
liczbę naturalną w systemie binarnym.
Wykorzystaj algorytm Hornera.
W zapisie programu nie możesz korzystać z funkcji języka konwertujących napisy na liczby i odwrotnie.
'''
#Algorytm Hornera.
#int => bin

def to_int(a):
    x = 0 
    for el in a:
        x= 2*x + int(el)
    return x
#bin => base
def to_base(a,b):
    liczba = to_int(a)
    base = []
    while liczba != 0:
        reszta = liczba%b
        if 0 <= reszta <=9:
            base.append(chr(48+reszta))
        else:
            base.append(chr(97 +(reszta-10)))
        liczba //= b
    base.reverse()
    return "".join(base)

'''
Napisz funkcję obliczającą sumę wszytskich cyfr danej liczby.

123 % 10 = 3
123 // 10 = 12
12 
'''
def sum(a):
    suma = 0
    while a != 0:
        suma +=a % 10
        a//=10
    return suma


'''
Wykorzystaj napisaną powyżej funkcję, do stwierdzenia, czy dana liczba 
jest podzielna przez 3 (korzystając z cechy podzielności liczby przez 3).
'''

def czy_podziel_przez_trzy(a):
    if sum(a)%3 == 0:
        return True
    else:
        return False

# all() - wszytskie są prawdziwe
# any() - co najmniej jedna jest True
# abs()
#sorted(lista)
#list()
#zip()
#max()
#lista = ' '.join(chain(*lista_pod))