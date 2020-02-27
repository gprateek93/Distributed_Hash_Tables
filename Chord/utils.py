import math

def chord_distance(a,b,m):
    if(b == a):
        return math.pow(2,m)
    res =  (b-a+math.pow(2,m)) % (math.pow(2,m)) 
    return int(res)


def contains(id_1,id_2,ide,m):
    if chord_distance(id_1,id_2,m) > chord_distance(id_1,ide,m):
        return True
    else:
        return False

def calculate_interval(ide,i,m):
    res = ide + math.pow(2,i)
    return int(res%math.pow(2,m))

