from biblioteca.biblioteca_amostra import ordem


class Grafo:
    somatorio = 0

    def __init__(self, quantidadeVertices):
        self.quantidadeVertices = quantidadeVertices
        self.aresta = [[0 for j in range(self.quantidadeVertices)] for i in range(self.quantidadeVertices)]


    def adicionaAresta(self, vertice1, vertice2, peso):
        self.aresta[vertice1 - 1][vertice2 - 1] = peso
        self.aresta[vertice2 - 1][vertice1 - 1] = peso


    def exibeGrafo(self):
        print("=" * 25)
        print("\t", "GRAFO")
        print("=" * 25)
        for i in range(self.quantidadeVertices):
            print(f'{i + 1}:', end=' ')
            for j in range(self.quantidadeVertices):
                if self.aresta[i][j] != 0:
                    print(f' -> {j + 1}', end=' ')
            print('')
        print("\n")


    def retornaVizinhos(self, vertice):
        vizinhos = []
        for i in range(self.quantidadeVertices):
            if self.aresta[vertice - 1][i] != 0:
                vizinhos.append(i + 1)
        print(f">>> Vizinhos do vértice {vertice} -> {vizinhos}")
        print("\n")


    def menorCaminho(self, vertice):
        matrizL = []
        matrizR = []
        infinito = float("inf")
        n = self.quantidadeVertices
        for i in range(n):
            matrizL.append([infinito] * n)
            matrizR.append([0] * n)
        for i in range(n):
            for j in range(n):
                if i == j:
                    matrizL[i][j] = 0
                elif self.aresta[i][j] != 0:
                    matrizL[i][j] = self.aresta[i][j]
        for i in range(n):
            for j in range(n):
                if matrizL[i][j] != infinito:
                    matrizR[i][j] = i + 1
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matrizL[i][j] > matrizL[i][k] + matrizL[k][j]:
                        matrizL[i][j] = matrizL[i][k] + matrizL[k][j]
                        matrizR[i][j] = matrizR[k][j]
        self.imprimeDistancia(matrizL[vertice - 1], vertice)
        print("\n")
        for i in range(n):
            self.imprimeCaminhoMinimo(matrizR[vertice - 1], vertice, i + 1)


    def imprimeDistancia(self, vetorDT, vertice):
        for i in range(len(vetorDT)):
            print(f'Distância entre {vertice} e {i + 1}: {round(vetorDT[i], 2)}')

    def imprimeCaminhoMinimo(self, vetorROT, vertice1, vertice2):
        vertices = []
        proximo = vertice2
        for i in range(len(vetorROT)):
            vertices.append(proximo)
            if vetorROT[proximo - 1] == 0:
                print(vertice1)
                return
            elif vetorROT[proximo - 1] != vertice1:
                proximo = vetorROT[proximo - 1]
            else:
                break
        vertices.append(vertice1)
        vertices.reverse()
        print(f'Menor caminho entre {vertice1} e {vertice2}:')
        for v in vertices:
            print(f' -> {v}', end=" ")
        print(" ")

    def grauVertice(self, vertice):
        grau = 0
        for i in range(self.quantidadeVertices):
            if self.aresta[vertice - 1][i] != 0:
                grau += 1
        print(f'>>> Grau do vértice {vertice}: {grau}\n')


    def sequenciaGraus(self):
        sequencia = [0 for i in range(self.quantidadeVertices)]
        for i in range(self.quantidadeVertices):
            for j in range(self.quantidadeVertices):
                if self.aresta[i][j] != 0:
                    sequencia[i] += 1

        sequencia.sort(reverse=True)
        print(f'\n>>> Sequência de graus do grafo: {sequencia}\n')


    def ordem(self):
        ordem = self.quantidadeVertices
        return ordem


    def tamanho(self):
        tam = 0
        for i in range(self.quantidadeVertices):
            for j in range(self.quantidadeVertices):
                if self.aresta[i][j] != 0:
                    tam += 1
        tam = tam / 2
        return int(tam)


    def centralidade(self, vertice):
        N = ordem()
        self.menorCaminho(vertice)
        C = (N-1)/self.somatorio
        return (C)

