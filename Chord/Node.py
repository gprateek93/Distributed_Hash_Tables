from utils import *

class Node:
    ''' This class defines the bsic structure of a node in the distributed hash table. 
    It defines the attributes of the node and its functions'''

    def __init__(self,node_list = [], m = 160,ide = 0):
        '''Keywords: 'node_list' is the list of nodes in the dht. 'm' is the number of hash bits. 'ide' is the ide of the node.
           Function: Initialises a new node with the given ide'''
        self.m = m
        self.ide = ide
        self.finger_table = [] #initialize an empty finger table. Entry in a row is tuple <start_id,end_id,successor_node,successor node id>
        self.pred = self #initialise the node with the predecessor pointer pointing to itself.
        if len(node_list) == 0: #this is the first node in our dht
            finger_table = [] 
            for i in range(m):
                finger_table.append([calculate_interval(self.ide,i,m), calculate_interval(self.ide,i+1,m),self,self.ide]) #As it is the first node all the fingers will have same successor node that is the self node.
            self.finger_table = finger_table
        else: # Chose a random node in the dht and use that node to join the dht.
            self.join(node_list[0])
    
    def successor(self):
        '''This function takes returns the successor of the given node. The successor of the node is the first node in the node's finger table. '''
        return self.finger_table[0][2]

    def find_succ(self,ide):
        '''Keywords: 'ide' is the id of the node/resource whose successor is needed.
           Function: This function asks the self node to find the successor of the node/resource with id = 'ide'.'''
        
        n_ = self.find_pred(ide)
        return n_.successor() #successor of a node/resource is the successor of the predecessor of the node in the present network
    
    def find_pred(self,ide):
        '''Keywords: 'ide' is the id of the node/resource whose predecessor is needed.
           Function: This function asks the self node to find the predecessor of a node/resource with ide = ide'''

        n_ = self
        while not contains(n_.ide,n_.successor().ide,ide) and ide != n_.successor().ide: #run the loop until the ide comes between a node and its sucessor.
            n_ = n_.find_Closest_Preceding_Finger(ide)
        return n_

    def find_Closest_Preceding_Finger(self,ide):
        '''Keywords: 'ide' is the id of the node/resource.
           Function: This function returns the finger node of the self node whose id is closest preceding to the queried node/resource id'''
        
        m = self.m
        for i in range(m-1,-1,-1):
            if contains(self.ide,ide,self.finger_table[i][2].ide) : #if the ith finger of the self node lies between the self node and the queried node then this is the finger just preceding the queried id.
                return self.finger_table[i][2]

        return self #if there is no such finger between the self node and the queried node then return the self node.
    

    def join(self,node):
        ''' Keywords: 'node' is the helper node.
            Funciton: This function is used to insert the self node in the network by using the help of the helper node.'''

        self.init_finger_table(node) #initialize the finger table of the node
        self.update_others() #update the finger table of other nodes

    def init_finger_table(self,node):
        '''Keywords: 'node' is the helper node.
           Functoin: This function is used to initialize the finger table of the self node by using the help of the helper node. '''

        finger_table = [] #initialize an empty finger table. Entry in a row is tuple <start_id,end_id,successor_node,successor_node id>
        ide= self.ide
        m = self.m
        finger_table.append([calculate_interval(ide,0,m), calculate_interval(ide,1,m),None,0])
        finger_table[0][2] = node.find_succ(finger_table[0][0])
        finger_table[0][3] = finger_table[0][2].ide
        self.pred = finger_table[0][2].pred #The predecessor of the self node is the predecessor of the successor of the self node.
        finger_table[0][2].pred = self #The predecessor of the successor of the self node is self node itself.
        for i in range(m-1):
            finger_table.append([calculate_interval(ide,i+1,m),calculate_interval(ide,i+2,m),None,0])
            if finger_table[i+1][0] ==self.ide or contains(self.ide,finger_table[i][2].ide,finger_table[i+1][0]): #Current finger's start lies between the self node and previous finger's successor.
                finger_table[i+1][2] = finger_table[i][2]
                finger_table[i+1][3] = finger_table[i+1][2].ide
            else: 
                finger_table[i+1][2] = node.find_succ(finger_table[i+1][0])
                finger_table[i+1][3] = finger_table[i+1][2].ide
        self.finger_table = finger_table
        print(self.finger_table)
        

    def update_others(self):
        '''Function: This function is used to update the finger table of other nodes in the network which are affected by the addition of the new self node. '''

        for i in range(self.m):
            # find the last node pred whose ith finger might be self node
            val = self.ide - math.pow(2,i)
            pred = self.find_succ(val) #if the val is itself a node we need that also so we will find its successor's predecessor.
            if pred.ide != val:
                pred = self.find_pred(val)
            if pred.ide == self.ide: #no need to update the finger table of the pred node as it is the same self node.
                continue
            pred.update_Finger_Table(self,i)
        
    def update_Finger_Table(self,node,i):
        '''Keywords: 'node' is the node who has affected the self node by getting added into the network.
                      'i' is the number of the finger table entry which might be affected.
           Function: This function updates self node's finger table if ith finger of the self node is the new node. '''

    
        if self.ide == node.ide or contains(node.successor().ide, self.finger_table[i][2].ide,node.ide):
            self.finger_table[i][2] = node
            self.finger_table[i][3] = self.finger_table[i][2].ide
            pred = self.pred #get the first node preceding self as chances are that it also needs to be updated.
            if pred.ide != node.ide:
                pred.update_Finger_Table(node,i)
    