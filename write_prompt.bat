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

REM バッチファイルの引数から画像ファイル名を取得
set "image_file=%~1"
set "txt_file=%~dpn1.txt"

REM .txtファイルの存在を確認
if not exist "%txt_file%" (
    echo .txt file not found. Operation canceled.
    exit /b 1
)

REM .txtファイルの内容を標準入力に供給
python write_prompt.py "%image_file%" "%txt_file%"

pause
