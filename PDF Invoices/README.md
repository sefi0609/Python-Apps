# PDF Invoices

This script automates the creation of invoices from Excel files in the Invoice folder and generates corresponding PDF files in the PDFs folder.
It reads data from Excel, formats it into invoice templates, and outputs each invoice as a PDF.

## Features
- Automatically create invoices from Excel files
- Output invoices as PDF files in the PDFs folder
- Customizable invoice template for formatting the data
- Supports multiple invoices in one run

## Technologies Used
✅ **Python** – Main programming language  
✅ **Pandas** – To process and read Excel data  
✅ **FPDF** – To generate PDF files  

## Example
- **Input Excel File**: A sample Excel file with columns like Item Name, Quantity, Price, etc. (see [Invoices](Invoices) folder)
- **Generated PDF Invoice**: The output will be a PDF formatted with the invoice details from the Excel file. (see [PDFs](PDFs) folder)
