from manim import *
import numpy as np

# -------------
# パラメータ
# -------------
# 最大反復回数
nmax = 20
# 終了判定の閾値
eps = 1e-15
# 初期値
n = 0
x = -10
# 結果を格納する配列
result = np.zeros(nmax)

# ------------
# ニュートン法
# ------------
done = 0
while done==0:
    # 出力
    #print('x%d:%.16f\n', n, x)
    result[n] = x
    f = (x-1)/3 - np.exp(-(x-1))
    fx = 1/3 + np.exp(-(x-1))
    y = x - f/fx
    # 厳密解との残差
    r = abs(f)
    # 移動量
    d = abs(y-x)
    # 後処理と終了判定
    x = y
    n += 1
    # 必要に応じて判定条件を設定
    #if r <= eps:
        #done = 1
    #if d <= eps:
        #done = 2
    if n == nmax:
        done = 3

# ----------
# 結果を出力
# ----------
for i in range(nmax):
    print("x%d=%.16f"%(i, result[i]))
