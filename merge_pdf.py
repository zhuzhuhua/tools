# -*- coding: UTF-8 -*-
from PyPDF2 import PdfFileMerger
merger = PdfFileMerger()
dirpath="/Users/zhuyun/Desktop/dew3/"
input1 = open(dirpath+"1.pdf", "rb")
input2 = open(dirpath+"2.pdf", "rb")
input3 = open(dirpath+"3.pdf", "rb")
input4 = open(dirpath+"4.pdf", "rb")
input5 = open(dirpath+"5.pdf", "rb")
input6 = open(dirpath+"6.pdf", "rb")
merger.append(input1)
merger.append(input2)
merger.append(input3)
merger.append(input4)
merger.append(input5)
merger.append(input6)
# Write to an output PDF document
output = open(dirpath+"达尔威3月份运维月报.pdf", "wb")
merger.write(output)