import pandas as pd

def dot2slash(file_type, csv_paths):
    for csv_path in csv_paths:
        csv = pd.read_csv('./second(before_preprocessing)/'+ file_type + '/' + csv_path)
        for i in range(len(csv)):
            temp = csv['Date'][i].split('.')
            if len(temp) == 3:
                csv['Date'][i] = temp[0] + '-' + temp[1] + '-' + temp[2]

        csv.to_csv('./second(before_preprocessing)/' + file_type + '/' + csv_path, index=False)

def dot2slash_whole(file_type, csv_paths):
    for csv_path in csv_paths:
        csv = pd.read_csv('./second(before_preprocessing)/whole/' + file_type + '/' + csv_path)
        for i in range(len(csv)):
            temp = csv['Date'][i].split('.')
            if len(temp) == 3:
                csv['Date'][i] = temp[0] + '-' + temp[1] + '-' + temp[2]

        csv.to_csv('./second(before_preprocessing)/whole/'+file_type+'/'+csv_path, index = False)

# dot2slash('delta',
#     [
#         '4/22/2007_2008.csv', '4/22_test/2009_2010.csv',
#         '4/22/2009_2010.csv', '4/22_test/2011_2012.csv',
#         '4/22/2011_2012.csv', '4/22_test/2013_2014.csv',
#         '4/22/2013_2014.csv', '4/22_test/2015_2016.csv',
#         '4/22/2015_2016.csv', '4/22_test/2017_2018.csv',

#         '4/31/2007_2009.csv', '4/31_test/2010_2010.csv',
#         '4/31/2009_2011.csv', '4/31_test/2012_2012.csv',
#         '4/31/2011_2013.csv', '4/31_test/2014_2014.csv',
#         '4/31/2013_2015.csv', '4/31_test/2016_2016.csv',
#         '4/31/2015_2017.csv', '4/31_test/2018_2018.csv',

#         '6/33/2007_2009.csv', '6/33_test/2010_2012.csv',
#         '6/33/2010_2012.csv', '6/33_test/2013_2015.csv',
#         '6/33/2013_2015.csv', '6/33_test/2016_2018.csv',

#         '6/42/2007_2010.csv', '6/42_test/2011_2012.csv',
#         '6/42/2010_2013.csv', '6/42_test/2014_2015.csv',
#         '6/42/2013_2016.csv', '6/42_test/2017_2018.csv',

#         '8/44/2007_2010.csv', '8/44_test/2011_2014.csv',
#         '8/44/2011_2014.csv', '8/44_test/2015_2018.csv',

#         '8/53/2007_2011.csv', '8/53_test/2012_2014.csv',
#         '8/53/2011_2015.csv', '8/53_test/2016_2018.csv'
#     ]
# )

# dot2slash_whole('delta',
#     [
#         '2007_2010.csv', '2009_2012.csv', '2011_2014.csv', '2013_2016.csv', '2015_2018.csv',
#         '2007_2012.csv', '2010_2015.csv', '2013_2018.csv',
#         '2007_2014.csv', '2011_2018.csv'
#     ]
# )

dot2slash('rate',
    [
        '4/22/2007_2008.csv',
        '4/22/2009_2010.csv',
        '4/22/2011_2012.csv',
        '4/22/2013_2014.csv',
        '4/22/2015_2016.csv',

        '4/31/2007_2009.csv',
        '4/31/2009_2011.csv',
        '4/31/2011_2013.csv',
        '4/31/2013_2015.csv',
        '4/31/2015_2017.csv',

        '6/33/2007_2009.csv',
        '6/33/2010_2012.csv',
        '6/33/2013_2015.csv',

        '6/42/2007_2010.csv',
        '6/42/2010_2013.csv',
        '6/42/2013_2016.csv',

        '8/44/2007_2010.csv',
        '8/44/2011_2014.csv',

        '8/53/2007_2011.csv',
        '8/53/2011_2015.csv'
    ]
)

dot2slash_whole('rate',
    [
        '2007_2010.csv', '2009_2012.csv', '2011_2014.csv', '2013_2016.csv', '2015_2018.csv',
        '2007_2012.csv', '2010_2015.csv', '2013_2018.csv',
        '2007_2014.csv', '2011_2018.csv'
    ]
)
