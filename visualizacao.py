import networkx as nx
import matplotlib.pyplot as plt

def desenhar_grafo(grafo, cores=None):
    G = nx.Graph()
    for u in grafo:
        for v in grafo[u]:
            G.add_edge(u, v)

    pos = nx.spring_layout(G, seed=42)
    if cores:
        cores_nos = ["skyblue" if cores[n]==0 else "lightcoral" for n in G.nodes()]
    else:
        cores_nos = "lightgray"

    nx.draw(G, pos, with_labels=True, node_color=cores_nos, node_size=800, font_size=10)
    plt.show()
