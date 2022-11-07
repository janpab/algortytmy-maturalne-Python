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

#anagram - wyraz ułożony z tych samych liter
def is_anagram(a,b):
    if sorted(a) == sorted(b):
        return True
    else:
        return False

#silnia (rekurencyjna)
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

#czy liczba "a " występuje w tablicy "tab"
#złożoność liniowa 
def is_in_tab(a,tab):
    for i in range(len(tab)):
        if tab[i] == a:
            return i
    return -1  

#przeszukiwanie binarne
#
def przesz_bin(a,tab):
    idx_l=0
    idx_r=len(tab)-1

    while True:
        idx = (idx_l+idx_r)//2
        if tab[idx]==a:
            return idx
        if tab[idx]<a:
            idx_l = idx+1
        if tab[idx]>a:
            idx_r = idx-1
        if idx_r < idx_l:
            return -1
#sortowanie bąbelkowe

def sort_bab(tab):
    for i in range(len(tab)):
        for k in range(len(tab)-1):
            if tab[k] > tab[k+1]:
                tmp = tab[k+1]
                tab[k+1] = tab[k]
                tab[k] = tmp
    return tab

def sort_bab_2(tab):
    for i in range(len(tab)):
        for k in range(len(tab)-1-i):
            if tab[k] > tab[k+1]:
                tmp = tab[k+1]
                tab[k+1]= tab[k]
                tab[k] = tmp
    return tab

#sortowanie przez wstawianie
#https://binarnie.pl/sortowanieprzezwstawianiealgorytmimplementacjacpp/

#a = [5,   3,1,2,4]
# a = [3,5,   1,2,4]
# a = [1,3,5,   2,4]
# a = [1,2,3,5,   4]
# a = [1,2,3,4,5   ]

def insert_sort(tab):
    for i in range(len(tab)-1):
        #wyszukiewanie liniowe
        for k in range(i+1):
            if tab[k]>tab[i+1]:
                idx = k
                num = tab[i+1]
                break
        for j in range(i,k-1,-1):
            tab[j+1] = tab[j]
        tab[idx] = num
    return tab

#sortowanie binarne
def sort_bin(tab):
    for i in range(len(tab)-1):
        num = tab[i+1]
        idx_l = 0
        idx_r = i
        while True:
            idx = (idx_l+idx_r)//2
            if tab[idx] == num:
                break
            if tab[idx] <num:
                idx_l = idx+1
            if tab[idx]>num:
                idx_r=idx-1
            if idx_r < idx_l:
                idx = idx_l
                break
        for j in range(i,idx-1,-1):
            tab[j+1] = tab[j]
        tab[idx] = num
        print(tab,"sort bin")

# sortowanie przez wyszukiwanie
#https://pl.wikipedia.org/wiki/Sortowanie_przez_wybieranie

def select_sort(tab):
    for i in range(len(tab)):
        min = tab[i]
        idx = i #najmniejszy
        for k in range(i,len(tab)):
            if tab[k] < min:
                min = tab[k]
                idx = k
        for j in range(idx,i,-1):
            tab[j] = tab[j-1]
        tab[i] = min
    print(tab, "sort wyszuk")

#sortowanie kubełkowe
#https://binarnie.pl/sortowanie-kubelkowe/

