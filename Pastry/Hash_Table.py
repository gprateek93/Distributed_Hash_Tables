from Node import Node
from utils import euclidean_distance
import math

class DHT:
    def __init__(self, b=2, m=16):
        self.b = b
        self.m = m
        self.total_nodes = 0
        self.node_list = {}

    def add_node(self,ide=0,coordinates=None):
        L = list(self.node_list.values())
        min_distance = -math.inf
        helper = None
        for node in list(L):
            node_coord = node.coord
            dist = euclidean_distance(node_coord,coordinates)
            if dist<min_distance:
                min_distance = dist
                helper = node
        new_node = Node(coordinate=coordinates,ide=ide,b=self.b,m=self.m,helper=helper)
        if new_node:
            self.node_list[ide] = new_node
            self.total_nodes+=1
            print("Node with id "+str(ide)+" added in the dht successfully.")
            return True
        else:
            print("Error: The node with id "+str(ide)+" could not be added in the DHT.")
            return False

