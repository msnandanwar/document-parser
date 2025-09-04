import pandas as pd
import logging
import re
from datetime import datetime
from io import StringIO

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_csv(csv_string):
    """
    Write a function validate_csv(csv_string) that:
    1. Uses pandas to read the CSV string
    2. Checks for any rows where both Debit and Credit are not null
    3. Checks for any missing values in critical columns (Date, Balance)
    4. Logs warnings for any potential issues
    5. Returns the DataFrame and a validation report
    """
    validation_report = {
        'is_valid': True,
        'warnings': [],
        'errors': [],
        'row_count': 0,
        'issues_found': []
    }
    
    try:
        # Read CSV string into DataFrame
        df = pd.read_csv(StringIO(csv_string))
        validation_report['row_count'] = len(df)
        
        logger.info(f"CSV loaded successfully with {len(df)} rows")
        
        # Check required columns
        required_columns = ['Date', 'Cheque No.', 'Narration', 'Debit', 'Credit', 'Balance']
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            validation_report['errors'].append(f"Missing required columns: {missing_columns}")
            validation_report['is_valid'] = False
            return None, validation_report
        
        # Validate date format
        date_issues = validate_dates(df, validation_report)
        
        # Check for rows with both Debit and Credit filled
        debit_credit_issues = validate_debit_credit(df, validation_report)
        
        # Check for missing critical values
        missing_value_issues = validate_missing_values(df, validation_report)
        
        # Validate numeric fields
        numeric_issues = validate_numeric_fields(df, validation_report)
        
        # Validate balance consistency
        balance_issues = validate_balance_consistency(df, validation_report)
        
        # Check for duplicate transactions
        duplicate_issues = check_duplicates(df, validation_report)
        
        # Summary
        total_issues = len(validation_report['warnings']) + len(validation_report['errors'])
        if total_issues > 0:
            logger.warning(f"Validation completed with {total_issues} issues")
        else:
            logger.info("Validation passed - CSV is clean!")
        
        return df, validation_report
        
    except Exception as e:
        validation_report['errors'].append(f"Failed to parse CSV: {str(e)}")
        validation_report['is_valid'] = False
        logger.error(f"CSV validation failed: {str(e)}")
        return None, validation_report

def validate_dates(df, report):
    """Validate date format consistency"""
    date_pattern = r'^\d{4}-\d{2}-\d{2}$'
    invalid_dates = []
    
    for idx, date_val in df['Date'].items():
        if pd.notna(date_val):
            date_str = str(date_val).strip()
            if not re.match(date_pattern, date_str):
                invalid_dates.append(f"Row {idx + 1}: '{date_str}'")
    
    if invalid_dates:
        report['warnings'].append(f"Invalid date formats found: {invalid_dates[:5]}")  # Show first 5
        report['issues_found'].append('date_format')

def validate_debit_credit(df, report):
    """Check for rows with both Debit and Credit filled"""
    both_filled = []
    
    for idx, row in df.iterrows():
        debit = pd.notna(row['Debit']) and str(row['Debit']).strip() != ''
        credit = pd.notna(row['Credit']) and str(row['Credit']).strip() != ''
        
        if debit and credit:
            both_filled.append(idx + 1)
    
    if both_filled:
        report['errors'].append(f"Rows with both Debit and Credit filled: {both_filled}")
        report['issues_found'].append('debit_credit_conflict')
        report['is_valid'] = False

def validate_missing_values(df, report):
    """Check for missing values in critical columns"""
    critical_columns = ['Date', 'Balance']
    
    for col in critical_columns:
        missing_count = df[col].isna().sum()
        empty_count = (df[col] == '').sum()
        total_missing = missing_count + empty_count
        
        if total_missing > 0:
            report['warnings'].append(f"Missing values in {col}: {total_missing} rows")
            report['issues_found'].append(f'missing_{col.lower()}')

def validate_numeric_fields(df, report):
    """Validate numeric fields contain proper numbers"""
    numeric_fields = ['Debit', 'Credit', 'Balance']
    
    for field in numeric_fields:
        invalid_values = []
        
        for idx, val in df[field].items():
            if pd.notna(val) and str(val).strip() != '':
                val_str = str(val).strip()
                # Check if it's a valid number
                try:
                    float(val_str)
                except ValueError:
                    invalid_values.append(f"Row {idx + 1}: '{val_str}'")
        
        if invalid_values:
            report['warnings'].append(f"Invalid numeric values in {field}: {invalid_values[:3]}")
            report['issues_found'].append(f'invalid_{field.lower()}')

def validate_balance_consistency(df, report):
    """Check if running balance makes mathematical sense"""
    try:
        inconsistencies = []
        prev_balance = None
        
        for idx, row in df.iterrows():
            current_balance = parse_numeric_value(row['Balance'])
            debit = parse_numeric_value(row['Debit'])
            credit = parse_numeric_value(row['Credit'])
            
            if current_balance is not None and prev_balance is not None:
                expected_balance = prev_balance - (debit or 0) + (credit or 0)
                difference = abs(expected_balance - current_balance)
                
                if difference > 0.01:  # Allow for small rounding differences
                    inconsistencies.append(f"Row {idx + 1}: Expected {expected_balance:.2f}, got {current_balance:.2f}")
            
            if current_balance is not None:
                prev_balance = current_balance
        
        if inconsistencies:
            report['warnings'].append(f"Balance inconsistencies: {inconsistencies[:3]}")
            report['issues_found'].append('balance_inconsistency')
            
    except Exception as e:
        report['warnings'].append(f"Could not validate balance consistency: {str(e)}")

