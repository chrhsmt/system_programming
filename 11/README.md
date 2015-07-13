# 第十一回
## PythonでのOS・システム関連のAPI
### OS・システム関連のAPI
* sys
* os
* コマンド実行
  * os.system('command')
  * os.exec*
    * l -> コマンドライン引数を列挙
    * v -> コマンドライン引数をリスト型で渡す
    * p -> 環境変数PATHを利用
    * e -> 環境変数を辞書型で渡す
    * コマンドを置換する
  * os.fork()
    * フォーク
  * os.spawn*
    * fork & exec
  * pipe
  * popen, popen2 -> 推奨されていない
  * commands -> これも推奨されていない
  * subprocess パッケージ
* ディレクトリ
  * listdir
  * glob
  * os.path.* -> パス名の操作
  * os.stat
* アカウント
  * pwd
  * grp
* 時間関係
  * datetime
  * time

## 積み残しの件
### 組み込み関数
* dir
* type
### import
* import ".pyを取った名前"
* ファイルの探索順
* from math import * -> 名前空間が汚れる....
* as 別名
  * import math as m
* ディレクトリを作る場合は、 __init__.pyを作る
### with
* with open(...) as f
  * 暗黙的にcloseが呼び出される
### class
* コンストラクタは __init__(self)
* 多重継承ができる
### __name__
* Pythonから直接スクリプトとして呼び出されると、 __name__ は __main__となる
* パッケージとしてimportされると、.pyを取った名前になる
### 予約後
* assert
* finally
* is
* yeild
* None
* nonlocal
* exec
### Pythonのバージョン
* python3への移行は進んでいない

## 開発環境の構築
### パッケージ管理
* site-packages
  * setup.py
  * packaging
* easy_instakk, pip
### 仮想環境
* virtualenv




