import pandas as pd
from statsmodels.formula.api import ols
'''
Creating an expample of reusable code building of the fibonacci example

>>> import fish
>>> fish.weight(30)
'Your fish length: 30 cm, your fish weight: 363.4 g'
'''

def weight(L):
    # Importing dataset and creating dataframe
    df = pd.read_csv('data/Fish.csv')

    # Fitting model
    model = ols('Weight ~ Length3', data=df).fit()

    # Predicts on user input
    output = model.predict({'Length3':[float(L)]})

    return 'Your fish length: {} cm, your fish weight: {} g'.format(L, output[0].round(2))