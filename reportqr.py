import time, os, pyqrcode, png, csv, sys
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Flowable, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from pyqrcode import QRCode

print(sys.argv)

current_dir = os.getcwd()
report_file_dir = current_dir + "/static/"
barcode_dir = current_dir + "/barcodes/"

person_row_data = []

# this class exists solely for the long line across the bottom!!!
class MCLine(Flowable):

    def __init__(self, width, height=0):
        Flowable.__init__(self)
        self.width = width
        self.height = height

    def __repr__(self):
        return "Line(w=%s)" % self.width

    def draw(self):
        self.canv.line(0, self.height, self.width, self.height)

data= [
['Incorrect Asset Tag ',       '[    ]',                   '  ', 'Missing Charger',    '[    ]'],
['  '],
['Incorrect Asset Tag Number:', '_________________________', '  ', 'Missing Chromebook', '[    ]'],
]
t=Table(data)

def make_pdf(name,email,asset,advisor):
    person = [name,email,asset,advisor]
    if "’" in person[0]:
        person[0] = person[0].replace("’","'")
    try:
        index3 = person[3]
    except:
        index3 = "MYSchool"
    student_name = person[0]
    # removes the @domain from email
    student_email = person[1].split("@")[0]
    student_asset = person[2]
    student_dept = index3

    qr_filename = barcode_dir + str(student_dept) + "-" + student_email + "-" + student_asset + ".png"
    qr = pyqrcode.create(student_name + "," + student_email + "," + student_asset + "," + student_dept)
    qr.png(qr_filename, scale=6)
    pdf_file_name = report_file_dir + student_asset + ".pdf"
    doc = SimpleDocTemplate(pdf_file_name ,pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=52,bottomMargin=18)
    # Builds the story
    story=[]

    logo = qr_filename
    im = Image(logo, 2*inch, 2*inch)

    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    headline_style = styles['Heading1']
    headline_style.alignment = 1
    headline_style.fontSize = 18

    subhead_style = styles["Heading2"]
    subhead_style.alignment = 0
    subhead_style.fontSize = 18

    story.append(Paragraph("MY School Chromebook Return", headline_style))
    story.append(im)
    story.append(Paragraph(student_name, subhead_style))
    story.append(Paragraph(student_email + "@myschool.org", subhead_style))
    story.append(Paragraph(student_asset, subhead_style))
    story.append(Spacer(1, 12))
    ptext = 'Dear %s:' % student_name
    story.append(Paragraph(ptext, styles["Normal"]))
    story.append(Spacer(1, 12))
    ptext = 'According to our records, you have been assigned a Chromebook with the asset number: %s.' % student_asset
    story.append(Paragraph(ptext, styles["Justify"]))
    story.append(Spacer(1, 12))

    ptext = 'You will need to bring this document, along with your Chrombook and charger, on the day of return.\
    This document is needed in order to accurately check your Chromebook back into our system, and will act as your receipt of the returned Chromebook. '
    story.append(Paragraph(ptext, styles["Justify"]))
    story.append(Spacer(1, 12))

    ptext = 'If you are missing your charger or Chromebook, please indicate that in the fields provided below.\
    If the Chromebook we have listed does not match the asset number on the Chromebook you currently have, provide the asset number of the one currently in your possession.'
    story.append(Paragraph(ptext, styles["Justify"]))
    story.append(Spacer(1, 12))

    ptext = 'Please note: You will still receive credit for returning a Chromebook even if the one you have is\
    not the same as the one we have on record. However, you are encouraged to turn in the correct one, or work with your teacher to resolve the discrepancy.'
    story.append(Paragraph(ptext, styles["Justify"]))
    story.append(Spacer(1, 12))

    ptext = 'Returning your MYSchool device is important. Failure to return your device will prevent you from\
    attending Graduation/Promotion and other end-of-year functions. Also, you and your family will be billed for a replacement Chromebook (at a price of $350) if it is not returned prior to the last day of school.'
    story.append(Paragraph(ptext, styles["Justify"]))
    story.append(Spacer(1, 12))

    ptext = 'Thank you for your understanding, and enjoy your summer!'
    story.append(Paragraph(ptext, styles["Justify"]))
    story.append(Spacer(1, 12))
    ptext = 'Sincerely,'
    story.append(Paragraph(ptext, styles["Normal"]))
    story.append(Spacer(1, 18))
    ptext = 'MYSchool IT Team'
    story.append(Paragraph(ptext, styles["Normal"]))
    story.append(Spacer(1, 12))
    line = MCLine(455)
    story.append(line)
    story.append(Spacer(1, 26))
    story.append(t)

    doc.build(story)
