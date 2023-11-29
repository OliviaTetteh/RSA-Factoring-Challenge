#!/usr/bin/python3

import sys
import time

def factorize(num):
    for j in range(2, int(num**0.5)+1):
        if num % j == 0:
            return (j, num//j)
    return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <files>")
        exit()

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print ("File not found")
        exit ()

    start_time = time.time()

    for line in lines:
        num = int(line.strip())
        factors = factorize(num)
        if factors:
            print(f"{num}={factors[0]}*{factors[1]}")

        if time.time() - start_time > 5:
            print("Time limit exceeded")
            exit()
