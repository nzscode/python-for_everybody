import random
import math

num = random.randint(1, 100) + 1
print("Number : " + str(num) + "/ 5")

if num % 5 == 0:
    print("Quotient: " + str(num / 5))
else:
    print("Quotient: " + str((math.floor(num / 5))), "Remainder: " + str(num % 5))
