import pdfplumber

pdf_path = r"D:\00biz\azeros\AETHERIS Automotive MVP.pdf"
text = ""
try:
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    with open("pdf_content.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("Content extracted successfully to pdf_content.txt")
except Exception as e:
    print(f"Error: {e}")
