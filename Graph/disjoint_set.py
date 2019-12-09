disjoint_map = {}

class disJointSet:
    data = None
    parent = None
    rank = None

def makeSet(data):
    node = disJointSet()
    node.data = data
    node.rank = 0
    node.parent = node
    disjoint_map[data] = node

def union(data1, data2):
    node1 = disjoint_map[data1]
    node2 = disjoint_map[data2]

    parent1 = findSet(node1)
    parent2 = findSet(node2)

    if parent1.data == parent2.data:
        return
    
    if parent1.rank >= parent2.rank:
        if parent1.rank == parent2.rank:
            parent1.rank += 1
        parent2.parent = parent1
    else:
        parent1.parent = parent2

def findSetOfData(data):
    return findSet(disjoint_map[data]).data

def findSet(node):
    if node.parent == node:
        return node
    node.parent = findSet(node.parent)
    return node.parent

makeSet(1)
makeSet(2)
makeSet(3)
makeSet(4)
makeSet(5)
makeSet(6)
makeSet(7)

makeSet(11)
makeSet(12)
makeSet(13)
makeSet(14)

union(1,2)
union(1,3)
union(3,5)
union(4,7)
union(6,7)
union(1,6)

union(11,13)
union(12,13)
union(12,14)

union(7,13)
print(findSetOfData(1))
print(findSetOfData(2))
print(findSetOfData(3))
print(findSetOfData(4))
print(findSetOfData(5))
print(findSetOfData(6))
print(findSetOfData(7))

print(findSetOfData(12))
