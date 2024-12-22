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

        pix = page.get_pixmap(matrix=fitz.Matrix(4, 4))  # 进一步提升分辨率

        img = fitz.Pixmap(fitz.csRGB, pix)
        img.invert_irect(img.irect)

        page.insert_image(page.rect, pixmap=img)

    doc.save(output_pdf)

