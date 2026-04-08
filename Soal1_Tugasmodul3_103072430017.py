import networkx as nx

G = nx.Graph()

edges = [
    ("Arad", "Zerind", 75),
    ("Zerind", "Oradea", 71),
    ("Oradea", "Sibiu", 151),
    ("Arad", "Sibiu", 140),
    ("Arad", "Timisoara", 118),
    ("Timisoara", "Lugoj", 111),
    ("Lugoj", "Mehadia", 70),
    ("Mehadia", "Drobeta", 75),
    ("Drobeta", "Craiova", 120),
    ("Craiova", "Rimnicu Vilcea", 146),
    ("Craiova", "Pitesti", 138),
    ("Rimnicu Vilcea", "Sibiu", 80),
    ("Rimnicu Vilcea", "Pitesti", 97),
    ("Sibiu", "Fagaras", 99),
    ("Fagaras", "Bucharest", 211),
    ("Pitesti", "Bucharest", 101),
    ("Bucharest", "Giurgiu", 90),
    ("Bucharest", "Urziceni", 85),
    ("Urziceni", "Hirsova", 98),
    ("Hirsova", "Eforie", 86),
    ("Urziceni", "Vaslui", 142),
    ("Vaslui", "Iasi", 92),
    ("Iasi", "Neamt", 87)
]

G.add_weighted_edges_from(edges)

paths = dict(nx.all_pairs_dijkstra_path(G))
distances = dict(nx.all_pairs_dijkstra_path_length(G))

print("=== SHORTEST PATH GRAF EROPA ===\n")

for src in paths:
    for dst in paths[src]:
        print(f"{src} -> {dst}")
        print(f"Path   : {paths[src][dst]}")
        print(f"Jarak  : {distances[src][dst]}")
        print("-" * 40)