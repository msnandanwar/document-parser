# Import pdfplumber
import pdfplumber
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_text_from_pdf(pdf_path):
    """
    Write a function extract_text_from_pdf(pdf_path) that:
    1. Opens the PDF using pdfplumber
    2. Iterates through all pages
    3. Extracts both text and table data
    4. Returns a combined string of all text and table data for LLM processing
    """
    try:
        all_text = []
        
        with pdfplumber.open(pdf_path) as pdf:
            logger.info(f"Processing PDF with {len(pdf.pages)} pages")
            
            for page_num, page in enumerate(pdf.pages, 1):
                logger.info(f"Processing page {page_num}")
                
                # Add page separator
                all_text.append(f"\n--- PAGE {page_num} ---\n")
                
                # Extract tables first (higher priority for bank statements)
                tables = page.extract_tables()
                if tables:
                    logger.info(f"Found {len(tables)} tables on page {page_num}")
                    for table_num, table in enumerate(tables, 1):
                        all_text.append(f"\n[TABLE {table_num} START]\n")
                        for row in table:
                            if row:  # Skip empty rows
                                # Join non-empty cells with pipe separator
                                row_text = " | ".join([cell.strip() if cell else "" for cell in row])
                                if row_text.strip():  # Only add non-empty rows
                                    all_text.append(row_text)
                        all_text.append(f"[TABLE {table_num} END]\n")
                
                # Extract remaining text (non-table content)
                page_text = page.extract_text()
                if page_text:
                    # Remove excessive whitespace and clean up
                    cleaned_text = "\n".join([line.strip() for line in page_text.split('\n') if line.strip()])
                    all_text.append(cleaned_text)
                    
        combined_text = "\n".join(all_text)
        logger.info(f"Extracted {len(combined_text)} characters total")
        
        return combined_text
        
    except Exception as e:
        logger.error(f"Error extracting text from PDF: {str(e)}")
        raise

def extract_text_with_layout(pdf_path):
    """
    Alternative extraction method that preserves layout better
    Useful for complex bank statement formats
    """
    try:
        all_content = []
        
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages, 1):
                all_content.append(f"\n=== PAGE {page_num} ===\n")
                
                # Try to extract with layout preservation
                text_with_layout = page.extract_text(layout=True)
                if text_with_layout:
                    all_content.append(text_with_layout)
                
                # Also extract tables separately for better structure
                tables = page.extract_tables()
                for table in tables:
                    all_content.append("\n[STRUCTURED TABLE DATA]\n")
                    for row in table:
                        if row and any(cell for cell in row if cell):
                            row_data = []
                            for cell in row:
                                if cell:
                                    row_data.append(str(cell).strip())
                                else:
                                    row_data.append("")
                            all_content.append(" | ".join(row_data))
                    all_content.append("[END TABLE DATA]\n")
        
        return "\n".join(all_content)
        
    except Exception as e:
        logger.error(f"Error in layout extraction: {str(e)}")
        return extract_text_from_pdf(pdf_path)  # Fallback to regular extraction
