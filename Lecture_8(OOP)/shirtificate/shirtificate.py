from fpdf import FPDF

def main():
    # Asking user for name
    name = input("Name: ")
    message = f"{name.title()} took CS50"

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    
    # title
    pdf.set_font('Helvetica', style='B', size=40)
    pdf.cell(w=0, h=30, text="CS50 Shirtificate", align="C")

    # Adding shirt image
    pdf.image("shirtificate.png", x=15, y=40, w=180)

    # Adding user's name
    pdf.set_font("helvetica","B", 20)
    pdf.set_text_color(255, 255, 255)
    pdf.text(x=65, y=110, text=message)

    # Saving
    pdf.output("shirtificate.pdf")
    

if __name__ == "__main__":
    main()