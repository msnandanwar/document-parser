#!/usr/bin/env python3
"""
Setup verification script for the Bank Statement Parser
Run this after installation to verify everything is working
"""

import os
import sys
from pathlib import Path

def check_dependencies():
    """Check if all required packages are installed"""
    print("=== Checking Dependencies ===")
    
    required_packages = [
        'pdfplumber',
        'google.generativeai', 
        'pandas',
        'dotenv'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✓ {package}")
        except ImportError:
            print(f"✗ {package}")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\nMissing packages: {missing_packages}")
        print("Run: pip install -r requirements.txt")
        return False
    
    print("All dependencies installed successfully!")
    return True

def check_env_file():
    """Check if .env file exists and has required API key"""
    print("\n=== Checking Environment Configuration ===")
    
    env_path = Path('.env')
    if not env_path.exists():
        print("✗ .env file not found")
        print("Please create a .env file with your API key:")
        print("GEMINI_API_KEY=your_gemini_api_key_here")
        return False
    
    # Read .env file
    with open(env_path, 'r') as f:
        env_content = f.read()
    
    if 'GEMINI_API_KEY' not in env_content:
        print("✗ GEMINI_API_KEY not found in .env file")
        return False
    
    # Check if key looks like placeholder
    if 'your_gemini_api_key_here' in env_content:
        print("⚠ GEMINI_API_KEY appears to be placeholder")
        print("Please replace with your actual Google Gemini API key")
        return False
    
    print("✓ .env file configured")
    return True

def check_api_connection():
    """Test connection to Gemini API"""
    print("\n=== Testing API Connection ===")
    
    try:
        from llm_parser import validate_api_connection
        
        if validate_api_connection():
            print("✓ Google Gemini API connection successful")
            return True
        else:
            print("✗ Google Gemini API connection failed")
            print("Please check your API key in .env file")
            return False
            
    except Exception as e:
        print(f"✗ API connection test failed: {str(e)}")
        return False

def check_project_structure():
    """Verify all required files are present"""
    print("\n=== Checking Project Structure ===")
    
    required_files = [
        'main.py',
        'pdf_extractor.py',
        'llm_parser.py',
        'csv_handler.py',
        'prompts.py',
        'requirements.txt',
        '.env'
    ]
    
    missing_files = []
    
    for file in required_files:
        if Path(file).exists():
            print(f"✓ {file}")
        else:
            print(f"✗ {file}")
            missing_files.append(file)
    
    if missing_files:
        print(f"\nMissing files: {missing_files}")
        return False
    
    print("All required files present!")
    return True

def check_directories():
    """Ensure required directories exist"""
    print("\n=== Checking Directories ===")
    
    required_dirs = ['inputs', 'outputs']
    
    for dir_name in required_dirs:
        dir_path = Path(dir_name)
        if dir_path.exists():
            print(f"✓ {dir_name}/")
        else:
            print(f"Creating {dir_name}/")
            dir_path.mkdir(exist_ok=True)
    
    return True

def main():
    """Run all setup checks"""
    print("Bank Statement Parser - Setup Verification")
    print("=" * 50)
    
    checks = [
        check_project_structure,
        check_dependencies,
        check_directories,
        check_env_file,
        check_api_connection
    ]
    
    all_passed = True
    
    for check in checks:
        if not check():
            all_passed = False
    
    print("\n" + "=" * 50)
    
    if all_passed:
        print("✓ All checks passed! Your setup is ready.")
        print("\nQuick start:")
        print("python main.py --input your_statement.pdf --output data.csv")
    else:
        print("✗ Some checks failed. Please fix the issues above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
