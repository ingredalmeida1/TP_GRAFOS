class Grafo:
    matrizL = []
    matrizR = []
    somatorio = 0
    flag = 0

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

    
    def excentricidade(self, vertice):
        if self.flag == 1:
            dt = self.matrizL[vertice - 1]
            dt.sort()
            return (dt[-1])
        else:
            print(
                "Ciclo negativo identificado, por consequência não é possível calcular"
            )


    def raio(self):
        if self.flag == 1:
            menor = self.excentricidade(0)
            for i in range(self.quantidadeVertices):
                a = self.excentricidade(i)

                if (a < menor):
                    menor = a
            return menor
        else:
            return "Ciclo negativo identificado, por consequência não é possível calcular"


    def diametro(self):
        if self.flag == 1:
            maior = 0
            for i in range(self.quantidadeVertices):
                excentricidade = self.excentricidade(i)
                if excentricidade > maior:
                    maior = excentricidade
            return (maior)
        else:
            return "Ciclo negativo identificado, por consequência não é possível calcular"
    
    def centro(self):
        menor = self.raio()
        centro = []
        for i in range(self.quantidadeVertices):
            if self.excentricidade(i) == menor:
                centro.append(i)
        return centro


    # def buscaProfundidade()


    def centralidade(self, vertice):
        if self.flag == 1:
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
                        self.flag = 0
                    else:
                        self.flag = 1
        

    def imprimeCaminho(self, vOrigem, vDestino):
        if self.flag == 1:
            caminho = []
            caminho.append(vDestino)
            i = self.matrizR[vOrigem - 1][vDestino - 1]
            while(True):
                caminho.append(i)
                if i == vOrigem:
                    break
                else:
                    i = self.matrizR[vOrigem-1][i-1]
            caminho.reverse()
            return caminho
        else:
            return

    def imprimeDistancia(self, vertice):
        dt = self.matrizL[vertice - 1]
        for i in range(len(dt)):
            print(f'>>> Distância entre {vertice} e {i + 1}: {round(dt[i], 2)}')