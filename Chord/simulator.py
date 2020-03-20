import sys
import Hash_Table
import random
from utils import generate_id
import math
import matplotlib.pyplot as plt


def main(args):
    m =  args[0]
    dht = Hash_Table.DHT(m)
    L = list(set([random.randrange(0, math.pow(2,m), 1) for i in range(100)]))
    # L = [1,7,9,11,14,15]
    print(L)
    dht.file_lookup(10)
    for i in L:

        print(i)
        dht.add_node(ide = i)

    
    #add files:
    F = list(set([random.randrange(0, math.pow(2,m), 1) for i in range(10000)]))
    for i in F:
        dht.add_file(i,"Prateek_"+str(i))

    # for i in [random.randrange(1, 100, 1) for i in range(50)]:
    #     dht.delete_node(L[i])

    for i in  list(set([random.randrange(0, len(F), 1) for i in range(100000)])) :
        dht.file_lookup(F[i],logs=True)
    
    print(dht.search_queries)
    print(dht.total_hops)
    plt.hist(dht.hop, bins=5)
    plt.title("Chord Distribution of hops when number of nodes = 100 with 50% nodes randomly deleted")
    plt.xlabel("Number of Hops")
    plt.ylabel("Distribution Count")
    plt.savefig("chord_distribution_r"+str(100) + ".svg")
    plt.show()

main([10])


