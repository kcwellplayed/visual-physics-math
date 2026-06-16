'''動画用'''
'''振り子二つ，角度も記載'''


from manim import *
import math
import numpy as np


class pendulum(Scene):
    def construct(self):
        g = 9.807                                 # 重力加速度
        yu = 1                                    # 上端のy座標
        yl = -0.5                                 # 下端のy座標
        l = yu - yl                               # 紐の長さ
        UpperEdge = np.array([0, yu, 0])          # 上端の座標
        LowerEdge = np.array([0, yl, 0])          # 下端の座標

        thetaA0 = math.pi / 24                    # おもりAの初期角度
        thetaB0 = math.pi / 3                    # おもりBの初期角度
        omegaA0 = 0                               # おもりAの初期角速度
        omegaB0 = 0                               # おもりBの初期角速度
        uA = np.array([thetaA0, omegaA0])         # (thetaA, omegaA)
        uB = np.array([thetaB0, omegaB0])         # (thetaB, omegaB)
        pre_thetaA = thetaA0
        pre_thetaB = thetaB0


        # --------------
        # オブジェクト
        # --------------
        # 状態管理
        state = Mobject()

        # 紐
        rodA = Line(
                UpperEdge,
                LowerEdge,
                stroke_width = 1,
                color=BLUE
        )
        rodB = Line(
                UpperEdge,
                LowerEdge,
                stroke_width = 1,
                color=RED
        )

        # おもり
        dotA = Dot(
            LowerEdge, 
            radius=0.1, 
            color=BLUE
        )
        dotB = Dot(
            LowerEdge, 
            radius=0.1, 
            color=RED
        )

        # 上端点
        upper_dot = Dot(UpperEdge, radius=0.03)
        # 鉛直線
        ver_line = DashedLine(
            UpperEdge,
            LowerEdge,
            stroke_width=1,
            dash_length=0.05,
            dashed_ratio=0.7
        )
        # おもりの角度
        arcA = Arc(
            radius=l*0.4,
            start_angle=-math.pi/2,
            angle=thetaA0,
            arc_center=UpperEdge,
            color=BLUE,
            stroke_width=2
        )
        arcB = Arc(
            radius=l*0.4,
            start_angle=-math.pi/2,
            angle=thetaB0,
            arc_center=UpperEdge,
            color=RED,
            stroke_width=2
        )
        # 角度の数式
        argTexA = MathTex(
            r"\theta_A",
            color=BLUE,  
            font_size=16 
        ).move_to(UpperEdge + DOWN*0.8 + RIGHT*0.1) #0.8, 0.1
        argTexB = MathTex(
            r"\theta_B",
            color=RED,  
            font_size=16 
        ).move_to(UpperEdge + DOWN*0.7 + RIGHT*0.1) #0.7, 0.5
        ThetaTexA = MathTex(
            r"\theta_A=\frac{\pi}{24}",
            color=BLUE,
            font_size=20
        ).move_to(DOWN*1 + LEFT*0.5)
        ThetaTexB = MathTex(
            r"\theta_B=\frac{\pi}{12}",
            color=RED,
            font_size=20
        ).move_to(DOWN*1 + RIGHT*0.5)

        # --------------
        # 物理アップデート
        # --------------
        # Runge-Kutta
        def func_f(x):
            nonlocal g, l
            return np.array([x[1], -(g * math.sin(x[0]))/l])
        
        def update_system(mob, dt):
            nonlocal uA, uB, pre_thetaA, pre_thetaB
            k1 = func_f(uA)
            k2 = func_f(uA + (dt/2)*k1)
            k3 = func_f(uA + (dt/2)*k2)
            k4 = func_f(uA + dt*k3)
            uA = uA + (dt/6)*(k1 + 2*k2 + 2*k3 + k4)     

            k1 = func_f(uB)
            k2 = func_f(uB + (dt/2)*k1)
            k3 = func_f(uB + (dt/2)*k2)
            k4 = func_f(uB + dt*k3)
            uB = uB + (dt/6)*(k1 + 2*k2 + 2*k3 + k4)    

            if(pre_thetaA * uA[0] < 0):
                self.add_sound("pon.wav")
            if(pre_thetaB * uB[0] < 0):
                self.add_sound("pon.wav")

            pre_thetaA = uA[0]
            pre_thetaB = uB[0]

        # 位置更新
        def update_dotA(mob):
            mob.move_to(
                UpperEdge + np.array([l * math.sin(uA[0]), -l * math.cos(uA[0]), 0]),
            )
        def update_dotB(mob):
            mob.move_to(
                UpperEdge + np.array([l * math.sin(uB[0]), -l * math.cos(uB[0]), 0]),
            )     
        
        def update_rodA(mob):
            mob.put_start_and_end_on(
                UpperEdge,
                UpperEdge + np.array([l * math.sin(uA[0]), -l * math.cos(uA[0]), 0]) 
            )
        def update_rodB(mob):
            mob.put_start_and_end_on(
                UpperEdge,
                UpperEdge + np.array([l * math.sin(uB[0]), -l * math.cos(uB[0]), 0]) 
            )
        
        # -------------
        # 動かす
        # -------------

        ## オブジェクトを表示
        ### おもりA
        self.play(Create(rodA))
        #self.wait(1)
        self.play(FadeIn(upper_dot))
        #self.wait(1)
        self.play(Create(dotA))
        #self.wait(1)

        # theta0まで持ち上げる
        rodA.add_updater(lambda m: m.put_start_and_end_on(
            UpperEdge, 
            dotA.get_center()
        ))
        self.play(dotA.animate.move_to(
            UpperEdge + np.array([l * math.sin(uA[0]), -l * math.cos(uA[0]), 0])
        ))
        self.play(Create(ver_line))
        self.play(Create(arcA))
        self.play(Write(argTexA), Write(ThetaTexA))
        self.wait(0.5)
        self.remove(arcA, argTexA)
        rodA.clear_updaters()

        ### おもりB
        self.play(Create(rodB))
        self.add(upper_dot)
        #self.wait(1)
        self.play(Create(dotB))
        #self.wait(1)

        # theta0まで持ち上げる
        rodB.add_updater(lambda m: m.put_start_and_end_on(
            UpperEdge, 
            dotB.get_center()
        ))
        self.play(dotB.animate.move_to(
            UpperEdge + np.array([l * math.sin(uB[0]), -l * math.cos(uB[0]), 0])
        ))
        self.play(Create(arcB))
        self.play(Write(argTexB), Write(ThetaTexB))
        self.wait(0.5)
        self.remove(arcB, argTexB)
        rodB.clear_updaters()

        ## シミュレーション開始
        self.add(rodB, dotB)
        self.add(state)
        state.add_updater(update_system)
        dotA.add_updater(update_dotA)
        rodA.add_updater(update_rodA)
        dotB.add_updater(update_dotB)
        rodB.add_updater(update_rodB)
        self.wait(10)
        