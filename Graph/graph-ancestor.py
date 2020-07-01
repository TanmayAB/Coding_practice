"""
Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

For example, in this diagram, the earliest ancestor of 6 is 14, and the earliest ancestor of 15 is 2. 

         14
         |
  2      4
  |    / | \
  3   5  8  9
 / \ / \     \
15  6   7    11

Write a function that, for a given individual in our dataset, returns their earliest known ancestor -- the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return any one of them. If the input individual has no parents, the function should return null (or -1).

Sample input and output:

parent_child_pairs_3 = [
    (2, 3), (3, 15), (3, 6), (5, 6), (5, 7),
    (4, 5), (4, 8), (4, 9), (9, 11), (14, 4),
]

find_earliest_ancestor(parent_child_pairs_3, 8) => 14
find_earliest_ancestor(parent_child_pairs_3, 7) => 14
find_earliest_ancestor(parent_child_pairs_3, 6) => 14
find_earliest_ancestor(parent_child_pairs_3, 15) => 2
find_earliest_ancestor(parent_child_pairs_3, 14) => null or -1
find_earliest_ancestor(parent_child_pairs_3, 11) => 14

Additional example:

  14
  |
  2      4    1
  |    / | \ /
  3   5  8  9
 / \ / \     \
15  6   7    11

parent_child_pairs_4 = [
    (2, 3), (3, 15), (3, 6), (5, 6), (5, 7),
    (4, 5), (4, 8), (4, 9), (9, 11), (14, 2), (1, 9)
]

find_earliest_ancestor(parent_child_pairs_4, 8) => 4
find_earliest_ancestor(parent_child_pairs_4, 7) => 4
find_earliest_ancestor(parent_child_pairs_4, 6) => 14
find_earliest_ancestor(parent_child_pairs_4, 15) => 14
find_earliest_ancestor(parent_child_pairs_4, 14) => null or -1
find_earliest_ancestor(parent_child_pairs_4, 11) => 4 or 1

n: number of pairs in the input


"""
from collections import defaultdict

parent_child_pairs_3 = [
    (2, 3), (3, 15), (3, 6), (5, 6), (5, 7),
    (4, 5), (4, 8), (4, 9), (9, 11), (14, 4),
]

parent_child_pairs_4 = [
    (2, 3), (3, 15), (3, 6), (5, 6), (5, 7),
    (4, 5), (4, 8), (4, 9), (9, 11), (14, 2), (1, 9)
]



def build_set_of_pairs(parent_child_pairs):
    set_of_pairs = set()

    for item in parent_child_pairs:
        p,c = item
        set_of_pairs.add(p)
        set_of_pairs.add(c)
    
    return set_of_pairs
    # print(set_of_pairs)

def build_child_parent_dict(parent_child_pairs):
    heirarchy = defaultdict(list)
    
    for item in parent_child_pairs:
        p, c = item
#         print(p,c)
        heirarchy[c].append(p)
    
    return heirarchy
#     print(heirarchy)


def find_nodes_with_zero_and_one_parents(parent_child_pairs):

    heirarchy = build_child_parent_dict(parent_child_pairs)

    set_of_pairs = build_set_of_pairs(parent_child_pairs)

    result = []

    nodes_with_zero_parents = []
    nodes_with_exactly_one_parent = []

    for item in heirarchy:
        set_of_pairs.remove(item)
        if len(heirarchy[item]) == 1:
            nodes_with_exactly_one_parent.append(item)

    nodes_with_zero_parents = list(set_of_pairs)

    result.append(nodes_with_zero_parents)
    result.append(nodes_with_exactly_one_parent)

    return result

# print(find_nodes_with_zero_and_one_parents(parent_child_pairs_1))
    

def get_parents(heirarchy, node, result):
    if node in heirarchy:
        for item in heirarchy[node]:
            result.add(item)
            get_parents(heirarchy, item, result)
    return result

def has_common_ancestor(parent_child_pairs, node1, node2):
    
    heirarchy = build_child_parent_dict(parent_child_pairs)
    parents_set_1 = set()
    parents_set_2 = set()
    
    parents_set_1 = get_parents(heirarchy, node1, parents_set_1)
    parents_set_2 = get_parents(heirarchy, node2, parents_set_2)
    
    if parents_set_1.intersection(parents_set_2):
        return True
    else:
        return False
    

# print(has_common_ancestor(parent_child_pairs_1, 5, 8))

# print(has_common_ancestor(parent_child_pairs_1, 3, 8)) #=> false
# print(has_common_ancestor(parent_child_pairs_1, 5, 8)) # => true
# print(has_common_ancestor(parent_child_pairs_1, 6, 8)) #=> true
# print(has_common_ancestor(parent_child_pairs_1, 6, 9)) #=> true
# print(has_common_ancestor(parent_child_pairs_1, 1, 3)) #=> false
# print(has_common_ancestor(parent_child_pairs_1, 3, 1)) #=> false
# print(has_common_ancestor(parent_child_pairs_1, 7, 11))# => true
# print(has_common_ancestor(parent_child_pairs_1, 6, 5))#=> true
# print(has_common_ancestor(parent_child_pairs_1, 5, 6)) #=> true


# print(has_common_ancestor(parent_child_pairs_2, 4, 12))# => true
# print(has_common_ancestor(parent_child_pairs_2, 1, 6))# => false
# print(has_common_ancestor(parent_child_pairs_2, 1, 12))# => false

def get_farthest_parent(heirarchy, node, counter):
  #  print("Checking for node : ", node)
    to_send = {"counter":counter, "parent":node}
    if node in heirarchy and heirarchy[node]:
        for item in heirarchy[node]:
            result = get_farthest_parent(heirarchy, item, counter + 1)
            if result["counter"] > to_send["counter"]:
                to_send["counter"] = result["counter"]
                to_send["parent"] = result["parent"]
        return to_send
    else:
        return {"counter":counter, "parent":node}


def find_earliest_ancestor(parent_child_pairs, node):
    heirarchy = build_child_parent_dict(parent_child_pairs)
    if node not in heirarchy:
        return {"counter": -1, "parent":"-1"}
    return get_farthest_parent(heirarchy, node, 0)


# print(find_earliest_ancestor(parent_child_pairs_3, 8) )#=> 14
# print(find_earliest_ancestor(parent_child_pairs_3, 7) )#=> 14
# print(find_earliest_ancestor(parent_child_pairs_3, 6) )#=> 14
# print(find_earliest_ancestor(parent_child_pairs_3, 15))# => 2
# print(find_earliest_ancestor(parent_child_pairs_3, 14))# => null or -1
# print(find_earliest_ancestor(parent_child_pairs_3, 11))# => 14



print(find_earliest_ancestor(parent_child_pairs_4, 8) )#=> 4
print(find_earliest_ancestor(parent_child_pairs_4, 7) )#=> 4
print(find_earliest_ancestor(parent_child_pairs_4, 6) )#=> 14
print(find_earliest_ancestor(parent_child_pairs_4, 15))# => 14
print(find_earliest_ancestor(parent_child_pairs_4, 14))# => null or -1
print(find_earliest_ancestor(parent_child_pairs_4, 11))# => 4 or 1
