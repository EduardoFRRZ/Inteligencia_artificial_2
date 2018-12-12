import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier

tabelaOR = pd.read_csv(r'or.csv')

df = pd.DataFrame(tabelaOR)
print(df)

X = df[['x1','x2']]
Y = df['y']

ppn = MLPClassifier(hidden_layer_sizes=(14, 12, 10), max_iter = 200)

ppn.fit(X, Y)

y_pred = ppn.predict(X)

print(y_pred)

print('Accuracy: %.2f' % accuracy_score(Y, y_pred))