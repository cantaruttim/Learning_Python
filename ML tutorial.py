https://www.youtube.com/playlist?list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v

-- REGRESSION
#import numpy as np
#import pandas as pd
#import Quandl, math, datetime
#from sklearn import preprocessing, cross_validation, svm
#from sklearn.linear_model import LinearRegression
#import matplotlib.pyplot as plt
#from matplotlib import style
#import pickle 

#stryle.use('ggplot')

# uma forma de selecionar as colunas que vc quer para usar como as variáveis X (previsoras) e #y (preditoras)
#X = np.array(df.drop(['coluna que nao quero'], 1))
#y = np.array(df['coluna y'])


#X = preprocessing.scale(X)
#X = X[:]

#X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

# Utilizando o modleo de regressão Linear
#cfl = LinearRegression( n_jobs=30 )

#with open('linearregression.pickle','wb') as f:
#    pickle.dump(clf, f)

#pickle_in = open('linearregression.pickle', 'rb')
#clf = pickle.load()

#clf.fit(X_train, y_train)
#accuracy = clf.score(X_test, y_test)

#print(accuracy)

# Prediction

#previsao = cls.predict(X)

#print(previsao)

#df['Forecast'] = np.nan

#last_date = df.iloc[-1].name
#last_unix =  last_date.timestamp()
#one_day = 86400
#next_unix = last_unix + one_day

#for i in previsao:
#    next_date = datetime.datetime.fromtimestamp(next_unix)
#    next_unix += one_day
#    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

#df['Adj. Close'].plot()
#df['previsoes'].plot()
#plt.legend(loc=4)
#plt.xlabel('Date')
#plt.yabel('Price')
#plt.show()

### Understanding Linear Regression with Python

from statistics import mean
import numpy as np
import matplotlib.pyplot as plt

xs = np.array([1,2,3,4,5,6], dtype=np.float64)
ys = np.array([5,4,6,5,6,7], dtype=np.float64)

def best_fit_slope(xs, ys):
    m = mean( ((xs) * mean(ys) ) - mean(xs*ys)) / ( (mean(xs)*mean(xs)) - mean(xs**2)) ) 
    return m

m = best_fit_slope(xs,ys)
#print(m)

plt.scatter(xs, ys)
plt.show()

 




 
