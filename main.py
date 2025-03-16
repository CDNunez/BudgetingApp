import os

from dotenv import load_dotenv
from pdfreader import *

import tkinter as tk
from tkinter.filedialog import askopenfilename

load_dotenv()

PDF = os.getenv('PDF')
PDF_two = os.getenv('PDF_two')

# step 1
#Main function to run program once PDF file is dropped into application
def main_parse_function():
    filename = askopenfilename()
    # call extract func passing through  PDF file path to the func
    extract_pdf_text(filename)

main_parse_function()