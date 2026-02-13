import numpy as np
# for i in range(100):
#     cislo = np.random.randint(5)
#     pes = input("zadej cislo: ")
#     print(pes)
#     if pes == cislo:
#         print("super vyhral si 67")
#     else:
#         print("zkus to znovu")
#
target = np.random.randint(20)
pocet = 0

while True:
    while True:
        x = input("napis cislo: ")
        try:
            cislo = int(x)
            break
        except:
            print("neni cislo")

    pocet += 1
    if cislo == target:
        print("super vyhral si 67")
        break
    elif target > cislo:
        print("musis dat vetsi")

    elif target < cislo:
        print("musis dat mensi")

print(x)
print(pocet)

