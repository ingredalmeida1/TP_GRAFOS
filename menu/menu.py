from grafo.GrafoNaoOrientado import Grafo
from leitor.LeitorTxt import TxtLeitor

def menu():
    print("="* 60)
    print(3*"\t","MENU")
    print("="* 60)

def escolhaArq():
    print("\n(0) Arquivo txt\n(1) Arquivo json")
    tipo = int(input(">>> "))
    return tipo

def biblioteca():
        print("\n")
        print("="* 60)
        print(3*"\t", "BIBLIOTECA:")
        print("="* 60)
        print("(0) Sair")
        print("(1) Ordem do grafo")
        print("(2) Tamanho do grafo")
        print("(3) Vizinhos de um vértice")
        print("(4) Grau de um vertice")
        print("(5) Sequência de graus")
        print("(6) Excentricidade de um vértice")
        print("(7) Raio do grafo")
        print("(8) Diâmetro do grafo")
        print("(9) Centro do grafo")
        print("(10) Busca em profundidade")
        print("(11) Distancia e caminho minimo ")
        print("(12) Centralidade de um vértice")
        print("(13) Imprimir o grafo")
        escolha = int(input(">>> "))
        return escolha