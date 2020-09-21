# 두번재 단계로
# 특징 선택을 위한
# 4년                                                   (평가, 테스트)
# 2007-2008, 2009-2010, 2011-2012, 2013-2014, 2015-2016 (2년, 2년)
# 2007-2009, 2009-2011, 2011-2013, 2013-2015, 2015-2017 (3년, 1년)
# 6년
# 2007-2009, 2010-2012, 2013-2015 (3년, 3년)
# 2007-2010, 2010-2013, 2013-2016 (4년, 2년)
# 8년
# 2007-2010, 2011-2014 (4년, 4년)
# 2007-2011, 2011-2015 (5년, 3년)

#2차 전처리
##특징선택을 위한 폴더
###4
####22
####31
###6
####33
####42
###8
####44
####53
import pandas as pd
import copy
def cutByYear(csv_paths, cut_list):
    for csv_path in csv_paths:
        csv = pd.read_csv(csv_path)
        for folder, detail, start, end in cut_list:
            temp_csv = copy.deepcopy(csv)
            delete_list = []
            for i in range(len(temp_csv)):
                split_date = temp_csv['Date'][i].split('-')
                if len(split_date) > 1:
                    if split_date[0] != str(start) and split_date[0] != str(end):
                        delete_list.append(i)
                else:
                    split_date = temp_csv['Date'][i].split('.')
                    if split_date[0] != str(start) and split_date[0] != str(end):
                        delete_list.append(i)
            temp_csv = temp_csv.drop(delete_list, 0)
            temp_csv.to_csv('./2차전처리(특징선택)/'+str(folder)+'/'+str(detail)+'/'+str(start)+'_'+str(end)+'.csv', index = False)


cutByYear(['./주식_지수_1차_전처리.csv', './주식_변화량_1차_전처리.csv'],
[
    [4, 22, 2007, 2008],
    [4, 22, 2009, 2010],
    [4, 22, 2011, 2012],
    [4, 22, 2013, 2014],
    [4, 22, 2015, 2016],

    [4, 31, 2007, 2009],
    [4, 31, 2009, 2011],
    [4, 31, 2011, 2013],
    [4, 31, 2013, 2015],
    [4, 31, 2015, 2017],

    [6, 33, 2007, 2009],
    [6, 33, 2010, 2012],
    [6, 33, 2013, 2015],

    [6, 42, 2007, 2010],
    [6, 42, 2010, 2013],
    [6, 42, 2013, 2016],

    [8, 44, 2007, 2010],
    [8, 44, 2011, 2014],

    [8, 53, 2007, 2011],
    [8, 53, 2011, 2015]
])
