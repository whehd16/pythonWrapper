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

scaler = MinMaxScaler()
NUMBER_OF_FEATURES = 264
POPULATION_SIZE = 50
KOSPI_NOW_INDEX = 1
best_fit_and_chromosome = []
chromosomes = []
result_fitness = []

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
        print("\t"+str(i)+"번째")
        #낮아야함 반환되는 값에 마이너스 붙을 것.
        lambda1 = []
        lambda3 = []
        lambda5 = []
        combi = combinations(features_indexs[i], 2)
        for x, y in combi:
            lambda1.append(pearson(x, y, csv_file))
            lambda3.append(mutual_information(x, y, csv_file))
            lambda5.append(f_test(x, y, csv))
        #낮아야함 반환되는 값에 플러스 붙을 것
        lambda2 = []
        lambda4 = []
        lambda6 = []
        for y in features_indexs[i]:
            lambda2.append(pearson(KOSPI_NOW_INDEX, y, csv_file))
            lambda4.append(mutual_information(KOSPI_NOW_INDEX, y, csv_file))
            lambda6.append(f_test(KOSPI_NOW_INDEX, y, csv))

        lambda1 = [lambda1]
        scaler.fit(np.transpose(lambda1))
        lambda1 = scaler.transform(np.transpose(lambda1))

        lambda2 = [lambda2]
        scaler.fit(np.transpose(lambda2))
        lambda2 = scaler.transform(np.transpose(lambda2))

        print(lambda3)
        lambda3 = [lambda3]
        scaler.fit(np.transpose(lambda3))
        lambda3 = scaler.transform(np.transpose(lambda3))

        lambda4 = [lambda4]
        scaler.fit(np.transpose(lambda4))
        lambda4 = scaler.transform(np.transpose(lambda4))

        lambda5 = [lambda5]
        scaler.fit(np.transpose(lambda5))
        lambda5 = scaler.transform(np.transpose(lambda5))

        lambda6 = [lambda6]
        scaler.fit(np.transpose(lambda6))
        lambda6 = scaler.transform(np.transpose(lambda6))

        print("\t\tpearson")
        print("\t\t",max(lambda1), min(lambda1))
        print("\t\t",max(lambda2), min(lambda2))
        print("\t\tmutual_information")
        print("\t\t", max(lambda3), min(lambda3))
        print("\t\t", max(lambda4), min(lambda4))
        print("\t\tf_test")
        print("\t\t", max(lambda5), min(lambda5))
        print("\t\t",max(lambda6), min(lambda6))
        # print("\t\tf_test")
        # for l in lambda5:
        #     print("\t\t",l)
        # # print("\t\t", sum(lambda5))
        # print('---------------------------')
        # print("\t\t", sum(lambda6)/max(lambda6))

        fitness_values[i] = -sum(lambda1) + sum(lambda2)- sum(lambda3) + sum(lambda4) - sum(lambda5) + sum(lambda6)

        #  - (sum(lambda5) / max(lambda5)) + (sum(lambda6)/max(lambda6))
        # print(lambda1)
        # print("\t\t- sum(lambda1) / max(lambda1) : ", (sum(lambda1) / len(lambda1)))
        # print("\t\t  sum(lambda2) / max(lambda2) : ", (sum(lambda2) / len(lambda2)))
        # print("\t\t- sum(lambda3) / max(lambda3) : ", (sum(lambda3) / len(lambda3)))
        # print("\t\t  sum(lambda4) / max(lambda4) : ", (sum(lambda4) / len(lambda4)))
        print(fitness_values[i])

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
    x = convert_index_to_numpy(x, csv) #특징 배열
    y = convert_index_to_array(y, csv) #타겟
    f_test, p_value = f_regression(x, y)
    return f_test

def make_roulette_wheels(fitness_values):
    roulette = []
    sum_fintess = sum(fitness_values)
    for i in range(len(fitness_values)):
        for _ in range(math.ceil((fitness_values[i] / sum_fintess) * 100)):
            roulette.append(i)
    return roulette

def selection(roulette):
    return random.sample(roulette, 1)[0]

def remove_values_from_list(the_list, val):
    return [value for value in the_list if value!=val]
csv = pd.read_csv('./second(before_preprocessing)/index/4/22/2007_2008.csv')

def crossover(index1, index2, chromosomes, new_chromosomes):
    one_point = random.randint(1, NUMBER_OF_FEATURES - 1)
    ch1_front = chromosomes[index1][0:one_point]
    ch2_end = chromosomes[index2][one_point:NUMBER_OF_FEATURES+1]
    new_chromosomes.append(ch1_front+ch2_end)

def best_fitness(values):
    return values.index(max(values))

chromosomes = []
roulette_wheels = []
initialization(chromosomes)

for generation in range(10):
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
    roulette_wheels = make_roulette_wheels(fitness_values)
    for _ in range(POPULATION_SIZE):
        selected_index1 = selection(roulette_wheels)
        removed_roulette_wheels = remove_values_from_list(roulette_wheels, selected_index1)
        selected_index2 = selection(removed_roulette_wheels)
        crossover(selected_index1, selected_index2, chromosomes, new_chromosomes)
    chromosomes = copy.deepcopy(new_chromosomes)
    print(best_fit_and_chromosome[generation])

for values, chromosome in best_fit_and_chromosome:
    print('--------------------------------------')
    print(values)
    print(chromosome)
