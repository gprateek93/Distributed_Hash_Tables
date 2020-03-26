import math
import numpy as np 
from prettytable import PrettyTable

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
    count = 0
    for i in range(len(c)):
        if c[i] != d[i]:
            break
        else:
            count+=1
    return count-1

def get_digit_at(number, n):
    a = str(hex(number))[2:]
    return int(a[n],16)

def compare_tables(table_1 = [],table_2 = [], node = None):
    for i in range(len(table_2)):
        for j in range(len(table_2[i])):
            if table_2[i][j] is not None and table_2[i][j] != node.ide:
                if table_1[i][j] is None:
                    table_1[i][j] = table_2[i][j]
                else:
                    val = abs(node.ide - table_1[i][j]) < abs(node.ide - table_2[i][j])
                    if not val:
                        table_1[i][j] = table_2[i][j]
    return table_1

def insort(l,node):
    i = 0
    while i<len(l) and node.ide > l[i].ide:
        i+=1
    l.insert(i,node)
    return l

def print_list(l=[],id=0,name=""):
    print("Printing the " + name + " of the node with id "+ str(id))
    p = [i.ide for i in l]
    print(p)

def print_table(t = [], id = 0, name =""):
    print("Printing the " + name + " of the node with id "+ str(id))
    p = PrettyTable()
    for i in t:
        p.add_row(i)
    print(p)