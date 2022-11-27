from grafo.GrafoNaoOrientado import Grafo
from leitor.LeitorTxt import TxtLeitor
from leitor.LeitorJSON import converteJSON
from menu.menu import biblioteca, escolhaArq, menu, menuBiblioteca

menu()
tipoEntrada = escolhaArq()

if tipoEntrada == 0:
    nomeSimplesTxt = input("\nNome do arquivo txt: ")
    nomeArquivoTxt = f'{nomeSimplesTxt}.txt'
    dados = TxtLeitor(nomeArquivoTxt)
    numVertices = dados['numVertices']
    grafo = Grafo(numVertices)
    list_arestas = dados.items()
    for aresta in list_arestas:
        if aresta[0] != 'numVertices':
            vertice1 = int(aresta[1]['vertice1'])
            vertice2 = int(aresta[1]['vertice2'])
            peso = float(aresta[1]['peso'])
            grafo.adicionaAresta(vertice1, vertice2, peso)
else:
    nomeSimplesJson = input("\nNome do arquivo JSON: ")
    nomeArquivoJson = f'{nomeSimplesJson}.json'
    nomeTxt = nomeSimplesJson + "_json.txt"
    converteJSON(nomeArquivoJson, nomeTxt)
    dados = TxtLeitor(nomeTxt)
    numVertices = dados['numVertices']
    grafo = Grafo(numVertices)
    list_arestas = dados.items()
    for aresta in list_arestas:
        if aresta[0] != 'numVertices':
            vertice1 = int(aresta[1]['vertice1'])
            vertice2 = int(aresta[1]['vertice2'])
            peso = 1
            grafo.adicionaAresta(vertice1, vertice2, peso)

while (True):
    escolha = menuBiblioteca()
    if escolha == 0:
        break
    else:
        biblioteca(grafo, numVertices, escolha)