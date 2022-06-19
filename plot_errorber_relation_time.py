# coding: UTF-8
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime as dt
#matplotlib.use('TkAgg')
import matplotlib.ticker as ptick

#x = np.array([l for l in range(5)], dtype=float)
#x_label = ['30~39.9%', '40~49.9%', '50~59.9%', '60~69.9%', '70~80%']

#グラフを描く

y = [0.767009,0.649940,0.487281,0.349911,0.237829]
yerr = [[0.0440821,0.118703,0.138755,0.0673696,0.078718],[0.0323028,0.128719,0.147444,0.0875684,0.122389]]
#[負のエラー]、[正のエラー]の組み合わせ

#誤差棒を描く
#plt.errorbar(x,y,yerr,label="", fmt='o', color="b",ecolor='b',capsize=4.0)#fmtが折れ線にするかどうかとか決める
#棒グラフにするとき
#plt.bar(x, y, color="dodgerblue", label="glpk", tick_label=x_label, align="center")

#for i in range(0,7):
#    plt.scatter(x[i],y[i],c="r")
#plt.errorbar(x[0],y[0],xerr=[[xerr[0][0]],[xerr[1][0]]],yerr=[[yerr[0][0]],[yerr[1][0]]],label="XMM1", fmt='o', color="black",ecolor='black',capsize=4.0)
#plt.errorbar(x[1],y[1],xerr=[[xerr[0][0]],[xerr[1][0]]],yerr=[[yerr[0][1]],[yerr[1][1]]],label="XMM2", fmt='o', color="r",ecolor='r',capsize=4.0)
#plt.errorbar(x[2],y[2],xerr=[[xerr[0][0]],[xerr[1][0]]],yerr=[[yerr[0][2]],[yerr[1][2]]],label="XMM3", fmt='o', color="g",ecolor='g',capsize=4.0)
#plt.errorbar(x[3],y[3],xerr=[[xerr[0][0]],[xerr[1][0]]],yerr=[[yerr[0][3]],[yerr[1][3]]],label="XMM4", fmt='o', color="blue",ecolor='blue',capsize=4.0)
#plt.errorbar(x[4],y[4],xerr=[[xerr[0][0]],[xerr[1][0]]],yerr=[[yerr[0][4]],[yerr[1][4]]],label="XMM5", fmt='o', color="cyan",ecolor='cyan',capsize=4.0)
#plt.errorbar(x[5],y[5],xerr=[[xerr[0][0]],[xerr[1][0]]],yerr=[[yerr[0][5]],[yerr[1][5]]],label="XMM6", fmt='o', color="m",ecolor='m',capsize=4.0)
#plt.errorbar(x[6],y[6],xerr=[[xerr[0][0]],[xerr[1][0]]],yerr=[[yerr[0][6]],[yerr[1][6]]],label="XMM7", fmt='o', color="y",ecolor='y',capsize=4.0)
#plt.errorbar(x[7],y[7],xerr=[[xerr[0][7]],[xerr[1][7]]],yerr=[[yerr[0][0]],[yerr[1][0]]],label="XMM8", fmt='o', color="orange",ecolor='orange',capsize=4.0)
#plt.scatter(x[7],y[7],label="", color="b")
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(0,800000.0 )
ax.xaxis.set_major_formatter(ptick.ScalarFormatter(useMathText=True))   # こっちを先に書くこと。
ax.ticklabel_format(style="sci", axis="x", scilimits=(5,5))   # 10^3単位の指数で表示する。


xerr = [[47755.0,49455.0,49459.0,47757.0,49459.0],[47755.0,49455.0,49459.0,47757.0,49459.0]]

left = np.array([47755.0,218716.0,391650.0,565909.0,736880.0])
height = np.array([0.767009,0.649940,0.487281,0.349911,0.237829])

plt.bar(left[0], height[0],xerr=[[xerr[0][0]],[xerr[1][0]]],yerr=[[yerr[0][0]],[yerr[1][0]]], ecolor="red")
plt.bar(left[1], height[1],xerr=[[xerr[0][1]],[xerr[1][1]]],yerr=[[yerr[0][1]],[yerr[1][1]]], ecolor="green")
plt.bar(left[2], height[2],xerr=[[xerr[0][2]],[xerr[1][2]]],yerr=[[yerr[0][2]],[yerr[1][2]]], ecolor="blue")
plt.bar(left[3], height[3],xerr=[[xerr[0][3]],[xerr[1][3]]],yerr=[[yerr[0][3]],[yerr[1][3]]], ecolor="cyan")
plt.bar(left[4], height[4],xerr=[[xerr[0][4]],[xerr[1][4]]],yerr=[[yerr[0][4]],[yerr[1][4]]], ecolor="magenta")

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
plt.rcParams['font.size'] = 15 #フォントの大きさ
plt.rcParams['axes.linewidth'] = 1.0# 軸の線幅edge linewidth。囲みの太さ
plt.savefig("xmm_cov_time_powfree.pdf")

plt.show()

#plt.savefig("xmm_cov_time_powfree.pdf")

