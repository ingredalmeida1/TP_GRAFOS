#Esse arquivo foi criado só para estruturar a pasta, podem apagar quando criarem outros arquivos na pasta

def ordem(dict_arquivo):

    ordem = dict_arquivo.numVertices
    return (ordem)

#def diametro():
    #N = ordem(dict_arquivo)
    #maior = 0
    #não tenho que inicializar i = 0?
    #for i range N
        #chama a função de excentricidade passando o vertice i
        #if exentricidade > maior
            #maior = exentricidade
    #return (maior)

def menorCaminhoSomatorio(self, vertice):
        matrizL = []
        matrizR = []
        infinito = float("inf") # Cria um número infinito
        n = self.quantidadeVertices
        
        # Inicialização das matrizes
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

        # Cálculo do menor caminho
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matrizL[i][j] > matrizL[i][k] + matrizL[k][j]:
                        matrizL[i][j] = matrizL[i][k] + matrizL[k][j]
                        matrizR[i][j] = matrizR[k][j]

        somatorio = 0

        for j in range (n):
            somatorio = somatorio +matrizL[j][vertice]
        return (somatorio)

def centralidade(dict_arquivo, vertice):
    N = ordem(dict_arquivo)
    C = (N-1)/menorCaminhoSomatorio(vertice)
    return (C)
