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

def createPlot():
    '''
    绘制
    :return:
    '''
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    createPlot.ax1 = plt.subplot(111, frameon=False)
    plotNode(u'决策节点', (0.5, 0.1), (0.1, 0.5), decisionNode)
    plotNode(u'叶子节点', (0.8, 0.1), (0.3, 0.8), leafNode)
    plt.show()


if __name__ == '__main__':
    createPlot()