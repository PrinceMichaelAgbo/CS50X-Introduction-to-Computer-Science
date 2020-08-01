from cs50 import get_float

coins = -1
while (coins < 0):
    coins = get_float("How much change is owed? ")

# The coins conversions are done below
cents = coins * 100
numquarters = cents // 25
rem1 = cents % 25
numdimes = rem1 // 10
rem2 = rem1 % 10
numnickels = rem2 // 5
numpennies = rem2 % 5
# the total coin number
numcoins = numquarters + numdimes + numnickels + numpennies
print(int(numcoins))
