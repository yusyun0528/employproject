# 遺伝的アルゴリズムによるシフトメイカー
 
 
# 特徴
 
Pythonのライブラリの一つであるdeapの遺伝的アルゴリズムを使用したウェブアプリです。 [deap](https://github.com/DEAP/deap/blob/master/examples/ga/onemax.py)

また、[こちら](https://github.com/shouta-dev/nurse-scheduling-ga/blob/master/nurse_scheduling_by_ga.py)のソースコードも参考にさせて頂きました。
 
```python
import deap
```
[deap](https://github.com/DEAP/deap/blob/master/examples/ga/onemax.py)は遺伝的アルゴリズムだけでなく他にも様々な進化的計算のアルゴリズムが実装されているようです。
 
 
# 使用したライブラリやパッケージ
 
* Python 3.8.5
* django 3.1.3
* deap
* pandas
 
これに加え、デザインにBootstrapを使用しました。  環境はWindows上で[Ubuntu20.04.1](https://www.ubuntulinux.jp/)を使用したLinuxOsです。  
ファイル管理にAWSのS3を使用しています。
 

# インストール
 
各パッケージは pip コマンドでインストールしました.
 
```bash
pip3 install django
pip3 install deap
pip3 install pandas
```
 
# アプリの使用
 

[こちら](https://employproject.herokuapp.com/home/)からデプロイしたアプリを使用できます。(動画冒頭のホーム画面に遷移します。)
サンプルアカウントは以下のものを使用してください。(10人程度の従業員情報を追加済みのアカウントです。)
***
ユーザー名：root  
パスワード：abc


 
# ノート
 
* 上記の開発環境以外ではテストしていません。


# 作成者
 
* 鈴木　悠春
* 小樽商科大学2年
 

ありがとうございました！

