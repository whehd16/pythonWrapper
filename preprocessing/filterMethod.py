import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import os
import datetime
# import xgboost as xgb
from sklearn import model_selection, preprocessing

def makeArff(kospiCSV, f):
    target = 'KOSPI'
    f.write('@relation ' + target + '\n')

    for column in kospiCSV.columns:
        f.write('@attribute ' + column)
        if (column == 'Date'):
            f.write(' date yyyy-MM-dd\n')
        else:
            f.write(' numeric\n')

    f.write('\n@data\n')

    rows = len(kospiCSV)
    for row in range(rows):
        # print(row)
        try:
            for column in kospiCSV.columns:
                f.write(str(kospiCSV.loc[row][column]))
                if (column != kospiCSV.columns[len(kospiCSV.columns) - 1]):
                    f.write(', ')
                else:
                    f.write('\n')

        except:
            f.close()

def filter(csvPath, resultPath, storePath):
    train_set = pd.read_csv(csvPath)
    result_csv = pd.read_csv(resultPath)
    for f in train_set.columns:
        if train_set[f].dtype=='object':
            lbl = preprocessing.LabelEncoder()
            lbl.fit(list(train_set[f].values))
            train_set[f] = lbl.transform(list(train_set[f].values))
    # print(train_set)
    dtype_df = train_set.dtypes.reset_index()
    # print(dtype_df)
    dtype_df.columns=["Count", "Column Type"]
    dtype_df.groupby("Column Type").aggregate('count').reset_index()
    # print(dtype_df)
    corrmat = train_set.drop(['Date'], axis=1).corr(method='pearson')
    # print(corrmat)
    corrmat = np.abs(corrmat)

    remain_num = 264
    corr_target = corrmat['KOSPI_Now'].reset_index()[:-2]
    # print(corr_target)
    corr_target.columns = ['feature', 'abs_corr']
    corr_target = corr_target.sort_values(by = 'abs_corr', ascending = True)[:remain_num].loc[corr_target['abs_corr'] < 0.4]
    # print(corr_target)
    remove_columns_list = []

    for a,b in corr_target.values:
        remove_columns_list.append(a)
    print(len(remove_columns_list))
    result_csv = result_csv.drop(remove_columns_list, axis=1)

    makeArff(result_csv, storePath)

#filter(필터 적용할 csv 파일, 해당 연도 풀 파일, arff 파일)
# open('./third(after_preprocessing)/whole_normal/index/2007_2010.arff', 'w')
# filter('./second(before_preprocessing)/index/4/22/2007_2008.csv', './second(before_preprocessing)/whole/index/2007_2010.csv', open('./third(after_preprocessing)/filter/index/4/22/2007_2008.arff','w'))
# filter('./second(before_preprocessing)/index/4/22/2009_2010.csv', './second(before_preprocessing)/whole/index/2009_2012.csv', open('./third(after_preprocessing)/filter/index/4/22/2009_2010.arff','w'))
# filter('./second(before_preprocessing)/index/4/22/2011_2012.csv', './second(before_preprocessing)/whole/index/2011_2014.csv', open('./third(after_preprocessing)/filter/index/4/22/2011_2012.arff','w'))
# filter('./second(before_preprocessing)/index/4/22/2013_2014.csv', './second(before_preprocessing)/whole/index/2013_2016.csv', open('./third(after_preprocessing)/filter/index/4/22/2013_2014.arff','w'))
# filter('./second(before_preprocessing)/index/4/22/2015_2016.csv', './second(before_preprocessing)/whole/index/2015_2018.csv', open('./third(after_preprocessing)/filter/index/4/22/2015_2016.arff','w'))

