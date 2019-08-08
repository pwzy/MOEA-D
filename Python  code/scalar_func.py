#!/usr/bin/python
# # -*- coding:utf-8 -*-
import math

def scalar_func(numObjectives, idealpoint, y_obj, namda, nbi_node, strFunctionType = "_TCH1"):
    fvalue = 0;
    # Tchebycheff approach // 切比雪夫方法
    if strFunctionType == "_TCH1":
        max_fun = -1.0e+30;
        for n in range(numObjectives):
            diff = math.fabs(y_obj[n] - idealpoint[n])
            if namda[n] == 0:
                feval = 0.00001*diff
            else:
                feval = diff * namda[n]
            if feval > max_fun:
                max_fun = feval
        fvalue = max_fun




    #  normalized Tchebycheff approach // 正则化切比雪夫方法
    if strFunctionType == "_TCH2":
        pass





    # * Boundary intersection approach  //插界法

    if strFunctionType == "_PBI":
        pass


    return  fvalue




def main():

    pass


if __name__=="__main__":
    main()