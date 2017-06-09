# sample graph implemented as a dictionary
graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}



# visits all the nodes of a graph (connected component) using BFS
def bfs1(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]

    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]

            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored


bfs1(graph, 'A')



def bfs(graph, start):
    visited , queue , record = set(), [start], []
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            record.append(vertex)
            queue.extend(set(graph[vertex]) - visited)
    return [visited, record]

bfs(graph, 'A')[1]

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

list(bfs_paths(graph, 'G', 'D'))


def dfs(graph, start):
    visited, stack, record = set(), [start], []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            record.append(vertex)
            stack.extend(set(graph[vertex]) - visited)
    return [visited,record]


dfs(graph, 'A')[1]

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

list(dfs_paths(graph, 'G', 'D'))



