# Stable Diffusion EZTweak tools

Stable Diffusion向けの、かゆいところに手が届くツール

EZ: 簡単
Tweak: 微調整

## 要件

* Pillow

## インストール

プロジェクト ディレクトリに移動し、モジュールをインストールします。

```
python -m pip install -r requirements.txt
```

## copy_prompt.py

`copy_prompt.py`は、指定したフォルダ内の画像ファイルからStable Diffusionのプロンプト情報を読み込み、別フォルダの画像ファイルにプロンプト情報のコピーを行うツールです。

画像をペイントソフトで修正するとプロンプトが無くなったりもします。
AI画像の投稿サイト等で投稿すると使用したプロンプトを自動で抽出してくれる機能がありますが、
その際にプロンプト無しになってしまいます。

よって元となった画像のプロンプトをファイルに記録したい場合を想定しています。

### 使い方

```
python copy_prompt.py (from_folder) (to_folder)
```

(from_folder): コピー元のフォルダへのパス

(to_folder): コピー先のフォルダへのパス

コマンドライン引数として、コピー元のフォルダとコピー先のフォルダを指定してください。

ユーザーに確認を求め、承認された場合、コピーを行います。

## move_file_model.py

`move_file_model.py`は、指定したフォルダ内の画像ファイルからStable Diffusionのプロンプト情報を読み込み、モデル名を抽出して対応するサブフォルダに移動するツールです。

モデルはデフォルトだとハッシュ値で出力されるので、名称として出力したい場合はStable Diffusion(AUTOMATIC1111)の設定を変更してください。

### 使い方

```
python move_file_model.py (folder_path)
```

(folder_path): 処理対象のフォルダへのパス

コマンドライン引数として、処理対象のフォルダを指定してください。

## 貢献する

Stable Diffusion EZTweak tools に貢献したい場合は、問題を開いてアイデアを議論するか、プル リクエストを送信してください。

## 作者

ナツキソ

- Twitter: [@natukin1978iai](https://twitter.com/natukin1978iai)
- Mastodon: [@natukin1978iai@pawoo.net](https://pawoo.net/web/accounts/2199670)
- GitHub: [@natukin1978](https://github.com/natukin1978)
- Mail: natukin1978iai@gmail.com

## ライセンス

Stable Diffusion EZTweak tools は [MIT License](https://opensource.org/licenses/MIT) の下でリリースされました。
