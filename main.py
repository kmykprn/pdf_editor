from PIL import Image
import pytesseract

# 画像ファイルの読み込み
image = Image.open("image.png")

# デフォルト設定でOCR実行
text = pytesseract.image_to_string(image)

# 結果の出力
print("認識テキスト:", text)