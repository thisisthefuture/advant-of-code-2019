import math

def fuel_amount(mass):
    return math.floor(int(mass)/3) - 2

txt = open("day01_input")

total = 0
for line in txt:
    total += fuel_amount(line)

print(total)

txt.close()