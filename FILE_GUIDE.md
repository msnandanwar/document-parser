# 📋 Complete File Guide

**Quick reference for every file in the Bank Statement Parser project**

## 🚀 **Entry Points - Start Here**

### `main.py` ⭐ **Main Application**
- **Purpose**: Primary CLI interface for production use
- **Usage**: `python main.py -i "input.pdf" -o "output.csv"`
- **Features**: Full argument parsing, error handling, logging
- **When to use**: Production processing, batch operations, automation

### `demo.py` 🎮 **Auto-Demo Script**
- **Purpose**: Automated demonstration without arguments
- **Usage**: `python demo.py`
- **Features**: Auto-finds PDFs, shows step-by-step progress, sample output preview
- **When to use**: First-time testing, client demos, quick verification

### `quick_start.py` 🛠️ **Interactive Setup Guide**
- **Purpose**: Guided onboarding for new users
- **Usage**: `python quick_start.py`
- **Features**: Interactive prompts, environment validation, sample downloads
- **When to use**: First-time setup, troubleshooting setup issues

## ⚙️ **Core Engine Components**

### `pdf_extractor.py` 📄 **PDF Processing Engine**
- **Purpose**: Extracts text and tables from PDF files
- **Key Function**: `extract_text_from_pdf(pdf_path)`
- **Technology**: Uses pdfplumber for robust PDF parsing
- **Handles**: Multi-page documents, complex layouts, table structures

### `llm_parser.py` 🤖 **AI Integration Hub**
- **Purpose**: Google Gemini API communication and parsing
- **Key Functions**: `parse_with_gemini()`, `validate_api_connection()`
- **Features**: Error handling, retry logic, response validation
- **Security**: Secure API key management via environment variables

### `csv_handler.py` ✅ **Data Validation & Output**
- **Purpose**: CSV validation, cleaning, and business rule enforcement
- **Key Function**: `save_csv_with_validation(csv_content, output_path)`
- **Features**: Data validation, format cleaning, duplicate detection
- **Quality**: Ensures production-ready CSV output

### `prompts.py` 💡 **Prompt Engineering**
- **Purpose**: Contains expert-crafted AI prompts
- **Key Constant**: `BANK_STATEMENT_PROMPT`
- **Features**: Optimized for accuracy, handles edge cases
- **Why Important**: The "secret sauce" that makes parsing work reliably

## 🔧 **Setup & Configuration Files**

### `setup_check.py` 🩺 **Environment Validator**
- **Purpose**: Verifies complete environment setup
- **Usage**: `python setup_check.py`
- **Checks**: Dependencies, API connectivity, file permissions
- **When to use**: Troubleshooting, pre-deployment verification

### `requirements.txt` 📦 **Dependencies**
- **Purpose**: Python package requirements for pip
- **Usage**: `pip install -r requirements.txt`
- **Contains**: pdfplumber, google-generativeai, pandas, python-dotenv
- **Version**: Tested and pinned versions for stability

### `.env` 🔐 **API Configuration**
- **Purpose**: Secure storage for API keys and configuration
- **Format**: `GEMINI_API_KEY=your_actual_api_key_here`
- **Security**: Never commit to version control (in .gitignore)
- **Setup**: You create this file with your API key

### `.gitignore` 🚫 **Version Control Rules**
- **Purpose**: Prevents sensitive files from being committed
- **Protects**: API keys, output files, cache files, virtual environments
- **Essential**: Keeps your secrets safe in version control

## 📁 **Data Directories**

### `inputs/` 📥 **Source Files**
- **Purpose**: Place your bank statement PDF files here
- **Structure**: Contains README.md with usage instructions
- **Best Practice**: Organize by date or bank for multiple files

### `outputs/` 📤 **Generated Results**
- **Purpose**: CSV files automatically saved here
- **Structure**: Contains README.md explaining output format
- **Cleanup**: Files removed during security cleanup (no sensitive data)

## 📚 **Documentation Files**

### `README.md` 📖 **Quick Start Guide**
- **Purpose**: Primary project documentation and quick start
- **Audience**: New users, GitHub visitors, quick reference
- **Content**: Setup, usage examples, project overview

### `COMPREHENSIVE_DOCUMENTATION.md` 📋 **Technical Deep Dive**
- **Purpose**: Detailed technical documentation
- **Audience**: Developers, architects, technical stakeholders
- **Content**: Architecture, API details, troubleshooting, advanced usage

### `PROMPT_ENGINEERING.md` 🎯 **Prompt Strategy**
- **Purpose**: Documents prompt design and optimization
- **Audience**: AI engineers, prompt engineers, technical reviewers
- **Content**: Prompt evolution, testing results, optimization strategies

### `FILE_GUIDE.md` 📋 **This File**
- **Purpose**: Complete reference for every file in the project
- **Audience**: Developers, maintainers, new team members
- **Content**: What you're reading now!

## 🎯 **Usage Patterns**

### **For Production Use**:
1. `python setup_check.py` (verify environment)
2. `python main.py -i "statement.pdf" -o "result.csv"` (process file)

### **For Development/Testing**:
1. `python demo.py` (quick test)
2. `python setup_check.py` (verify setup)

### **For New Users**:
1. `python quick_start.py` (guided setup)
2. `python demo.py` (see it work)
3. `python main.py --help` (learn CLI options)

## 🔍 **File Dependencies**

```
main.py
├── pdf_extractor.py
├── llm_parser.py
├── csv_handler.py
└── prompts.py

demo.py
├── pdf_extractor.py
├── llm_parser.py
├── csv_handler.py
└── prompts.py

setup_check.py
└── llm_parser.py (for API testing)
```

## 📊 **File Sizes & Complexity**

| File | Purpose | Lines | Complexity |
|------|---------|-------|------------|
| `main.py` | CLI Interface | ~174 | Medium |
| `pdf_extractor.py` | PDF Processing | ~50 | Low |
| `llm_parser.py` | AI Integration | ~100 | Medium |
| `csv_handler.py` | Data Validation | ~150 | High |
| `prompts.py` | Prompt Definitions | ~50 | Low |
| `demo.py` | Demo Script | ~102 | Low |
| `quick_start.py` | Setup Guide | ~100 | Low |
| `setup_check.py` | Environment Check | ~100 | Medium |

---

**This guide covers every file in the project. For specific technical details, see COMPREHENSIVE_DOCUMENTATION.md**
