from collections import defaultdict

def ler_grafo(arquivo):
    grafo = defaultdict(list)
    with open(arquivo, "r") as f:
        linhas = f.read().splitlines()
    tipo = linhas[0].strip()  # ND ou D
    for linha in linhas[1:]:
        a, b = linha.split()
        grafo[a].append(b)
        if tipo == "ND":
            grafo[b].append(a)
    return grafo

def sao_adjacentes(grafo, v1, v2):
    return v2 in grafo.get(v1, [])

def grau(grafo, v):
    return len(grafo.get(v, []))

def vizinhos(grafo, v):
    return grafo.get(v, [])

def listar_arestas(grafo):
    arestas = set()
    for u in grafo:
        for v in grafo[u]:
            arestas.add(tuple(sorted((u, v))))
    return sorted(arestas)
