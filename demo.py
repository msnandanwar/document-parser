#!/usr/bin/env python3
"""
Demo script for Bank Statement Parser
Demonstrates the complete PDF to CSV conversion process
"""

import os
import sys
from pathlib import Path

# Import our modules
from pdf_extractor import extract_text_from_pdf
from llm_parser import parse_with_gemini
from csv_handler import save_csv_with_validation
from prompts import BANK_STATEMENT_PROMPT

def run_demo():
    """Run a complete demonstration of the parser"""
    
    print("Bank Statement Parser - Demo")
    print("=" * 40)
    
    # Check if we have a sample PDF
    sample_files = list(Path('.').glob('*.pdf'))
    inputs_files = list(Path('inputs').glob('*.pdf')) if Path('inputs').exists() else []
    
    all_pdfs = sample_files + inputs_files
    
    if not all_pdfs:
        print("No PDF files found for demo.")
        print("Please add a bank statement PDF to the current directory or inputs/ folder.")
        return False
    
    # Use the first PDF found
    input_file = str(all_pdfs[0])
    output_file = "outputs/demo_result.csv"
    
    print(f"Input: {input_file}")
    print(f"Output: {output_file}")
    print()
    
    try:
        # Step 1: Extract text
        print("Step 1: Extracting text from PDF...")
        text_data = extract_text_from_pdf(input_file)
        print(f"✓ Extracted {len(text_data)} characters")
        
        # Step 2: Parse with AI
        print("\nStep 2: Parsing with Google Gemini...")
        csv_result = parse_with_gemini(text_data, BANK_STATEMENT_PROMPT)
        
        if not csv_result:
            print("✗ Parsing failed")
            return False
        
        print("✓ Parsing successful")
        
        # Step 3: Save result
        print("\nStep 3: Saving and validating result...")
        
        # Ensure outputs directory exists
        Path("outputs").mkdir(exist_ok=True)
        
        save_csv_with_validation(csv_result, output_file)
        print(f"✓ Saved to {output_file}")
        
        # Show sample results
        print("\nSample output (first 5 rows):")
        print("-" * 50)
        
        lines = csv_result.split('\n')
        for i, line in enumerate(lines[:6]):  # Header + 5 data rows
            print(line)
        
        if len(lines) > 6:
            print(f"... and {len(lines) - 6} more rows")
        
        print("-" * 50)
        print(f"✓ Demo completed successfully!")
        print(f"Total transactions parsed: {len(lines) - 1}")
        
        return True
        
    except Exception as e:
        print(f"✗ Demo failed: {str(e)}")
        return False

def main():
    """Main demo function"""
    success = run_demo()
    
    if success:
        print("\n🎉 Demo completed successfully!")
        print("The parser is working correctly.")
    else:
        print("\n❌ Demo failed!")
        print("Please check your setup and try again.")
        sys.exit(1)

if __name__ == "__main__":
    main()
