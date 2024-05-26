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
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, title):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title(title)
    plt.show()

def generate_colors(n):
    return ["#" + ''.join([format(int(x*255), '02x') for x in colorsys.hsv_to_rgb(i/n, 1, 1)]) for i in range(n)]

def dfs(node, step_colors, step_count, visited):
    if node:
        node.color = step_colors[step_count[0]]
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

# Дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_cost = 0
    total_calories = 0
    chosen_items = []

    for item, details in sorted_items:
        if total_cost + details['cost'] <= budget:
            chosen_items.append(item)
            total_cost += details['cost']
            total_calories += details['calories']

    return chosen_items, total_cost, total_calories

def dynamic_programming(items, budget):
    item_list = list(items.items())
    n = len(item_list)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        item, details = item_list[i - 1]
        cost = details['cost']
        calories = details['calories']

        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    w = budget
    chosen_items = []
    total_cost = 0
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item, details = item_list[i - 1]
            chosen_items.append(item)
            total_cost += details['cost']
            w -= details['cost']

    chosen_items.reverse()
    total_calories = dp[n][budget]
    return chosen_items, total_cost, total_calories

budget = 100

greedy_items, greedy_total_cost, greedy_total_calories = greedy_algorithm(items, budget)
print(f"Жадібний алгоритм вибрав наступні страви:")
for item in greedy_items:
    print(f"- {item} (Вартість: {items[item]['cost']}, Калорійність: {items[item]['calories']})")
print(f"Загальна вартість: {greedy_total_cost}, Загальна калорійність: {greedy_total_calories}\n")

dp_items, dp_total_cost, dp_total_calories = dynamic_programming(items, budget)
print(f"Динамічне програмування вибрало наступні страви:")
for item in dp_items:
    print(f"- {item} (Вартість: {items[item]['cost']}, Калорійність: {items[item]['calories']})")
print(f"Загальна вартість: {dp_total_cost}, Загальна калорійність: {dp_total_calories}")
