"""クイックソートをアニメーションで説明（Lomuto分割法による右端ピボット）"""
from manim import *
import random

config.frame_width = 18
config.frame_height = 32


class QS(Scene):
    def construct(self):
        random.seed(123)
        data_size = 15
        data_max = 20
        Data = [random.randint(0, data_max) for _ in range(data_size)]
        #Data = [3, 5, 3, 6, 1, 2, 8, 5]
        n = len(Data)

        # 可視化用のグラフ
        ax = Axes(
            x_range = [0, n+1, 1],
            y_range = [0, data_max, 4],
            x_length = 9,
            y_length = 9,
            axis_config={"include_numbers": False, "font_size":20},
        )
        # ヒストグラムの生成
        bars = []
        bar_width = 0.3
        for i, val in enumerate(Data):
            p1 = ax.c2p(i, 0)
            p2 = ax.c2p(i+1, Data[i])
            bar = Rectangle(
                height = p2[1] - p1[1],
                width = bar_width,
                fill_opacity = 0.4
            ).move_to(ax.c2p(i+1, 0), aligned_edge=DOWN)
            bars.append(bar)

        # 棒を画面に一斉に表示
        self.play(Create(ax))
        self.play(
            AnimationGroup(
                *[Create(bar) for bar in bars], 
                lag_ratio=0.1))
        

    # ------------------------------
    # 注目部分の背景を塗る関数
    # ------------------------------
        # 背景を初期化
        p0l = ax.c2p(0, 0)
        p0r = ax.c2p(n+1, data_max+2)
        area = Rectangle(
            height = p0r[1] - p0l[1],
            width = p0r[0] - p0l[0] - 1/2,
            fill_opacity = 0,
            stroke_width = 0,
            color = GRAY,
        ).move_to(ax.c2p((n+1)/2, 0), aligned_edge=DOWN)
        self.play(Create(area))

        def BackColor(l, r):
            nonlocal ax, data_max, area
            self.remove(area)
            pl = ax.c2p(l, 0) 
            pr = ax.c2p(r+2, data_max+2)  
            area = Rectangle(
                height = pr[1] - pl[1],
                width = pr[0] - pl[0] - 1/2,
                fill_opacity = 0.4,
                stroke_width = 0,
                color = GRAY,
            ).move_to(ax.c2p((l+r+2)/2, 0), aligned_edge=DOWN)
            self.play(Create(area))

    # ---------------------------
    # iとjのデータと棒をswapする関数
    # ---------------------------
        def swap(a, i, j, idx):
            nonlocal current_bars
            if(a[i]==a[j]):
                return -1
            # データの入れ替え
            a[i], a[j] = a[j], a[i]
            # 棒の入れ替え
            p1 = ax.c2p(i+1, 0)
            p2 = ax.c2p(j+1, 0)
            self.play(
                current_bars[i].animate.move_to(p2, aligned_edge=DOWN),
                current_bars[j].animate.move_to(p1, aligned_edge=DOWN),
                run_time=0.4
            )
            self.wait(0.2)
            current_bars[i], current_bars[j] = current_bars[j], current_bars[i]
            if(idx == i):
                return j
            elif(idx == j):
                return i
            else:
                return -1

    # ------------
    # クイックソート (右端ピボット)
    # ------------
        data = Data.copy()
        current_bars = list(bars)
        
        def quick_sort(data, left, right):
            nonlocal ax
            if(right <= left):
                return 
            
            BackColor(left, right)
            
            # ピボットを右端に固定
            pivot_index = right
            x = data[pivot_index]
            self.play(current_bars[pivot_index].animate.set_fill(RED), run_time=0.2)
            
            # iとjを交差するまで移動，条件をみたすときswap
            i = left - 1
            for j in range(left, right):
                if data[j] <= x:
                    i = i + 1
                    ok = swap(data, i, j, pivot_index)
                    if(ok != -1):
                        pivot_index = ok
            
            # ピボットと中央の入れ替え
            ok = swap(data, i + 1, right, pivot_index)
            if(ok != -1):
                pivot_index = ok
                
            self.play(current_bars[pivot_index].animate.set_fill(WHITE), run_time=0.2)
            
            # 再帰
            quick_sort(data, left, pivot_index - 1)
            quick_sort(data, pivot_index + 1, right) 
        
    # -----
    # 実行
    # -----    
        quick_sort(data, 0, n-1)