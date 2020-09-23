import pandas as pd

def makeArrf(kospiCSV, f):
    target = 'KOSPI'
    f.write('@relation ' + target + '\n')
    columns = kospiCSV.columns
    for column in columns:
        f.write('@attribute ' + column)
        if (column == 'Date'):
            f.write(' date yyyy-MM-dd\n')
        else:
            f.write(' numeric\n')

    f.write('\n@data\n')

    rows = 3193
    for row in range(rows):
        # print(row)
        try:
            for column in columns:
                f.write(str(kospiCSV.loc[row][column]))
                if (column != columns[len(columns) - 1]):
                    f.write(', ')
                else:
                    f.write('\n')

        except:
            f.close()

#csv to Aff for weka
#numbering 되어있는거 있으면 지워야함
# origin_2007_2010 = pd.read_csv('../data/2007-2010.csv')
# origin_2009_2012 = pd.read_csv('../data/2009-2012.csv')
# origin_2011_2014 = pd.read_csv('../data/2011-2014.csv')
# origin_2013_2016 = pd.read_csv('../data/2013-2016.csv')
# origin_2015_2018 = pd.read_csv('../data/2015-2018.csv')

# origin_2007_2012 = pd.read_csv('../data/2007-2012.csv')
# origin_2010_2015 = pd.read_csv('../data/2010-2015.csv')
# origin_2013_2018 = pd.read_csv('../data/2013-2018.csv')
#
# origin_2007_2014 = pd.read_csv('../data/2007-2014.csv')
# origin_2011_2018 = pd.read_csv('../data/2011-2018.csv')
######################################################################################
fs_22_2007_2010 = pd.read_csv('../data/afterFS_ver2/4/22/2007-2010.csv')
fs_22_2009_2012 = pd.read_csv('../data/afterFS_ver2/4/22/2009-2012.csv')
fs_22_2011_2014 = pd.read_csv('../data/afterFS_ver2/4/22/2011-2014.csv')
fs_22_2013_2016 = pd.read_csv('../data/afterFS_ver2/4/22/2013-2016.csv')
fs_22_2015_2018 = pd.read_csv('../data/afterFS_ver2/4/22/2015-2018.csv')

fs_31_2007_2010 = pd.read_csv('../data/afterFS_ver2/4/31/2007-2010.csv')
fs_31_2009_2012 = pd.read_csv('../data/afterFS_ver2/4/31/2009-2012.csv')
fs_31_2011_2014 = pd.read_csv('../data/afterFS_ver2/4/31/2011-2014.csv')
fs_31_2013_2016 = pd.read_csv('../data/afterFS_ver2/4/31/2013-2016.csv')
fs_31_2015_2018 = pd.read_csv('../data/afterFS_ver2/4/31/2015-2018.csv')

fs_33_2007_2012 = pd.read_csv('../data/afterFS_ver2/6/33/2007-2012.csv')
fs_33_2010_2015 = pd.read_csv('../data/afterFS_ver2/6/33/2010-2015.csv')
fs_33_2013_2018 = pd.read_csv('../data/afterFS_ver2/6/33/2013-2018.csv')

fs_42_2007_2012 = pd.read_csv('../data/afterFS_ver2/6/42/2007-2012.csv')
fs_42_2010_2015 = pd.read_csv('../data/afterFS_ver2/6/42/2010-2015.csv')
fs_42_2013_2018 = pd.read_csv('../data/afterFS_ver2/6/42/2013-2018.csv')

fs_44_2007_2014 = pd.read_csv('../data/afterFS_ver2/8/44/2007-2014.csv')
fs_44_2011_2018 = pd.read_csv('../data/afterFS_ver2/8/44/2011-2018.csv')

# fs_53_2007_2014 = pd.read_csv('../data/afterFS/8/53/2007-2014.csv')
# fs_53_2011_2018 = pd.read_csv('../data/afterFS/8/53/2011-2018.csv')
######################################################################################
# arff_origin_2007_2010 = open("../data/arff/original/original_2007_2010.arff",'w')
# arff_origin_2009_2012 = open("../data/arff/original/original_2009_2012.arff",'w')
# arff_origin_2011_2014 = open("../data/arff/original/original_2011_2014.arff",'w')
# arff_origin_2013_2016 = open("../data/arff/original/original_2013_2016.arff",'w')
# arff_origin_2015_2018 = open("../data/arff/original/original_2015_2018.arff",'
# w')
#
# arff_origin_2007_2012 = open("../data/arff/original/original_2007_2012.arff",'w')
# arff_origin_2010_2015 = open("../data/arff/original/original_2010_2015.arff",'w')
# arff_origin_2013_2018 = open("../data/arff/original/original_2013_2018.arff",'w')
#
# arff_origin_2007_2014 = open("../data/arff/original/original_2007_2014.arff",'w')
# arff_origin_2011_2018 = open("../data/arff/original/original_2011_2018.arff",'w')
######################################################################################
arff_fs_22_2007_2010 = open("../data/arff_ver2/afterFS/4/22/fs_2007_2010.arff",'w')
arff_fs_22_2009_2012 = open("../data/arff_ver2/afterFS/4/22/fs_2009_2012.arff",'w')
arff_fs_22_2011_2014 = open("../data/arff_ver2/afterFS/4/22/fs_2011_2014.arff",'w')
arff_fs_22_2013_2016 = open("../data/arff_ver2/afterFS/4/22/fs_2013_2016.arff",'w')
arff_fs_22_2015_2018 = open("../data/arff_ver2/afterFS/4/22/fs_2015_2018.arff",'w')

