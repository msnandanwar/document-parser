#!/usr/bin/env python3
"""
Intelligent Bank Statement Parser
Professional PDF-to-CSV converter using Google Gemini AI
"""

import argparse
import os
import sys
import logging
from pathlib import Path

# Import our modules
from pdf_extractor import extract_text_from_pdf
from llm_parser import parse_with_gemini, validate_api_connection
from csv_handler import save_csv_with_validation
from prompts import BANK_STATEMENT_PROMPT

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def validate_input_file(file_path):
    """
    Validate that input file exists and is a PDF
    
    Args:
        file_path (str): Path to input file
        
    Returns:
        bool: True if valid
        
    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If file is not a PDF
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Input file not found: {file_path}")
    
    if not file_path.lower().endswith('.pdf'):
        raise ValueError("Input file must be a PDF")
    
    return True

def ensure_output_directory(output_path):
    """
    Ensure output directory exists, create if necessary
    
    Args:
        output_path (str): Path where output file will be saved
    """
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        logger.info(f"Created output directory: {output_dir}")

def process_bank_statement(input_path, output_path):
    """
    Main processing function that orchestrates the conversion
    
    Args:
        input_path (str): Path to input PDF file
        output_path (str): Path for output CSV file
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Step 1: Validate input
        logger.info(f"Processing: {input_path}")
        validate_input_file(input_path)
        ensure_output_directory(output_path)
        
        # Step 2: Extract text from PDF
        logger.info("Extracting text from PDF...")
        text_data = extract_text_from_pdf(input_path)
        
        if not text_data or len(text_data.strip()) == 0:
            logger.error("No text extracted from PDF")
            return False
        
        logger.info(f"Extracted {len(text_data)} characters from PDF")
        
        # Step 3: Parse with Gemini AI
        logger.info("Parsing with Google Gemini AI...")
        csv_result = parse_with_gemini(text_data, BANK_STATEMENT_PROMPT)
        
        if not csv_result:
            logger.error("Failed to parse with Gemini")
            return False
        
        # Step 4: Save and validate output
        logger.info("Saving and validating CSV output...")
        save_csv_with_validation(csv_result, output_path)
        
        logger.info(f"Successfully converted PDF to CSV: {output_path}")
        return True
        
    except Exception as e:
        logger.error(f"Processing failed: {str(e)}")
        return False

def main():
    """Main CLI function"""
    parser = argparse.ArgumentParser(
        description="Convert bank statement PDFs to structured CSV using Google Gemini AI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py --input statement.pdf --output data.csv
  python main.py -i bank_statement.pdf -o parsed_data.csv
  
Requirements:
  - Google Gemini API key in .env file
  - PDF bank statement file
        """
    )
    
    parser.add_argument(
        '--input', '-i',
        required=True,
        help='Path to input PDF bank statement'
    )
    
    parser.add_argument(
        '--output', '-o',
        required=True,
        help='Path for output CSV file'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose logging'
    )
    
    parser.add_argument(
        '--test-connection',
        action='store_true',
        help='Test API connection and exit'
    )
    
    args = parser.parse_args()
    
    # Set logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Test connection if requested
    if args.test_connection:
        logger.info("Testing Gemini API connection...")
        if validate_api_connection():
            logger.info("✓ API connection successful")
            sys.exit(0)
        else:
            logger.error("✗ API connection failed")
            sys.exit(1)
    
    # Process the bank statement
    success = process_bank_statement(args.input, args.output)
    
    if success:
        print(f"✓ Successfully converted {args.input} to {args.output}")
        sys.exit(0)
    else:
        print(f"✗ Failed to convert {args.input}")
        sys.exit(1)

if __name__ == "__main__":
    main()
