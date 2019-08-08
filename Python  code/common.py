#!/usr/bin/python
# # -*- coding:utf-8 -*-

import random
import math

def distanceArray(vec1, vec2, dim):
    sum = 0
    for n in range(dim):
        sum += (vec1[n]-vec2[n])*(vec1[n]-vec2[n])
    return math.sqrt(sum)
def distanceVector(vec1, vec2):
    sum = 0
    for n in range(len(vec1)):
        sum += (vec1[n]-vec2[n])*(vec1[n]-vec2[n])
    return math.sqrt(sum)
def norm_vector(x):
    sum = 0
    for i in range(len(x)):
        sum = sum + x[i]*x[i]
    return math.sqrt(sum)
def sum_vector(vec):
    sum = 0
    for i in range(len(vec)):
        sum = sum + vec[i]
    return sum
def innerproduct(vec1, vec2):
    sum = 0
    for i in range(len(vec1)):
        sum += vec[i]*vec2[i]
    return sum
# 将数组按从小到大排序，找到距离权重最小的m个向量的索引值并存储在idx的前m个数据中，距离存储在x数组中
def minfastsort(x, idx, n, m):  # n代表的是种群规模，m代表的是领域的大小
    for i in range(m):
        for j in range(i+1, n):
            if x[i] > x[j] :
                temp = x[i]
                x[i] = x[j]
                x[j] = temp
                id = idx[i]
                idx[i] = idx[j]
                idx[j] = id
def main():

    pass


if __name__=="__main__":
    main()