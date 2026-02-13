promenna = "Ahoj Karle, jak se máš?"

# vypište jednotlivé znaky pod sebe
# (pomocí for-cyklu)

for i in range(len(promenna)):
    print(promenna[i])

# vypište totez, ale pozpatku

for i in range(len(promenna)):
    print(promenna[-i-1])

# nebo pouziji tohle, ale oboji je spravne

for i in range(len(promenna)-1, -1, -1):
    print(promenna[i])

# vypište podle zadání (na tabuli)

for i in range(len(promenna)):
    print(promenna[:i+1])

# vypište podle zadání (na tabuli)

for i in range(len(promenna)-1):
    print(promenna[i:i+2])

# upravte tohle aby to vypisovalo po třech

for i in range(len(promenna)-2):
    print(promenna[i:i+3])

# vypište vedle sebe vždy první a poslední písmeno, pak druhy a predposledni, ... a koncime v polovine textu
# funkce int zaokrouhli jakoby desetinne cislo myslim

for i in range(int(len(promenna)/2)):
    print(promenna[i],promenna[-i-1])

# promenna = promenna.replace("a","x")
print(promenna)
print(promenna.find("jak"))
print(promenna.strip())
a = " kfjesfhdsjkfe"
print(a)
print(a.strip())
a = "5"

print(a.zfill(5))