x = input("Mennyi az autód országúti fogyasztása?")
y = input("Mennyi az autód városi fogyasztása?")
z = input("Mekkora az országúti táv?")
q = input("Mekkora a városi táv?")
v = input("Mennyi a benzin ára?")

print("Odaút fogyasztása:")
print((int(z) / 100 * int(x)) + int(q) / 100 * int(y))
print("Fogyasztás teljes útra:")
print(((int(z) / 100 * int(x)) + int(q) / 100 * int(y)) * 2)
print("Teljes út ára:")
print((((int(z) / 100 * int(x)) + int(q) / 100 * int(y)) * 2) * int(v))

# Fogyasztás csak oda
# országúton: táv/ 100 * fogyasztás 170/100*7 = 11.9
# varosban: 35/100*9 = 3.15