# filter('./second(before_preprocessing)/index/4/31/2007_2009.csv', './second(before_preprocessing)/whole/index/2007_2010.csv', open('./third(after_preprocessing)/filter/index/4/31/2007_2009.arff','w'))
# filter('./second(before_preprocessing)/index/4/31/2009_2011.csv', './second(before_preprocessing)/whole/index/2009_2012.csv', open('./third(after_preprocessing)/filter/index/4/31/2009_2011.arff','w'))
# filter('./second(before_preprocessing)/index/4/31/2011_2013.csv', './second(before_preprocessing)/whole/index/2011_2014.csv', open('./third(after_preprocessing)/filter/index/4/31/2011_2013.arff','w'))
# filter('./second(before_preprocessing)/index/4/31/2013_2015.csv', './second(before_preprocessing)/whole/index/2013_2016.csv', open('./third(after_preprocessing)/filter/index/4/31/2013_2015.arff','w'))
# filter('./second(before_preprocessing)/index/4/31/2015_2017.csv', './second(before_preprocessing)/whole/index/2015_2018.csv', open('./third(after_preprocessing)/filter/index/4/31/2015_2017.arff','w'))

# filter('./second(before_preprocessing)/index/6/33/2007_2009.csv', './second(before_preprocessing)/whole/index/2007_2012.csv', open('./third(after_preprocessing)/filter/index/6/33/2007_2009.arff','w'))
# filter('./second(before_preprocessing)/index/6/33/2010_2012.csv', './second(before_preprocessing)/whole/index/2010_2015.csv', open('./third(after_preprocessing)/filter/index/6/33/2010_2012.arff','w'))
# filter('./second(before_preprocessing)/index/6/33/2013_2015.csv', './second(before_preprocessing)/whole/index/2013_2018.csv', open('./third(after_preprocessing)/filter/index/6/33/2013_2015.arff','w'))

# filter('./second(before_preprocessing)/index/6/42/2007_2010.csv', './second(before_preprocessing)/whole/index/2007_2012.csv', open('./third(after_preprocessing)/filter/index/6/42/2007_2010.arff','w'))
# filter('./second(before_preprocessing)/index/6/42/2010_2013.csv', './second(before_preprocessing)/whole/index/2010_2015.csv', open('./third(after_preprocessing)/filter/index/6/42/2010_2013.arff','w'))
# filter('./second(before_preprocessing)/index/6/42/2013_2016.csv', './second(before_preprocessing)/whole/index/2013_2018.csv', open('./third(after_preprocessing)/filter/index/6/42/2013_2016.arff','w'))

# filter('./second(before_preprocessing)/index/8/44/2007_2010.csv', './second(before_preprocessing)/whole/index/2007_2014.csv', open('./third(after_preprocessing)/filter/index/8/44/2007_2010.arff','w'))
# filter('./second(before_preprocessing)/index/8/44/2011_2014.csv', './second(before_preprocessing)/whole/index/2011_2018.csv', open('./third(after_preprocessing)/filter/index/8/44/2011_2014.arff','w'))

# filter('./second(before_preprocessing)/index/8/53/2007_2011.csv', './second(before_preprocessing)/whole/index/2007_2014.csv', open('./third(after_preprocessing)/filter/index/8/53/2007_2011.arff','w'))
# filter('./second(before_preprocessing)/index/8/53/2011_2015.csv', './second(before_preprocessing)/whole/index/2011_2018.csv', open('./third(after_preprocessing)/filter/index/8/53/2011_2015.arff','w'))

#########################################################################################################################

# filter('./second(before_preprocessing)/delta/4/22/2007_2008.csv', './second(before_preprocessing)/whole/delta/2007_2010.csv', open('./third(after_preprocessing)/filter/delta/4/22/2007_2008.arff','w'))
# filter('./second(before_preprocessing)/delta/4/22/2009_2010.csv', './second(before_preprocessing)/whole/delta/2009_2012.csv', open('./third(after_preprocessing)/filter/delta/4/22/2009_2010.arff','w'))
# filter('./second(before_preprocessing)/delta/4/22/2011_2012.csv', './second(before_preprocessing)/whole/delta/2011_2014.csv', open('./third(after_preprocessing)/filter/delta/4/22/2011_2012.arff','w'))
# filter('./second(before_preprocessing)/delta/4/22/2013_2014.csv', './second(before_preprocessing)/whole/delta/2013_2016.csv', open('./third(after_preprocessing)/filter/delta/4/22/2013_2014.arff','w'))
# filter('./second(before_preprocessing)/delta/4/22/2015_2016.csv', './second(before_preprocessing)/whole/delta/2015_2018.csv', open('./third(after_preprocessing)/filter/delta/4/22/2015_2016.arff','w'))

