from PIL import Image
import os

img_dir = "images/"
pdf_name = "pdf/image.pdf"

# ディレクトリ内のすべての.pngファイルを取得
images = [i for i in os.listdir(img_dir) if i.endswith(".png")]

# 画像をPIL Imageオブジェクトとして読み込む
image_objs = [Image.open(os.path.join(img_dir, i)).convert('RGB') for i in images]

# 最初の画像を保存し、その後の画像を追加する
image_objs[0].save(pdf_name, "PDF" ,resolution=100.0, save_all=True, append_images=image_objs[1:])