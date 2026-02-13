vstup = input("zadej cislo: ")
try:
    cislo = int(vstup)
except:
    cislo = 0

print("vstup = " + vstup)

#    if cislo < 10:
#        print("cislo je mensi nez 10 bludisssss")
#    elif 20 > cislo > 10:
#       print("cislo je mezi 10 a 20 ty trumberko")
#    elif cislo > 20:
#       print("cislicko je vetsi nez 20 ty kryso")

if cislo > 10:
    print("cislo je vetsi nez 10")
if cislo%2 == 0:
    print("cislo je sude")
else:
    print("cislo je liche")
if cislo > 10 and cislo < 20:
    print("cislo je vetsi nez 10, ale mensi nez 20")