vstup = input("zadej cislo: ")
try:
    cislo = int(vstup)
except:
    cislo = 0

print("vstup = " + vstup)

if cislo > 5:
    print("vetsi")
    print(cislo)
    print("je")
    print("vetsi nez 5")
elif cislo > 10:
    print("nevim neco")

else:
    print("neni vetsi nez 5")
if cislo < 7:
    print("cislo je mensi nez 7")

print("konec")

a = input("zadej A")
b = input("zadej B")
c = input("zadej C")