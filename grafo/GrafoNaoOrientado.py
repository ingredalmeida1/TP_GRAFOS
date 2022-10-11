class Grafo:
    def __init__(self, quantidadeVertices):
        self.quantidadeVertices = quantidadeVertices
        # Como em uma lista de adjacência eu só sei que o número de 
        # linhas será igual ao de colunas, e não se as posições vão
        # estar ocupadas, eu apenas inicializo as linhas
        self.grafo = [[] for i in range(self.quantidadeVertices)]

    def adicionaAresta(self, vertice1, vertice2, peso):
        # É preciso adicionar de vertice1 para vertice2 e vice e versa
        # pois se trata de um grafo não direcionado, então a direção não
        # importa, e precisa ser adicionado nas duas linhas
        self.grafo[vertice1 - 1].append([vertice2, peso])
        self.grafo[vertice2 - 1].append([vertice1, peso])

    def exibeGrafo(self):
        for i in range(self.quantidadeVertices):
            print(f'{i + 1}:', end=' ')
            for j in (self.grafo[i]):
                print(f'{j}', end=' ')
            print('')

# Variáveis que serão lidas do arquivo.txt
quantidadeVertices = 5

# Inicializando o grafo
grafo = Grafo(quantidadeVertices)

# Adicionando arestas
grafo.adicionaAresta(1, 2, 1.2)
grafo.adicionaAresta(2, 5, 2.3)
grafo.adicionaAresta(3, 5, -8.4)
grafo.adicionaAresta(3, 4, 0.3)
grafo.adicionaAresta(4, 5, 4.6)
grafo.adicionaAresta(1, 5, 0.1)

# Mostrando o grafo
grafo.exibeGrafo()