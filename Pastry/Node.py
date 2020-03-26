from utils import prefix_match,euclidean_distance,get_digit_at,compare_tables,insort
import math

class Node:
    def __init__(self,coordinate=None,ide=0,b=4,m=16,helper=None,nodelist=[]):
        self.ide = ide
        self.coord = coordinate
        self.leaf_set_small = []
        self.leaf_set_big = []
        self.routing_table = [[None for i in range(pow(2,b))] for j in range(math.ceil(math.log(pow(2,m),pow(2,b))))]
        self.neighbours = []
        self.joining_list = []
        if helper is not None:
            helper.join(node=self,nodelist=nodelist)

    def routing(self,node=None,init=False,nodelist = []):
        if init:
            node.joining_list.append(self)
        ide= node.ide   
        if len(self.leaf_set_small)!=0 and len(self.leaf_set_big)!=0 and ide >= self.leaf_set_small[0].ide and ide<=self.leaf_set_big[-1].ide:
            min_distance = math.inf
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
            if helper in node.joining_list:
                return self
            else:

                return helper.routing(node=node,init=init,nodelist=nodelist)

        elif len(self.leaf_set_big) == 0 and len(self.leaf_set_small)!=0 and ide >= self.leaf_set_small[0].ide and ide <= self.ide:
            min_distance = math.inf
            helper = None
            for i in range(len(self.leaf_set_small)):
                dist = abs(self.leaf_set_small[i].ide - node.ide)
                if min_distance > dist:
                    min_distance = dist
                    helper = self.leaf_set_small[i]
            if helper in  node.joining_list:
                return self
            else:

                return helper.routing(node=node,init=init,nodelist=nodelist)
        
        elif len(self.leaf_set_small) == 0 and len(self.leaf_set_big)!=0 and ide >= self.ide and ide <= self.leaf_set_big[-1].ide:
            min_distance = math.inf
            helper = None
            for i in range(len(self.leaf_set_big)):
                dist = abs(self.leaf_set_big[i].ide - node.ide)
                if min_distance > dist:
                    min_distance = dist
                    helper = self.leaf_set_big[i]
            if helper in node.joining_list:
                return self
            else:

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
                        if helper in  node.joining_list:
                            return self
                        return helper.routing(node=node,init=init,nodelist=nodelist)
                node.routing_table[l][get_digit_at(node.ide,l)] = self.ide
                return self

    def update_routing_table(self):
        for node in self.joining_list:
            self.routing_table = compare_tables(self.routing_table, node.routing_table,self)
    
    def update_others(self,nodelist=[], b =4):
        for node in nodelist:
            if node != self:
                node.routing_table = compare_tables(node.routing_table,self.routing_table,node)
                node.neighbours = insort(node.neighbours,self)
                if(node.ide < self.ide):
                    node.leaf_set_big = insort(node.leaf_set_big,self)
                else:
                    node.leaf_set_small = insort(node.leaf_set_small,self)
                if len(node.neighbours) > pow(2,b+1):
                    node.neighbours = node.neighbours[:-1]
                if len(node.leaf_set_small) > pow(2,b-1):
                    node.leaf_set_small = node.leaf_set_small[1:]
                if len(node.leaf_set_big) > pow(2,b-1):
                    node.leaf_set_big = node.leaf_set_big[:-1]

    def table_initialization(self,nodelist = [], b = 4):
        self.update_routing_table()
        self.update_others(nodelist, b)
    

    def join(self,node=None,nodelist = [],b = 4):
        closest_node = self.routing(node=node, nodelist=nodelist, init= True)
        node.neighbours = [i for i in self.neighbours]
        node.neighbours = insort(node.neighbours,self)
        node.leaf_set_small = [i for i in closest_node.leaf_set_small]
        node.leaf_set_big = [i for i in closest_node.leaf_set_big]
        if closest_node.ide > node.ide:
            node.leaf_set_big = insort(node.leaf_set_big,closest_node)
        else:
            node.leaf_set_small = insort(node.leaf_set_small,closest_node)
        if len(node.neighbours) > pow(2,b+1):
            node.neighbours = node.neighbours[:-1]
        if len(node.leaf_set_small) > pow(2,b-1):
            node.leaf_set_small = node.leaf_set_small[1:]
        if len(node.leaf_set_big) > pow(2,b-1):
            node.leaf_set_big = node.leaf_set_big[:-1]
        node.table_initialization(nodelist,b)





    