
def TxtLeitor(nomeArquivo):
     
    with open(nomeArquivo, 'r') as arq:
        #pegar o numero de vertices e retornar
        numVertices = arq.readline()
        numVertices = int(numVertices)
        dict_arquivo = {
            'numVertices' : numVertices,
        }
        #pegar para cada um dos vertices, as as arestas que ligam neles e os pesos
        for linha in arq:
            vertice1, vertice2, peso = linha.rstrip('\n').split(' ')
            dict_aresta = {
                'aresta-'+vertice1+'-'+vertice2:{
                    'vertice1' : vertice1,
                    'vertice2' : vertice2,
                    'peso' : peso,
                },
            }
            dict_arquivo.update(dict_aresta)
           
    return(dict_arquivo)
