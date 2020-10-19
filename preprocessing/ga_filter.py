from random import choice, getrandbits
import pandas as pd
import numpy as np
import scipy.stats
import random
import copy
import math
from itertools import combinations
from sklearn.feature_selection import f_regression, mutual_info_regression
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import sys
import pickle

scaler = MinMaxScaler()
NUMBER_OF_FEATURES = 264
POPULATION_SIZE = 50
KOSPI_NOW_INDEX = 1
GENERATIONS = 10
MAXSIZE = sys.maxsize - 1
chromosomes = []
result_fitness = []



###################################################
##메모이제이션


def initialization(chromosomes):
    # features_indexs = []
    for _ in range(POPULATION_SIZE):
        # features_index = []
        features = []
        for i in range(NUMBER_OF_FEATURES):
            if random.randint(0, 1) % 2 == 0:
                features.append(0)
            else:
                features.append(1)
                # features_index.append(i+2)
        chromosome = copy.deepcopy(features)
        chromosomes.append(chromosome)
        # features_indexs.append(features_index)

    # return features_indexs

def feature_find(chromosomes):
    features_indexs = []
    for chromosome in chromosomes:
        features_index = []
        for i in range(NUMBER_OF_FEATURES):
            if chromosome[i] == 1:
                features_index.append(i+2)
        features_indexs.append(features_index)
    return features_indexs

def fitness_function(chromosomes, features_indexs, csv_file):
    fitness_values = [0.0] * POPULATION_SIZE
    # print(len(features_indexs))
    for i in range(len(features_indexs)):  #feature 는 1로 인코딩 된 특징 col 번호 리스트임.
        # print("\t"+str(i)+"번째")
        #낮아야함 반환되는 값에 마이너스 붙을 것.
        lambda1 = []
        lambda3 = []
        lambda5 = []
        combi = combinations(features_indexs[i], 2)
        # for x, y in combi:
        #     lambda1.append(pearson(x, y, csv_file))
        #     lambda3.append(mutual_information(x, y, csv_file))
        #     lambda5.append(f_test(x, y, csv))

        for x, y in combi:
            if otherFeatures_CFS[x][y] == MAXSIZE:
                otherFeatures_CFS[x][y] = pearson(x, y, csv_file)
            lambda1.append(otherFeatures_CFS[x][y])

            if otherFeatures_IG[x][y] == MAXSIZE:
                otherFeatures_IG[x][y] = mutual_information(x, y, csv_file)
            lambda3.append(otherFeatures_IG[x][y])

            if otherFeatures_F[x][y] == MAXSIZE:
                otherFeatures_F[x][y] = f_test(x, y, csv)
            lambda5.append(otherFeatures_F[x][y])

        #낮아야함 반환되는 값에 플러스 붙을 것
        lambda2 = []
        lambda4 = []
        lambda6 = []
        # for y in features_indexs[i]:
        #     lambda2.append(pearson(KOSPI_NOW_INDEX, y, csv_file))
        #     lambda4.append(mutual_information(KOSPI_NOW_INDEX, y, csv_file))
        #     lambda6.append(f_test(KOSPI_NOW_INDEX, y, csv))

        for y in features_indexs[i]:
            if kospi_CFS[y] == MAXSIZE:
                kospi_CFS[y] = pearson(KOSPI_NOW_INDEX, y, csv_file)
            lambda2.append(kospi_CFS[y])

            if kospi_IG[y] == MAXSIZE:
                kospi_IG[y] = mutual_information(KOSPI_NOW_INDEX, y, csv_file)
            lambda4.append(kospi_IG[y])

            if kospi_F[y] == MAXSIZE:
                kospi_F[y] = f_test(KOSPI_NOW_INDEX, y, csv)
            lambda6.append(kospi_F[y])

        lambda1 = [lambda1]
        scaler.fit(np.transpose(lambda1))
        lambda1 = scaler.transform(np.transpose(lambda1))

        lambda2 = [lambda2]
        scaler.fit(np.transpose(lambda2))
        lambda2 = scaler.transform(np.transpose(lambda2))

        # lambda3 = [np.array(lambda3)]
        scaler.fit(np.array(lambda3))
        lambda3 = scaler.transform(np.array((lambda3)))

        # lambda4 = [lambda4]
        scaler.fit(np.array(lambda4))
        lambda4 = scaler.transform(np.array(lambda4))

        # lambda5 = [lambda5]
        # print(lambda5)
        # print(lambda5)
        scaler.fit(np.array(lambda5))
        lambda5 = scaler.transform(np.array(lambda5))

        # lambda6 = [lambda6]
        scaler.fit(np.array(lambda6))
        lambda6 = scaler.transform(np.array(lambda6))

        # print("lambda1")
        # print(lambda1)
        # print("lambda2")
        # print(lambda2)
        # print("lambda3")
        # print(lambda3)
        # print("lambda4")
        # print(lambda4)
        # print("lambda5")
        # print(lambda5)
        # print("lambda6")
        # print(lambda6)

        fitness_values[i] = -sum(lambda1)/len(lambda1) + sum(lambda2)/len(lambda1) - sum(lambda3)/len(lambda1) + sum(lambda4)/len(lambda1) - sum(lambda5)/len(lambda1) + sum(lambda6)/len(lambda1)

        #  - (sum(lambda5) / max(lambda5)) + (sum(lambda6)/max(lambda6))
        # print(lambda1)
        # print("\t\t- sum(lambda1) / max(lambda1) : ", (sum(lambda1) / len(lambda1)))
        # print("\t\t  sum(lambda2) / max(lambda2) : ", (sum(lambda2) / len(lambda2)))
        # print("\t\t- sum(lambda3) / max(lambda3) : ", (sum(lambda3) / len(lambda3)))
        # print("\t\t  sum(lambda4) / max(lambda4) : ", (sum(lambda4) / len(lambda4)))
        # print(fitness_values[i])

        # print("\t\t"+str(fitness_values[i]))

    return fitness_values

