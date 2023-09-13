from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 16)
        self.cell(40, 10, "CS50 Shirtificate", align="C")
        self.ln(20)


def main():
    print(create(input("Name: ")))


def create(s):
    pdf = PDF(orientation="portrait", format="A4")
    pdf.add_page()

    pdf.image("shirtificate.png", 10, 70, 190)

    pdf.set_text_color(186, 254, 255)
    pdf.cell(0, 213, f"{s} took CS50", align="C")

    pdf.output("shirtificate.pdf")

main()
