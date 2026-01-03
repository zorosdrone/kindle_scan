import time
import os
import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def main():
    parser = argparse.ArgumentParser(description="Kindle Cloud Reader からスクリーンショットを撮影します。")
    parser.add_argument("--output", "-o", default="kindle_scan", help="保存先ディレクトリ (デフォルト: kindle_scan)")
    parser.add_argument("--pages", "-p", type=int, default=100, help="撮影するページ数 (デフォルト: 100)")
    parser.add_argument("--delay", "-d", type=float, default=2.0, help="ページめくり後の待機時間(秒) (デフォルト: 2.0)")
    parser.add_argument("--direction", choices=["left", "right"], default="right", help="ページめくり方向: left(縦書き/右開き), right(横書き/左開き) (デフォルト: right)")
    args = parser.parse_args()

    output_dir = args.output
    total_pages = args.pages
    delay = args.delay
    key = Keys.ARROW_LEFT if args.direction == "left" else Keys.ARROW_RIGHT

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Chromeの起動オプション
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    # ブラウザ起動
    driver = webdriver.Chrome(options=options)

    try:
        # 1. Kindle Cloud Readerにアクセス
        driver.get("https://read.amazon.co.jp/")
        
        print("=== 手動操作フェーズ ===")
        print("1. ブラウザでAmazonにログインしてください")
        print("2. スキャンしたい本を開いてください")
        print("3. 開始したいページを表示し、ウィンドウサイズやマウスカーソルを調整してください")
        input("準備ができたら、このコンソールでEnterキーを押してください...")
        
        driver.switch_to.window(driver.window_handles[-1])
        print(f"現在の対象ページ: {driver.title}")

        body = driver.find_element(By.TAG_NAME, "body")

        for i in range(total_pages):
            filename = os.path.join(output_dir, f"page_{i:04d}.png")
            driver.save_screenshot(filename)
            print(f"Saved ({i+1}/{total_pages}): {filename}")
            
            body.send_keys(key) 
            time.sleep(delay) 

        print("完了しました")

    except Exception as e:
        print(f"エラー発生: {e}")

    finally:
        print("ブラウザを閉じますか？ (y/n)")
        if input().lower() == 'y':
            driver.quit()

if __name__ == "__main__":
    main()