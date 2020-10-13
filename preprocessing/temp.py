import pandas as pd
import random
import numpy as np
from sklearn.feature_selection import f_regression, mutual_info_regression
import matplotlib.pyplot as plt
import scipy.stats

np.random.seed(0)
# X = np.random.rand(5, 3)
# print(X)
# y = X[:, 0] + np.sin(6 * np.pi * X[:, 1]) + 0.1 * np.random.randn(5)
# print(y)
X = np.array([[-1, 22, 33], [-2, 3, 4], [-3, 4, 5], [-4, 5, 6], [-5, 6, 7]])
y= np.array([2,3,4,5,6])
f_test, p_value = f_regression(X, y)
# f_test /= np.max(f_test)
print(f_test)
print(p_value)
mi = mutual_info_regression(X, y)
# mi /= np.max(mi)
print(mi)
plt.figure(figsize=(15, 5))
for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.scatter(X[:, i], y, edgecolor='black', s=20)
    plt.xlabel("$x_{}$".format(i + 1), fontsize=14)
    if i == 0:
        plt.ylabel("$y$", fontsize=14)
    plt.title("F-test={:.2f}, MI={:.2f}".format(f_test[i], mi[i]),
              fontsize=16)
plt.show()
