# def backtrack(nbrs, visited, path):
#    if len(path) == len(nbrs):
#       return path
#    curr = path[-1]
#    for nbr in nbrs[curr]:
#       if nbr not in visited:
#          visited.add(nbr)
#          path.append(nbr)
#          ret = backtrack(nbrs, visited, path)
#          if ret:
#             return ret
#          visited.remove(nbr)
#          path.pop(-1)
#    return None

# def itinerary(flights: list[tuple], start: str) -> list[str]:
#   visited = set()
#   nbrs = {}
#   for x, y in flights:
#     if x in nbrs:
#       nbrs[x].append(y)
#     else:
#        nbrs[x] = [y]
#     if y not in nbrs:
#        nbrs[y] = []
#   visited.add(start)
#   return backtrack(nbrs, visited, [start]) 

from collections import defaultdict

def itinerary(flights, start):
    nbrs = defaultdict(list)
    cities = set()
    for s, t in flights:
        nbrs[s].append(t)
        cities.add(s)
        cities.add(t)
    for s in nbrs:
        nbrs[s].sort()
    path = []
    visited = set([start])
    visited_edge = set()
    def visit(curr):
        while nbrs[curr]:
            nbr = nbrs[curr].pop(0)
            edge = (curr, nbr)
            if edge not in visited_edge:
                visited_edge.add(edge)
                visited.add(nbr)
                visit(nbr)
        path.append(curr)
    visit(start)
    if len(visited) == len(cities):
        return path[::-1]
    else:
        return None

if __name__ == "__main__":
    flights = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
    start = 'YUL'
    result = itinerary(flights, start)
    print(flights)
    print(start)
    print(result)  # Output: ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
    print('*'*70)
   #  flights = [('SFO', 'COM'), ('COM', 'YYZ')]
   #  start = 'COM'
    flights = [('a', 'c'), ('c', 'a'), ('a', 'b')]
    start = 'a'
    result = itinerary(flights, start)
    print(flights)
    print(start)
    print(result)  # Output: None

