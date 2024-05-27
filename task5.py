import uuid
import networkx as nx
import matplotlib.pyplot as plt
import colorsys

class Node:
    def __init__(self, key, color="#000000"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=str(node.val))
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

def draw_tree(tree_root, title):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    colors = [node_data['color'] for node, node_data in tree.nodes(data=True)]
    labels = {node: node_data['label'] for node, node_data in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title(title)
    plt.show()

def generate_colors(n):
    # Generate colors from dark to light in shades of blue
    return ["#" + ''.join([format(int(x*255), '02x') for x in colorsys.hsv_to_rgb(0.6, 1, (i+1)/n)]) for i in range(n)]

def dfs(node, step_colors, step_count, visited):
    if node:
        node.color = step_colors[step_count[0]]
        print(f"DFS visiting node {node.val} with color {node.color}")
        visited.append(node)
        step_count[0] += 1
        dfs(node.left, step_colors, step_count, visited)
        dfs(node.right, step_colors, step_count, visited)

def bfs(root, step_colors, visited):
    queue = [root]
    step_count = [0]
    while queue:
        node = queue.pop(0)
        if node:
            node.color = step_colors[step_count[0]]
            print(f"BFS visiting node {node.val} with color {node.color}")
            visited.append(node)
            step_count[0] += 1
            queue.append(node.left)
            queue.append(node.right)

def build_heap(array):
    if not array:
        return None

    nodes = [Node(val) for val in array]

    for i in range(len(nodes) // 2):
        if 2 * i + 1 < len(nodes):
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < len(nodes):
            nodes[i].right = nodes[2 * i + 2]

    return nodes[0]

array = [3, 1, 6, 5, 2, 4]

heap_root = build_heap(array)

node_count = len(array)
step_colors = generate_colors(node_count)

print("DFS Traversal:")
visited_dfs = []
dfs(heap_root, step_colors, [0], visited_dfs)
draw_tree(heap_root, "DFS Traversal")

heap_root = build_heap(array)
step_colors = generate_colors(node_count)

print("BFS Traversal:")
visited_bfs = []
bfs(heap_root, step_colors, visited_bfs)
draw_tree(heap_root, "BFS Traversal")
