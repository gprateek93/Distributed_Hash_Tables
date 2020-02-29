import math

def contains(start_id, end_id,node_id):
    '''Keywords: 'start_id' is the starting index of the limit. 'end_id' is the ending index of the limit. 'node_id' is the index of the queried node
       Function: This function is used to tell if the node id lies in the range (start_id,end_id) or not. ''' 

    if node_id == start_id or node_id == end_id: #Return False as () is considered.
        return False
    elif start_id == end_id: #return true as this will cover the whole circle
        return True
    elif start_id > end_id: 
        return not contains(end_id,start_id,node_id) #circular property
    else:
        if node_id > start_id and node_id < end_id:
            return True
        return False

def calculate_interval(ide,i,m):
    '''Keywords: 'ide' is the id of the queried node. 'i' is the index of the finger whose location is neede. 'm' is the number of hash bits.
       Functions: This function is used to calculate the id of the ith finger of the node with id = ide '''
       
    res = ide + math.pow(2,i)
    return int(res%math.pow(2,m))