def convert_index_to_array(target_index, csv):
    arr = csv[csv.columns[target_index]]
    return arr

def convert_index_to_numpy(target_index, csv):
    temp = []
    arr = csv[csv.columns[target_index]]
    temp.append(arr)
    return np.transpose(temp)

def pearson(x, y, csv):
    #kospi_Now 와 특징간의 상관계수 반환
    #특징 끼리의 상관계수 반환
    x = convert_index_to_array(x, csv)
    y = convert_index_to_array(y, csv)
    return abs(float(scipy.stats.pearsonr(x, y)[0]))

## X : [[1],[2],[3]]
## Y : [1,2,3]
def mutual_information(x, y, csv):
    x = convert_index_to_numpy(x, csv)
    y = convert_index_to_array(y, csv)
    mi = mutual_info_regression(x, y)
    return mi

def f_test(x, y, csv):
    # x = np.round(convert_index_to_numpy(x, csv)[1:],15) #특징 배열
    # y = convert_index_to_array(y, csv)[1:] #타겟
    x = np.round(convert_index_to_numpy(x, csv),15) #특징 배열
    y = convert_index_to_array(y, csv) #타겟
    f_test, p_value = f_regression(x, y)
    # print(f_test)
    return f_test

def make_roulette_wheels(fitness_values):
    roulette = []
    temp_fitness_values = np.transpose(np.array(fitness_values))
    scaler.fit(np.transpose(temp_fitness_values))
    temp_fitness_values = scaler.transform(np.transpose(temp_fitness_values))
    for i in range(len(fitness_values)):
        for _ in range(int(temp_fitness_values[i] * 1000)):
            roulette.append(i)
    return roulette

def selection(roulette):
    return random.sample(roulette, 1)[0]

def remove_values_from_list(the_list, val):
    return [value for value in the_list if value!=val]

def crossover(index1, index2, chromosomes, new_chromosomes):
    one_point, two_point = sorted(random.sample([i for i in range(2, NUMBER_OF_FEATURES-2)],2))
    ch1_front = chromosomes[index1][0:one_point]
    ch2_mid = chromosomes[index2][one_point:two_point]
    ch1_end = chromosomes[index1][two_point:NUMBER_OF_FEATURES+1]
    new_chromosomes.append(ch1_front+ch2_mid+ch1_end)

def best_fitness(values):
    return values.index(max(values))

