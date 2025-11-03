import pdfplumber
import re
import json

def parse_kotak_statement(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"

    # Define regex patterns for key fields
    data = {}

    # 1. Card Issuer
    data["card_issuer"] = "Kotak Mahindra Bank"

    # 2. Card Last 4 Digits
    match_card = re.search(r"PrimaryCardNumber \d{4}X{8}(\d{4})", text)
    data["card_last_4_digits"] = match_card.group(1) if match_card else None

    # 3. Statement Date
    match_date = re.search(r"StatementDate (\d{2}-[A-Za-z]{3}-\d{4})", text)
    data["statement_date"] = match_date.group(1) if match_date else None

    # 4. Payment Due Date
    match_due = re.search(r"Remembertopayby (\d{2}-[A-Za-z]{3}-\d{4})", text)
    data["payment_due_date"] = match_due.group(1) if match_due else None

    # 5. Total Amount Due
    match_total = re.search(r"TotalAmountDue\(TAD\) Rs\.([\d,]+\.\d{2})", text)
    data["total_amount_due"] = match_total.group(1) if match_total else None







    return data

if __name__ == "__main__":
    pdf_path = "Oct-25.pdf"  # your uploaded PDF
    extracted_data = parse_kotak_statement(pdf_path)

    print("Extracted Credit Card Data:")
    print(json.dumps(extracted_data, indent=4))