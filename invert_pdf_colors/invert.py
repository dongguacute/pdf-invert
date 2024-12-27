import fitz  # PyMuPDF
import os

def invert_pdf_colors(input_pdf, output_pdf):
    doc = fitz.open(input_pdf)

    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)

        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if block["type"] == 0:
                for line in block["lines"]:
                    for span in line["spans"]:
                        span["color"] = 0xFFFFFF if span["color"] == 0x000000 else 0x000000

        pix = page.get_pixmap(matrix=fitz.Matrix(8, 8),  # 将分辨率提高到8倍
                             alpha=False,  # 禁用alpha通道以提高清晰度
                             colorspace=fitz.csRGB)  # 使用RGB色彩空间

        img = fitz.Pixmap(fitz.csRGB, pix)
        img.invert_irect(img.irect)

        page.insert_image(page.rect, 
                         pixmap=img,
                         keep_proportion=True,  # 保持图像比例
                         overlay=True)  # 覆盖模式

    doc.save(output_pdf,
             garbage=4,  # 最高级别的垃圾收集
             deflate=True,  # 使用压缩
             clean=True)  # 清理未使用的元素

