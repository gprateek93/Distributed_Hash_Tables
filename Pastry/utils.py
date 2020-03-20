import math
import numpy as np 

def euclidean_distance(coord1,coord2):
    x_dist = math.pow((coord1[0] - coord2[0]),2)
    y_dist = math.pow((coord1[1] - coord2[1]),2)
    return math.sqrt(x_dist + y_dist)

def make_same_len(c,d):
    l = max(len(c),len(d))
    if(len(c) < l):
        c = c.zfill(l)
    else:
        d = d.zfill(l)
    return c,d

def prefix_match(a,b):
    c = str(hex(a))[2:]
    d = str(hex(b))[2:]
    c,d = make_same_len(c,d)
    print(c,d)
    count = 0
    for i in range(len(c)):
        if c[i] != d[i]:
            break
        else:
            count+=1
    return count-1

def get_digit_at(number, n):
    a = str(hex(number))[2:]
    return a[n]



