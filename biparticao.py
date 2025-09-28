from collections import deque

def bipartido(grafo):
    cor = {}
    for v in grafo:
        if v not in cor:
            cor[v] = 0
            fila = deque([v])
            while fila:
                u = fila.popleft()
                for viz in grafo[u]:
                    if viz not in cor:
                        cor[viz] = 1 - cor[u]
                        fila.append(viz)
                    elif cor[viz] == cor[u]:
                        return False, None
    return True, cor
