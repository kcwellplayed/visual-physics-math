# visual-physics-math
YouTubeチャンネル「目で見る物理・数学」の動画制作に使用した，数値シミュレーションおよびManimアニメーションのソースコード集です．

---

## コンテンツ一覧

興味のあるテーマのフォルダをクリックすると，数理的な背景とソースコードをご覧いただけます．

### 1. [ニュートン法による近似解の求め方（`newton-method/`）](./newton-method/)
方程式の解を，近似的に求めるアルゴリズムの一つである「ニュートン法」の幾何的な意味を，アニメーションを用いて解説します．  
([動画はこちら](https://youtube.com/shorts/KYvabxt-I2s?si=hFvHEmnMLT0SffIn))


### 2. [Kapitzaの振り子(`kapitza-pendulum/`)](./kapitza-pendulum/)
振り子は最上部に不安定な平衡点をもちます．しかし，ある操作をするだけでこの点を安定化し，振り子を立たせることができます．  
安定化する方法とその理由について，アニメーションを用いて解説します．  
([動画はこちら](https://youtube.com/shorts/2gwCVb6JM9Y?si=boI_iPTyTmN4RKiM))


### 3. [振り子の等時性の破れ（`pendulum-period/`）](./pendulum-period/)
ガリレオが発見したとされる振り子の等時性が，厳密には成立しないことをアニメーションで確認します．  
([動画はこちら](https://youtube.com/shorts/xsiBWq917Lw?si=k-U7v8xneDxCXlxo))


### 4. [エネルギー保存則を維持する差分化（`energy-preserving-discretization/`）](./energy-preserving-discretization/)
汎用的な差分化手法であるオイラー法では，もとの微分方程式のもつ性質が失われることを，単振動を例に挙げて視覚的に解説します．   
また微分方程式に応じて，性質を維持するような差分化手法を設計できることを解説しています．  
([動画はこちら](https://youtube.com/shorts/HkTlT67olfg?si=vOHsdeTIGh90HjuG))

### 5. [高速なソートアルゴリズム('quick-sort/')](./quick-sort/)
データを昇順，または降順に並び替えるアルゴリズムというものがあります．  
プログラミング初学時によく扱われる「バブルソート」は実装は簡単ですが，データ数が多いと計算時間が膨大になってしまいます．  
ここではデータ数が多くても比較的高速に計算できる「クイックソート」について，アニメーションで解説します．  
([動画はこちら](https://youtube.com/shorts/8swTbxbzhc0?si=NIz2I4CL7dKJ2RKt))




---

## 開発環境・必要なライブラリ

本リポジトリのコードではmanimライブラリを使用しています．使い方等は[こちら](https://www.manim.community/)を参照してください．

---

## 著作権・ライセンス

このリポジトリのコードは **MIT License** のもとで公開しています。
個人の学習や研究の参考など、自由にご活用ください。
