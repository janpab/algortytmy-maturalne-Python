with open(r'C:\Users\Ja\Desktop\KOREPETYCJE\algorytmy\programy\matura 2016\punkty.txt') as f:
    f= f.readlines()

punkty = [el.strip().split() for el in f]
for el in punkty:
    for i in range(len(el)):
        el[i] = int(el[i])
#print(punkty)


def zad_1():
    licznik = 0
    for el in punkty:
        x = el[0]
        y = el[1]

        if (x - 200)*(x - 200) + (y-200)*(y-200) == 200*200:
            print(x, y, "BRZEG KOŁA")
        if (x - 200)*(x - 200) + (y-200)*(y-200) < 200*200:            
            licznik +=1
    print(licznik)
#zad_1()

'''
Po = pi*r^2
Pk = 4*r^2

no/nk = Po/Pk = pi/4
pi = 4 * no/n

'''

def przyb_pi(tab, n):
    licznik = 0
    for el in tab[:n]:
        x = el[0]
        y = el[1]
        if (x - 200)*(x - 200) + (y-200)*(y-200) <= 200*200:            
            licznik +=1
    nk = licznik 
    
    pi = nk/n
    return pi*4
print(round(przyb_pi(punkty, 100),4))
print(round(przyb_pi(punkty, 1000),4))
print(round(przyb_pi(punkty, 5000),4))
print(round(przyb_pi(punkty, len(punkty)),4))
