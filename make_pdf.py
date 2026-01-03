import os
import img2pdf
import argparse

# デフォルト設定
DEFAULT_INPUT_DIR = "kindle_scan"
DEFAULT_OUTPUT_PDF = "kindle_book.pdf"

def main():
    parser = argparse.ArgumentParser(description="画像ファイルをPDFに変換します。")
    parser.add_argument("--input", "-i", default=DEFAULT_INPUT_DIR, help=f"画像が入っているフォルダ (デフォルト: {DEFAULT_INPUT_DIR})")
    parser.add_argument("--output", "-o", default=DEFAULT_OUTPUT_PDF, help=f"出力するPDFファイル名 (デフォルト: {DEFAULT_OUTPUT_PDF})")
    args = parser.parse_args()

    input_dir = args.input
    output_pdf = args.output

    # フォルダが存在しない場合のチェック（files/ 下なども探してみる）
    if not os.path.exists(input_dir):
        alt_path = os.path.join("files", input_dir)
        if os.path.exists(alt_path):
            input_dir = alt_path
        else:
            print(f"エラー: フォルダ '{input_dir}' が見つかりません。")
            return

    # 画像リストを取得してソート
    img_paths = [
        os.path.join(input_dir, f) 
        for f in sorted(os.listdir(input_dir)) 
        if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ]

    if not img_paths:
        print(f"エラー: {input_dir} フォルダに画像が見つかりません。")
        return

    print(f"'{input_dir}' から {len(img_paths)} 枚の画像を '{output_pdf}' に変換します...")

    # PDF作成
    try:
        with open(output_pdf, "wb") as f:
            f.write(img2pdf.convert(img_paths))
        print(f"完了しました！: {output_pdf}")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()