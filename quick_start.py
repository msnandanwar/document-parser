#!/usr/bin/env python3
"""
Quick Start Guide for Bank Statement Parser
Run this to get started quickly
"""

import os
import sys
from pathlib import Path

def print_welcome():
    """Print welcome message"""
    print("Welcome to Bank Statement Parser!")
    print("=" * 40)
    print("Professional PDF-to-CSV converter using Google Gemini AI")
    print()

def check_setup():
    """Quick setup check"""
    print("Checking setup...")
    
    # Check if .env exists
    if not Path('.env').exists():
        print("⚠ .env file not found")
        print("Creating template .env file...")
        
        with open('.env', 'w') as f:
            f.write("# Store your Google Gemini API key securely\n")
            f.write("GEMINI_API_KEY=your_gemini_api_key_here\n")
        
        print("✓ Created .env template")
        print("Please edit .env and add your actual Gemini API key")
        return False
    
    # Check if API key is configured
    with open('.env', 'r') as f:
        content = f.read()
    
    if 'your_gemini_api_key_here' in content:
        print("⚠ Please configure your Gemini API key in .env file")
        return False
    
    print("✓ Setup looks good!")
    return True

def show_usage():
    """Show usage examples"""
    print("\nQuick Usage:")
    print("-" * 20)
    print("1. Setup verification:")
    print("   python setup_check.py")
    print()
    print("2. Run demo (if you have a PDF):")
    print("   python demo.py")
    print()
    print("3. Process your PDF:")
    print("   python main.py --input statement.pdf --output data.csv")
    print()
    print("4. Test API connection:")
    print("   python main.py --test-connection")
    print()

def main():
    """Main quick start function"""
    print_welcome()
    
    setup_ok = check_setup()
    
    if setup_ok:
        print("✓ Ready to use!")
    else:
        print("⚠ Setup required - please follow the instructions above")
    
    show_usage()
    
    print("For detailed documentation, see:")
    print("- README.md")
    print("- COMPREHENSIVE_DOCUMENTATION.md")
    print("- PROMPT_ENGINEERING.md")

if __name__ == "__main__":
    main()
