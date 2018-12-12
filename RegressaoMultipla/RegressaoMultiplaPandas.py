from sklearn import linear_model
import matplotlib.pyplot as plt
import pandas as pd


Stock_Market = pd.read_csv(r'acoes.csv')

def graficos(df):
	plt.scatter(df['taxa_de_juros'], df['indicador_preco_acoes'], color='red')
	plt.title('Indicador de Preco Vs Taxa de Juros', fontsize=14)
	plt.xlabel('Taxa de Juros', fontsize=14)
	plt.ylabel('Indicador de Precos', fontsize=14)
	plt.grid(True)
	plt.show()

	plt.scatter(df['taxa_de_desemprego'], df['indicador_preco_acoes'], color='green')
	plt.title('Indicador de Preco Vs Taxa de Desemprego', fontsize=14)
	plt.xlabel('Taxa de Desemprego', fontsize=14)
	plt.ylabel('Indicador de Precos', fontsize=14)
	plt.grid(True)
	plt.show()

def main():
	df = pd.DataFrame(Stock_Market,columns=['Ano','Mes','taxa_de_juros','taxa_de_desemprego','indicador_preco_acoes'])

	graficos(df)

	X = df[['taxa_de_juros','taxa_de_desemprego']] # 2 veriaveis para regressao multipla
	Y = df['indicador_preco_acoes']

	# regressao com sklearn
	regr = linear_model.LinearRegression() #gera funcao de regressao
	regr.fit(X, Y) #gera reta de regressao

	print("indicador_preco_acoes = ( %f) + ( %f ) * X 1 + (%f) * X2" %(regr.intercept_,regr.coef_[0],regr.coef_[1]))

	# predicao com sklearn
	New_taxa_de_juros = 2
	New_taxa_de_desemprego = 5.9
	print ('Predicao do Indicador Preco Acoes: \n', regr.predict([[New_taxa_de_juros ,New_taxa_de_desemprego]]))

main()