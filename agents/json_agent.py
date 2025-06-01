import json

class JSONAgent:
    def extract_and_validate(self, content):
        try:
            # Load JSON from string content
            data = json.loads(content)

            # Basic validation
            required_fields = ["invoice_id", "customer", "items", "total", "date"]
            missing = [field for field in required_fields if field not in data]

            result = data.copy()
            if missing:
                result["anomalies"] = f"Missing fields: {', '.join(missing)}"
            else:
                result["anomalies"] = None

            return result

        except Exception as e:
            return {"error": f"Failed to load JSON: {str(e)}"}
