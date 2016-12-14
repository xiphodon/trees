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


def splitDataSet(dataSet, axis, value):
    '''
    按照给定特征划分数据集
    :param dataSet: 待划分的数据集
    :param axis: 划分数据集的特征
    :param value: 需要返回的特征的值
    :return: 符合条件的数据列表
    '''
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value: # 将符合特征的数据值抽取出
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    '''
    选择最好的数据集划分方式
    遍历整个数据集，循环计算香农熵和splitDataSet()函数
    :param dataSet: 数据集
    :return:
    '''
    numFeatures = len(dataSet[0]) - 1 # 特征的个数，最后一列作为标签
    baseEntropy = calcShannonEnt(dataSet) # 计算原始数据的香农熵
    bestInfoGain = 0.0; bestFeature = -1 # 信息增量，最佳特征
    for i in range(numFeatures): # 迭代完所有的特征
        featList = [example[i] for example in dataSet] # 当前特征下的所有数据的特征值列表
        uniqueVals = set(featList) # 列表去重
        newEntropy = 0.0 # 熵
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value) # 划分数据集
            prob = len(subDataSet)/float(len(dataSet)) # 划分后数据出现的频数
            newEntropy += prob * calcShannonEnt(subDataSet) # 计算该特征的香农熵
        infoGain = baseEntropy - newEntropy # 信息增益
        if (infoGain > bestInfoGain): # 对比信息增益，获取最大增益量和最大增益量的特征
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature


if __name__ == '__main__':
    dataSet, labels = createDataSet()
    print(calcShannonEnt(dataSet))
    print(splitDataSet(dataSet,0,1))