# filter('./second(before_preprocessing)/delta/4/31/2007_2009.csv', './second(before_preprocessing)/whole/delta/2007_2010.csv', open('./third(after_preprocessing)/filter/delta/4/31/2007_2009.arff','w'))
# filter('./second(before_preprocessing)/delta/4/31/2009_2011.csv', './second(before_preprocessing)/whole/delta/2009_2012.csv', open('./third(after_preprocessing)/filter/delta/4/31/2009_2011.arff','w'))
# filter('./second(before_preprocessing)/delta/4/31/2011_2013.csv', './second(before_preprocessing)/whole/delta/2011_2014.csv', open('./third(after_preprocessing)/filter/delta/4/31/2011_2013.arff','w'))
# filter('./second(before_preprocessing)/delta/4/31/2013_2015.csv', './second(before_preprocessing)/whole/delta/2013_2016.csv', open('./third(after_preprocessing)/filter/delta/4/31/2013_2015.arff','w'))
# filter('./second(before_preprocessing)/delta/4/31/2015_2017.csv', './second(before_preprocessing)/whole/delta/2015_2018.csv', open('./third(after_preprocessing)/filter/delta/4/31/2015_2017.arff','w'))

# filter('./second(before_preprocessing)/delta/6/33/2007_2009.csv', './second(before_preprocessing)/whole/delta/2007_2012.csv', open('./third(after_preprocessing)/filter/delta/6/33/2007_2009.arff','w'))
# filter('./second(before_preprocessing)/delta/6/33/2010_2012.csv', './second(before_preprocessing)/whole/delta/2010_2015.csv', open('./third(after_preprocessing)/filter/delta/6/33/2010_2012.arff','w'))
# filter('./second(before_preprocessing)/delta/6/33/2013_2015.csv', './second(before_preprocessing)/whole/delta/2013_2018.csv', open('./third(after_preprocessing)/filter/delta/6/33/2013_2015.arff','w'))

# filter('./second(before_preprocessing)/delta/6/42/2007_2010.csv', './second(before_preprocessing)/whole/delta/2007_2012.csv', open('./third(after_preprocessing)/filter/delta/6/42/2007_2010.arff','w'))
# filter('./second(before_preprocessing)/delta/6/42/2010_2013.csv', './second(before_preprocessing)/whole/delta/2010_2015.csv', open('./third(after_preprocessing)/filter/delta/6/42/2010_2013.arff','w'))
# filter('./second(before_preprocessing)/delta/6/42/2013_2016.csv', './second(before_preprocessing)/whole/delta/2013_2018.csv', open('./third(after_preprocessing)/filter/delta/6/42/2013_2016.arff','w'))

# filter('./second(before_preprocessing)/delta/8/44/2007_2010.csv', './second(before_preprocessing)/whole/delta/2007_2014.csv', open('./third(after_preprocessing)/filter/delta/8/44/2007_2010.arff','w'))
# filter('./second(before_preprocessing)/delta/8/44/2011_2014.csv', './second(before_preprocessing)/whole/delta/2011_2018.csv', open('./third(after_preprocessing)/filter/delta/8/44/2011_2014.arff','w'))

# filter('./second(before_preprocessing)/delta/8/53/2007_2011.csv', './second(before_preprocessing)/whole/delta/2007_2014.csv', open('./third(after_preprocessing)/filter/delta/8/53/2007_2011.arff','w'))
# filter('./second(before_preprocessing)/delta/8/53/2011_2015.csv', './second(before_preprocessing)/whole/delta/2011_2018.csv', open('./third(after_preprocessing)/filter/delta/8/53/2011_2015.arff','w'))


##########################################################################################


