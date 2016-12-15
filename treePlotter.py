#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/15 09:32
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : treePlotter.py
# @Software: PyCharm

# 绘制决策树

import matplotlib.pyplot as plt

# 定义文本框和箭头格式
decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    '''
    绘制带箭头的注解
    :param nodeTxt: 注释文字
    :param centerPt: 箭头指向坐标
    :param parentPt: 箭头起始坐标
    :param nodeType: 节点显示样式
    :return:
    '''
    createPlot.ax1.annotate(nodeTxt, xy=parentPt,  xycoords='axes fraction',
             xytext=centerPt, textcoords='axes fraction',
             va="center", ha="center", bbox=nodeType, arrowprops=arrow_args )

# def createPlot():
#     '''
#     绘制
#     :return:
#     '''
#     fig = plt.figure(1, facecolor='white')
#     fig.clf()
#     createPlot.ax1 = plt.subplot(111, frameon=False)
#     plotNode(u'决策节点', (0.5, 0.1), (0.1, 0.5), decisionNode)
#     plotNode(u'叶子节点', (0.8, 0.1), (0.3, 0.8), leafNode)
#     plt.show()


def getNumLeafs(myTree):
    '''
    计算树的叶子节点个数
    :param myTree:
    :return:
    '''
    numLeafs = 0
    firstStr = list(myTree.keys())[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict': # 测试节点的数据类型是否为字典
            numLeafs += getNumLeafs(secondDict[key])
        else:   numLeafs +=1
    return numLeafs

def getTreeDepth(myTree):
    '''
    计算树的深度
    :param myTree:
    :return:
    '''
    maxDepth = 0
    firstStr = list(myTree.keys())[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict': # 测试节点的数据类型是否为字典
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:   thisDepth = 1
        if thisDepth > maxDepth: maxDepth = thisDepth
    return maxDepth

def plotMidText(cntrPt, parentPt, txtString):
    '''
    在父子节点间填充文本信息
    :param cntrPt: 当前节点
    :param parentPt: 父节点
    :param txtString: 文本信息
    :return:
    '''
    xMid = (parentPt[0]-cntrPt[0])/2.0 + cntrPt[0]
    yMid = (parentPt[1]-cntrPt[1])/2.0 + cntrPt[1]
    createPlot.ax1.text(xMid, yMid, txtString, va="center", ha="center", rotation=-30)

def plotTree(myTree, parentPt, nodeTxt):
    '''
    绘制策略树
    :param myTree: 树字典
    :param parentPt: 父节点坐标
    :param nodeTxt: 节点文本
    :return:
    '''
    numLeafs = getNumLeafs(myTree)  #this determines the x width of this tree
    depth = getTreeDepth(myTree)
    firstStr = list(myTree.keys())[0]     #the text label for this node should be this
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs))/2.0/plotTree.totalW, plotTree.yOff)
    plotMidText(cntrPt, parentPt, nodeTxt)
    plotNode(firstStr, cntrPt, parentPt, decisionNode)
    secondDict = myTree[firstStr]
    plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalD
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':#test to see if the nodes are dictonaires, if not they are leaf nodes
            plotTree(secondDict[key],cntrPt,str(key))        #recursion
        else:   #it's a leaf node print the leaf node
            plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
    plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD


def createPlot(inTree):
    '''
    创建绘制
    :param inTree:
    :return:
    '''
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)    #no ticks
    #createPlot.ax1 = plt.subplot(111, frameon=False) #ticks for demo puropses
    plotTree.totalW = float(getNumLeafs(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
    plotTree.xOff = -0.5/plotTree.totalW; plotTree.yOff = 1.0;
    plotTree(inTree, (0.5,1.0), '')
    plt.show()


def retrieveTree(i):
    '''
    测试树
    :param i: 获取该索引对应的树字典
    :return: 返回树
    '''
    listOfTrees =[{u'不浮出水面是否可以生存': {0: 'no', 1: {u'是否有脚蹼': {0: 'no', 1: 'yes'}}}},
                  {u'不浮出水面是否可以生存': {0: 'no', 1: {u'是否有脚蹼': {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}
                  ]
    return listOfTrees[i]


if __name__ == '__main__':
    createPlot(retrieveTree(1))