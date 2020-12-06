#!/usr/bin/env python3

import random

if __name__ == '__main__':
    b_column = random.sample(range(1, 16), 5)
    i_column = random.sample(range(16, 31), 5)
    n_column = random.sample(range(31, 46), 4)
    g_column = random.sample(range(46, 61), 5)
    o_column = random.sample(range(61, 76), 5)

    print('----------------')
    print('| B| I| N| G| O|')
    print('|--------------|')

    for i in range(5):
        b_column_value = b_column[i]
        i_column_value = i_column[i]
        n_column_value = None
        g_column_value = g_column[i]
        o_column_value = o_column[i]

        if i < 2:
            n_column_value = n_column[i]
        elif i == 2:
            n_column_value = 'F'
        elif i > 2:
            n_column_value = n_column[i - 1]

        print('|%2s|%2s|%2s|%2s|%2s|' % (b_column_value, i_column_value, n_column_value, g_column_value, o_column_value))
        print('|--------------|' if i != 4 else '----------------')
