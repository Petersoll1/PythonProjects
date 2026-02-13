from operator import truediv

cislo_jako_text = input("zadej cislo: ")

try:
    cislo = int(cislo_jako_text)
except:
    cislo = 0

print("zadane cislo + 10 = " + str(cislo + 10))
                    #
                    #   666666666             777777777777777
                    # 6666      666                       77
                    # 666                                77
                    # 666                               77
                    # 666                              77
                    # 666666666666               77777777777
                    # 66666      666                 77
                    # 666         666               77
                    # 666         666              77
                    #  6666     6666              77
                    #      66666                 77


while True:
    x = input("napic cislo: ")
    try:
        a = int(x)
        break
    except:
        pass
print(a)
