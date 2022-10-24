class Grafo:
    matrizL = []
    matrizR = []
    somatorio = 0

    def __init__(self, quantidadeVertices):
        self.quantidadeVertices = quantidadeVertices
        self.aresta = [[0 for j in range(self.quantidadeVertices)] for i in range(self.quantidadeVertices)]


    def adicionaAresta(self, vertice1, vertice2, peso):
        self.aresta[vertice1 - 1][vertice2 - 1] = peso
        self.aresta[vertice2 - 1][vertice1 - 1] = peso


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


    def retornaVizinhos(self, vertice):
        vizinhos = []
        for i in range(self.quantidadeVertices):
            if self.aresta[vertice - 1][i] != 0:
                vizinhos.append(i + 1)
        print(f"\n>>> Vizinhos do vértice {vertice} -> {vizinhos}")


    def grauVertice(self, vertice):
        grau = 0
        for i in range(self.quantidadeVertices):
            if self.aresta[vertice - 1][i] != 0:
                grau += 1
        print(f'\n>>> Grau do vértice {vertice}: {grau}')


    def sequenciaGraus(self):
        sequencia = [0 for i in range(self.quantidadeVertices)]
        for i in range(self.quantidadeVertices):
            for j in range(self.quantidadeVertices):
                if self.aresta[i][j] != 0:
                    sequencia[i] += 1
        sequencia.sort(reverse=True)
        print(f'\n>>> Sequência de graus do grafo: {sequencia}')

    
    # def excentricidade()
    # def raio()
    # def diametro()
    # def centro()
    # def buscaProfundidade()


    def centralidade(self, vertice):
        flag = self.floydWarshall(vertice)
        if flag == 1:
            for j in range(self.quantidadeVertices):
                self.somatorio = self.somatorio + self.matrizL[j][vertice]
            N = self.ordem()
            C = (N-1)/self.somatorio
            return (round(C, 2))
        else:
            return "Ciclo negativo identificado, por consequência não é possível calcular"


    def floydWarshall(self, vertice):
        n = self.quantidadeVertices
        infinito = float("inf")
        for i in range(n):
            self.matrizL.append([infinito] * n)
            self.matrizR.append([0] * n)
        for i in range(n):
            for j in range(n):
                if i == j:
                    self.matrizL[i][j] = 0
                elif self.aresta[i][j] != 0:
                    self.matrizL[i][j] = self.aresta[i][j]
        for i in range(n):
            for j in range(n):
                if self.matrizL[i][j] != infinito:
                    self.matrizR[i][j] = i + 1
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if self.matrizL[i][j] > self.matrizL[i][k] + self.matrizL[k][j]:
                        self.matrizL[i][j] = self.matrizL[i][k] + self.matrizL[k][j]
                        self.matrizR[i][j] = self.matrizR[k][j]
        for i in range(n):
            for j in range(n):
                if i == j:
                    if self.matrizL[i][j] < 0:
                        print(">>> Ciclo negativo identificado, não é possível encontrar o menor caminho")
                        return 0
                    else:
                        return 1
        

    def imprimeCaminhoMinimo(self, vertice):
        flag = self.floydWarshall(vertice)
        if flag == 1:
            rot = self.matrizR[vertice - 1]
            for i in range(len(rot)):
                print(f'>>> Caminho mínimo entre {vertice} e {i + 1}: {round(rot[i], 2)}')
            print("\n")
            dt = self.matrizL[vertice - 1]
            for i in range(len(dt)):
                print(f'>>> Distância entre {vertice} e {i + 1}: {round(dt[i], 2)}')
        else:
            return