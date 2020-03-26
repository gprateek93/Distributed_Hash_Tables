import math
from Hash_Table import *
import random
from utils import print_list,print_table

dht = DHT()
F = list(set([random.randrange(0, math.pow(2,16), 1) for i in range(100)]))

for i in F:
    print(i)
    dht.add_node(ide=i,coordinates=(i,i+1))

print("printing neighbours")
print(dht.node_list)
for k in dht.node_list:
    print_table(dht.node_list[k].routing_table,k,"Routing Table")
    


