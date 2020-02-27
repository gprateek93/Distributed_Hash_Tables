import sys
from hashlib import sha1
from itertools import combinations, permutations
import Node
import Hash_Table
import random


def generate_id(ip_address,k):
    result = sha1(ip_address.encode())
    c = bin(int(result.hexdigest(),16)).replace("0b","")
    c_ = ""
    for i in range(k):
        c_ = c_ + c[random.randint(0,len(c)-1)]

    return int(c_,2)

def generate_ip(num):
    P = range(256)
    print(list(combinations(P,4))[:num])

def main(args):
    m =  args[0]
    dht = Hash_Table.DHT(m)
    # L = list(set([random.randrange(0, 16, 1) for i in range(10)]))
    L = [1,7,9,11,12,14,15]
    print(L)
    for i in L:

        print(i)
        dht.add_node(i)
        print("Node added successfully")
    
    for i in range(len(L)):
        print(L[i])
        print(dht.node_list[i])
        print(dht.node_list[i].finger_table)

main([4])


