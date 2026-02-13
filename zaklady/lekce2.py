print("ahoj")

odpoved = input("tohle se napíše do řádky:")

print(odpoved)
print(type(odpoved))

try :
    odpoved_jako_cislo = int(odpoved)
except:
    print("ty jsi ale peknej *****, ze neumis zadat cislo. nastavuju na 0")
    odpoved_jako_cislo = 0


print("ahoj " + "vole")
print(22 + odpoved_jako_cislo)

