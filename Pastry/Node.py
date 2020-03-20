from utils import prefix_match,euclidean_distance,get_digit_at
import math
from bisect import insort

class Node:
    def __init__(self,coordinate=None,ide=0,b=2,m=16,helper=None):
        self.ide = ide
        self.coord = coordinate
        self.leaf_set_small = []
        self.leaf_set_big = []
        self.routing_table = []
        self.neighbours = []
        self.joining_list = []
        if helper is not None:
            helper.join(self)

    def routing(self,node=None,init=False,nodelist = []):
        if init:
            node.joining_list.append(self)
        ide= node.ide
        if ide >= self.leaf_set_small[0].ide and ide<=self.leaf_set_big[-1].ide:
            min_distance = -math.inf
            helper = None
            for i in range(len(self.leaf_set_small)):
                dist = abs(self.leaf_set_small[i].ide - node.ide)
                if min_distance > dist:
                    min_distance = dist
                    helper = self.leaf_set_small[i]
            
            for i in range(len(self.leaf_set_big)):
                dist = abs(self.leaf_set_big[i].ide - node.ide)
                if min_distance > dist:
                    min_distance = dist
                    helper = self.leaf_set_big[i]
            return helper.routing(node=node,init=init,nodelist=nodelist)
        else:
            l = prefix_match(self.ide,node.ide)
            n = get_digit_at(node.ide,l+1)
            if self.routing_table[l+1][n]:
                return self.routing_table[l+1][n].routing(node=node,init=init,nodelist=nodelist)
            else:
                for helper in nodelist:
                    l1 = prefix_match(helper.ide,node.ide)
                    if(l1>=l) and abs(helper.ide - node.ide) < abs(self.ide - node.ide):
                        return helper.routing(node=node,init=init,nodelist=nodelist)
                return self


    def table_initialization(self,nodelist = []):
        self.update_routing_table()
        self.update_others(nodelist)
    

    def join(self,node=None,nodelist = [],b = 4):
        closest_node = self.routing(node=node, nodelist=nodelist, init= True)
        node.neighbours = self.neighbours
        insort(node.neighbours,self.ide)
        node.leaf_set_small = closest_node.leaf_set_small
        node.leaf_set_big = closest_node.leaf_set_big
        if closest_node.ide > node.ide:
            insort(node.leaf_set_big,closest_node.ide)
        else:
            insort(node.leaf_set_small,closest_node.ide)
        if len(node.neighbours) > pow(2,b):
            node.neighbours = node.neighbours[:-1]
        if len(node.leaf_set_small) > pow(2,b-1):
            node.leaf_set_small = node.leaf_set_small[1:]
        if len(node.leaf_set_big) > pow(2,b-1):
            node.leaf_set_big = node.leaf_set_big[:-1]
        node.table_initialization(nodelist)





    