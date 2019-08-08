#!/usr/bin/python
# -*- coding:utf-8 -*-

import random
import math

def objectives(x_var, y_obj, strTestInstance, numVariables, numObjectives):
    if strTestInstance == "ZDT1":
        g = 0.0
        for n in range(1,numVariables):
            g += x_var[n]
        g = 1 + 9 * g / (numVariables - 1)
        y_obj[0] = x_var[0]
        y_obj[1] = g * (1 - math.sqrt(y_obj[0] / g))
        return y_obj
    if strTestInstance == "ZDT2":
        g = 0.0
        for n in range(1,numVariables):
            g += x_var[n]
        g = 1 + 9 * g / (numVariables - 1)
        y_obj[0] = x_var[0]
        y_obj[1] = g * (1 - math.pow(y_obj[0] / g, 2))
        return y_obj
    if strTestInstance == "ZDT3":
        g = 0.0
        for n in range(1,numVariables):
            g += x_var[n]
        g = 1 + 9 * g / (numVariables - 1)
        y_obj[0] = x_var[0]
        y_obj[1] = g * (1 - math.sqrt(x_var[0] / g) - x_var[0] * math.sin(10 * math.pi * x_var[0]) / g)
        return y_obj
    if strTestInstance == "ZDT4":
        g = 0.0
        for n in range(1, numVariables):
            tem = 10*(x_var[n] - 0.5)
            g += tem * tem - 10 * math.cos(4 * math.pi * tem)
        g = 1 + 10 * (numVariables - 1) + g
        y_obj[0] = x_var[0]
        y_obj[1] = g * (1 - math.sqrt(y_obj[0] / g))
        return y_obj
    if strTestInstance == "ZDT6":
        g = 0.0
        for n in range(1, numVariables):
            g += x_var[n] / (numVariables - 1)
        g = 1 + 9 * math.pow(g, 0.25)
        y_obj[0] = 1 - math.exp(-4 * x_var[0]) * math.pow(math.sin(6 * math.pi * x_var[0]), 6)
        y_obj[1] = g * (1 - math.pow(y_obj[0] / g, 2));
        return y_obj
    if strTestInstance == "OKA-1":
        x1 = 2 * math.pi * (x_var[0] - 0.5)
        x2 = (x_var[1] - 0.5) * 10
        y_obj[0] = x1
        y_obj[1] = pi - x1 + math.fabs(x2 - 5*math.cos(x1))
        return y_obj
    if strTestInstance == "OKA-2":
        x1 = 2*math.pow(math.pi,3)*(x_var[0] - 0.5)
        x2 = (x_var[1] - 0.5)*10;
        if x1 >= 0:
            eta = math.pow(x1, 1.0 / 3)
        else:
            eta = -math.pow(-x1,1.0/3)

        y_obj[0] = eta
        y_obj[1] = math.pi - eta + math.fabs(x2 - 5*math.cos(x1))
        return y_obj
    if strTestInstance == "DTLZ1":
        g = 0.0
        for n in range(2,numVariables):
            g = g + math.pow(x_var[n] - 0.5, 2) - math.cos(20 * math.pi * (x_var[n] - 0.5))
        g = 100 * (numVariables - 2 + g)
        y_obj[0] = (1 + g) * x_var[0] * x_var[1]
        y_obj[1] = (1 + g) * x_var[0] * (1 - x_var[1])
        y_obj[2] = (1 + g) * (1 - x_var[0])
        return y_obj
    if strTestInstance == "DTLZ2":
        g = 0.0
        xx = (x_var[0] + x_var[1])/2.0
        for n in range(2, numVariables):
            x = 2 * (x_var[n] - 0.5)
            g = g + x * x
        g = 100 * (numVariables - 2 + g)
        y_obj[0] = (1 + g) * math.cos(x_var[0] * math.pi / 2) * math.cos(x_var[1] * math.pi / 2)
        y_obj[1] = (1 + g) * math.cos(x_var[0] * math.pi / 2) * math.sin(x_var[1] * math.pi / 2)
        y_obj[2] = (1 + g) * math.sin(x_var[0] * math.pi / 2)
        return y_obj

def main():
    y_obj = objectives(list(range(1,31)), list(range(1,4)), "DTLZ2", 10, 3)
    print(y_obj)

if __name__=="__main__":
    main()