
import math
import random
import matplotlib.pyplot as plt


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None


def distance(node1, node2):
    return math.sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2)


def nearest_neighbor(node_list, random_node):
    nearest_node = node_list[0]
    for node in node_list:
        if distance(node, random_node) < distance(nearest_node, random_node):
            nearest_node = node
    return nearest_node


def new_node(nearest_node, random_node, step_size):
    d = distance(nearest_node, random_node)
    if d <= step_size:
        return random_node
    else:
        theta = math.atan2(random_node.y - nearest_node.y, random_node.x - nearest_node.x)
        x = nearest_node.x + step_size * math.cos(theta)
        y = nearest_node.y + step_size * math.sin(theta)
        return Node(x, y)


def collision_free(node):
    # Comprueba si el nodo está dentro de una región segura
    # Devuelve True si el nodo es seguro, False si no lo es
    return True


def rrt(start, goal, max_iter, step_size):
    node_list = [start]
    for i in range(max_iter):
        random_node = Node(random.uniform(0, 10), random.uniform(0, 10))
        nearest_node = nearest_neighbor(node_list, random_node)
        new_node_ = new_node(nearest_node, random_node, step_size)
        if collision_free(new_node_):
            new_node_.parent = nearest_node
            node_list.append(new_node_)
        if distance(node_list[-1], goal) <= step_size:
            goal.parent = node_list[-1]
            node_list.append(goal)
            return node_list
    return None


def draw_graph(node_list):
    for node in node_list:
        if node.parent:
            plt.plot([node.x, node.parent.x], [node.y, node.parent.y], "k-", linewidth=0.5)
    for node in node_list:
        if distance(node, goal) <= 0.5:
            plt.plot(node.x, node.y, "ro")
        else:
            plt.plot(node.x, node.y, "bo")
    plt.plot(start.x, start.y, "go")
    plt.plot(goal.x, goal.y, "yo")
    plt.axis("equal")
    plt.axis([-1, 11, -1, 11])
    plt.show()


start = Node(0, 0)
goal = Node(10, 10)
max_iter = 1000
step_size = 1.0

node_list = rrt(start, goal, max_iter, step_size)
if node_list is not None:
    draw_graph(node_list)
else:
    print("Failed to find a path")