arff_fs_31_2007_2010 = open("../data/arff_ver2/afterFS/4/31/fs_2007_2010.arff",'w')
arff_fs_31_2009_2012 = open("../data/arff_ver2/afterFS/4/31/fs_2009_2012.arff",'w')
arff_fs_31_2011_2014 = open("../data/arff_ver2/afterFS/4/31/fs_2011_2014.arff",'w')
arff_fs_31_2013_2016 = open("../data/arff_ver2/afterFS/4/31/fs_2013_2016.arff",'w')
arff_fs_31_2015_2018 = open("../data/arff_ver2/afterFS/4/31/fs_2015_2018.arff",'w')

arff_fs_33_2007_2012 = open("../data/arff_ver2/afterFS/6/33/fs_2007_2012.arff",'w')
arff_fs_33_2010_2015 = open("../data/arff_ver2/afterFS/6/33/fs_2010_2015.arff",'w')
arff_fs_33_2013_2018 = open("../data/arff_ver2/afterFS/6/33/fs_2013_2018.arff",'w')

arff_fs_42_2007_2012 = open("../data/arff_ver2/afterFS/6/42/fs_2007_2012.arff",'w')
arff_fs_42_2010_2015 = open("../data/arff_ver2/afterFS/6/42/fs_2010_2015.arff",'w')
arff_fs_42_2013_2018 = open("../data/arff_ver2/afterFS/6/42/fs_2013_2018.arff",'w')

arff_fs_44_2007_2014 = open("../data/arff_ver2/afterFS/8/44/fs_2007_2014.arff",'w')
arff_fs_44_2011_2018 = open("../data/arff_ver2/afterFS/8/44/fs_2011_2018.arff",'w')

# arff_fs_53_2007_2014 = open("../data/arff/afterFS/8/53/fs_2007_2014.arff",'w')
# arff_fs_53_2011_2018 = open("../data/arff/afterFS/8/53/fs_2011_2018.arff",'w')
###################################################################################

# makeArrf(origin_2007_2010, arff_origin_2007_2010)
# makeArrf(origin_2009_2012, arff_origin_2009_2012)
# makeArrf(origin_2011_2014, arff_origin_2011_2014)
# makeArrf(origin_2013_2016, arff_origin_2013_2016)
# makeArrf(origin_2015_2018, arff_origin_2015_2018)

# makeArrf(origin_2007_2012, arff_origin_2007_2012)
# makeArrf(origin_2010_2015, arff_origin_2010_2015)
# makeArrf(origin_2013_2018, arff_origin_2013_2018)
#
# makeArrf(origin_2007_2014, arff_origin_2007_2014)
# makeArrf(origin_2011_2018, arff_origin_2011_2018)
##################################################################################
makeArrf(fs_22_2007_2010, arff_fs_22_2007_2010)
makeArrf(fs_22_2009_2012, arff_fs_22_2009_2012)
makeArrf(fs_22_2011_2014, arff_fs_22_2011_2014)
makeArrf(fs_22_2013_2016, arff_fs_22_2013_2016)
makeArrf(fs_22_2015_2018, arff_fs_22_2015_2018)

makeArrf(fs_31_2007_2010, arff_fs_31_2007_2010)
makeArrf(fs_31_2009_2012, arff_fs_31_2009_2012)
makeArrf(fs_31_2011_2014, arff_fs_31_2011_2014)
makeArrf(fs_31_2013_2016, arff_fs_31_2013_2016)
makeArrf(fs_31_2015_2018, arff_fs_31_2015_2018)

makeArrf(fs_33_2007_2012, arff_fs_33_2007_2012)
makeArrf(fs_33_2010_2015, arff_fs_33_2010_2015)
makeArrf(fs_33_2013_2018, arff_fs_33_2013_2018)

makeArrf(fs_42_2007_2012, arff_fs_42_2007_2012)
makeArrf(fs_42_2010_2015, arff_fs_42_2010_2015)
makeArrf(fs_42_2013_2018, arff_fs_42_2013_2018)

makeArrf(fs_44_2007_2014, arff_fs_44_2007_2014)
makeArrf(fs_44_2011_2018, arff_fs_44_2011_2018)

# makeArrf(fs_53_2007_2014, arff_fs_53_2007_2014)
# makeArrf(fs_53_2011_2018, arff_fs_53_2011_2018)
