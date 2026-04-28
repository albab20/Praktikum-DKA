import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

edges = [
    ("Arad", "Zerind", 75), ("Arad", "Timisoara", 118), ("Arad", "Sibiu", 140),
    ("Zerind", "Oradea", 71), ("Oradea", "Sibiu", 151),
    ("Sibiu", "Fagaras", 99), ("Sibiu", "Rimnicu Vilcea", 80),
    ("Rimnicu Vilcea", "Pitesti", 97), ("Rimnicu Vilcea", "Craiova", 146),
    ("Pitesti", "Bucharest", 101), ("Fagaras", "Bucharest", 211),
    ("Timisoara", "Lugoj", 111), ("Lugoj", "Mehadia", 70),
    ("Mehadia", "Drobeta", 75), ("Drobeta", "Craiova", 120),
    ("Craiova", "Pitesti", 138),
    ("Bucharest", "Giurgiu", 90), ("Bucharest", "Urziceni", 85),
    ("Urziceni", "Hirsova", 98), ("Hirsova", "Eforie", 86),
    ("Urziceni", "Vaslui", 142), ("Vaslui", "Iasi", 92),
    ("Iasi", "Neamt", 87)
]

G.add_weighted_edges_from(edges)

path = nx.dijkstra_path(G, "Arad", "Bucharest")
cost = nx.dijkstra_path_length(G, "Arad", "Bucharest")

print("Path:", path)
print("Cost:", cost)

pos = {
    "Arad": (1, 5), "Zerind": (1, 7), "Oradea": (2, 8),
    "Sibiu": (3, 5.5), "Timisoara": (1, 3), "Lugoj": (2, 2),
    "Mehadia": (2, 1), "Drobeta": (2, 0),
    "Craiova": (4, 0), "Rimnicu Vilcea": (4, 4),
    "Fagaras": (5, 5.5), "Pitesti": (5, 3),
    "Bucharest": (7, 3),
    "Giurgiu": (7, 1),
    "Urziceni": (8, 3),
    "Hirsova": (9, 3),
    "Eforie": (10, 2),
    "Vaslui": (9, 5),
    "Iasi": (9, 7),
    "Neamt": (8, 8)
}

plt.figure(figsize=(12,8))
nx.draw(G, pos, with_labels=True, node_size=700, font_size=8)

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7)

path_edges = list(zip(path, path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3)

plt.title("Graf Eropa (Layout Mirip Soal)")
plt.show()