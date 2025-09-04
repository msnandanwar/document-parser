# Output Files Directory

Generated CSV files will be saved here.

## File Structure
Each processed PDF generates:
- `filename.csv` - Main structured data output
- Validation reports (if errors occur)

## Data Security
- This directory is ignored by git to protect sensitive data
- Clean output files before sharing the project
- Generated files contain structured financial data

## Sample Output Format
```csv
Date,Cheque No.,Narration,Debit,Credit,Balance
2024-01-15,,Opening Balance,,,10000.00
2024-01-16,123456,Salary Credit,,5000.00,15000.00
2024-01-17,,ATM Withdrawal,500.00,,14500.00
```
