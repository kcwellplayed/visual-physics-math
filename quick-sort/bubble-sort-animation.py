"""バブルソートをアニメーションで確認"""
from manim import *
import random

config.frame_width = 18
config.frame_height = 32


class BS(Scene):
    def construct(self):
        # ソートするデータ(乱数で生成or要素を指定)
        Data = [6, 15, 2, 4, 8, 5, 11, 9, 7, 13]
        #random.seed(12)
        #data_size = 20
        #data_max = 60
        #Data = [random.randint(0, data_max) for _ in range(data_size)]
        n = len(Data)

        # 可視化用のグラフ
        ax = Axes(
            x_range = [0, n+1, 1],
            y_range = [0, 20, 4],
            x_length = 9,
            y_length = 9,
            axis_config={"include_numbers": False, "font_size":20},
        )
        # ヒストグラムの生成
        bars = []
        bar_width = 0.6
        for i, val in enumerate(Data):
            p1 = ax.c2p(i, 0)
            p2 = ax.c2p(i+1, Data[i])
            bar = Rectangle(
                height = p2[1] - p1[1],
                width = bar_width,
                fill_opacity = 0.8
            ).move_to(ax.c2p(i+1, 0), aligned_edge=DOWN)
            bars.append(bar)

        # 棒を画面に表示
        self.play(Create(ax))
        self.play(
            AnimationGroup(
                *[Create(bar) for bar in bars], 
                lag_ratio=0.1))
        self.wait(1)

        # バブルソート 
        data = Data.copy()
        current_bars = list(bars)
        flag = True
        for i in range(len(data)):
            for j in range(len(data)-1-i):
                if flag:
                    # 注目する棒を赤色にする
                    self.play(current_bars[j].animate.set_fill(RED), run_time=0.2)
                else:
                    flag = True
                if(data[j] > data[j+1]):
                    # データの交換
                    tmp = data[j+1]
                    data[j+1] = data[j]
                    data[j] = tmp

                    # 移動先を計算
                    p1 = ax.c2p(j+1, 0)
                    p2 = ax.c2p(j+2, 0)
                    
                    # 棒を移動  
                    self.play(
                        current_bars[j].animate.move_to(p2, aligned_edge=DOWN),
                        current_bars[j + 1].animate.move_to(p1, aligned_edge=DOWN),
                        run_time=0.2
                    )
                    # リスト内のオブジェクトも交換
                    current_bars[j], current_bars[j + 1] = current_bars[j + 1], current_bars[j]
                else:
                    # 赤色を移動
                    self.play(
                        current_bars[j].animate.set_fill(WHITE), 
                        current_bars[j+1].animate.set_fill(RED), 
                        run_time=0.2)
                    flag = False
            # ソートが確定した末尾の棒を緑色にする
            self.play(current_bars[n - i - 1].animate.set_fill(GREEN), run_time=0.2)



        


