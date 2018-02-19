"""
Baum-Sweet Sequence Challenge

Your challenge today is to write a program that generates the
Baum-Sweet sequence from 0 to some number n. For example,
given "20" your program would emit:
1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0
"""


def to_bin(n):
    return str("{0:b}".format(n))


def baumify(dec):
    if dec == 0 or dec == 1:
        return 1

    count = 0
    bin = to_bin(dec)
    for bit in bin:
        if bit == '1':
            if count > 0 and count % 2 == 1:
                return 0
            count = 0

        else:
            count += 1

    if count > 0 and count % 2 == 1:
        return 0

    return 1


def print_sequence(n):
    for i in range(n + 1):
        print(baumify(i), end=' ')

valid_input = False
while not valid_input:
    n = input("Enter a number to create a baum-sweet sequence: ")

    try:
        n = int(n)
        if n > 0:
            print_sequence(n)
            valid_input = True
        else:
            print("Number cannot be negative")

    except ValueError:
        print("Invalid number\n")