def kvadraticka(a,b,c):
    D = b**2 - 4*a*c
    if D > 0:
        horejsek = -b + D**(1/2)
        dolejsek = 2*a
        vysledek = (horejsek/dolejsek)
        horejsekminus = -b - D**(1/2)
        vysledek2 = (horejsekminus/dolejsek)
        return vysledek, vysledek2
    if D <0:
        print("NEMA RESENI")
        return
    if D ==0:
        horejsek = -b
        dolejsek = 2 * a
        vysledek = (horejsek / dolejsek)
        return vysledek

m = kvadraticka(1,2,1)
print(m)

m = kvadraticka(1,3,1)
print(m)

m = kvadraticka(1,1,1)
print(m)