def mutation(new_chromosomes):
    for chromosome in new_chromosomes:
        for i in range(len(chromosome)):
            if random.randint(1,10000) % 666 == 0:
                chromosome[i] += 1
                chromosome[i] %= 2

csv1 = pd.read_csv('./second(before_preprocessing)/delta/4/22/2007_2008.csv')
csv2 = pd.read_csv('./second(before_preprocessing)/delta/4/22/2009_2010.csv')
csv3 = pd.read_csv('./second(before_preprocessing)/delta/4/22/2011_2012.csv')
csv4 = pd.read_csv('./second(before_preprocessing)/delta/4/22/2013_2014.csv')
csv5 = pd.read_csv('./second(before_preprocessing)/delta/4/22/2015_2016.csv')

csv6 = pd.read_csv('./second(before_preprocessing)/delta/4/31/2007_2009.csv')
csv7 = pd.read_csv('./second(before_preprocessing)/delta/4/31/2009_2011.csv')
csv8 = pd.read_csv('./second(before_preprocessing)/delta/4/31/2011_2013.csv')
csv9 = pd.read_csv('./second(before_preprocessing)/delta/4/31/2013_2015.csv')
csv10 = pd.read_csv('./second(before_preprocessing)/delta/4/31/2015_2017.csv')

csv11 = pd.read_csv('./second(before_preprocessing)/delta/6/33/2010_2012.csv')

csv12 = pd.read_csv('./second(before_preprocessing)/delta/6/42/2007_2010.csv')
csv13 = pd.read_csv('./second(before_preprocessing)/delta/6/42/2010_2013.csv')
csv14 = pd.read_csv('./second(before_preprocessing)/delta/6/42/2013_2016.csv')

csv15 = pd.read_csv('./second(before_preprocessing)/delta/8/44/2011_2014.csv')

csv16 = pd.read_csv('./second(before_preprocessing)/delta/8/53/2007_2011.csv')
csv17 = pd.read_csv('./second(before_preprocessing)/delta/8/53/2011_2015.csv')
##########################################################################################
csv18 = pd.read_csv('./second(before_preprocessing)/rate/4/22/2007_2008.csv')
csv19 = pd.read_csv('./second(before_preprocessing)/rate/4/22/2009_2010.csv')
csv20 = pd.read_csv('./second(before_preprocessing)/rate/4/22/2011_2012.csv')
csv21 = pd.read_csv('./second(before_preprocessing)/rate/4/22/2013_2014.csv')
csv22 = pd.read_csv('./second(before_preprocessing)/rate/4/22/2015_2016.csv')

csv23 = pd.read_csv('./second(before_preprocessing)/rate/4/31/2007_2009.csv')
csv24 = pd.read_csv('./second(before_preprocessing)/rate/4/31/2009_2011.csv')
csv25 = pd.read_csv('./second(before_preprocessing)/rate/4/31/2011_2013.csv')
csv26 = pd.read_csv('./second(before_preprocessing)/rate/4/31/2013_2015.csv')
csv27 = pd.read_csv('./second(before_preprocessing)/rate/4/31/2015_2017.csv')

csv28 = pd.read_csv('./second(before_preprocessing)/rate/6/33/2010_2012.csv')

csv29 = pd.read_csv('./second(before_preprocessing)/rate/6/42/2007_2010.csv')
csv30 = pd.read_csv('./second(before_preprocessing)/rate/6/42/2010_2013.csv')
csv31 = pd.read_csv('./second(before_preprocessing)/rate/6/42/2013_2016.csv')

csv32 = pd.read_csv('./second(before_preprocessing)/rate/8/44/2011_2014.csv')

csv33 = pd.read_csv('./second(before_preprocessing)/rate/8/53/2007_2011.csv')
csv34 = pd.read_csv('./second(before_preprocessing)/rate/8/53/2011_2015.csv')
##########################################################################################
csv35= pd.read_csv('./second(before_preprocessing)/index/4/22/2007_2008.csv')
csv36 = pd.read_csv('./second(before_preprocessing)/index/4/22/2009_2010.csv')
csv37= pd.read_csv('./second(before_preprocessing)/index/4/22/2011_2012.csv')
csv38= pd.read_csv('./second(before_preprocessing)/index/4/22/2013_2014.csv')
csv39 = pd.read_csv('./second(before_preprocessing)/index/4/22/2015_2016.csv')

