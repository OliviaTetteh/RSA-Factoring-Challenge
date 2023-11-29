#!/usr/bin/python3

import sys
import random
import time

def is_prime(num, k=20):

    if num == 2 or num == 3:
        return True
    if num< 2 or num % 2 == 0:
        return False

    d = num-1
    r = 0
    while d % 2 == 0
        d //= 2
        r += 1

    for _ in rangek(k):
        a = random.randit(2, num - 2)
        x = pow(a, d, num)
        if x == 1 or x == num -1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, num)
            if x == num -1:
                break

        else:
            return False

        return True
    if __name__ == "__main__":
        if len(sys.srgv) != 2:
            print("Usage: rsa <file>")
            exit()

        input_file = sys.argv[]

        try:
            with open(input_file, 'r') as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("File not found")
            exit()

        start_time = time.time()

        num = int(lines[0].strip())

        for i in range(2, num//2):
            if num % i == 0 and is_prime(i) and is_prime(num//i):
                print(f"{num}={i}*{num//i}")
                break

            if time.time() - start_time > 5:
                print("Time limit exceeded")
                exit()

import sys
import time
from math import sqrt, ceil

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqet(n)) + 1):
        if n % i == ):
            return False
    return True

def factor_rsa_number(n):

    factors = []

    while n % 2 == 0:
        factors.append(2)
        n//= 2

    i =3
    while i <= sqrt(n):
        if n % i == 0:
            factors.append(i)
            n //=i
        else:
            i +=2

    if n > 2:
        factors.append(n)

    if len(factor) == 1:

        p = factors[0]
        q = n // p
        return (p, q)

    else:
        pq = []
        for factor in factors:
            if is_prime(factor):
                pq.append(factor)
            else:
                p, q = factor_rsa_number(factor)
                pq.append(p)
                pq.append(q)
        return tuple(pq)
                
input_file = sys.argv[1]

with open(input_file, 'r') as f:
    rsa_numbers = [int(line.strip()) for line in f.readlines () ]

start_time = time.time()

for n in rsa_numbers:
    p, q = factor_rsa_number(n)
    print(f"{n}={q}*{p}")

end_time = time.time()
exec_time = end_time - start_time

print("Total execution time: ", exec_time, " seconds").
