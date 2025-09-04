# AI Bank Statement Parser

**Convert bank statement PDFs to clean CSV files using Google Gemini AI**

**Demo Version**: Processes up to ~130 transactions per file  
**Enterprise Ready**: Unlimited processing available on request

## Quick Start

### 1. Get Running in 5 Minutes
```bash
# Clone repository
git clone https://github.com/msnandanwar/document-parser.git
cd document-parser

# Install dependencies
pip install -r requirements.txt

# Get free API key: https://aistudio.google.com/app/apikey
# Edit .env file and add your API key

# Test setup
python setup_check.py

# Run demo
python demo.py
```

### 2. Basic Usage
```bash
# Place your PDF in inputs/ folder, then:
python main.py --input "inputs/statement.pdf" --output "outputs/data.csv"

# Or use interactive mode:
python quick_start.py
```

## What It Does

- **Extracts** transaction data from complex PDF layouts
- **Parses** dates, amounts, descriptions, and balances using AI
- **Validates** data integrity and removes duplicates
- **Outputs** clean CSV with standardized format
- **Handles** multi-page statements and various bank formats

## Features

### Current Demo Capabilities
- High-accuracy transaction extraction
- Smart date/amount parsing and validation
- Automatic duplicate removal
- Clean CSV output with proper formatting
- Supports major bank statement formats
- Processes up to ~130 transactions per file

### Enterprise Features (Available on Request)
- Unlimited transaction processing with intelligent chunking
- Batch processing for multiple files
- Custom parsing rules for specific bank formats
- Advanced validation and error handling
- Integration APIs and automated workflows

## File Structure

```
pdf2csv-demo/
├── main.py              # CLI entry point
├── demo.py              # Auto-demo script
├── quick_start.py       # Interactive setup
├── pdf_extractor.py     # PDF text extraction
├── llm_parser.py        # Gemini AI integration
├── csv_handler.py       # CSV validation & output
├── prompts.py           # AI parsing prompts
├── setup_check.py       # Environment validation
├── inputs/              # Place PDFs here
├── outputs/             # CSV results here
└── .env                 # API key configuration
```

## Technical Details

### Requirements
- **Python 3.8+**
- **Google Gemini API key** (free tier available)
- **Internet connection** for AI processing

### Dependencies
- `pdfplumber` - PDF text extraction
- `google-generativeai` - Gemini AI integration  
- `pandas` - Data processing
- `python-dotenv` - Environment management

### Architecture
- **Modular design** for easy customization
- **Robust error handling** for production use
- **Security-first** approach with API key protection
- **Scalable** foundation for enterprise deployment

## Demo Limitations

This demo version has intentional limitations:

- **~130 transactions per file** (natural chunking limit)
- **Sequential processing** (one file at a time)
- **Basic validation** rules

**Enterprise version removes all limitations** and adds advanced features like unlimited processing, batch operations, and custom integrations.

## Security & Privacy

- **API keys** stored securely in `.env` files
- **No data logging** or external storage
- **Local processing** with encrypted API calls
- **Sensitive data** automatically excluded from repository

## Support & Licensing

- **License**: Demo Use Only - Commercial license required for business use
- **Commercial Use**: Contact for licensing terms and full enterprise features
- **Modifications**: Source code modifications require written permission
- **Support**: Enterprise support available with commercial licensing

## Perfect For

- **Financial analysts** processing bank statements
- **Accounting firms** digitizing client data
- **Businesses** automating reconciliation processes
- **Developers** needing CSV data from PDFs
- **Anyone** converting bank PDFs to spreadsheet format

---

**Ready to process your bank statements with AI?** Place a PDF in the `inputs/` folder and run `python demo.py`!
```bash
python demo.py
```

## What It Does

- **Input**: Bank statement PDF (any size, any bank)
- **Output**: Clean, structured CSV file
- **Processing**: ~120-130 transactions per run (demo version)
- **Accuracy**: Near-perfect transaction capture for processed data
- **Speed**: ~30 seconds for typical 8-page document
- **Cost**: Uses efficient Gemini 2.0 Flash API

### Demo Version Capabilities:
- **Single-pass processing** for statements up to ~130 transactions  
- **High accuracy parsing** with professional validation  
- **Clean CSV output** with proper formatting  
- **Complete architecture** demonstration  

### Full Implementation Features:
- **Unlimited transaction processing** via intelligent chunking  
- **Multi-document batch processing**  
- **Advanced error recovery** and retry logic  
- **Custom format adaptation** for different banks  
- **Performance optimization** for large datasets

## Core Features

- **AI-Powered Parsing**: Uses Google Gemini 2.0 Flash for intelligent document understanding
- **Robust Validation**: Multiple validation layers ensure data quality
- **Demo Processing**: Handles up to ~130 transactions per document in single pass
- **Production Ready**: Comprehensive error handling and logging
- **Modular Design**: Clean architecture for easy maintenance and extension
- **Secure**: API keys managed securely via environment variables

### Enterprise Features (Full Implementation):
- **Intelligent Chunking**: Process unlimited transactions by breaking large documents into optimal chunks
- **Batch Processing**: Handle multiple statements simultaneously
- **Advanced Reconciliation**: Cross-validate chunked results for accuracy
- **Custom Optimization**: Tailored chunking strategies for different bank formats

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
├── README.md            # This file - complete guide and overview
├── SETUP.md             # Step-by-step installation instructions
└── LICENSE              # Demo license terms
```

## File Guide - What Each File Does

### **Main Scripts (Start Here)**
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

### **Core Engine Files**
- **`pdf_extractor.py`** - Extracts text and tables from PDF files using pdfplumber
- **`llm_parser.py`** - Handles all Google Gemini AI API communication
- **`csv_handler.py`** - Validates, cleans, and saves CSV output with business rules
- **`prompts.py`** - Contains the expert-crafted prompts that make parsing accurate

### **Setup & Configuration**
- **`setup_check.py`** - Verifies environment, dependencies, and API connectivity
- **`requirements.txt`** - Python package dependencies for pip install
- **`.env`** - Your API key file (you create this with: `GEMINI_API_KEY=your_key`)
- **`.gitignore`** - Keeps sensitive files out of version control

### **Data Directories**
- **`inputs/`** - Put your bank statement PDF files here
- **`outputs/`** - Generated CSV files appear here automatically

### **Documentation**
- **`README.md`** - This file - quick start and overview
- **`SETUP.md`** - Step-by-step installation guide

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

1. **Quick Setup**: Follow `SETUP.md` for 5-minute installation
2. **Interactive Guide**: Run `python quick_start.py` for guided setup  
3. **Auto Demo**: Run `python demo.py` to test with your PDF files
4. **Manual Usage**: Use `python main.py --input "file.pdf" --output "result.csv"`

## API Key Setup

Get your free Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey) and add it to your `.env` file.

## License

**Demo Use Only** - See `LICENSE` file for complete terms. Commercial use requires licensing.
