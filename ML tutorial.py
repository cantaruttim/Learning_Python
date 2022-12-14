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
from matplotlib import style

style.use('fivethirtyeight')

xs = np.array([1,2,3,4,5,6], dtype=np.float64)
ys = np.array([5,4,6,5,6,7], dtype=np.float64)

# calculando m and b
# b = mean(y) - m*mean(x)

def best_fit_slope_and_intercept(xs, ys):
    m = mean( ((mean(xs) * mean(ys)) - mean(xs*ys)) / ((mean(xs)*mean(xs)) - mean(xs**2)) )

    b = mean(ys) - m * mean(xs)

    return m, b

m, b = best_fit_slope_and_intercept(xs,ys)
#print(m, b)

regression_line = [(m*x) + b for x in xs]

predict_x = 8
predict_y = (m*predict_m)+b

plt.scatter(xs, ys)
plt.scatter(predict_x, predict_y, color='g')
plt.plot(xs, regression_line)
plt.show()

### Determinando acurácia 
# R Squared Theory
# marca quão distante os dados estão da reta (quão bom a reta # está alocada entre os dados)

# r² = 1 - (SE\hat{y} / SE mean(y) )

def squared_error(ys_original, ys_line):
    return sum((ys_line - ys_original) ** 2) 
 
def coeficient_of_determination(ys_original,ys_line):
    y_mean_line = [ mean(ys_original) for y in ys_original ]
    squared_error_regression = squared_error(ys_original, ys_line)
    squared_error_y_mean = squared_error(ys_original, ys_mean_line)
    return 1 - (squared_error_regression / squared_error_y_mean)


























 




 
