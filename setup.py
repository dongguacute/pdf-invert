from setuptools import setup, find_packages

setup(
    name="invert_pdf_colors",
    version="0.1",
    description="A Python library to invert PDF text and background colors.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "PyMuPDF",  # 依赖的库
    ],
    entry_points={
        'console_scripts': [
            'invert-pdf=invert_pdf_colors.invert:invert_pdf_colors',  # 添加命令行脚本
        ],
    },
)
