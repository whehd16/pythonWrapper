import pandas as pd

csv = pd.read_csv('./주식_변화량.csv')

print(len(csv.columns))
csv = csv.drop([csv.columns[178], csv.columns[179], csv.columns[180], csv.columns[181]], 1)
print(csv.columns[178])
