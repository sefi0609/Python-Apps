from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path

filepaths = glob.glob('Invoices/*.xlsx')

for filepath in filepaths:
    pdf = FPDF(orientation='p', unit='mm', format='a4')

    # get invoice number and date from file name
    filename = Path(filepath).stem
    invoice_number, date = filename.split('-')

    pdf.add_page()

    # add titles
    pdf.set_font('Times', 'B', 18)
    pdf.cell(0, 10, f'Invoice num.{invoice_number}', ln=1)
    pdf.cell(0, 10, f'Date {date}', ln=1)

    df = pd.read_excel(filepath, sheet_name='Sheet 1')
    columns = df.columns
    columns = [column.replace('_', ' ').title() for column in columns]

    # build table header
    pdf.ln(10)
    pdf.set_font('Times', 'B', 10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=68, h=8, txt=columns[1], border=1)
    pdf.cell(w=32, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

    # build table body
    pdf.set_font('Times', size=10)
    pdf.set_text_color(80, 80, 80)
    for index, row in df.iterrows():
        pdf.cell(w=30, h=8, txt=str(row['product_id']), border=1)
        pdf.cell(w=68, h=8, txt=str(row['product_name']), border=1)
        pdf.cell(w=32, h=8, txt=str(row['amount_purchased']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['price_per_unit']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['total_price']), border=1, ln=1)

    total_sum = df['total_price'].sum()

    # build total amount row
    pdf.cell(w=30, h=8, txt='', border=1)
    pdf.cell(w=68, h=8, txt='', border=1)
    pdf.cell(w=32, h=8, txt='', border=1)
    pdf.cell(w=30, h=8, txt='', border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

    # add total amount and company name and logo
    pdf.ln(10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 8, f'The total due amount is {total_sum} Euros', ln=1)
    pdf.cell(35, 8, f'The Best Company')
    pdf.image('company_logo.png', w=7)

    pdf.output(f'PDFs/{filename}.pdf')
