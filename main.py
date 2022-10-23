from grafo.GrafoNaoOrientado import Grafo
from leitor.LeitorTxt import TxtLeitor
from menu.menu import biblioteca, escolhaArq, menu

menu()
tipoEntrada = escolhaArq()

if tipoEntrada == 0: 
    arq = input("\nNome do arquivo txt: ")
    dados = TxtLeitor(arq)
    numVertices = dados['numVertices']
    grafo = Grafo(numVertices)
    list_arestas = dados.items()
    for aresta in list_arestas:
        if aresta[0] != 'numVertices':
            vertice1 = int(aresta[1]['vertice1'])
            vertice2 = int(aresta[1]['vertice2'])
            peso = float(aresta[1]['peso'])
            grafo.adicionaAresta(vertice1, vertice2, peso)

while(True):
    escolhaFuncao = biblioteca()
    print("\n")
    if escolhaFuncao == 1:
        print("\n>>> Ordem do grafo: ", grafo.ordem())
    elif escolhaFuncao == 2:
        print("\n>>> Tamanho do grafo: ", grafo.tamanho())
    elif escolhaFuncao == 3:
        v = int(input(">>> Escolha um vértice para saber seus vizinhos: "))
        grafo.retornaVizinhos(v)
    elif escolhaFuncao == 4:
        v = int(input(">>> Escolha um vértice para saber seu grau: "))
        grafo.grauVertice(v)
    elif escolhaFuncao == 5:
        grafo.sequenciaGraus()
    elif escolhaFuncao == 6:
        print("\n>>> Excentricidade do vértice: ")
    elif escolhaFuncao == 7:
        print("\n>>> Raio do grafo: ")
    elif escolhaFuncao == 8:
        print("\n>>> Diâmetro do grafo: ")
    elif escolhaFuncao == 9:
        print("\n>>> Centro do grafo: ")
    elif escolhaFuncao == 10:
        print("\n>>> Busca em profundidade: ")
    elif escolhaFuncao == 11:
        v = int(input(">>> Escolha um vértice de origem: "))
        grafo.menorCaminho(v)
    elif escolhaFuncao == 12:
        print("\n>>> Centralidade: ")
    elif escolhaFuncao == 13:
        print("\n>>> Grafo representado por uma lista de adjacência: \n")
        grafo.exibeGrafo()
    else:
        break