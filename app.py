import streamlit as st
import json
from pdfparse import parse_kotak_statement
import os

st.title("KBank Credit Statement PDF Parser")

st.write("Upload your KBank credit statement PDF to extract key information.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Save the uploaded file temporarily
    with open(os.path.join("uploaded_statement.pdf"), "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.write("Processing PDF...")
    try:
        # Call the parsing function with the path to the temporary file
        extracted_data = parse_kotak_statement("uploaded_statement.pdf")
        
        st.subheader("Extracted Data:")
        st.json(extracted_data)
        
    except Exception as e:
        st.error(f"An error occurred during PDF processing: {e}")
    finally:
        # Clean up the temporary file
        if os.path.exists("uploaded_statement.pdf"):
            os.remove("uploaded_statement.pdf")
