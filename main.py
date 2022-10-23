from grafo.GrafoNaoOrientado import Grafo
from leitor.LeitorTxt import TxtLeitor
from menu.menu import escolhaArq, imprimeBiblioteca, menu
import os

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

vertice = int(input("\nEscolha um vértice: "))
os.system("clear")
imprimeBiblioteca(vertice, grafo)