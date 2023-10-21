import pandas as pd
from fpdf import FPDF

df = pd.read_csv('topics.csv')

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)


# length of A4 page is 210
def create_multiple_lines():
    for i in range(20, 290, 10):
        pdf.line(10, i, 210 - 10, i)
        

for index, line in df.iterrows():
    pdf.add_page()

    # header
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=line['Topic'], border=0, ln=1, align='L')
    
    create_multiple_lines()

    # footer
    pdf.ln(264)
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(0, 8, line['Topic'], align='R')

    for page in range(line['Pages'] - 1):
        pdf.add_page()

        create_multiple_lines()
        
        # footer
        pdf.ln(276)
        pdf.cell(0, 8, line['Topic'], align='R')

pdf.output('output.pdf')
