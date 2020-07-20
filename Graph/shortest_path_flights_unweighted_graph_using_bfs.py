
from collections import defaultdict

flights =  [['GUJ', 'MUM'], ['MUM', 'DEL'],['DEL', 'KOL'],['GUJ', 'BENG'],['BENG', 'KOL']]

# 'guj': 'beng', 'mum'
# 'beng': 'kol'
# 'del': 'kol'
# 'mum': 'del'

# OP: 'guj' ->'beng' -> 'kol'

flights_graph = defaultdict(list)

shortest_paths = {}

for i in flights:
    src, dest = i[0], i[1]
    flights_graph[src].append(dest)
    shortest_paths[src] = []
    shortest_paths[dest] = []

src = 'GUJ'
dest = 'KOL'

visited = set()

def explore(graph, src, dest, visited, shortest_paths):
    queue = [src]
    shortest_paths[src] = [src]
    visited.add(src)
    while queue:
        for i in range(len(queue)):
            curr = queue.pop(0)
            if curr == dest:
                return shortest_paths
            for item in graph[curr]:
                if item not in visited:
                    visited.add(item)
                    shortest_paths[item] = shortest_paths[curr]+ [item]
                    queue.append(item)
    return None

else:
    if explore(flights_graph, src, dest, visited, shortest_paths):
        if dest in shortest_paths and shortest_paths[dest]:
            print("Shortest path from : ", src, " to ", dest, " is : ", shortest_paths[dest])
        else:
            print("No flights go from : ", src, " to ", dest)
    else:
        print("No flights go from : ", src, " to ", dest)
