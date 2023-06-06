from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
# setting pages not to be broken automatically
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    # --------SETTING A HEADER --------
    # setting a font
    pdf.set_font(family="Times", style="B", size=24)
    # adding rgb values for the gray color
    pdf.set_text_color(100, 100, 100)
    # adding a text through cells
    pdf.cell(w=0, h=12, txt=row["Topic"],
             align="L", ln=1)
    # coordinates as the arguments
    pdf.line(10, 22, 200, 22)

    # --------SETTING A fOOTER --------
    pdf.ln(260)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    # creating pages (nested for-loop)
    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # set the Footer for other pages
        pdf.ln(272)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")