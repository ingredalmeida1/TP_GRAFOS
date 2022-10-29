import os


def menu():
    print("=" * 60)
    print(3 * "\t", "MENU")
    print("=" * 60)


def escolhaArq():
    print("\n(0) Arquivo txt\n(1) Arquivo json")
    tipo = int(input(">>> "))
    return tipo


def biblioteca(grafo, numVertices):
    print("ESCOLHA UMA FUNCIONALIDADE:\n")
    print("(0) Para sair")
    print("(1) Ordem do grafo")
    print("(2) Tamnho do grafo")
    print("(3) Retornar vizinhos do vértice")
    print("(4) Grau do vértice")
    print("(5) Sequência de graus")
    print("(6) Excentricidade do vértice")
    print("(7) Raio do grafo")
    print("(8) Diâmetro do grafo")
    print("(9) Centro do grafo")
    print("(10) Busca em profundidade")
    print("(11) Distância e caminho mínimo")
    print("(12) Centralidade")
    escolha = int(input(">>> "))
    os.system("clear")

    vertice = int(input("\nEscolha um vértice: "))
    if vertice > grafo.ordem():
        print("O vértice digitado não existe no grafo")
        return
    else:
        grafo.floydWarshall(vertice)
        if escolha == 1:
            print("\n>>> Ordem do grafo: ", grafo.ordem())
        elif escolha == 2:
            print("\n>>> Tamanho do grafo: ", grafo.tamanho())
        elif escolha == 3:
            grafo.retornaVizinhos(vertice)
        elif escolha == 4:
            grafo.grauVertice(vertice)
        elif escolha == 5:
            grafo.sequenciaGraus()
        elif escolha == 6:
            print(f'\n>>> Excentricidade do vértice {vertice}: ',
                  grafo.excentricidade(vertice))
        elif escolha == 7:
            print("\n>>> Raio do grafo: ", grafo.raio())
        elif escolha == 8:
            print("\n>>> Diâmetro do grafo: ", grafo.diametro())
        elif escolha == 9:
            print("\n>>> Centro do grafo: ", grafo.centro())
        elif escolha == 10:
            print(f"\n>>> Busca em profundidade {vertice} : ",
                  grafo.buscaProfundidade(vertice))
        elif escolha == 11:
            print("\n>>> Distância e caminho mínimo\n")
            for i in range(numVertices):
                print(
                    f'>>>Caminho minimo entre {vertice} e {i + 1}: {grafo.imprimeCaminho(vertice, i + 1)}'
                )
            print("\n")
            grafo.imprimeDistancia(vertice)
        elif escolha == 12:
            print("\n>>> Centralidade: ", grafo.centralidade(vertice))
        else:
            return