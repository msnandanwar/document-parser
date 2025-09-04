"""
AI Parser Module - Google Gemini Integration
Handles intelligent parsing of bank statement text using Google Gemini 2.0 Flash
"""

import google.generativeai as genai
import os
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def configure_gemini():
    """
    Configure the Gemini API with the API key from environment variables
    
    Returns:
        GenerativeModel: Configured Gemini model instance
        
    Raises:
        ValueError: If GEMINI_API_KEY not found in environment
    """
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables. Please add it to your .env file.")
    
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-2.0-flash-exp')

def parse_with_gemini(text_data, prompt):
    """
    Parse bank statement text using Google Gemini 2.0 Flash
    
    Args:
        text_data (str): Extracted text from PDF bank statement
        prompt (str): System prompt with parsing instructions
        
    Returns:
        str: Parsed CSV string or None if parsing fails
        
    Raises:
        Exception: If API call fails or response is invalid
    """
    try:
        logger.info("Initializing Gemini model...")
        model = configure_gemini()
        
        # Combine prompt and text data for processing
        full_prompt = f"{prompt}\n\nBank Statement Text to Parse:\n{text_data}"
        
        logger.info("Sending request to Gemini API...")
        response = model.generate_content(full_prompt)
        
        if response.text:
            logger.info("Successfully received response from Gemini")
            return response.text.strip()
        else:
            logger.error("Empty response received from Gemini")
            return None
            
    except Exception as e:
        logger.error(f"Error in Gemini parsing: {str(e)}")
        raise Exception(f"Gemini parsing failed: {str(e)}")

def validate_api_connection():
    """
    Test the connection to Gemini API
    
    Returns:
        bool: True if connection successful, False otherwise
    """
    try:
        model = configure_gemini()
        # Simple test request
        test_response = model.generate_content("Hello")
        return test_response.text is not None
    except Exception as e:
        logger.error(f"API connection test failed: {str(e)}")
        return False
