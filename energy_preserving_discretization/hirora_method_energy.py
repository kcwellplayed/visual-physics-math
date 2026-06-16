'''広田の差分化によって得られる離散系のエネルギーをグラフで確認'''

from manim import *
import numpy as np
import math

config.frame_width = 10
config.frame_height = 5


# 広田の差分化(陽的)
def hirota_step(x, v, omega, dt):
    x_new = ((4-(omega*dt)**2)/(4+(omega*dt)**2))*x + ((4*dt)/(4+(omega*dt)**2))*v 
    v_new =  -((4*(omega**2)*dt)/(4+(omega*dt)**2))*x + ((4-(omega*dt)**2)/(4+(omega*dt)**2))*v
    return x_new, v_new


class HirotaSpring(Scene):
    def construct(self):
        # パラメータ
        m = 5
        k = 2
        omega = math.sqrt(k/m)

        # 初期条件
        x = 2
        v = 0
        t = 0

        # 座標軸
        ax = Axes(
            x_range=[0, 12, 2],
            y_range=[0, 8, 1],
            x_length=5,
            y_length=3.5,
            axis_config={
                "include_numbers": True, 
                "tip_length": 0.01         }
        )
        ax.shift(UP * 0.5)
        # 軸ラベル
        x_label = MathTex("t")
        y_label = MathTex("E_n")
        x_label.next_to(ax.x_axis, DOWN)
        y_label.next_to(ax.y_axis, LEFT)

        # 初期エネルギー
        E0 = (m*(v**2))/2 + (k*(x**2))/2
        Em0 = (m*(v**2))/2
        Ek0 = (k*(x**2))/2

        # 点
        dotE = Dot(color=RED).move_to(ax.c2p(0, E0))
        dotEm = Dot(color=BLUE).move_to(ax.c2p(0, Em0))
        dotEk = Dot(color=GREEN).move_to(ax.c2p(0, Ek0))

        # 軌跡
        pathE = TracedPath(dotE.get_center, stroke_color=RED)
        pathEm = TracedPath(dotEm.get_center, stroke_color=BLUE)
        pathEk = TracedPath(dotEk.get_center, stroke_color=YELLOW)

        # updater
        def update_system(mob, dt):
            nonlocal x, v, t

            x, v = hirota_step(x, v, omega, dt)
            t += dt

            E = (m*(v**2))/2 + (k*(x**2))/2
            Em = (m*(v**2))/2
            Ek = (k*(x**2))/2

            dotE.move_to(ax.c2p(t, E))
            dotEm.move_to(ax.c2p(t, Em))
            dotEk.move_to(ax.c2p(t, Ek))

        # 動かす
        dotE.add_updater(update_system)
        self.add(ax, x_label, y_label,
                 pathE, pathEm, pathEk,
                 dotE, dotEm, dotEk)
        self.wait(10)
