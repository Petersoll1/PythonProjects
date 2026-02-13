promenna = [1, 2, 3, 4, 5]

print(promenna)

p2 = [1, "abc", 5.5, True, [1,2,"a"]]
print(p2)

print(type(p2))
print(p2[2])
print(type(p2[2]))
print(p2[4][1])
print(type(p2[4][1]))
print(p2[1:3])

x = [1, 2, 8, 4, 5, 6, 11, 4, 7, ]

for i in range(len(x)):
    print(x[i])

for i in range(len(promenna)):
    print(promenna[i])

for i in range(len(x)):
    if i%2 == 0:
        print(x[i])

