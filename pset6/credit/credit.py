from cs50 import get_int


crednum = -1
while (crednum < 0):
    crednum = get_int("Number: ")

length = len(str(crednum))

n = crednum
notmultotal = 0
addeveryother = 0

while (n != 0):  # get each second number right to left
    rem = (n % 100)
    multby2 = (rem // 10) * 2  # the numbers that will be multiplied by 2
    notmult = (rem % 10)  # the numbers that will not be multiplied by 2
    notmultotal += notmult  # add the numbers not multiplied by 2
    prodigits = (multby2 // 10) + (multby2 % 10)
    addeveryother += prodigits  # add the digits of the numbers multiplied by 2
    n = n // 100
    if ((n >= 100) and (n < 1000) and (length % 2 != 0)):  # 400
        secondnum = (n % 100) // 10  # get the second number if card number length is odd

    if (n == 0):
        if (length % 2 == 0):
            firstnum = rem // 10  # get the first number if card number length is even
            secondnum = rem % 10  # get the second number if card number length is even
        else:
            firstnum = rem  # get the first number if card number length is odd

sum = addeveryother + notmultotal
valid = (sum % 10) == 0  # check if the card number is valid

# below are just the conditions for each type of credit card
if (valid):
    if ((length == 15) and (firstnum == 3) and (secondnum == 4 or secondnum == 7)):
        print("AMEX")
    elif ((length == 16 or length == 13) and (firstnum == 4)):
        print("VISA")
    elif ((length == 16) and (firstnum == 5 or firstnum == 2) and (secondnum < 6)):
        print("MASTERCARD")
    else:
        print("INVALID")
else:
    print("INVALID")
