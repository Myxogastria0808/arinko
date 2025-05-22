# arinko

画像中の蟻の数をカウントする。ただそれだけ。

## 使い方

### 0. 依存packageのinstall

> [!IMPORTANT]
> `python3.12`と`pip`がinstallされている必要があります。

```sh
pip install -r requirements.txt
```

### 1. `data/normal/inputs/`配下と`data/red/inputs/`配下にそれぞれ画像を設置

- `data/normal/inputs/` ... 通常の照明の画像
- `data/red/inputs/` ... 赤い照明の画像

### 2. カウントの実行

#### 通常の照明の画像の蟻のカウント

```sh
python3 ./src/main.py -n
```

or

```sh
python3 ./src/main.py --normal
```

#### 赤い照明の画像の蟻のカウント

```sh
python3 ./src/main.py -r
```

or

```sh
python3 ./src/main.py --red
```

### 3. 結果の画像とcsvが出力される

- `data/normal/result/` ... 通常の照明の処理後の画像
- `data/normal/result/divide/` ... 通常の照明の処理後の分割された画像
- `data/normal/result/csv/` ... 通常の照明のカウント結果のcsv
- `data/red/result/` ... 赤い照明の処理後の画像
- `data/red/result/divide/` ... 赤い照明の処理後の分割された画像
- `data/red/result/csv/` ... 赤い照明のカウント結果のcsv
