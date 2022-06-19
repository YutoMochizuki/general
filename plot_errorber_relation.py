#!/bin/sh

#errorbarつきのグラフをplotするプログラム

# coding: UTF-8
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime as dt

#x = np.array([l for l in range(5)], dtype=float)
#x_label = ['30~39.9%', '40~49.9%', '50~59.9%', '60~69.9%', '70~80%']

#グラフを描く
x = [17.8311,15.5864,38.9078,32.2195,25.9606,34.7712,468.293,291.053]
xerr = [[2.95789,1.24739,6.6354,13.7198,13.5253,19.5708,2.53828,354.916],[7.23516,1.21813,8.03996,10.4397,4.7236,11.5844,0.367754,-460.475]]
y = [-0.156598,4.45509E-02,-7.95222E-02,-0.106447,-0.134924,-9.96277E-02,5.05914E-02,7.53024]
yerr = [[0.00889729,0.0162037,0.0115118,0.00645306,0.00622193,0.00629463,0.0717015,0.570283],[0.014483,0.0150324,0.0111963,0.00979645,0.00571796,0.00796921,0.0182881,0.540141]]
#[負のエラー]、[正のエラー]の組み合わせ

#誤差棒を描く
#plt.errorbar(x,y,yerr,label="", fmt='o', color="b",ecolor='b',capsize=4.0)#fmtが折れ線にするかどうかとか決める
#棒グラフにするとき
#plt.bar(x, y, color="dodgerblue", label="glpk", tick_label=x_label, align="center")

#for i in range(0,7):
#    plt.scatter(x[i],y[i],c="r")
plt.errorbar(x[0],y[0],xerr=[[xerr[0][0]],[xerr[1][0]]],yerr=[[yerr[0][0]],[yerr[1][0]]],label="XMM1", fmt='o', color="black",ecolor='black',capsize=4.0)
plt.errorbar(x[1],y[1],xerr=[[xerr[0][0]],[xerr[1][0]]],yerr=[[yerr[0][1]],[yerr[1][1]]],label="XMM2", fmt='o', color="r",ecolor='r',capsize=4.0)
plt.errorbar(x[2],y[2],xerr=[[xerr[0][0]],[xerr[1][0]]],yerr=[[yerr[0][2]],[yerr[1][2]]],label="XMM3", fmt='o', color="g",ecolor='g',capsize=4.0)
plt.errorbar(x[3],y[3],xerr=[[xerr[0][0]],[xerr[1][0]]],yerr=[[yerr[0][3]],[yerr[1][3]]],label="XMM4", fmt='o', color="blue",ecolor='blue',capsize=4.0)
plt.errorbar(x[4],y[4],xerr=[[xerr[0][0]],[xerr[1][0]]],yerr=[[yerr[0][4]],[yerr[1][4]]],label="XMM5", fmt='o', color="cyan",ecolor='cyan',capsize=4.0)
plt.errorbar(x[5],y[5],xerr=[[xerr[0][0]],[xerr[1][0]]],yerr=[[yerr[0][5]],[yerr[1][5]]],label="XMM6", fmt='o', color="m",ecolor='m',capsize=4.0)
#plt.errorbar(x[6],y[6],xerr=[[xerr[0][0]],[xerr[1][0]]],yerr=[[yerr[0][6]],[yerr[1][6]]],label="XMM7", fmt='o', color="y",ecolor='y',capsize=4.0)
#plt.errorbar(x[7],y[7],xerr=[[xerr[0][7]],[xerr[1][7]]],yerr=[[yerr[0][0]],[yerr[1][0]]],label="XMM8", fmt='o', color="orange",ecolor='orange',capsize=4.0)
#plt.scatter(x[7],y[7],label="", color="b")

#print(yerr[0][1])

plt.legend()#凡例をつけるコマンド
plt.xlabel("Nh")#上付きとか全部tex
plt.ylabel("redshiht")
#plt.title("partial covering fraction")
#plt.axis([0,6,0,100])
#saveするとき
#plt.savefig("xmm_Nh_z_powfree.pdf")
#plt.savefig("xmm_cov_hflux.png")
plt.grid(False)#Trueでgrid表示

#論文の図の体裁のテンプレ
plt.rcParams["xtick.top"] = True            # 上部に目盛り線を描くかどうか
plt.rcParams["xtick.bottom"] = True         # 下部に目盛り線を描くかどうか
plt.rcParams["ytick.left"] = True           # 左部に目盛り線を描くかどうか
plt.rcParams["ytick.right"] = True          # 右部に目盛り線を描くかどうか

plt.rcParams['font.family'] ='sans-serif'#使用するフォント
plt.rcParams['xtick.direction'] = 'in'#x軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
plt.rcParams['ytick.direction'] = 'in'#y軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
plt.rcParams['xtick.major.width'] = 1.0#x軸主目盛り線の線幅
plt.rcParams['ytick.major.width'] = 1.0#y軸主目盛り線の線幅
plt.rcParams['font.size'] = 8 #フォントの大きさ
plt.rcParams['axes.linewidth'] = 1.0# 軸の線幅edge linewidth。囲みの太さ

plt.show()

#plt.savefig("xmm_norm_time_powfree.pdf")