def check_duplicates(df, report):
    """Check for potential duplicate transactions"""
    # Consider transactions duplicate if Date, Narration, and amount are same
    subset_cols = ['Date', 'Narration']
    
    # Add amount column (combine debit and credit)
    df_temp = df.copy()
    df_temp['Amount'] = df_temp['Debit'].fillna(0).astype(str) + df_temp['Credit'].fillna(0).astype(str)
    
    duplicates = df_temp.duplicated(subset=subset_cols + ['Amount'], keep=False)
    duplicate_count = duplicates.sum()
    
    if duplicate_count > 0:
        report['warnings'].append(f"Potential duplicate transactions: {duplicate_count}")
        report['issues_found'].append('duplicates')

def parse_numeric_value(value):
    """Parse a value as numeric, return None if not possible"""
    if pd.isna(value) or str(value).strip() == '':
        return None
    try:
        return float(str(value).strip())
    except ValueError:
        return None

def save_csv_with_validation(csv_string, output_path, validate=True):
    """Save CSV string to file with optional validation and automatic fixing"""
    try:
        # Clean and fix the CSV content first
        cleaned_csv = clean_csv_response(csv_string)
        fixed_csv = fix_incomplete_csv(cleaned_csv)
        
        if validate:
            df, report = validate_csv(fixed_csv)
            
            if not report['is_valid']:
                logger.error("CSV validation failed, but saving fixed version...")
                logger.error(f"Errors: {report['errors']}")
            
            if report['warnings']:
                logger.warning(f"Warnings: {report['warnings']}")
        
        # Save the cleaned CSV
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(fixed_csv)
        
        logger.info(f"CSV saved successfully to: {output_path}")
        
        if validate:
            return df, report
        else:
            return True
            
    except Exception as e:
        logger.error(f"Failed to save CSV: {str(e)}")
        raise

def clean_csv_response(llm_response):
    """Clean LLM response to extract only the CSV content and fix formatting issues"""
    # Remove markdown code blocks if present
    cleaned = re.sub(r'^```csv\s*\n', '', llm_response, flags=re.MULTILINE)
    cleaned = re.sub(r'^```\s*\n', '', cleaned, flags=re.MULTILINE)
    cleaned = re.sub(r'\n```\s*$', '', cleaned, flags=re.MULTILINE)
    
    # Remove any leading/trailing explanatory text
    lines = cleaned.strip().split('\n')
    csv_lines = []
    csv_started = False
    
    for line in lines:
        # Look for CSV header
        if 'Date' in line and 'Narration' in line and ('Debit' in line or 'Credit' in line):
            csv_started = True
            csv_lines.append(line)
        elif csv_started and line.strip():
            # Check if line is complete (has enough commas for all columns)
            comma_count = line.count(',')
            expected_commas = 5  # Date,Cheque No.,Narration,Debit,Credit,Balance = 5 commas
            
            if comma_count >= expected_commas:
                csv_lines.append(line)
            elif comma_count > 0:
                # Incomplete line - log and skip
                logger.warning(f"Skipping incomplete line: {line[:50]}...")
                continue
        elif csv_started and not line.strip():
            # Empty line might indicate end of CSV
            break
    
    return '\n'.join(csv_lines) if csv_lines else cleaned

def fix_incomplete_csv(csv_content):
    """Fix common CSV formatting issues"""
    lines = csv_content.strip().split('\n')
    fixed_lines = []
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Skip header
        if i == 0 or 'Date,' in line:
            fixed_lines.append(line)
            continue
        
        # Count commas to ensure complete rows
        comma_count = line.count(',')
        expected_commas = 5  # Date,Cheque No.,Narration,Debit,Credit,Balance
        
        if comma_count == expected_commas:
            # Complete row
            fixed_lines.append(line)
        elif comma_count < expected_commas:
            # Incomplete row - skip it
            logger.warning(f"Removed incomplete row {i+1}: {line[:50]}...")
            continue
        else:
            # Too many commas - might be an issue with narration field
            # Try to fix by ensuring narration is properly quoted
            fixed_line = fix_narration_field(line)
            fixed_lines.append(fixed_line)
    
    return '\n'.join(fixed_lines)

def fix_narration_field(line):
    """Fix narration field that might contain unescaped commas"""
    parts = line.split(',')
    if len(parts) <= 6:
        return line
    
    # Reconstruct with narration properly combined
    date = parts[0]
    cheque_no = parts[1]
    # Combine middle parts as narration
    narration = ','.join(parts[2:-3])
    debit = parts[-3]
    credit = parts[-2] 
    balance = parts[-1]
    
    return f'{date},{cheque_no},"{narration}",{debit},{credit},{balance}'

def generate_validation_summary(report):
    """Generate a human-readable validation summary"""
    summary = []
    summary.append(f"=== CSV Validation Report ===")
    summary.append(f"Total rows processed: {report['row_count']}")
    summary.append(f"Overall status: {'PASSED' if report['is_valid'] else 'FAILED'}")
    
    if report['errors']:
        summary.append(f"\nERRORS ({len(report['errors'])}):")
        for error in report['errors']:
            summary.append(f"  - {error}")
    
    if report['warnings']:
        summary.append(f"\nWARNINGS ({len(report['warnings'])}):")
        for warning in report['warnings']:
            summary.append(f"  - {warning}")
    
    if not report['errors'] and not report['warnings']:
        summary.append("\n✅ No issues found - CSV is clean and ready to use!")
    
    return '\n'.join(summary)
