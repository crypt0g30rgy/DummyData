#!/usr/bin/env python3

import random

# Open the input file and read the names
with open("names.txt", "r") as f:
    names = f.read().splitlines()

# Generate the email addresses
emails = []
while len(names) >= 2:
    # Take two names randomly
    name1 = names.pop(random.randint(0, len(names)-1))
    name2 = names.pop(random.randint(0, len(names)-1))
   
    # Generate a random number between 1-999 and add it to the name pair
    number = str(random.randint(1, 999)).zfill(3)
    email = name1.lower() + name2.lower() + number + "@gmail.com"
    emails.append(email)

# Write the emails to a file
with open("emails.txt", "w") as f:
    for email in emails:
        f.write(email + "\n")
