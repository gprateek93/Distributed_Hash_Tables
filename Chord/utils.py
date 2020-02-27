import math

def chord_distance(a,b,m):
    return (b-a+math.pow(2,m)) % (math.pow(2,m))


def contains(id_1,id_2,id,m):
    if chord_distance(id_1,id_2,m) > chord_distance(id_1,id,m):
        return True
    else:
        return False

       