import numpy as np

from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat
from pylatex.utils import italic, NoEscape
import os

if __name__ == '__main__':
    image_filename_1 = os.path.join(os.path.dirname(__file__), '01-hujan-frontal.jpg')
    image_filename_2 = os.path.join(os.path.dirname(__file__), '02-orografis.jpg')
    image_filename_3 = os.path.join(os.path.dirname(__file__), '03-hujan-zenit.png')
    image_filename_4 = os.path.join(os.path.dirname(__file__), '04-hujan-tropis.jpg')
    image_filename_5 = os.path.join(os.path.dirname(__file__), '05-hujan siklonal.jpg')

    geometry_options = {"tmargin": "4cm", "lmargin": "4cm", "rmargin": "3cm", "bmargin": "3cm"}
    doc = Document(geometry_options=geometry_options, documentclass='article', document_options='a4paper')

    latex_document_1 = 'text1.tex'
    latex_document_2 = 'text2.tex'
    latex_document_3 = 'text3.tex'

    with open(latex_document_1) as file:
        tex1 = file.read()

    with open(latex_document_2) as file:
        tex2 = file.read()

    with open(latex_document_3) as file:
        tex3 = file.read()

    with doc.create(Section('Jenis Hujan di Indonesia')):
        doc.append(NoEscape(tex1))
        with doc.create(Subsection('Hujan Frontal')):
            doc.append(NoEscape(tex2))
            with doc.create(Figure(position='h!')) as frontal_img:
                frontal_img.add_image(image_filename_1, width='120px')
                frontal_img.add_caption('Skema Terjadinya Hujan Frontal')

        with doc.create(Subsection('Hujan Orografis')):
            doc.append(NoEscape(tex3))
            with doc.create(Figure(position='h!')) as frontal_img:
                frontal_img.add_image(image_filename_2, width='120px')
                frontal_img.add_caption('Skema Terjadinya Hujan Orografis')

    doc.generate_pdf('full', clean_tex=False)