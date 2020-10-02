from matplotlib import pyplot as plt
import pandas as pd
import datetime

plt.rc('font', family='NanumGothicOTF')
plt.rcParams['axes.unicode_minus'] = False


# csv = pd.read_csv('../data/mergedData/코스피_변화율_interpolated_1.csv')
csv = pd.read_csv('./주식_rate_1차_전처리.csv')

dt_index = pd.date_range(start='20070111', end='20181228')

dt_list = dt_index.strftime('%Y-%m-%d').tolist()

del_list = []
csv_dates = []
# print(len('hello'.split('.')))

for i in csv['Date']:
    if len(i.split('.')) == 1:
        csv_dates.append(str(i))
    else:
        year = str(i.split('.')[0])
        month = str(i.split('.')[1])
        day = str(i.split('.')[2])
        if len(month) == 1:
            month = '0'+month
        if len(day) == 1:
            day = '0'+day
        csv_dates.append(
            year + '-' +
            month + '-' +
            day
            )


for d in dt_list:
    # dString = str(d.split('-')[0]) + str(d.split('-')[1]) + str(d.split('-')[2])
    # print(d)
    if str(d) not in csv_dates:
        del_list.append(d)

for dValue in del_list:
    try:
        dt_list.remove(dValue)
    except:
        continue

# print(len(dt_list))
plt.plot(dt_list,[csv['KOSPI_Now'][i] for i in range(len(dt_list))])
ax = plt.subplot()
ax.set_xticks([0,2961])
plt.xlabel('Date')
plt.ylabel('KOSPI_rate')

plt.show()
