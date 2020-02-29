from Node import Node

class DHT:
    '''This class defines the basic structure of chord DHT. It supports operations such adding a node/files in the network, looking up for a file, and deleting nodes.'''
    
    def __init__(self,m=160):
        '''Keywords: 'm' is the number of hash bit.
           Function: Initializes a new chord DHT. ''' 

        self.m = m
        self.total_nodes = 0 #Keeps track of the number of nodes in the hash table.
        self.node_list = [] #Keeps track of the nodes entered in the hash table.

    def add_node(self,ide):
        '''Keywords: 'ide' is the id of the node to be added in the network 
           Function: This function adds a new node with id = 'ide' in the DHT. '''

        node = Node(self.node_list,self.m,ide)
        if node:
            self.node_list.append(node)
            self.total_nodes+=1

    
