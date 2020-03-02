import sys
from itertools import combinations, permutations
import Node
import Hash_Table
import random
from utils import generate_id


def main(args):
    m =  args[0]
    dht = Hash_Table.DHT(m)
    # L = list(set([random.randrange(0, 16, 1) for i in range(10)]))
    L = [1,7,9,11,12,14,15]
    dht.file_lookup(10)
    for i in L:

        print(i)
        dht.add_node(ide = i)
    
    for i in L:
        print(i)
        print(dht.node_list[i])
        print(dht.node_list[i].finger_table)

    dht.file_lookup(10)
    #add files:
    F = [1,6,10,13,15]
    for i in F:
        dht.add_file(i,"Prateek_"+str(i))

    dht.delete_node(11)

    dht.file_lookup(10,logs=True)

main([4])


