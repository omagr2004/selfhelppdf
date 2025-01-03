def extract_text_from_pdf(file_path):
    import fitz  # PyMuPDF

    # Open the PDF file
    document = fitz.open(file_path)
    text = ""

    # Extract text from each page
    for page in document:
        text += page.get_text()

    document.close()
    return text