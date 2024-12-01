# PDF Maker using CSV
from fpdf import FPDF
import pandas as pd

# Read the CSV file
data = pd.read_csv('topics.csv')

pdf = FPDF(orientation='P', unit="mm", format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in data.iterrows():
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=24)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=12, txt=row["Topic"], ln=1, align='L')
    pdf.line(10, 21, 200, 21)
    pdf.line(10, 279, 200, 279)
    #Add page number
    pdf.ln(257)
    pdf.set_font(family = "Times", style="I", size=8)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(w=0, h=12, txt=f"Page: {pdf.page_no()}", ln=1, align='R')

    for i in range(row["Pages"]):
        pdf.add_page()
        # Set the footer for the inner page
        pdf.line(10, 279, 200, 279)
        pdf.ln(272)
        pdf.set_font(family = "Times", style="I", size=8)
        pdf.set_text_color(150, 150, 150)
        pdf.cell(w=0, h=4, txt=f"Page: {pdf.page_no()}", ln=1, align='R')
        pdf.cell(w=0, h=4, txt=f"{row['Topic']} Page:{i+1}", ln=1, align='R')

pdf.output('output.pdf')
