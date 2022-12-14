https://www.youtube.com/playlist?list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v

-- REGRESSION
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

# uma forma de selecionar as colunas que vc quer para usar como as variáveis X (previsoras) e y (preditoras)
X = np.array(df.drop(['coluna que nao quero'], 1))
y = np.array(df['coluna y'])


X = preprocessing.scale(X)
X = X[:]

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

# Utilizando o modleo de regressão Linear
cfl = LinearRegression( n_jobs=30 )

clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)

print(accuracy)

