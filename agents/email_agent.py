import re

class EmailAgent:
    def extract_email_info(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            return {"error": str(e)}

        # Extract sender (simple regex)
        sender_match = re.search(r"From:\s*(.+)", content)
        sender = sender_match.group(1).strip() if sender_match else "Unknown"

        # Extract subject
        subject_match = re.search(r"Subject:\s*(.+)", content)
        subject = subject_match.group(1).strip() if subject_match else "No subject"

        # Check urgency keywords
        urgency = "High" if any(word in content.lower() for word in ["urgent", "asap", "immediately"]) else "Normal"

        # Try to guess intent
        if 'quote' in content.lower() or 'rfq' in content.lower():
            intent = 'RFQ'
        elif 'invoice' in content.lower():
            intent = 'Invoice'
        elif 'complaint' in content.lower() or 'issue' in content.lower():
            intent = 'Complaint'
        else:
            intent = 'Unknown'

        # Return structured CRM-style info
        return {
            "sender": sender,
            "subject": subject,
            "intent": intent,
            "urgency": urgency,
            "raw_text": content
        }
