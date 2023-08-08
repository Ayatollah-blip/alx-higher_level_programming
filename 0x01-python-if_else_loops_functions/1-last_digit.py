#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
stringNum = str(number)
lastDigit = int(stringNum[-1])
if lastDigit == 0:
    print(f"Last digit of {number} is {lastDigit} and is 0")
elif lastDigit > 5:
    print(f"Last digit of {number} is {lastDigit} and is greater than 5")
elif lastDigit < 6 and lastDigit != 0:
    print(f"Last digit of {number} is {lastDigit}", end=' ')
    print("and is less than 6 and not 0")
