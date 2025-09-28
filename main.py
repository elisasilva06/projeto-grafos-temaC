from grafo import ler_grafo, sao_adjacentes, grau, vizinhos, listar_arestas
from biparticao import bipartido
from visualizacao import desenhar_grafo

def menu():
    print("\n--- Agendador de Processos Concorrentes ---")
    print("1 - Verificar adjacência")
    print("2 - Calcular grau de um processo")
    print("3 - Listar vizinhos de um processo")
    print("4 - Listar todas as arestas")
    print("5 - Testar bipartição (2-coloração)")
    print("6 - Visualizar grafo")
    print("0 - Sair")

def main():
    caminho = input("Digite o caminho do arquivo de entrada (.txt): ")
    grafo = ler_grafo(caminho)
    print(f"Grafo carregado do arquivo: {caminho}\n")

    vertices = list(grafo.keys())  # Lê automaticamente todos os vértices

    print("--- Informações do Grafo ---")

    # Verificar adjacência de todos os pares de vértices
    print("\nAdjacência entre vértices:")
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            v1 = vertices[i]
            v2 = vertices[j]
            print(f"{v1} - {v2}: {'Sim' if sao_adjacentes(grafo, v1, v2) else 'Não'}")

    # Grau de cada vértice
    print("\nGrau de cada vértice:")
    for v in vertices:
        print(f"{v}: {grau(grafo, v)}")

    # Vizinhos de cada vértice
    print("\nVizinhos de cada vértice:")
    for v in vertices:
        print(f"{v}: {vizinhos(grafo, v)}")

    # Listar todas as arestas
    print("\nArestas do grafo:")
    print(listar_arestas(grafo))

    # Testar bipartição
    print("\nTeste de bipartição (2-coloração):")
    ok, cores = bipartido(grafo)
    if ok:
        grupo1 = [v for v in cores if cores[v] == 0]
        grupo2 = [v for v in cores if cores[v] == 1]
        print("É possível agendar em 2 turnos ✅")
        print("Turno 1:", grupo1)
        print("Turno 2:", grupo2)
    else:
        print("Não é possível agendar em apenas 2 turnos ❌")

    # Visualizar grafo
    print("\nVisualização do grafo:")
    desenhar_grafo(grafo, cores if ok else None)

if __name__ == "__main__":
    main()

    
