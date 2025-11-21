#Úloha 1 - Napište program, který najde největší prvek v poli bez použití funkce.

pole = [5, 2, 9, 1, 7, 3, 10, 6, 4]

maximalni_prvek = pole[0]
pozice_max_prvku = 0

for i in range(1, len(pole)):
    if maximalni_prvek < pole[i]:
        maximalni_prvek = pole[i]
        pozice_max_prvku = i

print("Úloha 1:")
print("maximální prvek v seznamu je:", maximalni_prvek)
print("pozice maximálního prvku je:", pozice_max_prvku)

#Úloha 2 - Napište program, který najde nejmenší prvek v poli bez použití funkce.

minimalni_prvek = pole[0]
pozice_min_prvku = 0

for i in range(1, len(pole)):
    if minimalni_prvek > pole[i]:
        minimalni_prvek = pole[i]
        pozice_min_prvku = i

print("Úloha 2:")
print("minimální prvek v seznamu je:", minimalni_prvek)
print("pozice minimálního prvku je:", pozice_min_prvku)

#Úloha 3 - Spočítejte průměrnou hodnotu všem prvků v poli

soucet = pole[0]

for i in range(len(pole)):
    soucet = soucet + pole[i]

print("Úloha 3:")
print("Průměrná hodnota prvku v listu je:", soucet/len(pole))

#Úloha 4 - Zjistěte, kolik prvků v poli je větších než 5.

pocitadlo = 0
limit = 5

for i in range(len(pole)):
    if pole[i] > limit:
        pocitadlo += 1

print("Úloha 4:")
print("Prvků větších než " + str(limit)+ " je v poli: " + str(pocitadlo))

#Úloha 5 - Spočítejte součet všech prvků v poli

soucet = pole[0]

for i in range(len(pole)):
    soucet = soucet + pole[i]

print("Úloha 5:")
print("Součet všech prvků v seznamu je:", soucet)

#Úloha 6 - Vytvořte nové pole, které bude obsahovat prvky v obráceném pořadí

pole = [5, 2, 9, 1, 7, 3, 10, 6, 4]
nove_pole = []
#nevim uz koncime nestiham
nove_pole.append(pole[0])
print(nove_pole)

#Úloha 8

pole = [5, 2, 9, 1, 7, 3, 10, 6, 4]
pole2 = [3, 5, 4, 7, 5, 3, 4, 5, 10]

pole_vysledne = []

for i in range (len(pole)):
    pole_vysledne.append(pole[i] + pole2[i])

print("-------------------Úloha 8---------------------")
print(pole_vysledne)

#Úloha 8,5

pole = [5, 2, 9, 1, 7, 3, 10, 6, 4]
pole2 = [3, 5, 4, 7, 5, 3, 4, 5, 10]

pole_vysledne = []

for i in range(len(pole)):
    pole_vysledne.append(pole[i] + pole2[-i-1])

print("-------------------Úloha 8,5---------------------")
print(pole_vysledne)

#Úloha 9

pole3 = [5, 2, 9, 1, 7, 3, 10, 6, 4]
if pole[0]<pole[1]:
    nejvetsi = pole[0]
    druhe_nejvetsi = pole[1]
else:
    nejvetsi = pole[1]
    druhe_nejvetsi = pole[0]

for i in range(len(pole3)):
    if pole[i] > nejvetsi:
        druhe_nejvetsi = nejvetsi
        nejvetsi = pole[i]
    elif pole[i] > druhe_nejvetsi:
        druhe_nejvetsi = pole[i]

print("-------------------Úloha 9----------------------")
print(druhe_nejvetsi)

#Úloha 10, zjistěte zda je pole seřazeno vzestupně.

pole3 = [5, 2, 9, 1, 7, 3, 10, 6, 4]
je = True

for i in range(len(pole3)-1):
    if pole[i]> pole[i+1]:
        je = False
        break

print("-------------------Úloha 10----------------------")

if je:
    print("je")
else:
    print("neni")

#Úloha 11

pole3 = [5, 2, 9, 1, 7, 3, 10, 6, 4]

sude = 0
liche = 0

for i in range(len(pole3)):
    if pole[i]%2 == 0:
        sude += 1
    else:
        liche += 1

print(sude)
print(liche)