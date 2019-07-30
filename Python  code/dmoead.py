#!/usr/bin/python
# # -*- coding:utf-8 -*-

from individual import *
from common import *
from scalar_func import scalar_func
import random
from recombination import *
import copy

class TMOEAD:

    # 将上边定义的参考点进行初始化操作
    def init_reference_point(self):
        for i in range(self.numObjectives):
            self.indivpoint.append(TIndividual(self.strTestInstance, self.numVariables, self.numObjectives,
                                               self.lowBound, self.uppBound))
        # 随机初始化参考点并就计算参考点的值
        for n in range(self.numObjectives):
            self.idealpoint[n] = 1.0e+30
            self.indivpoint[n].rnd_init()
            self.indivpoint[n].obj_eval()



    # 构造函数的定义
    def __init__(self, strTestInstance, numVariables=30, numObjectives=2, lowBound=0, uppBound=1):
        self.niche = 0  # 定义领域大小
        self.pops = 0  # 定义种群大小
        self.strTestInstance = strTestInstance
        self.numVariables = numVariables
        self.numObjectives = numObjectives
        # 传入测试函数定义域的上下界信息
        self.lowBound = lowBound
        self.uppBound = uppBound
        # 参考点（每个目标函数就有有一个参考点，共有numObjectives个参考点）
        self.indivpoint = []
        self.idealpoint = [0 for i in range(numObjectives)]

        self.init_reference_point()

        # 定义种群
        self.population = []

    # 对每个子问题初始化权重
    def init_uniformweight(self, sd):
        # 生成权重向量的整数（权重向量的个数等于种群规模个数）
        for i in range(sd):
            if self.numObjectives == 2:
                sop = TSOP(self.strTestInstance, self.numVariables, self.numObjectives,
                                             self.lowBound, self.uppBound)
                sop.array.append(i)
                sop.array.append(sd-i)
                for j in range(len(sop.array)):
                    sop.namda.append(1.0*sop.array[j]/sd)
                self.population.append(sop)
            else:
                for j in range(sd):
                    if i+j <= sd:
                        sop = TSOP(self.strTestInstance, self.numVariables, self.numObjectives,
                                             self.lowBound, self.uppBound)
                        sop.array.append(i)
                        sop.array.append(j)
                        sop.array.append(sd-i-j)
                        for k in range(len(sop.array)):
                            sop.namda.append(1.0*sop.array[k]/sd)
                        self.population.append(sop)
        self.pops = len(self.population)

    # 初始化种群中的个体值
    def init_population(self):
        for i in range(self.pops):
            self.population[i].indiv.rnd_init()
            self.population[i].indiv.obj_eval()
            self.update_reference(self.population[i].indiv)

    # 计算每个问题的领域
    def init_neighbourhood(self):
        x = [ 0 for i in range(self.pops)]
        idx = [ 0 for i in range(self.pops)]
        for i in range(self.pops):
            for j in range(self.pops):
                x[j] = distanceVector(self.population[i].namda, self.population[j].namda)
                idx[j] = j
            minfastsort(x, idx, self.pops, self.niche)
            for k in range(self.niche):
                self.population[i].table.append(idx[k])
    # 更新参考点
    def update_reference(self, ind):
        for n in range(self.numObjectives):
            if ind.y_obj[n] < self.idealpoint[n] :
                self.idealpoint[n] = ind.y_obj[n]
                self.indivpoint[n].assignment(ind)

    def update_problem(self, indiv, id):
        for i in range(self.niche):   #  对正在操作中的向量的每一个领域中的向量进行遍历
            k = self.population[id].table[i] # k代表正在操作的向量的领域中的每一个向量（随着迭代分别代表 第1，2。。。niche个向量）
            f1 = scalar_func(self.numObjectives, self.idealpoint, self.population[k].indiv.y_obj, self.population[k].namda, self.indivpoint)
            f2 = scalar_func(self.numObjectives, self.idealpoint, indiv.y_obj, self.population[k].namda, self.indivpoint)
            if f2 < f1:
                self.population[k].indiv = indiv # 见MOEA/D的第2.4步
    def evolution(self):
        for i in range(len(self.population)):
            n = i
            s = len(self.population[n].table)
            r1 = random.randrange(0, s)  # r1代表生成0-s中的一个整数
            r2 = random.randrange(0, s)  # r2同上
            p1 = self.population[n].table[r1]
            p2 = self.population[n].table[r2]
            child = TIndividual(self.strTestInstance, self.numVariables, self.numObjectives, self.lowBound, self.uppBound)
            child2 = TIndividual(self.strTestInstance, self.numVariables, self.numObjectives, self.lowBound, self.uppBound)
            child, child2 = realbinarycrossover(self.population[p1].indiv, self.population[p2].indiv,
                                                self.numVariables, self.lowBound, self.uppBound, child,
                                                child2)
            child = realmutation(child, 1.0/self.numVariables, self.numVariables, self.lowBound, self.uppBound)
            child.obj_eval()
            self.update_reference(child)
            self.update_problem(child, n)

    def run(self, sd, nc, mg, rn):
        self.niche = nc
        self.init_uniformweight(sd)
        self.init_neighbourhood()
        self.init_population()
        for gen in range(2,mg+1):
            self.evolution()
        savefilename = "ParetoFront/DMOEA_" + self.strTestInstance + "_R" + str(rn) + ".txt"
        self.save_front(savefilename)
        self.population.clear()

    def save_front(self, saveFilename):
        target = open(saveFilename, mode='w+')
        for n in range(len(self.population)):
            for k in range(self.numObjectives):
                # target.writelines("%d  " % (self.population[n].indiv.y_obj[k]))
                target.writelines("%f  " % (self.population[n].indiv.y_obj[k]))
            # print(self.population[n].indiv.y_obj)
            target.writelines("\n")
        target.close()

def main():
    pass

if __name__=="__main__":
    main()