csv40 = pd.read_csv('./second(before_preprocessing)/index/4/31/2007_2009.csv')
csv41 = pd.read_csv('./second(before_preprocessing)/index/4/31/2009_2011.csv')
csv42= pd.read_csv('./second(before_preprocessing)/index/4/31/2011_2013.csv')
csv43= pd.read_csv('./second(before_preprocessing)/index/4/31/2013_2015.csv')
csv44 = pd.read_csv('./second(before_preprocessing)/index/4/31/2015_2017.csv')

csv45 = pd.read_csv('./second(before_preprocessing)/index/6/33/2010_2012.csv')

csv46 = pd.read_csv('./second(before_preprocessing)/index/6/42/2007_2010.csv')
csv47 = pd.read_csv('./second(before_preprocessing)/index/6/42/2010_2013.csv')
csv48 = pd.read_csv('./second(before_preprocessing)/index/6/42/2013_2016.csv')

csv49 = pd.read_csv('./second(before_preprocessing)/index/8/44/2011_2014.csv')

csv50 = pd.read_csv('./second(before_preprocessing)/index/8/53/2007_2011.csv')
csv51 = pd.read_csv('./second(before_preprocessing)/index/8/53/2011_2015.csv')
csv_files = [
    # csv1,
    csv2, csv3,
    # csv4,csv5,csv6,csv7,csv8,csv9,csv10,csv11,csv12,csv13,csv14,csv15,csv16,csv17,
    # csv18,csv19,csv20,csv21,csv22,csv23,csv24,csv25,csv26,csv27,csv28,csv29,csv30,csv31,csv32,csv33,csv34,
    # csv35,csv36,csv37,csv38,csv39,csv40,csv41,csv42,csv43,csv44,csv45,csv46,csv47,csv48,csv49,csv50,csv51
            ]

i = 2
global kospi_CFS
global otherFeatures_CFS

global kospi_IG
global otherFeatures_IG

global kospi_F
global otherFeatures_F

for csv in csv_files:

    kospi_CFS = [MAXSIZE] * 266
    otherFeatures_CFS = [[MAXSIZE] * 266]*266

    kospi_IG = [MAXSIZE] * 266
    otherFeatures_IG = [[MAXSIZE] * 266]*266

    kospi_F = [MAXSIZE] * 266
    otherFeatures_F = [[MAXSIZE] * 266]*266

    print("========================================================================")

    chromosomes = []
    roulette_wheels = []
    initialization(chromosomes)
    best_fit_and_chromosome = []

    generations = []
    fitness_per_generations = []
    for generation in range(500):
        new_chromosomes = []
        print(str(generation) + "세대")
        features_indexs = feature_find(chromosomes)
        fitness_values = fitness_function(chromosomes, features_indexs, csv)
        best_fit_and_chromosome.append(
            [
                max(fitness_values),
                chromosomes[fitness_values.index(max(fitness_values))]
            ]
        )
#         print(best_fit_and_chromosome)
        roulette_wheels = make_roulette_wheels(fitness_values)
        for _ in range(POPULATION_SIZE):
            selected_index1 = selection(roulette_wheels)
            removed_roulette_wheels = remove_values_from_list(roulette_wheels, selected_index1)
            selected_index2 = selection(removed_roulette_wheels)
            crossover(selected_index1, selected_index2, chromosomes, new_chromosomes)
            mutation(new_chromosomes)
        chromosomes = copy.deepcopy(new_chromosomes)

        generations.append(generation)
        fitness_per_generations.append(best_fit_and_chromosome[generation])
        print(best_fit_and_chromosome[generation])

    # with open('./fitness_list/data_generations_'+str(i)+'.pickle', 'wb') as f:
    #     pickle.dump(generations, f, pickle.HIGHEST_PROTOCOL)
    with open('./fit_result/data_fitness_'+str(i)+'.pickle', 'wb') as f:
        pickle.dump(fitness_per_generations, f, pickle.HIGHEST_PROTOCOL)

#     for values, chromosome in best_fit_and_chromosome:
#         print('--------------------------------------')
#         print(values)
#         print(chromosome)

    i+=1
