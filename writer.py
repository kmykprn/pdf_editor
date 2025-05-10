from typing import List
from PIL import Image
import tempfile
import os


def get_all_img_abs_paths(img_dir_path: str):
    """
    ディレクトリ内の画像ファイルを取得する関数

    Args:
        img_dir_path: 画像が格納されているディレクトリ
    """
    img_abs_paths = [
        os.path.abspath(os.path.join(img_dir_path, path))
        for path in os.listdir(img_dir_path)
        if path.endswith(".png")
    ]
    return img_abs_paths


def convert_image_to_pdf(img_dir_path: str="images", pdf_name: str="output.pdf"):
    """
    画像をpdfに変換する関数

    Args:
        img_dir_path: 画像が格納されているディレクトリ
        pdf_name: 出力するpdfファイル名
    """

    # ディレクトリ内のすべての.pngファイルを取得(絶対パス)
    img_abs_paths = get_all_img_abs_paths(img_dir_path)

    # 画像をPIL Imageオブジェクトとして読み込む
    image_objs = [Image.open(path).convert('RGB') for path in img_abs_paths]

    # 最初の画像を保存し、その後の画像を追加する
    image_objs[0].save(pdf_name, "PDF" ,resolution=100.0, save_all=True, append_images=image_objs[1:])


def convert_uploaded_images_to_pdf(image_list: List[str]):
    """
    Gradioから受け取った画像のリストをPDFに変換

    Args:
        image_list: アップロードされた画像のパス名

    Returns:
        PDFファイルへのパス（一時ファイル）
    """
    try:
        if not image_list:
            return "画像が選択されていません", None

        # 画像をPIL Imageオブジェクトとして読み込む
        image_objs = [Image.open(path).convert('RGB') for path in image_list]

        # 一時ファイルを作成
        tmpfile = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)
        temp_pdf_path = tmpfile.name
        tmpfile.close()

        # pdfを一時ファイルに保存
        image_objs[0].save(temp_pdf_path, "PDF", resolution=100.0, save_all=True, append_images=image_objs[1:])

        return temp_pdf_path

    except Exception as e:
        print(e)


if __name__ == '__main__':

    img_dir_path = "images/"
    pdf_name = "pdf/image.pdf"
    convert_image_to_pdf(img_dir_path, pdf_name)
