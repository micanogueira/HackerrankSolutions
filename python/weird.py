#!/bin/python3

n = int(input().rstrip())
if n % 2 != 0:
    print("Weird")
elif n < 5:
    print("Not Weird")
elif n <= 20:
    print("Weird")
else:
    print("Not Weird")
