
# 🏦 KBank Credit Statement PDF Parser

## 📖 Project Overview

The **KBank Credit Statement PDF Parser** is a Python-based tool designed to extract essential financial details from **Kotak Mahindra Bank** credit card statements in PDF format.

This application enables users to upload their credit card statement PDF and automatically parses the document to extract key details, presenting them in a clean, structured **JSON format** on a web interface.

---

## ⚙️ Features

✅ Upload a Kotak Bank credit card statement (PDF)
✅ Extract critical data points, including:

* **Card Issuer**
* **Last 4 digits of Credit Card**
* **Statement Date**
* **Payment Due Date**
* **Total Amount Due**
  ✅ Display extracted information in **JSON format**
  ✅ Simple and user-friendly web interface

---

## 🧩 Libraries Used

### 1. **pdfplumber**

* **Purpose:** Core library for PDF text extraction.
* **Usage:** Opens, reads, and extracts text content from PDF files.
* **How it Works:**
  `pdfplumber` gives programmatic access to the textual content, tables, and metadata within PDFs.
  In this project, it’s used to extract raw text for further parsing and structuring.

---

## 🏗️ How It Works

1. User uploads the **Kotak Bank PDF statement** via the web interface.
2. The backend uses **pdfplumber** to read and extract text data.
3. A parsing logic processes the extracted text to identify relevant information.
4. Extracted data (issuer, card digits, dates, amount, etc.) is formatted into **JSON output**.
5. The final JSON data is displayed neatly on the interface.

---

## 🚀 Setup Instructions

### Prerequisites

* Python 3.8+
* pip (Python package manager)

### Installation

```bash
git clone https://github.com/VarshaBuilds/kbank_parser.git
cd kbank_parser
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open your browser and navigate to:
👉 **[http://localhost:5000/](http://localhost:5000/)**

---

## 📦 Example Output

```json
{
  "Card Issuer": "Kotak Mahindra Bank",
  "Card Number (Last 4 Digits)": "1234",
  "Statement Date": "10-Oct-2025",
  "Payment Due Date": "30-Oct-2025",
  "Total Amount Due": "₹15,600.00"
}
```

---

## 🧠 Learning & Insights

* Gained hands-on experience working with **PDF parsing and text extraction** using Python.
* Understood **regular expressions** and **pattern matching** to extract structured data.
* Built a simple **Flask web app** for front-end interaction with backend parsing logic.
