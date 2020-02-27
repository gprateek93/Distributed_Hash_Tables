from utils import *

class Node:
    ''' This class defines the bsic structure of a node in the distributed hash table. 
    It defines the attributes of the node and its functions'''

    def __init__(self,node_list = [], m = 160,ide = 0):
        '''Initialises a new node with the given ide'''
        self.m = m
        self.ide = ide
        # self.finger_table = []
        if len(node_list) == 0: #this is the first node in our dht
            finger_table = []   #initialize an empty finger table. Entry in a row is tuple <start_id,end_id,successor_node>
            for i in range(m):
                finger_table.append([calculate_interval(self.ide,i,m), calculate_interval(self.ide,i+1,m),self,self.ide]) #As it is the first node all the fingers will have same successor node that is the self node.
            self.finger_table = finger_table
            self.pred = self
        else:
            self.join(node_list[0])
    
    def find_succ(self,ide):
        '''This function finds the successor of a node/resource with ide = ide'''
        n_ = self.find_pred(ide)
        return n_.finger_table[0][2] #successor of the node is the successor of the predecessor of the node in the present network
    
    def find_pred(self,ide):
        '''This function finds the predecessor of a node/resource with ide = ide'''
        n_ = self
        counter = 0
        # #print("insid_pred")
        # #print(n_.ide, n_.finger_table[0][2].ide)
        while not contains(n_.ide,n_.finger_table[0][2].ide,ide,self.m) and ide != n_.finger_table[0][2].ide:
            n_ = n_.find_Closest_Preceding_Finger(ide)
            ##print(counter+1)
            counter = counter+1

        return n_

    def find_Closest_Preceding_Finger(self,ide):
        '''This function returns the finger node whose ide is closest preceding to the queried node/resource ide'''
        m = self.m
        # #print("here")
        for i in range(m-1,-1,-1):
            if contains(self.ide,ide,self.finger_table[i][2].ide,m) :
                return self.finger_table[i][2]
        return self
    

    def join(self,node):
        ''' This function is used to insert a new node in the network.'''
        self.init_finger_table(node) #initialize the finger table of the node
        self.update_others() #update the finger table of other nodes

    def init_finger_table(self,node):
        '''This function is used to initialize the finger table of the given node '''
        finger_table = [] #initialize an empty finger table. Entry in a row is tuple <start_id,end_id,successor_node>
        self.finger_table = finger_table
        ide= self.ide
        m = self.m
        finger_table.append([calculate_interval(ide,0,m), calculate_interval(ide,1,m),None,0])
        finger_table[0][2] = node.find_succ(finger_table[0][0])
        finger_table[0][3] = finger_table[0][2].ide
        #print(finger_table[0])
        #print("here")
        self.pred = finger_table[0][2].pred
        finger_table[0][2].pred = self
        self.pred.finger_table[0][2] = self
        for i in range(m-1):
            finger_table.append([calculate_interval(ide,i+1,m),calculate_interval(ide,i+2,m),None,0])
            #print(finger_table[i+1][0])
            if finger_table[i+1][0] ==self.ide or contains(self.ide,finger_table[i][2].ide,finger_table[i+1][0],self.m):
                #print("here")
                finger_table[i+1][2] = finger_table[i][2]
            else:
                #print("here")
                finger_table[i+1][2] = node.find_succ(finger_table[i+1][0])
            finger_table[i+1][3] = finger_table[i+1][2].ide

        self.finger_table = finger_table
        #print(finger_table)
        

    def update_others(self):
        for i in range(self.m):
            #update the finger table of those nodes whose ith finger is self node.
            # #print(self.ide)
            #print((self.ide - math.pow(2,i)) % math.pow(2,self.m))
            pred = self.find_pred((self.ide - math.pow(2,i)) % math.pow(2,self.m))
            #print(pred.ide)
            pred.update_Finger_Table(self,i)
        
    def update_Finger_Table(self,node,i):
        if contains(self.finger_table[i][0], self.finger_table[i][2].ide,node.ide,self.m):
            self.finger_table[i][2] = node
            self.finger_table[i][3] = self.finger_table[i][2].ide
            pred = self.pred
            if pred.ide != node.ide:
                pred.update_Finger_Table(node,i)
    