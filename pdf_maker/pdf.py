from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


def create_pdf():
    filename = input("Enter PDF file name: ").strip()

    if not filename:
        print("Invalid file name.")
        return

    if not filename.endswith(".pdf"):
        filename += ".pdf"

    title = input("Enter PDF title: ")
    text = input("Enter your text: ")

    pdf = canvas.Canvas(filename, pagesize=A4)

    width, height = A4

    # Title
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawCentredString(width / 2, height - 70, title)

    # Content
    pdf.setFont("Helvetica", 12)

    y = height - 110

    # Split text into lines
    lines = text.split("\n")

    for line in lines:
        pdf.drawString(60, y, line)
        y -= 20

        # Create a new page if needed
        if y < 50:
            pdf.showPage()
            pdf.setFont("Helvetica", 12)
            y = height - 50

    pdf.save()

    print(f"\nPDF created successfully: {filename}")


create_pdf()
