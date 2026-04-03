from reportlab.platypus import SimpleDocTemplate, Table
import os

def create_report(data):
    path = "/storage/emulated/0/SHDA_Reports/"
    os.makedirs(path, exist_ok=True)

    doc = SimpleDocTemplate(path + "report.pdf")
    table = Table(data)
    doc.build([table])