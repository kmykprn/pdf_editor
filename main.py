import gradio as gr
from writer import convert_uploaded_images_to_pdf


# Gradioインターフェース構築
demo = gr.Interface(
    fn=convert_uploaded_images_to_pdf,
    inputs=[
        gr.File(
            file_types=[".png", ".jpg", ".jpeg"],
            file_count="multiple",
            label="画像ファイルをアップロード"
        ),
    ],
    outputs=[
        gr.File(label="出力PDF")
    ],
    title="画像 → PDF 変換ツール",
    description="複数の画像をPDFに簡単にまとめられます。"
)


if __name__ == "__main__":
    demo.launch()