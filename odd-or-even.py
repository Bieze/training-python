#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n > 100:
        print("Number must be 100 or smaller")
    elif n < 1:
        print("Number must be bigger than 0")
    else:
        if n % 2:
            print("Weird")
        else:
            if n > 1 and n < 6:
                print("Not Weird")
            elif n > 5 and n < 21:
                print("Weird")
            elif n > 20:
                print("Not Weird")