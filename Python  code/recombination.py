#!/usr/bin/python
# # -*- coding:utf-8 -*-
import random
import math


id_cx = 20    # crossover
id_mu = 20    # for mutation
EPS = 1.2e-7
eta_c = id_cx

# 模拟二进制交叉
def realbinarycrossover(parent1, parent2, numVariables, lowBound, uppBound, child1, child2):
    if random.random() <= 1.0:
        for i in range(numVariables):
            if random.random() <= 0.5:
                if math.fabs(parent1.x_var[i] - parent2.x_var[i] > EPS):
                    if parent1.x_var[i] < parent2.x_var[i]:
                        y1 = parent1.x_var[i]
                        y2 = parent2.x_var[i]
                    else:
                        y1 = parent2.x_var[i]
                        y2 = parent1.x_var[i]
                    yl = lowBound
                    yu = uppBound
                    rand = random.random()
                    beta = 1.0 + (2.0*(y1-yl)/(y2-y1))  # 定义参数beta的值
                    alpha = 2.0 - math.pow(beta, -(eta_c + 1.0))  # 定义参数alpha的值
                    if rand <= (1.0/alpha):
                        betaq = math.pow((rand*alpha), (1.0/(eta_c+1.0)))
                    else:
                        betaq = math.pow ((1.0/(2.0 - rand*alpha)), (1.0/(eta_c+1.0)))
                    c1 = 0.5*((y1+y2)-betaq*(y2-y1))
                    beta = 1.0 + (2.0 * (yu - y2) / (y2 - y1))
                    alpha = 2.0 - math.pow(beta, -(eta_c + 1.0))
                    if rand <= (1.0/alpha):
                        betaq = math.pow((rand * alpha), (1.0 / (eta_c + 1.0)))
                    else:
                        betaq = math.pow((1.0 / (2.0 - rand * alpha)), (1.0 / (eta_c + 1.0)))
                    c2 = 0.5 * ((y1 + y2) + betaq * (y2 - y1))
                    if c1 < yl:
                        c1 = yl
                    if c2 < yl:
                        c2 = yl
                    if c1 > yu:
                        c1 = yu
                    if c2 > yu:
                        c2 = yu
                    if random.random() <= 0.5:
                        child1.x_var[i] = c2
                        child2.x_var[i] = c1
                    else:
                        child1.x_var[i] = c1
                        child2.x_var[i] = c2
                else:
                    child1.x_var[i] = parent1.x_var[i]
                    child2.x_var[i] = parent2.x_var[i]
            else:
                child1.x_var[i] = parent1.x_var[i]
                child2.x_var[i] = parent2.x_var[i]
    else:
        child1.x_var[i] = parent1.x_var[i]
        child2.x_var[i] = parent2.x_var[i]



    return child1, child2


def realmutation(ind, rate, numVariables, lowBound, uppBound):
    eta_m = id_mu

    id_rnd = random.randrange(0, numVariables)  # id_rnd代表生成0-s中的一个整数
    for j in range(numVariables):
        if random.random() <= rate:
            y = ind.x_var[j]
            yl = lowBound
            yu = uppBound
            delta1 = (y - yl) / (yu - yl)
            delta2 = (yu - y) / (yu - yl)
            rnd = random.random()
            mut_pow = 1.0 / (eta_m + 1.0)
            if rnd <= 0.5:
                xy = 1.0 - delta1
                val = 2.0 * rnd + (1.0 - 2.0 * rnd) * (math.pow(xy, (eta_m + 1.0)))
                deltaq = math.pow(val, mut_pow) - 1.0
            else:
                xy = 1.0 - delta2
                val = 2.0 * (1.0 - rnd) + 2.0 * (rnd - 0.5) * (math.pow(xy, (eta_m + 1.0)))
                deltaq = 1.0 - (math.pow(val, mut_pow))
            y = y + deltaq*(yu-yl)
            if y < yl:
                y = yl
            if y > yu:
                y = yu
            ind.x_var[j] = y
    return ind





def main():

    pass


if __name__=="__main__":
    main()