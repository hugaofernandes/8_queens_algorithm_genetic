
# -*- coding: UTF-8 -*-

from individuo import Individuo
from random import randint
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText


def gerar_populacao(tamanho_populacao):
    populacao = []
    for i in range(tamanho_populacao):
        individuo = Individuo()
        #print (individuo)
        #print (individuo.cromossomo)
        populacao.append(individuo)
    return populacao

def roleta(populacao):
    avaliacao_total = 0
    roleta = []
    for individuo in populacao:
        avaliacao_total += individuo.avaliacao
    for individuo in populacao:
        #print (float(populacao[i].avaliacao)/float(avaliacao_total))
        porcentagem_individuo = (float(individuo.avaliacao)/float(avaliacao_total))*100
        for k in range(int(porcentagem_individuo)):
            roleta.append(individuo)
    return roleta

def avaliacao(geracao):
    aux = Individuo()
    aux.avaliacao = 64*64
    melhor_avaliacao = aux
    for individuo in geracao:
        if (individuo.avaliacao <= melhor_avaliacao.avaliacao):
            melhor_avaliacao = individuo
    return melhor_avaliacao

def main(tamanho_populacao, taxa_crossover, taxa_mutacao):
    nova_geracao = gerar_populacao(tamanho_populacao)
    #print (nova_geracao)
    numero_geracao = 1
    _taxa_crossover = int(tamanho_populacao*taxa_crossover)
    solucao = avaliacao(nova_geracao)
    relatorio_geracao = []
    relatorio_avaliacao = []
    relatorio_geracao.append(numero_geracao)
    relatorio_avaliacao.append(solucao.avaliacao)
    while (solucao.avaliacao != 0):
        aux = []
        _roleta = roleta(nova_geracao)
        tamanho_roleta = len(_roleta)
        #print (tamanho_roleta)
        for j in range(tamanho_populacao - _taxa_crossover):
            aux.append(_roleta[randint(0, tamanho_roleta - 1)])
        for j in range(_taxa_crossover):
            pai_1 = _roleta[randint(0, tamanho_roleta - 1)]
	    count = 0
	    pai_2 = pai_1
	    while (count < tamanho_roleta and pai_1.cromossomo == pai_2.cromossomo):
                pai_2 = _roleta[randint(0, tamanho_roleta - 1)]
		count += 1
            #print (pai_1)
            #print (pai_2)
            filho = pai_1.crossover(pai_2, taxa_crossover)
            aux.append(filho)
        if (randint(0, 100) <= taxa_mutacao*100):
            aux[randint(0, tamanho_populacao - 1)].mutacao()
        nova_geracao = aux
	numero_geracao += 1
        solucao = avaliacao(nova_geracao)
        relatorio_geracao.append(numero_geracao)
        relatorio_avaliacao.append(solucao.avaliacao)
    return solucao.cromossomo, relatorio_geracao, relatorio_avaliacao

def graficos(populacao, taxa_crossover, taxa_mutacao):
    result = main(populacao, taxa_crossover, taxa_mutacao)
    # Imprime Grafico Geracoes por aptidao
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title("Populacao: " + str(populacao) + " Taxa_Crossover: " + str(taxa_crossover) + " Taxa_Mutacao: " + str(taxa_mutacao))
    ax.set_xlabel('Geracoes')
    ax.set_ylabel('Aptidao')
    cromossomo_solucao = AnchoredText("Cromossomo Solucao: " + str(result[0]), loc=2)
    ax.add_artist(cromossomo_solucao)
    plt.plot(result[1], result[2])
    plt.show()
    # Imprime Tabuleiro de Xadrez com posicoes das rainhas
    nrows, ncols = 8, 8
    image = np.zeros(nrows*ncols)
    image = image.reshape((nrows, ncols))
    a = np.arange(nrows //2)
    a.fill(1)
    for i in range(0, nrows, 2):
        image[i][::2] = a
        image[i+1][1::2] = a
    x = 0
    for y in result[0]:
        image[x][y] = 2
        x += 1
    row_labels = range(nrows)
    col_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    plt.matshow(image, cmap=plt.cm.gray)
    plt.xticks(range(ncols), col_labels)
    plt.yticks(range(nrows), row_labels)
    plt.show()


if __name__ == "__main__":
    graficos(3, 0.5, 0.1)
    #graficos(10, 0.7, 0.5)
    #graficos(15, 0.9, 0.15)




