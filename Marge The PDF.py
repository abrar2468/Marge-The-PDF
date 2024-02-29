import PyPDF2

# Define input and output file paths
input_files = ["abir1.pdf", "Assessment_cst_2.pdf"]
output_file = "Abir.pdf"

# Create a PdfMerger object
merger = PyPDF2.PdfMerger()

# Loop through input files and add them to the merger
for filename in input_files:
    with open(filename, 'rb') as pdf_file:
        merger.append(PyPDF2.PdfReader(pdf_file))



# Write the merged PDF to the output file
with open(output_file, 'wb') as output:
    merger.write(output)

print("PDFs successfully merged!")
