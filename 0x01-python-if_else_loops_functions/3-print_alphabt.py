#!/usr/bin/python3
for letter in range(97, 123):
    lett = chr(letter)
    if lett != 'q' and lett != 'e':
        print("{}".format(chr(letter)), end='')
