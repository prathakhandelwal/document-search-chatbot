from pypdf import PdfReader
from docx import Document

class DocumentService:

    def extract_text(self,file_path:str):
        if file_path.endswith(".pdf"):
            return self._extract_text_from_pdf(file_path)
        elif file_path.endswith(".docx"):
            return self._extract_text_from_docx(file_path)
        elif file_path.endswith(".txt") or file_path.endswith(".md"):
            return self._extract_plain_txt(file_path)
        else:
            raise ValueError("Unsupported file type")
        
    def _extract_text_from_pdf(self,file_path):
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    
    def _extract_text_from_docx(self,file_path):
        doc = Document(file_path)
        text = ""
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text
    
    def _extract_plain_txt(self,file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()