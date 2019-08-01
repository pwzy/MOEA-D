#!/usr/bin/python
# # -*- coding:utf-8 -*-

import random
from objective import objectives

class TIndividual:     # 定义个体类
    # strTestInstance=""
    # numVariables = 30
    # numObjectives = 2
    # # 定义函上下界
    # lowBound = 0
    # uppBound = 1
    #x_var = range(30)
    # x_var = [ 0 for i in range(numVariables)]
    # y_obj = [ 0 for i in range(numObjectives)]
    # rank = 0  # 初始化分类登记为：0



    # 构造函数
    def __init__(self, strTestInstance, numVariables=30, numObjectives=2, lowBound=0, uppBound=1):
        self.strTestInstance = strTestInstance
        self.numVariables = numVariables
        self.numObjectives = numObjectives
        # 传入测试函数定义域的上下界信息
        self.lowBound = lowBound
        self.uppBound = uppBound

        self.x_var = [0 for i in range(numVariables)]
        self.y_obj = [0 for i in range(numObjectives)]
        self.rank = 0

    # 实现种群中个体的随机初始化（每个维度为0 - 1之间的随机值）
    def rnd_init(self):
        for n in range(0, self.numVariables):
            self.x_var[n] = self.lowBound + random.random()*(self.uppBound - self.lowBound)
    def obj_eval(self):
        y_obj = objectives(self.x_var, self.y_obj, self.strTestInstance, self.numVariables, self.numObjectives)
        return y_obj

    # 对"<"号重载，重新赋予意义，使"<"能在个体之间比较
    def __lt__(self, ind2):
        dominated = True
        for n in range(0, self.numObjectives):
            if ind2.y_obj[n]<self.y_obj[n]:
                dominated = False
                return False
        if ind2.y_obj[n] == self.y_obj[n]:
            dominated = False
            return False
        return dominated
    # 实现"=="运算符重载，实现每个个体的目标函数值的比较
    def  __eq__(self,ind2):
        if ind2.y_obj[n] == self.y_obj[n]:
            return True
        else:
            return False
    # 实现对象的赋值操作，相当于重载"="操作符的实现
    def assignment(self, ind2):
        self.x_var = ind2.x_var
        self.y_obj = ind2.y_obj
        self.rank = ind2.rank

    #  显示目标变量的值
    def show_objective(self):
        for n in range(0, self.numObjectives):
            printf("%f ", y_obj[n])
        printf("\n")

    # 显示个体的值
    def show_variable(self):
        for n in range(0, self.numObjectives):
            printf("%f ", x_obj[n])
        printf("\n")


class TSOP:    # 定义一个子问题的类
    def show(self):
        pass

    # strTestInstance = ""
    # numVariables = 30
    # numObjectives = 2
    # 定义函上下界
    # lowBound = 0
    # uppBound = 1

    def __init__(self, strTestInstance, numVariables=30, numObjectives=2, lowBound=0, uppBound=1):
        self.strTestInstance = strTestInstance
        self.numVariables = numVariables
        self.numObjectives = numObjectives
        # 传入测试函数定义域的上下界信息
        self.lowBound = lowBound
        self.uppBound = uppBound

        self.indiv = TIndividual(strTestInstance, numVariables, numObjectives, lowBound, uppBound)
        self.namda = []
        # 定义子问题的领域表
        self.table = []
        # 距离最近的领域数量的向量索引值
        self.array = []

    # # 定义个体
    # indiv = TIndividual(strTestInstance, numVariables, numObjectives, lowBound, uppBound)
    # # 定义权重
    # namda = []
    # # 定义子问题的领域表
    # table = []
    # # 距离最近的领域数量的向量索引值
    # array = []

    #  相当于"="的运算符重载，实现子问题的直接赋值的操作
    def assignment(self, sub2):
        self.indiv = sub2.namda
        self.table = sub2.namda
        self.namda = sub2.namda
        self.array = sub2.array

def main():
    # obj = TIndividual("ZDT3")
    # obj.rnd_init()
    # print(obj.obj_eval())
    pass


if __name__=="__main__":
    main()

