def menu():
    print("="* 60)
    print(3*"\t","MENU")
    print("="* 60)

def escolhaArq():
    print("\n(0) Arquivo txt\n(1) Arquivo json")
    tipo = int(input(">>> "))
    return tipo

def imprimeBiblioteca(vertice, grafo, n):
    grafo.floydWarshall(vertice)
    print(f'VÉRTICE ESCOLHIDO: {vertice}')
    print("\n>>> Ordem do grafo: ", grafo.ordem())
    print("\n>>> Tamanho do grafo: ", grafo.tamanho())
    grafo.retornaVizinhos(vertice)
    grafo.grauVertice(vertice)
    grafo.sequenciaGraus()
    print(f'\n>>> Excentricidade do vértice {vertice}: ', grafo.excentricidade(vertice))
    print("\n>>> Raio do grafo: ")
    print("\n>>> Diâmetro do grafo: ")
    print("\n>>> Centro do grafo: ")
    print("\n>>> Busca em profundidade: ")
    print("\n>>> Distância e caminho mínimo\n")
    for i in range(n):
        print(f'>>>Caminho minimo entre {vertice} e {i + 1}: {grafo.imprimeCaminho(vertice, i + 1)}')
    print("\n")
    grafo.imprimeDistancia(vertice)
    print("\n>>> Centralidade: ", grafo.centralidade(vertice))
    print("\n")