import fitz  # PyMuPDF, install with: pip install pymupdf
import re
from datetime import datetime

class PDFAgent:
    def extract_pdf_text(self, pdf_path):
        try:
            doc = fitz.open(pdf_path)
            full_text = ""
            for page in doc:
                full_text += page.get_text()
            return full_text
        except Exception as e:
            return f"Error reading PDF: {str(e)}"
    
    def classify_intent(self, text):
        # Simple keyword-based intent detection
        text = text.lower()
        if "invoice" in text:
            return "Invoice"
        elif "complaint" in text:
            return "Complaint"
        elif "regulation" in text:
            return "Regulation"
        elif "rfq" in text:
            return "RFQ"
        else:
            return "Unknown"

    def extract_info(self, pdf_path):
        text = self.extract_pdf_text(pdf_path)
        if text.startswith("Error"):
            return {"error": text}
        
        intent = self.classify_intent(text)
        
        # Just return text and intent for now (you can enhance with regex for fields)
        return {
            "extracted_text": text[:500] + "...",  # preview first 500 chars
            "intent": intent,
            "extracted_date": datetime.now().isoformat()
        }
