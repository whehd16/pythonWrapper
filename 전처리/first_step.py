#본 단계는 kospi 예측을 위한 데이터 전처리 1단계로
# 날짜를 하루씩 당기는 역할입니다.

import pandas as pd

def deleteCSV(csv_path, save_path):
    csv = pd.read_csv(csv_path)
    delete_list = []
    delete_list.append(0)
    delete_list.append(1)
    print(csv.columns)
    print(csv['Date'][0])
    for col in csv.columns:
        if col != 'Date' and col != 'KOSPI_Now':
            temp = csv[col][0]
            for length in range(1, len(csv)):
                temp1 = csv[col][length]
                csv[col][length] = temp
                temp = temp1
    for length in range(len(csv)):
        if csv['Date'][length].split('.')[0] == '2019' or csv['Date'][length].split('-')[0] == '2019':
            delete_list.append(length)

    csv = csv.drop(delete_list, 0)
    csv.to_csv(save_path, index=False)

deleteCSV('./주식_변화량.csv', './전처리/주식_변화량_1차_전처리.csv')
deleteCSV('./주식_지수.csv','./전처리/주식_지수_1차_전처리.csv')
