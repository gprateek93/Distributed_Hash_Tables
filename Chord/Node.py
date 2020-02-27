from utils import *

class Node:
    def __init__(self,m,id,succ,pred,fingerTable):
        self.m = m
        self.id = id
        self.succ = succ
        self.pred = pred
        self.finger_table = fingerTable
    
    def find_succ(self,id):
        n_ = self.find_pred(id)
        return n_.succ
    
    def find_pred(self,id):
        n_ = self
        while not contains(n_.id,n_.succ.id,id,self.m) and id != n_.succ.id:
            n_ = n_.find_Closest_Preceding_Finger(id)

        return n_

    def find_Closest_Preceding_Finger(self,id):
        m = self.m
        for i in range(m-1,-1,-1):
            if contains(self.id,id,self.finger_table[i].node.id,m):
                return self.finger_table[i].node
        return self
    


    