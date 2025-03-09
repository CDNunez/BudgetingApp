import os

from dotenv import load_dotenv
from pdfreader import *

load_dotenv()

PDF = os.getenv('PDF')
PDF_two = os.getenv('PDF_two')

# step 1
#Main function to run program once PDF file is dropped into application
def main_parse_function(pdf_file_path):
    # call extract func passing through  PDF file path to the func
    extract_pdf_text(pdf_file_path)

main_parse_function(PDF_two)