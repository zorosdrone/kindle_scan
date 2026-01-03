# kindle_scan

Kindle Cloud Reader のページを自動でスクリーンショット撮影し、PDFに変換するためのツールセットです。

## 構成

- `kindle_scan.py`: Kindle Cloud Reader を操作して各ページをスクリーンショット（PNG）として保存します。
- `make_pdf.py`: 保存された画像群を一つの PDF ファイルにまとめます。

## 必要条件

- Python 3.x
- Google Chrome
- ChromeDriver (Selenium経由で自動取得されますが、Chrome本体が必要です)

## インストール

必要なライブラリをインストールします。

```bash
pip install selenium img2pdf
```

## 使い方

### 1. ページのキャプチャ (`kindle_scan.py`)

1. `kindle_scan.py` を実行します。
   ```bash
   python kindle_scan.py --pages 100 --output my_book_images --direction right
   ```
   - `--pages`, `-p`: 撮影するページ数 (デフォルト: 100)
   - `--output`, `-o`: 保存先ディレクトリ (デフォルト: `kindle_scan`)
   - `--delay`, `-d`: ページめくり後の待機時間(秒) (デフォルト: 2.0)
   - `--direction`: ページめくり方向 (`right`: 横書き/左開き, `left`: 縦書き/右開き)

2. 自動で Chrome が起動し、Kindle Cloud Reader のログイン画面が開きます。
3. **手動でログイン**し、スキャンしたい本を開いてください。
4. 最初のページを表示し、準備ができたらコンソールで `Enter` キーを押します。
5. 指定したページ数分、自動でページめくりとスクリーンショットが行われます。
   - デフォルトでは `kindle_scan/` フォルダに保存されます。
   - ページ数や保存先はスクリプト内の `TOTAL_PAGES` や `OUTPUT_DIR` で調整可能です。

### 2. PDFへの変換 (`make_pdf.py`)

1. `make_pdf.py` を実行します。
   ```bash
   python make_pdf.py --input my_book_images --output my_book.pdf
   ```
   - `--input`, `-i`: 画像が入っているフォルダ (デフォルト: `kindle_scan`)
   - `--output`, `-o`: 出力するPDFファイル名 (デフォルト: `kindle_book.pdf`)

2. 指定したフォルダ内の画像が結合され、PDF が作成されます。
   - デフォルトでは `kindle_book.pdf` という名前で出力されます。

## 注意事項

- **利用規約**: Amazon Kindle Cloud Reader の利用規約では、自動化ツールによるアクセスやコンテンツの複製が禁止されている場合があります。本ツールの使用は自己責任で行ってください。
- **描画待ち**: ネットワーク環境やPCのスペックにより、ページの読み込みが間に合わない場合があります。その場合は `kindle_scan.py` 内の `time.sleep(2.0)` の値を大きく調整してください。
- **ページめくり方向**: 横書き（左開き）と縦書き（右開き）で送るキーが異なります。スクリプト内の `Keys.ARROW_RIGHT` または `Keys.ARROW_LEFT` を適宜切り替えてください。

## 免責事項

本ツールを使用したことによるアカウントの停止やその他のトラブルについて、作者は一切の責任を負いません。
