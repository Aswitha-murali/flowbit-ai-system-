import json

class ClassifierAgent:
    def classify(self, content):
        try:
            json.loads(content)
            format_type = "JSON"
        except:
            if "From:" in content and "Subject:" in content:
                format_type = "Email"
            else:
                format_type = "Unknown"

        # Check intent (simple examples)
        if "invoice" in content.lower():
            intent = "Invoice"
        elif "request for quote" in content.lower() or "rfq" in content.lower():
            intent = "RFQ"
        elif "complaint" in content.lower():
            intent = "Complaint"
        elif "regulation" in content.lower():
            intent = "Regulation"
        else:
            intent = "Unknown"

        return format_type, intent
