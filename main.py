from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    # setting a font
    pdf.set_font(family="Times", style="B", size=24)
    # adding rgb values for the gray color
    pdf.set_text_color(100, 100, 100)
    # adding a text through cells
    pdf.cell(w=0, h=12, txt=row["Topic"],
             align="L", ln=1)
    # coordinates as the arguments
    pdf.line(10, 22, 200, 22)

    # creating pages (nested for-loop)
    for i in range(row["Pages"] - 1):
        pdf.add_page()


pdf.output("output.pdf")