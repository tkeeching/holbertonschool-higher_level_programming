#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("number ->", number)
print("number % 10 ->", number % 10)
print("abs(number) % 10 ->", abs(number) % 10)
if (number % 10) == 0:
    print(f"Last digit of {number} is {number % 10} and is 0")
elif (abs(number) % 10) > 5 and number > 0:
    print(f"Last digit of {number} is {abs(number) % 10} and is greater than 5")
elif (abs(number) % 10) > 5 and number < 0:
    print(f"Last digit of {number} is -{abs(number) % 10} and is less than 6 and not 0")
elif (abs(number) % 10) < 6 and number < 0:
    print(f"Last digit of {number} is -{abs(number) % 10} and is less than 6 and not 0")
elif (abs(number) % 10) < 6 and number > 0:
    print(f"Last digit of {number} is {number % 10} and is less than 6 and not 0")
