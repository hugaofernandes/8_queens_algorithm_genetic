
from random import randint
import numpy as np


class Individuo(object):
    
    tamanho_cromossomo = 8

    def __init__(self):
        self.avaliacao = 0
        self.cromossomo = []
        self.gerar_cromossomo()
        
    def avaliar(self):
        x = 0
    	diagonais = []
    	for y in self.cromossomo:
    		_x = x
    		_y = y
		_x -= 1
    		_y -= 1
    		while (_x>=0 or _y>=0): #superior_esquerda
    			diagonais.append([_x, _y])
			_x -= 1
    			_y -= 1
    		_x = x
    		_y = y
		_x += 1
    		_y += 1
    		while (_x<self.tamanho_cromossomo or _y<self.tamanho_cromossomo): #inferior_direita
    			diagonais.append([_x, _y])
			_x += 1
    			_y += 1
    		_x = x
    		_y = y
		_x -= 1
    		_y += 1
    		while (_x>=0 or _y<self.tamanho_cromossomo): #superior_direita
    			diagonais.append([_x, _y])
			_x -= 1
    			_y += 1
    		_x = x
    		_y = y
		_x += 1
    		_y -= 1
    		while (_x<self.tamanho_cromossomo or _y>=0): #inferior_esquerda
    			diagonais.append([_x, _y])
			_x += 1
    			_y -= 1
    		x += 1
    	x = 0
    	for y in self.cromossomo:
    		self.avaliacao += diagonais.count([x, y])
    		x += 1

    def crossover(self, outro_individuo, taxa_crossover):
        novo_cromossomo = []
        corte = int(self.tamanho_cromossomo * taxa_crossover)
        for i in range(corte):
            novo_cromossomo.append(self.cromossomo[i])
        for i in set(novo_cromossomo).symmetric_difference(outro_individuo.cromossomo):
            novo_cromossomo.append(i)
        #print (self.cromossomo)
        #print (outro_individuo.cromossomo)
        #print (novo_cromossomo)
        filho = Individuo()
        filho.cromossomo = novo_cromossomo
        filho.avaliar()
        return filho

    def mutacao(self):
        gene_1 = randint(0, self.tamanho_cromossomo - 1)
	gene_2 = gene_1
	while(gene_1 == gene_2):
	        gene_2 = randint(0, self.tamanho_cromossomo - 1)
        aux = self.cromossomo[gene_1]
        self.cromossomo[gene_1] = self.cromossomo[gene_2]
        self.cromossomo[gene_2] = aux
        self.avaliar()

    def gerar_cromossomo(self):
        self.cromossomo = np.random.permutation(self.tamanho_cromossomo).tolist()
        self.avaliar()
        

