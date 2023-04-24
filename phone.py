#!/usr/bin/env python3

import random

with open("numbers.txt", "w") as file:
    for i in range(564):
        number = "+2547" + str(random.randint(10000000, 99999999))
        file.write(number + "\n")
