import numpy as np
import matplotlib.pyplot as plt

def graficoDispersao(X, Y):
	plt.scatter(np.array(X), np.array(Y), marker = 'x', color='r')
	plt.title("Dispersão")
	plt.xlabel('Quilometragem')
	plt.ylabel('Preço de Venda')
	plt.show()

def graficoDispersaoRegressao(X, Y, b0, b1):
	plt.scatter(np.array(X), np.array(Y), marker = 'x', color='r')
	plt.plot(np.array(X),np.array(b0 +b1*X), label='y = b0 + b1*X')
	plt.scatter(np.array(X), np.array(b0 +b1*(X)), marker = 'o', color='g')
	plt.title("Linha de Regresão")
	plt.xlabel('Quilometragem')
	plt.ylabel('Preço de Venda')
	plt.legend()
	plt.show()

def loadData(fileName):
    print(fileName)
    data = np.matrix(np.loadtxt(fileName, delimiter=',', skiprows = 1))
    return (data[:, 0], data[:, 1])

def SSR(Y, Yi):
	return sum(np.power(Yi - np.mean(Y),2))

def SSE(Y, Yi):
	return sum(np.power(Y - Yi,2))

def SST(Y, Yi):
	return SSE(Y, Yi) + SSR(Y, Yi)

def regresaoSimples(X, Y):
	n = len(X)
	b1 = (sum(np.multiply(X,Y))-n*np.mean(X)*np.mean(Y))/(sum(np.power(X,2))-n*np.power(np.mean(X),2))
	b0 = np.mean(Y) - b1*np.mean(X)
	print("Y = %.0lf  %.2lf * X" %(b0, b1))
	graficoDispersaoRegressao(X, Y, b0, b1)
	VTotal = 1 - SSE(Y, np.array(b0 +b1*X))/SST(Y, np.array(b0 +b1*X))
	print("R² = %.3f" %float(VTotal))
	print("R = %.3f" %float(-np.sqrt(VTotal)))

def main():
	X, Y = loadData("train.csv")
	graficoDispersao(X, Y)
	regresaoSimples(np.array(X),np.array(Y))
	

main()


