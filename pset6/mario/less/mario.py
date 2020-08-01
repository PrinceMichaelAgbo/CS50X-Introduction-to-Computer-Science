from cs50 import get_int


height = 0
while (height < 1 or height > 8):  # to prompt user until appropriate input is given
    height = get_int("Height: ")

for i in range(1, height+1, 1):  # to print the half pyramid
    print(" " * (height - i) + "#" * i)

