# ===== IMPORTS =====
from agents.classifier_agent import ClassifierAgent
from agents.email_agent import EmailAgent
from agents.json_agent import JSONAgent
from memory import SharedMemory
from agents.pdf_agent import PDFAgent
import os

# ===== INITIALIZE AGENTS =====
classifier = ClassifierAgent()
email_agent = EmailAgent()
json_agent = JSONAgent()
memory = SharedMemory()

# ===== INPUT FILE =====
input_file = 'samples/sample_invoice.pdf'  # Change to your test file

# ===== READ / HANDLE CONTENT =====
ext = os.path.splitext(input_file)[1].lower()

if ext == '.pdf':
    format_type, intent = 'PDF', 'Invoice'  # You can adjust intent detection if needed
    content = None  # No need to read PDF as text here
else:
    with open(input_file, "r") as f:
        content = f.read()
    print("Content being classified:\n", content)
    format_type, intent = classifier.classify(content)

print(f"Format: {format_type}")
print(f"Intent: {intent}")

# ===== ROUTING TO CORRECT AGENT =====
if format_type == 'Email':
    result = email_agent.extract_email_info(content)
    print("\n📬 Email Agent Output:")
    for k, v in result.items():
        print(f"{k}: {v}")

    memory.log_entry(
        source=input_file,
        format_type=format_type,
        intent=intent,
        extracted_values=result,
        thread_id="email-thread-001"
    )

elif format_type == 'JSON':
    result = json_agent.extract_and_validate(content)
    print("\n🗂 JSON Agent Output:")
    for k, v in result.items():
        print(f"{k}: {v}")

    memory.log_entry(
        source=input_file,
        format_type=format_type,
        intent=intent,
        extracted_values=result,
        thread_id="json-thread-001"
    )

elif format_type == 'PDF':
    pdf_agent = PDFAgent()
    result = pdf_agent.extract_info(input_file)  # Pass filename, PDF agent handles reading
    print("\n📄 PDF Agent Output:")
    for k, v in result.items():
        print(f"{k}: {v}")

    memory.log_entry(
        source=input_file,
        format_type=format_type,
        intent=intent,
        extracted_values=result,
        thread_id="pdf-thread-001"
    )

# ===== SHOW MEMORY =====
print("\n🧠 Shared Memory Log:")
for entry in memory.fetch_all():
    print(entry)
