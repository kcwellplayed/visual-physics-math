'''振り子の運動のアニメーション(運動方程式をRunge-Kuttaで計算)'''

from manim import *
import math
import numpy as np


config.frame_width = 9
config.frame_height = 16


class pendulum(Scene):
    def construct(self):
        # ---------
        # パラメータ
        # ---------
        g = 9.807                                 # 重力加速度
        yu = 1                                    # 上端のy座標
        yl = -0.5                                 # 下端のy座標
        l = yu - yl                               # 紐の長さ
        UpperEdge = np.array([0, yu, 0])          # 上端の座標
        LowerEdge = np.array([0, yl, 0])          # 下端の座標
        theta0 = math.pi / 6                      # 初期角度
        omega0 = 0                                # 初期角速度
        u = np.array([theta0, omega0])            # (theta, omega)


        # --------------
        # オブジェクト
        # --------------
        # 状態管理
        state = Mobject()

        # 紐
        rod = Line(
                UpperEdge,
                UpperEdge + np.array([l * math.sin(u[0]), -l * math.cos(u[0]), 0]),
                stroke_width = 1
        )

        # おもり
        dot = Dot(
            UpperEdge + np.array([l * math.sin(u[0]), -l * math.cos(u[0]), 0]), 
            radius=0.1, 
            color=BLUE
        )


        # --------------
        # 物理アップデート
        # --------------
        # Runge-Kutta
        def func_f(x):
            nonlocal g, l
            return np.array([x[1], -(g * math.sin(x[0]))/l])
        def update_system(mob, dt):
            nonlocal u
            k1 = func_f(u)
            k2 = func_f(u + (dt/2)*k1)
            k3 = func_f(u + (dt/2)*k2)
            k4 = func_f(u + dt*k3)
            u = u + (dt/6)*(k1 + 2*k2 + 2*k3 + k4)     

        # 位置更新
        def update_dot(mob):
            mob.move_to(
                UpperEdge + np.array([l * math.sin(u[0]), -l * math.cos(u[0]), 0]),
            )
        
        def update_rod(mob):
            mob.put_start_and_end_on(
                UpperEdge,
                UpperEdge + np.array([l * math.sin(u[0]), -l * math.cos(u[0]), 0]) 
            )
        
        # -------------
        # 動かす
        # -------------
        # オブジェクトを表示
        self.play(Create(rod))
        self.wait(1)
        self.play(Create(dot))
        self.wait(1)
        
        # シミュレーション開始
        self.add(state)
        state.add_updater(update_system)
        dot.add_updater(update_dot)
        rod.add_updater(update_rod)
        self.wait(10)