# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 12:39:05 2024

@author: Administrator
"""

import matplotlib.pyplot as plt
import numpy as np
#from matplotlib import ticker, cm
#先做一阶段输数据，
#假设1吨 密度0.868吨/立方米，计算得到扩散的半径为19.56米 一阶段持续时间206S
#最终扩散半径D为128.4
#V=50;
#K1=2.28
#K2=2.9
#K3=3.2
#T1=761
#T2=4813
#T3=39879

def disfussion(Py,V):
      V=50
      py=810
      K1=2.28
      K2=2.9
      K3=3.2
      T1=207.2*np.power(V,1/3)#T1=761
      T2=364.8*np.power(V,2/3)#T2=4813
      T3=5755*np.power(V,1/2)#T3=39879
      g=9.8
      Py=810
      Pw=1022
      lo=1-Py/Pw
      Bw=0.0000001
      C1=9.8*lo*V*T1*T1
      R1=1.14*np.power(C1,1/4)#R1正确
      C2=9.8*lo*V*V/0.001
      R2=1.45*np.power(C2,1/6)*np.power(T2,1/4)
      R3=178.4*np.power(V,3/8)
      print(lo)
      print(R1)
      print(R2)
      print(R3)
      N = 1000
      feng=1
      D=R3
      x = np.linspace(-D*feng,D*feng, N)#0.8为扩散系数综合了风力，水流合力
      y = np.linspace(-D, D, N)
      X, Y = np.meshgrid(x, y)#此处操作是为了将x,y的数据点数一致
      na=D*feng-abs(X*feng-D*feng)
      nb=D-abs(Y-D)#越接近圆心受到扩散的时间越早
      m1 = np.add(na*na,nb*nb)#Z = np.exp(-X**2 - Y**2)可以把Z轴作为时间轴
      Z=pow(m1,0.5)
#进行绘图 假设风力和水流力合力方向为任意角度如60度，加速系数为1.1.
      fig, ax = plt.subplots()#创建总画布和窗口
      cs = ax.contourf(X, Y, Z, 20)#等高线之间区域作图#cs = ax.contourf(X, Y, Z, cmap=plt.get_cmap('Spectral'))#等高线之间区域作图
      cs=plt.contour(X,Y,Z,[R1,R2,R3],colors='k')
      plt.rcParams['font.sans-serif']=['SimHei']
      plt.rcParams['axes.unicode_minus']=False
      plt.title("扩散范围")
      plt.xlabel("X轴方向")
      plt.ylabel("Y轴方向")
      plt.clabel(cs,fontsize=10,colors=('k'))
#添加colorbar
      cbar = fig.colorbar(cs)
      text1='difussion time:'+str(+int(T1))+'(s)'
      text2='difussion time:'+str(int(T2))+'(s)'
      text3='difussion time:'+str(int(T3))+'(s)'
      plt.text(R1,0,text1,color="r")
      plt.text(0,R2,text2,color="r")
      plt.text(0,R3-100,text3,color="r")
      plt.show()
