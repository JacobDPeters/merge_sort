import numpy as np
import pandas as pd


file = 'int_array.txt'
df=pd.read_csv(file, sep=',',header=None)

def count_merge(b,c):
    res_arr, inv_count = [], 0
    while len(b) > 0 or len(c) > 0:
        if len(b) > 0 and len(c) > 0:
            if b[0] < c[0]:
                res_arr.append(b[0])
                b = b[1:]
            else:
                res_arr.append(c[0])
                c = c[1:]
                inv_count += len(b)
        elif len(b) > 0:
            res_arr.append(b[0])
            b = b[1:]
        elif len(c) > 0:
            res_arr.append(c[0])
            c = c[1:]
    return res_arr, inv_count

def count_sort(a):
    length = len(a)
    if length <= 1:
        return a, 0
    l = int(length / 2)
    b,x = count_sort(a[:l])
    c,y = count_sort(a[l:])
    d,z = count_merge(b,c)


    return d, x+y+z


print(sort_and_count(df.values))
