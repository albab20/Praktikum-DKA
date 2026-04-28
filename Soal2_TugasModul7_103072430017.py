import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

edges = [
    ("Jakarta", "Cirebon", 327),
    ("Jakarta", "Bandung", 270),
    ("Bandung", "Cirebon", 120),
    ("Bandung", "Yogyakarta", 373),
    ("Cirebon", "Semarang", 305),
    ("Cirebon", "Yogyakarta", 210),
    ("Yogyakarta", "Semarang", 109),
    ("Yogyakarta", "Surakarta", 60),
    ("Semarang", "Surakarta", 97),
    ("Semarang", "Surabaya", 369),
    ("Surakarta", "Malang", 370),
    ("Surabaya", "Malang", 94)
]

G.add_weighted_edges_from(edges)

path = nx.dijkstra_path(G, "Bandung", "Malang")
cost = nx.dijkstra_path_length(G, "Bandung", "Malang")

print("Path:", path)
print("Cost:", cost)

pos = {
    "Jakarta": (0, 3),
    "Bandung": (1, 1),
    "Cirebon": (2, 3),
    "Semarang": (4, 3),
    "Yogyakarta": (4, 1),
    "Surakarta": (5, 2),
    "Surabaya": (7, 3),
    "Malang": (7, 1)
}

plt.figure(figsize=(10,5))
nx.draw(G, pos, with_labels=True, node_size=800, font_size=9)

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

path_edges = list(zip(path, path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3)

plt.title("Graf Jawa (Layout Mirip Soal)")
plt.show()