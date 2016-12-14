#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/14 16:25
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : trees.py
# @Software: PyCharm

# 决策树
import math

def createDataSet():
    '''
    创建数据矩阵
    :return: 数据矩阵，标签列表
    '''
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = [u'不浮出水面是否可以生存',u'是否有脚蹼']
    return dataSet, labels

def calcShannonEnt(dataSet):
    '''
    计算给定数据集的香农熵
    {公式：H = -∑(i=1,n)p(xi)log2p(xi)}
    :param dataSet: 数据矩阵
    :return: 香农熵
    '''
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        # 统计各个类别出现的频数
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0 # 香农熵
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries # 计算类别出现的频率
        shannonEnt -= prob * math.log(prob,2) # log以2为底
    return shannonEnt


if __name__ == '__main__':
    dataSet, labels = createDataSet()
    print(calcShannonEnt(dataSet))