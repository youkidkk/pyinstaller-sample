# pyinstaller-sample

pyinstaller のサンプル。

## パッケージのインストール

```shell
pipenv install
pipenv install --dev
```

## ビルド

```shell
pipenv run pyinstaller src/pyinstaller_sample.py --onefile --clean
# -> dist 配下にexeファイルが作成される
```

## exe ファイルの実行

以下のフォルダ、ファイル構成で配置し、exe ファイルを実行

- pyinstaller_sample.exe
- configs
  - log_conf.yml
- logs
