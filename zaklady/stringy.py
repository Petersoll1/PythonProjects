text = "ahoj"
text2 = "ahooooooooooooj"
text3 = "Sean O'Connery"
text4 = "Tak rekl: Co je ty pizzo"
text5 = 'Sean O\'Connery'
text6 = "cesta k souboru je c:\\hry\\soubor.txt"
text7 = "ahoj \n nazdar"

a = "ahoj"
b = "pane"

print(a+b)
print(a*3)
c = "a"
for i in range(5):
    c = c + "a"

print(c)

promenna = "Ahoj Karle, jak se máš?"

print(promenna[6]) # indexovani od 0 !!!!!!!!!!

print(len(promenna))
for i in range(len(promenna)):
    print(promenna[i])

print(promenna[len(promenna)-1])
print(promenna[-1])

print(promenna[5:10:2])