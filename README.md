# Intelligent Bank Statement Parser

**Professional PDF-to-CSV Converter Using Google Gemini AI**

## Quick Start

This solution converts bank statement PDFs into structured CSV files using Google Gemini AI with exceptional accuracy.

### Setup
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Add your API key to .env
GEMINI_API_KEY=your_actual_api_key_here

# 3. Run the parser
python main.py --input "statement.pdf" --output "data.csv"
```

### Quick verification
```bash
python setup_check.py
```

### Demo
```bash
python demo.py
```

## What It Does

- **Input**: Bank statement PDF (any size, any bank)
- **Output**: Clean, structured CSV file
- **Accuracy**: Near-perfect transaction capture
- **Speed**: ~30 seconds for typical 8-page document
- **Cost**: Uses efficient Gemini 2.0 Flash API

## Core Features

- **AI-Powered Parsing**: Uses Google Gemini 2.0 Flash for intelligent document understanding
- **Robust Validation**: Multiple validation layers ensure data quality
- **Production Ready**: Comprehensive error handling and logging
- **Modular Design**: Clean architecture for easy maintenance and extension
- **Secure**: API keys managed securely via environment variables

## Example Output

```csv
Date,Cheque No.,Narration,Debit,Credit,Balance
2025-06-01,,UPI Transfer to Merchant,44.00,,390986.87
2025-06-01,,ATM Withdrawal,3149.00,,387837.87
2025-06-01,,Internal Transfer,66709.00,,321128.87
```

## Project Structure

```
pdf2csv-demo/
├── main.py              # Main CLI entry point - run this to process PDFs
├── pdf_extractor.py     # PDF text and table extraction engine
├── llm_parser.py        # Google Gemini AI integration and API calls
├── prompts.py           # Expert-crafted prompts for parsing accuracy
├── csv_handler.py       # CSV validation, cleaning, and output management
├── demo.py              # Automated demo script (finds PDFs and processes them)
├── quick_start.py       # Interactive setup and getting started guide
├── setup_check.py       # Environment and dependency verification
├── requirements.txt     # Python package dependencies
├── .env                 # API key configuration (create this file)
├── .gitignore          # Git exclusion rules
├── inputs/              # Place your PDF files here
├── outputs/             # Generated CSV files appear here
└── Documentation/
    ├── README.md                        # This file - quick start guide
    ├── COMPREHENSIVE_DOCUMENTATION.md   # Detailed technical documentation
    └── PROMPT_ENGINEERING.md           # Prompt strategy and optimization
```

## File Guide - What Each File Does

### 🎯 **Main Scripts (Start Here)**
- **`main.py`** - The main CLI application. Run this to process bank statements.
  ```bash
  python main.py -i "statement.pdf" -o "output.csv"
  ```

- **`demo.py`** - Auto-demo script. Finds PDFs automatically and shows the complete process.
  ```bash
  python demo.py
  ```

- **`quick_start.py`** - Interactive setup guide for first-time users.
  ```bash
  python quick_start.py
  ```

### ⚙️ **Core Engine Files**
- **`pdf_extractor.py`** - Extracts text and tables from PDF files using pdfplumber
- **`llm_parser.py`** - Handles all Google Gemini AI API communication
- **`csv_handler.py`** - Validates, cleans, and saves CSV output with business rules
- **`prompts.py`** - Contains the expert-crafted prompts that make parsing accurate

### 🛠️ **Setup & Configuration**
- **`setup_check.py`** - Verifies environment, dependencies, and API connectivity
- **`requirements.txt`** - Python package dependencies for pip install
- **`.env`** - Your API key file (you create this with: `GEMINI_API_KEY=your_key`)
- **`.gitignore`** - Keeps sensitive files out of version control

### 📁 **Data Directories**
- **`inputs/`** - Put your bank statement PDF files here
- **`outputs/`** - Generated CSV files appear here automatically

### 📚 **Documentation**
- **`README.md`** - This file - quick start and overview
- **`COMPREHENSIVE_DOCUMENTATION.md`** - Detailed technical documentation
- **`PROMPT_ENGINEERING.md`** - How the AI prompts work and why they're effective

## Why This Solution Works

1. **Expert Prompt Engineering**: Carefully crafted prompts achieve consistent parsing accuracy
2. **Robust Error Handling**: Handles incomplete data, formatting issues, and edge cases
3. **Production Quality**: Built for reliability with comprehensive validation
4. **Google Gemini 2.0**: Uses state-of-the-art AI model optimized for structured data extraction

## Requirements

- Python 3.8+
- Google Gemini API key (get from Google AI Studio)
- Internet connection for API access

## Getting Started

1. Run `python quick_start.py` for guided setup
2. See `FILE_GUIDE.md` for complete file reference
3. See `COMPREHENSIVE_DOCUMENTATION.md` for detailed technical information
4. See `PROMPT_ENGINEERING.md` for prompt strategy details

## API Key Setup

Get your free Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey) and add it to your `.env` file.

## License

MIT License - Free to use and modify.
