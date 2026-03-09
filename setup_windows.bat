@echo off
chcp 65001 >nul
echo ========================================
echo   PSAG2 题库生成器 - Windows 安装脚本
echo ========================================
echo.

:: 检查Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 未检测到Python，请先从 https://www.python.org 下载安装
    echo [提示] 安装时勾选 "Add Python to PATH"
    pause
    exit /b 1
)

echo [1/4] 正在检查并升级pip...
python -m pip install --upgrade pip

echo.
echo [2/4] 正在创建虚拟环境...
if exist venv (
    echo   虚拟环境已存在，跳过创建
) else (
    python -m venv venv
)

echo.
echo [3/4] 正在安装依赖...
call venv\Scripts\pip.exe install -r requirements.txt

echo.
echo [4/4] 安装完成！
echo.
echo ===== 使用方法 =====
echo 双击运行 main.py 或使用:
echo   venv\Scripts\python.exe main.py
echo.
echo 打包为exe:
echo   venv\Scripts\pyinstaller.exe main.spec
echo.
pause