filter('./second(before_preprocessing)/rate/4/22/2007_2008.csv', './second(before_preprocessing)/whole/rate/2007_2010.csv', open('./third(after_preprocessing)/filter/rate/4/22/2007_2008.arff','w'))
filter('./second(before_preprocessing)/rate/4/22/2009_2010.csv', './second(before_preprocessing)/whole/rate/2009_2012.csv', open('./third(after_preprocessing)/filter/rate/4/22/2009_2010.arff','w'))
filter('./second(before_preprocessing)/rate/4/22/2011_2012.csv', './second(before_preprocessing)/whole/rate/2011_2014.csv', open('./third(after_preprocessing)/filter/rate/4/22/2011_2012.arff','w'))
filter('./second(before_preprocessing)/rate/4/22/2013_2014.csv', './second(before_preprocessing)/whole/rate/2013_2016.csv', open('./third(after_preprocessing)/filter/rate/4/22/2013_2014.arff','w'))
filter('./second(before_preprocessing)/rate/4/22/2015_2016.csv', './second(before_preprocessing)/whole/rate/2015_2018.csv', open('./third(after_preprocessing)/filter/rate/4/22/2015_2016.arff','w'))

filter('./second(before_preprocessing)/rate/4/31/2007_2009.csv', './second(before_preprocessing)/whole/rate/2007_2010.csv', open('./third(after_preprocessing)/filter/rate/4/31/2007_2009.arff','w'))
filter('./second(before_preprocessing)/rate/4/31/2009_2011.csv', './second(before_preprocessing)/whole/rate/2009_2012.csv', open('./third(after_preprocessing)/filter/rate/4/31/2009_2011.arff','w'))
filter('./second(before_preprocessing)/rate/4/31/2011_2013.csv', './second(before_preprocessing)/whole/rate/2011_2014.csv', open('./third(after_preprocessing)/filter/rate/4/31/2011_2013.arff','w'))
filter('./second(before_preprocessing)/rate/4/31/2013_2015.csv', './second(before_preprocessing)/whole/rate/2013_2016.csv', open('./third(after_preprocessing)/filter/rate/4/31/2013_2015.arff','w'))
filter('./second(before_preprocessing)/rate/4/31/2015_2017.csv', './second(before_preprocessing)/whole/rate/2015_2018.csv', open('./third(after_preprocessing)/filter/rate/4/31/2015_2017.arff','w'))

filter('./second(before_preprocessing)/rate/6/33/2007_2009.csv', './second(before_preprocessing)/whole/rate/2007_2012.csv', open('./third(after_preprocessing)/filter/rate/6/33/2007_2009.arff','w'))
filter('./second(before_preprocessing)/rate/6/33/2010_2012.csv', './second(before_preprocessing)/whole/rate/2010_2015.csv', open('./third(after_preprocessing)/filter/rate/6/33/2010_2012.arff','w'))
filter('./second(before_preprocessing)/rate/6/33/2013_2015.csv', './second(before_preprocessing)/whole/rate/2013_2018.csv', open('./third(after_preprocessing)/filter/rate/6/33/2013_2015.arff','w'))

filter('./second(before_preprocessing)/rate/6/42/2007_2010.csv', './second(before_preprocessing)/whole/rate/2007_2012.csv', open('./third(after_preprocessing)/filter/rate/6/42/2007_2010.arff','w'))
filter('./second(before_preprocessing)/rate/6/42/2010_2013.csv', './second(before_preprocessing)/whole/rate/2010_2015.csv', open('./third(after_preprocessing)/filter/rate/6/42/2010_2013.arff','w'))
filter('./second(before_preprocessing)/rate/6/42/2013_2016.csv', './second(before_preprocessing)/whole/rate/2013_2018.csv', open('./third(after_preprocessing)/filter/rate/6/42/2013_2016.arff','w'))

filter('./second(before_preprocessing)/rate/8/44/2007_2010.csv', './second(before_preprocessing)/whole/rate/2007_2014.csv', open('./third(after_preprocessing)/filter/rate/8/44/2007_2010.arff','w'))
filter('./second(before_preprocessing)/rate/8/44/2011_2014.csv', './second(before_preprocessing)/whole/rate/2011_2018.csv', open('./third(after_preprocessing)/filter/rate/8/44/2011_2014.arff','w'))

filter('./second(before_preprocessing)/rate/8/53/2007_2011.csv', './second(before_preprocessing)/whole/rate/2007_2014.csv', open('./third(after_preprocessing)/filter/rate/8/53/2007_2011.arff','w'))
filter('./second(before_preprocessing)/rate/8/53/2011_2015.csv', './second(before_preprocessing)/whole/rate/2011_2018.csv', open('./third(after_preprocessing)/filter/rate/8/53/2011_2015.arff','w'))
