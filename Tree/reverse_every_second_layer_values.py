class Node:
    val = None
    left = None
    right = None

    def __init__(self, val):
        self.val = val

def reverseNodesArray(arr):
    for i in range(len(arr)//2):
        last = len(arr) - i - 1
        temp = arr[i].val
        arr[i].val = arr[last].val
        arr[last].val = temp

def printTree(root):
    arr = [root]
    while arr:
        curr = arr.pop(0)
        print(curr.val, end=" ")
        if curr and curr.left:
            arr.append(curr.left)
        if curr and curr.right:
            arr.append(curr.right)

def reverseEverySecondOrder(arr, level):
    if not arr:
        return
    nodes_at_level = []
    i = 0
    while i < 2^level:
        if not arr:
            i += 1
            continue
        node = arr.pop(0)
        if (level + 1)  %2 == 0:
            nodes_at_level.append(node)
        if node and node.left:
            arr.append(node.left)
        if node and node.right:
            arr.append(node.right)
        i += 1
    if level %2 == 0:
        print("Nodes to filp : ")
        for item in nodes_at_level:
            print(item.val, end=" ")
        print("")
        reverseNodesArray(nodes_at_level)
    reverseEverySecondOrder(arr, level+1)

def mainFunc():
    node = Node('a')
    node.left = Node('b')
    node.right = Node('c')
    node.left.left = Node('d')
    node.left.right = Node('e')
    node.right.left = Node('f')
    node.right.right = Node('g')
    node.left.left.left = Node('h')
    node.left.left.right = Node('i')
    node.left.right.left = Node('j')
    node.left.right.right = Node('k')
    node.right.left.left = Node('l')
    node.right.left.right = Node('m')
    node.right.right.left = Node('n')
    node.right.right.right = Node('o')

    print("Before reverseEverySecondOrder : ", end=" ")
    printTree(node)

    reverseEverySecondOrder([node], 0)
    print("")
    print("After reverseEverySecondOrder : ", end=" ")
    printTree(node)

    print("")
mainFunc()

'''
                             a
                b                           c
        d               e           f               g
    h       i       j       k   l       m       n       o
'''

'''
                             a
                c                           b
        d               e           f               g
    o       n       m       l   k       j       i       h
'''

