import csv
import numpy as np


def vproximo(bart, homer, instancia):
	bart = np.sqrt(sum(np.power(bart - instancia, 2)))
	homer = np.sqrt(sum(np.power(homer - instancia, 2)))
  
	if bart == min(bart,homer):
		print(" \n Classificado como Bart");
	if homer == min(bart,homer):
		print("\n Classificado como Homer");

def loadInstancia():
	instancia = []
	perguntas = ['Idade(0-100): ','Sexo(0-1): ','Barba(0-1): ','Altura(0-10): ','Largura(0-5): ','Cabelo(0-10):','Quantidade de Filhos: ','Escolaridade:(0-8): ','Peso:(0-100): ','Cor:(0-5): ']
	print("Informe suas Caracteristicas respeitando a escala:")
	for pergunta in perguntas:
		instancia.append(int(input(pergunta)))

	return np.array(instancia)

def readCSV(arquivo):
	csvfile = open(arquivo)
	return csv.reader(csvfile, delimiter=',')


def main():
	bart = list(readCSV('Bart.csv'))
	homer = list(readCSV('Homer.csv'))
	print("Homer:", homer)
	print("Bart:", bart)
	homer =np.array([int(x) for x in homer[0]])
	bart = np.array([int(x) for x in bart[0]])
	instancia = loadInstancia()
	vproximo(bart, homer, instancia)


main()