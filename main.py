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

    while True:
        menu()
        opc = input("Escolha uma opção: ")
        
        if opc == "1":
            v1 = input("Vértice 1: ")
            v2 = input("Vértice 2: ")
            print("São adjacentes?", sao_adjacentes(grafo, v1, v2))
        
        elif opc == "2":
            v = input("Vértice: ")
            print("Grau de", v, "=", grau(grafo, v))
        
        elif opc == "3":
            v = input("Vértice: ")
            print("Vizinhos de", v, ":", vizinhos(grafo, v))
        
        elif opc == "4":
            print("Arestas:", listar_arestas(grafo))
        
        elif opc == "5":
            ok, cores = bipartido(grafo)
            if ok:
                grupo1 = [v for v in cores if cores[v] == 0]
                grupo2 = [v for v in cores if cores[v] == 1]
                print("É possível agendar em 2 turnos ✅")
                print("Turno 1:", grupo1)
                print("Turno 2:", grupo2)
            else:
                print("Não é possível agendar em apenas 2 turnos ❌")
        
        elif opc == "6":
            ok, cores = bipartido(grafo)
            desenhar_grafo(grafo, cores if ok else None)
        
        elif opc == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
