from Node import Node
import math
from hashlib import sha1

class DHT:
    '''This class defines the basic structure of chord DHT. 
       It supports operations such adding a node/files in the network, looking up for a file, and deleting nodes.'''
    
    def __init__(self,m=160):
        '''Keywords: 'm' is the number of hash bit.
           Function: Initializes a new chord DHT. ''' 

        self.m = m
        self.total_nodes = 0 #Keeps track of the number of nodes in the hash table.
        self.total_files = 0 #Keeps track of the number of files in the hash table
        self.node_list = {} #Keeps track of the nodes entered in the hash table.

    def add_node(self,ide):
        '''Keywords: 'ide' is the id of the node to be added in the network 
           Function: This function adds a new node with id = 'ide' in the DHT. '''

        node = Node(self.node_list,self.m,ide)
        if node:
            self.node_list[ide] = node
            self.total_nodes+=1
            print("Node with id "+str(ide)+" added in the dht successfully.")
            return True
        else:
            print("Error: The node with id "+str(ide)+" could not be added in the DHT.")
            return False

    def delete_node(self,ide):
        '''Keywords: 'ide' is the id of the node.
           Function: This function is used to delete a given node from the dht.  '''

        if ide not in self.node_list.keys():
            print(" The given node does not exist ")
            return False
        
        elif len(self.node_list.keys()) == 1: #only one node is in the list
            del self.node_list[ide]
            self.total_nodes-=1
            self.total_files = 0
            print("Node with id "+str(ide)+" deleted from the dht successfully.")
            return True

        else:
            node = self.node_list[ide]
            pred = node.pred
            succ = node.successor()
            pred.finger_table[0][2] = succ #node's successor's predecessor will be node's predecessor.
            pred.finger_table[0][3] = succ.ide
            succ.pred = pred #node's predecessor's successor will be node's successor.
            succ.key_values.update(node.key_values)
            for i in range(self.m):
                val = (node.ide - math.pow(2,i)) % math.pow(2,self.m)
                pred = pred.find_succ(val)
                if pred.ide != val:
                    pred = node.pred.find_pred(val)
                pred.update_Finger_Table(node,i,flag = 'delete')
            del self.node_list[ide]
            self.total_nodes-=1
            print("Node with id "+str(ide)+" deleted from the dht successfully.")
            return True
        
    def add_file(self,ide,data):
        '''Keywords: 'ide' is the id of the file.
                      'data' is the data of the file to be retrieved.
           Function: This function is used to add a particular file with id = ide in the dht. '''
        
        if self.total_nodes == 0:
            print("Error: DHT has no nodes")
            return False
        else:
            node = list(self.node_list.values())[0] #find a helper node
            file_node = node.find_succ(ide) #store the file at its successor
            file_node.key_values[ide] = data
            self.total_files+=1
            print("File with id "+str(ide)+" added in the dht successfully at the node with id "+str(file_node.ide)+".")
            return True
 
    def file_lookup(self,ide,logs=False):
        '''Keywords: 'ide' is the id of the file.
                     'logs' is the keyword to turn on and off log genration
           Function: This function tells the location of file with id = ide in the dht. '''

        if(self.total_nodes == 0):
            print("Error: The DHT has no node in it.")
            return
        elif(self.total_files == 0):
            print("Error: The DHT has no file in it.")
            return
        else:
            node = list(self.node_list.values())[0] #find a helper node
            print("Lookup for the file with id "+str(ide)+": ", end = "")
            file_node = node.find_succ(ide,logs=logs) #store the file at its successor
            try:
                data = file_node.key_values[ide]
                print("Data fetched successfully.")
                return data
            except KeyError:
                print("Error: Data not present in the dht.")
                return
            
