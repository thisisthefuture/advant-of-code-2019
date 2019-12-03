# ITERATIVELY

# import math

# def fuel_amount(mass):
#     return math.floor(int(mass)/3) - 2

# txt = open("day01_input")
# total = 0

# for line in txt:
#     remaining_fuel = int(line) # each line is the mass of a module
#     fuel = 0                   # setting the default fule requirement per module
#     while fuel >= 0:           # while fuel requirement is 0 or more
#         fuel = fuel_amount(remaining_fuel)  # calculate the fuel amount depending on mass (of module or new fuel)
#         if fuel > 0:           # if fuel mass is not negative add it to total
#             total += fuel
#         remaining_fuel = fuel  # remaining fuel to account for is the new fuel amount added

# print(total)

# txt.close()


#
# RECURSIVELY
#

import math

# returns the fuel requirement given a mass
def fuel_amount(mass):
    fuel = math.floor(int(mass)/3) - 2
    if fuel > 0:    # if fuel is > 0, need to account for its mass as well
        fuel + fuel_amount(fuel)
    return fuel

txt = open("day01_input")
total = 0

for line in txt:
    total += fuel_amount(line)

print(total)

txt.close()