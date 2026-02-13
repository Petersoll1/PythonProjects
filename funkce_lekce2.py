from funkce_lekce1 import vysledek

globalni_promenna = 10

def secti(a,b):
    globalni_promenna = 20
    vylsedek = a+b+globalni_promenna
    return vylsedek

def secti_tuple(a, b):
    globalni_promenna = 20
    vysledek = a+b+globalni_promenna
    return  vysledek, globalni_promenna

y = secti(5,3)
print(y)
print(globalni_promenna)

print(y)
print(type(y))
print(secti_tuple(5,3))
print(type(secti_tuple(5,3)))
print(globalni_promenna)

y[1] = 20
print(y)

