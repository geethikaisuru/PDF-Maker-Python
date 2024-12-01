# PDF Maker using CSV
from fpdf import FPDF
import pandas as pd

# Read the CSV file
data = pd.read_csv('topics.csv')

pdf = FPDF(orientation='P', unit="mm", format='A4')

for index, row in data.iterrows():
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(w=0, h=12, txt=row["Topic"], ln=1, align='L')
    pdf.line(10, 20, 200, 21)

pdf.output('output.pdf')
