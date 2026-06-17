'''Kapitzaの振り子のアニメーション'''

from manim import *
import math
import numpy as np

config.frame_width = 18
config.frame_height = 32


class Kapitza(Scene):
    def construct(self):
        # -------------
        # 定数
        # -------------          
        m = 1           # 質量 
        l = 5           # 棒の長さ
        x0 = 0          # 台の初期座標
        y0 = -3
        pos = np.array([x0, y0, 0], dtype=float)      # 支点の位置
        theta0 = 0.01   # 初期角度
        omega0 = 0.5    # 初期角速度
        Omega = 50      # 強制振動角周波数
        a = 0.3         # 強制振動振幅
        g = 9.807       # 重力加速度
        
        # -------------
        # 変数
        # -------------
        u = np.array([theta0, omega0], dtype=float)
        t = 0           # 時間

        # -------------
        # オブジェクト
        # -------------
        # 状態管理
        state = Mobject()

        # 紐
        rod = Line(
            pos,
            pos + np.array([-l*math.sin(u[0]), l*math.cos(u[0]), 0]),
            stroke_width = 2
        )

        # おもり
        dot = Dot(
            pos + np.array([-l*math.sin(u[0]), l*math.cos(u[0]), 0]), 
            radius=0.2, 
            color=BLUE
        )

        # 支点
        fulcrum = Dot(
            pos,
            radius=0.1,         
        )

        # 支点の移動範囲
        scope = Line(
            pos - a*UP,
            pos + a*UP,
            stroke_width = 4,
            color = RED
        )

        # -------------
        # 関数
        # -------------
        def func_f(t, u):
            nonlocal g, l, m
            return np.array(
                [u[1],
                 (g*math.sin(u[0]) - a*(Omega**2)*math.sin(u[0])*math.sin(Omega*t)) / l
                ]
            )
        
        def pivot(t):
            return np.array([x0, y0+a*math.sin(Omega*t), 0])

        def update_system(mob, dt):
            nonlocal u, t, pos, y0
            k1 = func_f(t, u)
            k2 = func_f(t+dt/2, u + (dt/2)*k1)
            k3 = func_f(t+dt/2, u + (dt/2)*k2)
            k4 = func_f(t+dt, u + dt*k3)
            u = u + (dt/6)*(k1 + 2*k2 + 2*k3 + k4)
            t = t + dt 

        # 位置更新
        def update_dot(mob):
            mob.move_to(
                pivot(t) + np.array([-l*math.sin(u[0]), l*math.cos(u[0]), 0])
            )
        
        def update_rod(mob):
            mob.put_start_and_end_on(
                pivot(t),
                pivot(t) + np.array([-l*math.sin(u[0]), l*math.cos(u[0]), 0])
            )
        
        def update_fulcrum(mob):
            mob.move_to(
                pivot(t) 
            )


        # -------------
        # 動かす
        # -------------
        # オブジェクトを表示
        self.play(Create(rod), Create(dot), Create(fulcrum), Create(scope))
        self.wait(1)
        
        # シミュレーション開始
        self.add(state)
        state.add_updater(update_system)
        dot.add_updater(update_dot)
        rod.add_updater(update_rod)
        fulcrum.add_updater(update_fulcrum)
        self.wait(10)