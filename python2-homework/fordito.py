print("Kérem a pozitív számokat!, 0 vége")

my_list = []
x = int(input())

while x != 0:
    my_list.append(x)
    x = int(input())

print(my_list)

reversed_list = my_list[::-1]
print(reversed_list)

