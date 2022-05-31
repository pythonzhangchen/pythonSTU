# -*- coding: utf-8 -*-
# @Time : 2022/5/19 14:00 
# @Author : chen.zhang 
# @File : pdf.py
import PyPDF2
import os

pdfFiles = []
for filename in os.listdir('pdf'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

pdf_lst = [os.path.join(r'pdf', filename) for filename in pdfFiles]

print(pdf_lst)

pdfWrite = PyPDF2.PdfFileMerger()
for pdf in pdf_lst:
    pdfWrite.append(pdf)
pdfWrite.write(r'merge.pdf')


