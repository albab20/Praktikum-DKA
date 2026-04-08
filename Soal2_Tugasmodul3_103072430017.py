import networkx as nx

G = nx.Graph()

edges = [
    ("Jakarta", "Cirebon", 327),
    ("Jakarta", "Bandung", 270),
    ("Bandung", "Cirebon", 120),
    ("Bandung", "Yogyakarta", 373),
    ("Cirebon", "Semarang", 305),
    ("Cirebon", "Yogyakarta", 210),
    ("Semarang", "Surakarta", 97),
    ("Semarang", "Surabaya", 369),
    ("Yogyakarta", "Surakarta", 60),
    ("Surakarta", "Surabaya", 370),
    ("Surabaya", "Malang", 94),
    ("Yogyakarta", "Malang", 109)
]

G.add_weighted_edges_from(edges)


paths = dict(nx.all_pairs_dijkstra_path(G))
distances = dict(nx.all_pairs_dijkstra_path_length(G))

print("=== SHORTEST PATH GRAF PULAU JAWA ===\n")

for src in paths:
    for dst in paths[src]:
        print(f"{src} -> {dst}")
        print(f"Path   : {paths[src][dst]}")
        print(f"Jarak  : {distances[src][dst]}")
        print("-" * 40)