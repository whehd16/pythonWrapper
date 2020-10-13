import pandas as pd
import random
import numpy as np
from sklearn.feature_selection import f_regression, mutual_info_regression
import matplotlib.pyplot as plt
import scipy.stats

from sklearn.preprocessing import MinMaxScaler
A = [1, 2, 3, 4, 5]
temp = [A]
print(temp)
# print(np.transpose(A))
scaler = MinMaxScaler()

scaler.fit(A)
print(scaler.transform(A))
