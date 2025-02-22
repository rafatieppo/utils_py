#!/usr/bin/env python3

"""Generate integer numbers randomly."""

import numpy as np


def app_lottery(n, vmin, vmax):
    """
    Generate integer numbers randomly.

    Parameters:
    n (int): amount of random numbers.
    vmin (int): minimal value value for a random number.
    vmax (int): max value value for a random number.
    """
    numbers = list(np.random.randint(vmin, vmax, n))
    # print('\nFirst list of numbers: {}'.format(sorted(numbers)))
    check_equal_all = 0
    while check_equal_all != n:
        for idx in range(len(numbers)):
            check_equal = 0
            for idy in range(len(numbers)):
                if numbers[idx] == numbers[idy]:
                    check_equal += 1
                    if check_equal > 1:
                        replace_num = np.random.randint(vmin, vmax, 1)[0]
                        numbers[idy] = replace_num
        numbers = sorted(numbers)
        for idz in range(len(numbers)):
            filter_num = lambda numb1: numb1 == numbers[idz]
            check_equal_all += len(list(filter(filter_num, numbers)))
        # print('Checl ALL is: {}'.format(check_equal_all))
    print('------------------------------------------------------------')
    print('------------------------------------------------------------')
    print(numbers)
    print('------------------------------------------------------------')
    print('------------------------------------------------------------')
    return numbers
#------------------------------------------------------------

n = int(input('\nType the amount random mumbers: '))
vmin = int(input('\nType the minimal value: '))
vmax = int(input('\nType the max value: '))

app_lottery(n, vmin, vmax)
