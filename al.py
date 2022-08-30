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
print(to_bin(12))

        