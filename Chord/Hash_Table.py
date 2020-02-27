from Node import Node

class DHT:
    def __init__(self,m=160):
        self.m = m
        self.total_nodes = 0
        self.node_list = []

    def add_node(self,ide):
        node = Node(self.node_list,self.m,ide)
        if node:
            self.node_list.append(node)
            self.total_nodes+=1

    
