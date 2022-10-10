import frappe
# import os
# import subprocess, sys
# import tempfile
from frappe.model.document import Document
# from PyPDF2 import PdfFileWriter, PdfFileReader
# import io
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter
# from frappe import _
# from frappe.core.doctype.access_log.access_log import make_access_log
# from frappe.utils.pdf import get_pdf
# from frappe.www.printview import validate_print_permission
# import requests

# def api_test(doc, method=None):
#     response = requests.get("http://192.168.1.38:8000/files/item_print_test.pdf")
#     return response.content
@frappe.whitelist()
def get_printer_status():

	frappe.response['message']={
		'data':'printer_status'
	}