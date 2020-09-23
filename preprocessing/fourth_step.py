import pandas as pd

#특징선택 이후 csv 편
def makeArrf(kospiCSV, f):
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

def deleteFeatures(csv_path, delete_list, f):
    csv = pd.read_csv(csv_path)
    csv = csv.drop([csv.columns[i-1] for i in delete_list], 1)
    makeArrf(csv, f)

# train csv 랑 test csv 모두 특징 지워서 arff 로 만들어보기!
#지수 unused
index_2007_2008 = [3,8,11,13,16,18,22,27,28,30,32,34,36,40,41,44,52,56,58,59,60,65,66,68,69,71,73,77,78,79,81,83,84,85,88,90,92,93,96,98,101,104,105,106,108,112,113,118,119,120,121,124,126,127,130,132,134,136,137,138,139,142,144,148,150,151,160,164,167,169,171,180,182,185,187,191,192,194,195,198,199,200,207,209,217,219,220,221,228,230,231,232,233,240,243,246,250,251,255,258,259,261,264,265,266] #106개 unused
index_2009_2010 = [6,8,11,14,18,20,21,23,24,26,27,31,33,37,43,45,50,54,58,61,68,72,81,83,84,85,88,90,96,101,105,106,107,111,112,115,118,119,121,123,125,126,133,136,137,138,139,142,143,146,147,151,152,154,155,156,158,160,164,165,169,170,171,172,174,176,183,184,185,186,187,190,191,194,195,200,204,208,212,216,217,218,220,221,223,224,226,230,231,232,235,241,242,243,246,247,249,252,253,254,259,261,262,263,265] #106개 unused
index_2011_2012 = []
index_2013_2014 = []
index_2015_2016 = []

index_2007_2009 = []
index_2009_2011 = []
index_2011_2013 = []
index_2013_2015 = []
index_2015_2017 = []

index_2010_2012 = []

index_2007_2010 = []
index_2010_2013 = []
index_2013_2016 = []

index_2011_2014 = []

index_2007_2011 = []
index_2011_2015 = []

####################
#변화량
delta_2007_2008 = []
delta_2009_2010 = []
delta_2011_2012 = []
delta_2013_2014 = []
delta_2015_2016 = []

delta_2007_2009 = []
delta_2009_2011 = []
delta_2011_2013 = []
delta_2013_2015 = []
delta_2015_2017 = []

delta_2010_2012 = []

delta_2007_2010 = []
delta_2010_2013 = []
delta_2013_2016 = []

delta_2011_2014 = []

delta_2007_2011 = []
delta_2011_2015 = []

arff_fs_22_2007_2010 = open("../data/arff_ver2/afterFS/4/22/fs_2007_2010.arff",'w')
origin_2007_2010 = pd.read_csv('../data/2007-2010.csv')
