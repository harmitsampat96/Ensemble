import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from nsepy import get_history
from datetime import date
import datetime


def technicalanalysis(stock):
    # nse_symbol = input('Enter the symbol')
    today = datetime.datetime.now().strftime("%Y%m%d")

    # year = today[0:4]
    # month = today[5:6]
    # day = today[6:8]

    # print(year, month, day)
    # abc = get_history(symbol='BANKBARODA', start=date(2000, 2, 1), end=date(int(year), int(month), int(day)))

    # abc.to_csv('Test3.csv')

    stock_data = pd.read_csv(stock + '_data.csv')

    # bob['Date'] = pd.to_datetime(bob.Date, format='%d-%m-%Y')
    stock_data.index = stock_data['Date']

    y = stock_data['Close']
    X_train = stock_data[:3000]
    X_test = stock_data[3000:]
    y_train = y[:3000]
    y_test = y[3000:]

    # if stock == 'Colgate':
    #     X_train = stock_data[:2000]
    #     X_test = stock_data[2000:]
    # else:


    # if stock == 'Colgate':
    #     y_train = y[:2000]
    #     y_test = y[2000:]
    # else:

    #X_train, X_test, y_train, y_test = train_test_split(bob, y, test_size=0.1)

    Date_test = X_test['Date']
    Date_train = X_train['Date']
    X_train = X_train.drop(['Close', 'Trades', 'Deliverable Volume', '%Deliverble', 'Symbol', 'Series', 'Date', 'Volume', 'Turnover'], axis=1)
    X_test = X_test.drop(['Close', 'Trades', 'Deliverable Volume', '%Deliverble', 'Symbol', 'Series', 'Date', 'Volume', 'Turnover'], axis=1)

    X_train = X_train / X_train.max()
    X_test = X_test / X_test.max()

    classifier3 = SVR(kernel='poly', C=1e3, gamma=0.1, degree=1)
    classifier3.fit(X_train, y_train)
    y_predict_SVR = classifier3.predict(X_test)
    y_predict_SVR = list(y_predict_SVR)
    y_test = list(y_test)
    # print('SVR:', r2_score(y_test, y_predict_SVR))

    mlp = MLPRegressor(hidden_layer_sizes=(30, 30, 30), max_iter=1000)
    mlp.fit(X_train, y_train)
    y_predict_MLP = mlp.predict(X_test)
    y_predict_MLP = list(y_predict_MLP)
    #print('MLP:', r2_score(y_test, y_predict_MLP))

    # for i in range(len(y_test)):
    #     print(y_test[i], ':', y_predict_MLP[i])

    return y_test, y_predict_SVR, y_predict_MLP, Date_test[3000:]

