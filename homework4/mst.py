from heapq import heappush, heappop

def initialize_graph_from_string(graph_description):
    graph = []
    for edge in graph_description.split("|"):
        t = edge.split(",")
        t = (t[0], t[1], int(t[2]))
        graph.append(t)
    return graph

def add_first_node_to_tree(tree, node):
    tree['nodes'].append(node)

def add_node_to_tree(node, tree, existing_node, weight):
    if node not in tree['nodes']:
        tree['nodes'].append(node)
        tree['edges'].append( (node, existing_node, weight) )

def add_neighbors_to_queue(graph, queue, tree, node):
    for node1, node2, weight in graph:
        if node1 in tree['nodes'] and node2 in tree['nodes']:
            continue
        if node in [node1, node2]:
            heappush(queue, (weight, (node1, node2)))

def both_nodes_in_tree(tree, node1, node2):
    return node1 in tree['nodes'] and node2 in tree['nodes']

def all_nodes_in_tree(tree, graph):
    for node1, node2, weight in graph:
        if (node1 or node2) not in tree['nodes']:
            return False
    return True

def mst(graph_description):
    tree = {'nodes': [], 'edges': []}
    queue = []
    graph = initialize_graph_from_string(graph_description)

    if len(graph) == 0:
        return []

    first_node = graph[0][0]
    add_first_node_to_tree(tree, first_node)
    add_neighbors_to_queue(graph, queue, tree, first_node)

    while len(queue) > 0:
        weight, (node1, node2) = heappop(queue)
        if both_nodes_in_tree(tree, node1, node2):
            continue
        node, existing_node = (node1,node2) if node2 in tree['nodes'] else (node2,node1)
        add_node_to_tree(node, tree, existing_node, weight)
        add_neighbors_to_queue(graph, queue, tree, node)

    if all_nodes_in_tree(tree, graph):
        return tree
    else:
        print("This graph is not connected")
        raise UnconnectedGraphException
    
class Error(Exception):
    "Base class for other exceptions"
    pass

class UnconnectedGraphException(Error):
    "When the graph is not connected"
    pass



g = "A,B,3|B,C,10|C,A,4|D,E,2|E,A,6"
print(mst(g))
g = "A,B,3|B,C,10|C,A,4|D,E,2|E,A,6|J,K,7"
print(mst(g))