def bucket_sort(tab, max_):
    lista = [[] for k in range(len(tab))] 
    rozmiar = max_/len(tab)  
    for i in range(len(tab)):
        idx = int(tab[i]//rozmiar)
        lista[idx].append(tab[i])
    lista_sorted= []
    for k in range(len(lista)):
        if len(lista[k])==1:
            lista_sorted.append(lista[k][0])
        if len(lista[k])>1:
            for j in range(len(lista[k])):
                min = lista[k][0]
                idx = 0 
                for l in range(len(lista[k])):
                    if lista[k][l]<min:
                        min = lista[k][l]
                        idx = l
                del lista[k][idx]
                lista_sorted.append(min)
    print(lista_sorted)
#sortowanie przez scalanie
def scal(a,b):
    idx_a = 0
    idx_b = 0
    sorted = []
    while True:
        if idx_a > len(a) - 1:
            for k in range(idx_b, len(b)):
                sorted.append(b[k])
            break
        if idx_b>len(b)-1:
            for k in range(idx_a,len(a)):
                sorted.append(a[k])
            break
        if a[idx_a]>b[idx_b]:
            sorted.append(b[idx_b])
            idx_b+=1
        else:
            sorted.append(a[idx_a])
            idx_a+=1
    print(sorted)
# scalanie danych elementów w środku tablicy

def scal2(tab, idx_l, idx_m, idx_r):

    lista1 = tab[idx_l:idx_m+1]
    lista2 = tab[idx_m+1:idx_r+1]
    idx_1 = 0
    idx_2 = 0
    idx_s = idx_l
# sortowanie przez scalanie iteracyjnie
# rozmiar tablicy = 2**N
a= [1, 6   ,8, 4,    2, 5,    8, 0]
# [1,6 ,4,8, 2,5, 0,8] # scalanie

# [1,6 ,4,8,     2,5, 0,8] 
# [1,4,6,8,      0,2,5,8] # scalenie

# [0,1,2,4,5,6,8]



def scal_iter(tab):
    n = 2
    while n <= len(tab):
        for i in range(0,len(tab)-1,n):
            #tablica = tab[i:i+1]
            #idx_tab = i
            idx_l = i
            idx_r = i+n-1
            idx_m = (idx_l+idx_r)//2
            scal(tab, idx_l, idx_m, idx_r)
            
        n *= 2
    print(tab,'scal iter')
# scal_iter(a)

# sortowanie szybkie - quicksort
'''
pivot = 5
[5,6,4,5,2,7,9]
 i       j
tab[i] >= pivot     pivot <= tab[j]

[2,6,4,5,5,7,9]
   i   j

[2,5,4,6,5,7,9]
     j i

'''
def quicksort(tab, idx_l=0, idx_r=None):
    if idx_r is None:
        idx_r = len(tab) - 1
    
    if idx_r <= idx_l:    #warunek zakończenia - jednoelementowa tablica
        return 

    pivot = tab[(idx_r+idx_l)//2]
    i = idx_l
    j = idx_r
    while j>i:
        while tab[i]<pivot:##
            i += 1
        while tab[j]>pivot:
            j-=1
        if j>=i:
            # zamieniamy miejscami elementy
            tmp = tab[j]
            tab[j] = tab[i]
            tab[i] = tmp
            i+=1
            j-=1
    quicksort(tab, idx_l, j)   
    quicksort(tab, i, idx_r)

a= [1, 6   ,8, 4,    2, 5,    8, 0]

quicksort(a)
print(a)




#POŁOWIENIE PRZEDZIAŁU/ BISEKCJA
# https://pl.wikipedia.org/wiki/Metoda_r%C3%B3wnego_podzia%C5%82u#/media/Plik:Bisection_method.png

# y = x*x - 2   [0, 2]
def f(x):
    return x-2 
    
# a * (10 ** b) ->  aeb
# 20000 -> 2e4
# 0.0005 -> 5e-4
def bisekcja(f, a, b, epsilon=1e-10):  # a < b
    while b-a>=epsilon:
        m = (a+b)/2
        if f(a)*f(m) < 0:#różnych znakow
            b = m
        else:
            a = m
        
    return (a+b)/2
print(bisekcja(f,0,3))

#SZYFROWOWANIE#
#Szyfr Cezara
#ord('a') => kod ascii
#chr(kod_ascii) => litera

def szyfruje(a,k):
    szyfr = []
    for ch in a:
        if ord(ch) + k > ord('z'):
            b = ord(ch)+k - (ord('z')-ord('a')+1)
        else:
            b = ord(ch)  + k 
        szyfr.append(chr(b))
    return "".join(szyfr)

def deszyfruje(a,k):
    tekst = []
    for ch in a:
        if ord(ch) -k < ord('a'):
            b = ord(ch)-k + (ord('z')-ord('a')+1)
        else:
            b = ord(ch) -k 
        tekst.append(chr(b))
    return "".join(tekst)
print(deszyfruje("rtqitco",2))

# szyfr permutacyjny
alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
klucz = 'YPDARFBLWQETZGSVIMKHNXJUOC'    # dowolna permutacja alfabetu

def permutacja_szyfruje(klucz,wyraz):
    a = {}
    wyraz = []
    for i in range(len(alfabet)):
        a [ alfabet[i]] = klucz[i]
    for el in wyraz:
        wyraz.append(a[el])
    return "".join(wyraz)

def permutacja_deszyfruje(klucz,wyraz):
    a = {}
    b = []
    for i in range(len(alfabet)):
        a[klucz[i]]=alfabet[i]
    for el in wyraz:
        b.append(a[el])
    return "".join(b)
#SZFR PRZESTAWIENIOWY

#PROGRAM

def szyfr_przestawieniowy(wyraz):
    a = [] 
    for i in range(0, len(wyraz),2):
        if i < len(wyraz)-1:
            a.append(wyraz[i+1])
        a.append(wyraz[i])
    return "".join(a)


# all() - wszytskie są prawdziwe
# any() - co najmniej jedna jest True
# abs()
#sorted(lista)
#list()
#zip()
#max()
#lista = ' '.join(chain(*lista_pod))
