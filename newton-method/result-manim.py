'''任意の反復回数，終了判定のニュートン法の結果をアニメーションで表示'''

from manim import *
import numpy as np

config.frame_width = 18
config.frame_height = 32

class newton(Scene):
    def construct(self):
    # ----------
    # パラメータ
    # ----------
        # 最大反復回数
        nmax = 11
        # 終了判定の閾値
        eps = 1e-15
        # 初期値
        n = 0
        x = 100
        # 結果を格納する配列
        result = np.zeros(nmax)

    # -----------
    # ニュートン法
    # -----------
        done = 0
        while done==0:
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
            # 判定条件を必要に応じて追加
            #if r <= eps:
                #done = 1
            #if d <= eps:
                #done = 2
            if n == nmax:
                done = 3
    # ---------
    # 結果を出力
    # ---------
        for i in range(nmax):
            formula_text = f"x_{{{i}}} = {result[i]:.15f}"
            tex = MathTex(formula_text).move_to(UP*3.5+DOWN*i*0.7)
            self.play(Write(tex), run_time=0.5)
        self.wait(1)
