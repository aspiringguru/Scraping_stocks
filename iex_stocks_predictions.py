'''
use the anaconda default python installed on my ubuntu machine.
https://scikit-learn.org/stable/install.html
https://pypi.org/project/iexfinance/

'''
import numpy as np
import os
import pandas as pd
from iexfinance.stocks import Stock
from datetime import datetime
import matplotlib.pyplot as plt
from iexfinance.stocks import get_historical_data
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from iexconfig import *

start = datetime(2017, 1, 1)
end = datetime(2020, 4, 26)
print("iexconfig=", iexconfig)
delta = get_historical_data('DAL', start, end, output_format='pandas', token=iexconfig)
delta.shape
type(delta)
df = delta.drop(['volume'], axis=1)
df.plot()
plt.savefig('delta.png')
