@echo off
setlocal

rem カレントディレクトリをこの .bat ファイルの場所にする
cd /d %~dp0

rem 初回起動時に venv 環境を作成
if not exist venv (
  python -m venv venv
)

rem venv を有効化
call .\venv\Scripts\activate.bat

rem 依存パッケージがインストール済みかチェック
python -m pip list | findstr -i Pillow > nul

rem 依存パッケージがインストール済みじゃなかったら入れる
if "%ERRORLEVEL%" neq "0" (
  python -m pip install -r requirements.txt
)

REM バッチファイルの引数から画像ファイルパスを取得
set "image_path=%~1"

REM 画像ファイルの拡張子を.txtに変更
set "output_file=%~dpn1.txt"

REM 既に同名の.txtファイルが存在するかチェック
if exist "%output_file%" (
    echo .txt file already exists. Operation canceled.
) else (
    REM Pythonスクリプトを実行してパラメータを取得し、.txtファイルに書き込む
    python read_prompt.py "%image_path%" > "%output_file%"
    echo Parameters extracted and saved to %output_file%
)
