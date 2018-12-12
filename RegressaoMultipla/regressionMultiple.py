from numpy.linalg import inv
import numpy as np

def loadData(fileName):
    print(fileName)
    data = np.matrix(np.loadtxt(fileName, delimiter=',', skiprows = 1))
    return data

def regressionMultiple(data):
	numLines = data.shape[0]
	X = np.ones((numLines,1))
	Y = np.array(data[:,0])
	for pos in range(1,data.shape[1]):
			X =np.append(X,data[:,pos], axis=1)
	B = (inv(X.transpose()*X))*X.transpose()*Y;
	print("Equação: Y = %.3f + %.3f*X1 + %.3f*X2" %(B[0],B[1],B[2]))
def main():
	regressionMultiple(loadData(input("Informe o arquivo:\n")))

main()