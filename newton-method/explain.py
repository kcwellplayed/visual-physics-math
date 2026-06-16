'''ニュートン法の幾何的な説明用アニメーション'''

from manim import *
import numpy as np


config.frame_width = 9
config.frame_height = 16


class explain(MovingCameraScene):
    def construct(self):

    # ------------------
    # 関数をグラフ上に表示
    # ------------------
        # 座標平面
        ax = Axes(
            x_range = [-1, 6, 1],
            y_range = [-1, 3, 1],
            x_length = 7,
            y_length = 4,
            tips = False
        )

        # 表示する関数
        def func(x):
            return (x-1)/3 - np.exp(-(x-1))
        
        # 表示する関数の導関数
        def func_d1(x):
            return 1/3 + np.exp(-(x-1))
        
        # 関数をグラフにのせる
        graph = ax.plot(
            func,
            x_range = [0, 6],
            color = BLUE,
            stroke_width = 2
        )

        texFunc = MathTex(
            r"y=\frac{x-1}{3}-e^{-(x-1)}",
            font_size = 48
        ).move_to(RIGHT+UP)
        self.play(Create(ax))
        self.play(Create(graph), Write(texFunc))
 
    # -----------------------------------
    # 初期値から接線を引きx軸との交点を求める
    # -----------------------------------
        # 初期値上の接線
        x0 = 5.7         
        y0 = func(x0)
        dot0 = Dot(ax.c2p(x0, y0), radius=0.07)
        dotx0 = Dot(ax.c2p(x0, 0), radius=0.07)
        texX0 = MathTex(
            r"x_0", font_size=48
        ).move_to(dotx0.get_center()+DOWN*0.5)
        line0 = DashedLine(
            dotx0.get_center(),
            dot0.get_center(),
            stroke_width=2,
            dash_length=0.05,
            dashed_ratio=0.7
        )
        tangent0 = ax.plot(
            lambda x: func_d1(x0)*(x-x0)+y0,
            color = RED,
            stroke_width=2
        )

        # x1上での接線
        x1 = -y0/func_d1(x0)+x0
        y1 = func(x1)
        dot1 = Dot(ax.c2p(x1, y1), radius=0.07)
        dotx1 = Dot(ax.c2p(x1, 0), radius=0.07)
        texX1 = MathTex(
            r"x_1", font_size=48
        ).move_to(dotx1.get_center()+UP*0.5+LEFT*0.1)
        line1 = DashedLine(
            dotx1.get_center(),
            dot1.get_center(),
            stroke_width=2,
            dash_length=0.05,
            dashed_ratio=0.7
        )
        tangent1 = ax.plot(
            lambda x: func_d1(x1)*(x-x1)+y1,
            color = RED,
            stroke_width=2
        )

        # x2上での接線
        x2 = -y1/func_d1(x1)+x1
        y2 = func(x2)
        dot2 = Dot(ax.c2p(x2, y2), radius=0.07)
        dotx2 = Dot(ax.c2p(x2, 0), radius=0.07)
        texX2 = MathTex(
            r"x_2", font_size=48
        ).move_to(dotx2.get_center()+UP*0.5+RIGHT*0.1)
        line2 = DashedLine(
            dotx2.get_center(),
            dot2.get_center(),
            stroke_width=2,
            dash_length=0.05,
            dashed_ratio=0.7
        )
        tangent2 = ax.plot(
            lambda x: func_d1(x2)*(x-x2)+y2,
            color = RED,
            stroke_width=2
        )

        # x3上での接線
        x3 = -y2/func_d1(x2)+x2
        y3 = func(x3)
        dotx3 = Dot(ax.c2p(x3, 0), radius=0.07)
        texX3 = MathTex(
            r"x_3", font_size=48
        ).move_to(dotx3.get_center()+DOWN*0.5+RIGHT*0.1)


    # ------------
    # 動かす
    # ------------
        # 接線1つ目
        self.play(Create(dotx0), Write(texX0))
        self.play(Create(line0), run_time=0.5)
        self.play(Create(dot0))
        self.play(Create(tangent0))

        # 接線2つ目
        self.play(Create(dotx1), Write(texX1))
        self.play(FadeOut(dot0), FadeOut(line0),run_time=0.1)
        self.play(Create(line1), run_time=0.5)
        self.play(FadeOut(tangent0), run_time=0.3)
        self.play(Create(dot1))
        self.play(Create(tangent1))

        # 接線3つ目
        self.play(Create(dotx2), Write(texX2))
        self.play(FadeOut(dot1), FadeOut(line1))
        # ズームする
        self.play(
            self.camera.frame.animate.move_to(dotx2).set(width=3) 
        )
        self.play(Create(line2))
        self.play(FadeOut(tangent1), run_time=0.3)
        self.play(Create(dot2))
        self.play(Create(tangent2))

        # 接線4つ目
        self.play(Create(dotx3), Write(texX3))
        self.play(FadeOut(dot2), FadeOut(line2), FadeOut(tangent2))
        self.wait(1)