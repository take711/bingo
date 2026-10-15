#!/bin/bash

# mambaを初期化
mamba init -q

# Pythonを最新にアップデート
mamba update python -qy

# 全パッケージのアップデート
mamba update -qy --all

# キャッシュ等を削除
mamba clean -qafy
