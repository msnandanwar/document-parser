# 🚀 Setup Guide

**Get the bank statement parser running in under 5 minutes!**

## Prerequisites
- Python 3.8+ installed
- Internet connection
- Git (to clone repository)

## Step-by-Step Installation

### 1. Clone Repository
```bash
git clone https://github.com/msnandanwar/document-parser.git
cd document-parser
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Get Free API Key
1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with Google account
3. Click "Create API Key"
4. Copy the generated key

### 4. Configure API Key
1. Open `.env` file in any text editor
2. Replace `your_gemini_api_key_here` with your actual API key
3. Save the file

**Example:**
```
GEMINI_API_KEY=your_actual_api_key_here_no_quotes
```

### 5. Verify Installation
```bash
python setup_check.py
```

You should see: ✓ Setup complete!

## Quick Test

```bash
# Option 1: Interactive guide
python quick_start.py

# Option 2: Auto demo
python demo.py

# Option 3: Process your PDF
python main.py --input "inputs/statement.pdf" --output "outputs/result.csv"
```

## Troubleshooting

**"No module found"** → Run: `pip install -r requirements.txt`

**"API key not found"** → Check `.env` file has your API key

**"Connection failed"** → Verify internet and API key validity

**Need help?** → Run `python setup_check.py` for diagnostics

---

**Installation complete! Ready to parse bank statements with AI.** 🎉
