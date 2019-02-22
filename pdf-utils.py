'''
Class that contains common functions to manipulate PDF's files
Methods:
    Merge - merges all pdf files in a directory into a single file
    Split - TODO

Dependencies: PyPDF2
'''

# imports
from PyPDF2 import PdfFileMerger
import os

class PDFUtils:
    def merge(self, file_name_output, src, dst=None):
        '''
        Description: Merge multiple PDF from a source directory to a destination directory
        Parameters:
            file_name_output - Name of the output file, must contain PDF extension(Ex: Filename.pdf)
            src - Source Folder
            dst - Destination folder, if source parameter is not passed, source folder will be used
        '''
        merger = PdfFileMerger()  # Initialize PyPDF2 Merger
        # Navigates directory and list all the files found
        for filename in os.listdir(src):
            if filename.endswith(".pdf"):  # Checks for the PDF extension
                file = os.path.join(src, filename)  # joins the filename to the src path
                merger.append(open(file, 'rb'))

        # Depending if the dst parameter is passed, pdf is written to the src or dst folder
        if dst:
            # Check if dst directory exist, if not creates a new directory
            try:
                os.makedirs(dst)
            except FileExistsError:
                # directory already exists
                pass
            finally:
                # set destination folder as the output folder
                file_output = os.path.join(dst, file_name_output)

        else:
            # sets the source folder as the output folder
            file_output = os.path.join(src, file_name_output)

        with open(file_output, 'wb') as fileout:
            merger.write(fileout)  # Writes pdf with the file_name_output passed
