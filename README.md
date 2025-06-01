# Flowbit AI System

A smart file classification and processing system built for FlowbitAI's assignment. This project automatically detects the file format and content intent of a given input, and applies relevant processing logic using modular agents.

---

# Features

-  Automatically detects file format (PDF or JSON)
-  Classifies content intent (e.g., Invoice)
- Modular agent-based processing system
-  Anomaly detection for JSON invoices
-  Shared memory log with timestamped results

---

## 📁 Project Structure
flowbit_ai_system/
├── main.py # entry point
├── agents/
│ ├── base_agent.py # base class
│ ├── pdf_agent.py # PDF processor
│ └── json_agent.py # JSON processor
├── shared_memory/
│ └── memory.json # storage for extracted info
├── samples/
│ ├── sample_invoice.pdf # test PDF
│ └── sample_invoice.json # test JSON
└── README.md # this file


---

# Example Output

If you run `main.py` on a sample invoice PDF, output may look like:
Format: PDF
Intent: Invoice

PDF Agent Output:
extracted_text: ...
intent: Invoice
extracted_date: 2025-05-29T23:12:46.384761


---

# Requirements

- Python 3.8+
- `PyMuPDF` (`pip install pymupdf`)

---

# Author

Created by [M.ASWITHA]  
Assignment for FlowbitAI (System Design Evaluation)






