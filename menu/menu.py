def menu():
    print("="* 60)
    print(3*"\t","MENU")
    print("="* 60)

def escolhaArq():
    print("\n(0) Arquivo txt\n(1) Arquivo json")
    tipo = int(input(">>> "))
    return tipo

def imprimeBiblioteca(vertice, grafo):
    print(f'VÉRTICE ESCOLHIDO: {vertice}\n')
    print("\n>>> Ordem do grafo: ", grafo.ordem())
    print("\n>>> Tamanho do grafo: ", grafo.tamanho())
    grafo.retornaVizinhos(vertice)
    grafo.grauVertice(vertice)
    grafo.sequenciaGraus()
    print("\n>>> Raio do grafo: ")
    print("\n>>> Diâmetro do grafo: ")
    print("\n>>> Centro do grafo: ")
    print("\n>>> Busca em profundidade: ")
    print("\n>>> Centralidade: ")
    grafo.menorCaminho(vertice)