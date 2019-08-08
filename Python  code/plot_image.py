#!/usr/bin/python
# -*- coding:utf-8 -*-

# instruction： This file realize the function of plot the data in the experiment.

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def plot_image2(x,y):
    # plt.close()
    fig = plt.figure()

    ax = fig.add_subplot(111)

    ax.scatter(x, y, c='b')
    ax.set_xlabel('f_1')
    ax.set_ylabel('f_2')

    plt.show()


def plot_image(x,y,z):
    # plt.close()
    fig = plt.figure()

    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(x, y, z, c='b')
    ax.set_xlabel('f_1')
    ax.set_ylabel('f_2')
    ax.set_zlabel('f_3')

    plt.show()




def main():


    file_name = r"ParetoFront/DMOEA_DTLZ1_R1.dat"

    x,y,z = np.loadtxt(file_name, unpack='true')

    fig = plt.figure()

    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(x, y, z, c='b')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()






if __name__ == "__main__":
    main()

