'''バネの振動のアニメーション (三角関数解で計算)'''

from manim import *
import numpy as np


config.frame_width = 8
config.frame_height = 4


class SpringOscillation(Scene):
    def construct(self):
        A = 2          # 振幅
        omega = 2      # 角振動数
        L0 = 4         # ばねの自然長
        turns = 15     # ジグザグの回数
        time = ValueTracker(0)
        # 下端
        bottom = DOWN * 0.5
        # 左端
        leftside = LEFT*3.5
        # 壁
        wall = Line(leftside + bottom, leftside + UP*1.5)
        # 床
        floor = Line(leftside + bottom, RIGHT*3 + bottom)

        # ばねを生成する関数
        def spring():
            x = A * np.cos(omega * time.get_value())
            length = L0 + x

            points = []
            for i in range(turns + 1):
                if(i!=turns):
                    t = i / turns 
                    a = 0.3 # ばねのジグザグの振幅
                else:
                    t = (i - 0.5) / turns
                    a = 0
                px = t * length
                py = a * (-1)**i
                points.append(leftside + [px, py, 0])
            points.append(leftside + [length+0.5, 0, 0])
            spring_line = VMobject()
            spring_line.set_points_as_corners(points)
            spring_line.set_color(WHITE)
            return spring_line

        spring_mob = always_redraw(spring)

        # おもり
        rad = 0.5 # おもりの半径
        mass = always_redraw(
            lambda: Circle(radius=rad, fill_opacity=1, color=YELLOW)
            .move_to(
                RIGHT * (leftside + L0 + A * np.cos(omega * time.get_value()))
                + bottom + rad * UP + rad * RIGHT 
            )
        )

        # 動かす
        self.add(wall, floor, spring_mob, mass)
        self.play(
            time.animate.set_value(4*PI),
            run_time=6,
            rate_func=linear
        )