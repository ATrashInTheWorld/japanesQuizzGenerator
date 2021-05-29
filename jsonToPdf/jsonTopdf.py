#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import json
from fpdf import FPDF
import os

def pdfDoc(ele_type ,elements):
    running_path = os.path.abspath(os.path.dirname(sys.argv[0]))
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.add_font('fireflysung', '', running_path+"/fireflysung.ttf", uni=True)
    pdf.set_font('fireflysung', '', 13)

    count = 0
    for element in elements:
        if count%2 ==0 and count != 0:
            if ele_type == "words":
                pdf.multi_cell(100,18, "", align='C', ln=1)
            elif ele_type == "kanjis":
                pdf.multi_cell(100,25, "", align='C', ln=1)
        pdf.multi_cell(100,5, element, align='L', ln=3)
        count +=1

    pdf.output(sys.argv[2], running_path)


def jsonData(file_path):
    x_elements = []
    data = json.load(open(file_path, encoding='utf8'))
    fileType = list(data.keys())[0]
    for element in data[fileType]:
        x_var = list(element.keys())[0]  # The actual word/kanji with kanji
        x_keys = list(element[x_var].keys())
        str_to_append = str(x_var)+"\n"
        for key in x_keys:
            if type(element[x_var][key]) == list:
                str_to_append+=key+": "+"".join(element[x_var][key])+"\n"
            else:
                str_to_append+=str(key+": "+element[x_var][key])+"\n"
        x_elements.append(str_to_append)
    return fileType, x_elements



def main():
    # [1] is the file path when called the script
    ################# [2] shall be output file path ##################
    file_type, elements = jsonData(sys.argv[1])
    pdfDoc(file_type, elements)
    # beta()


if __name__ == '__main__':
    main()