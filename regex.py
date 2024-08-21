import re
import pandas as pd

# Example prompt response from Gemini LLM
response_text = """
Trade ID: 001
Trade Date: 2024-08-20
Transaction Amount: $1,500.50
Status: Completed

Trade ID: 002
Trade Date: 2024-08-21
Transaction Amount: $2,300.75
Status: Pending

Trade ID: 003
Trade Date: 2024-08-22
Transaction Amount: $3,450.00
Status: Failed
"""

# Initialize lists to hold extracted data
trade_ids = []
trade_dates = []
transaction_amounts = []
statuses = []

# Define regex patterns to extract entities
trade_id_regex = r"Trade ID:\s*(\d+)"
trade_date_regex = r"Trade Date:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})"
transaction_amount_regex = r"Transaction Amount:\s*\$([0-9,]+\.\d{2})"
status_regex = r"Status:\s*(\w+)"

# Extract data using regex
trade_ids = re.findall(trade_id_regex, response_text)
trade_dates = re.findall(trade_date_regex, response_text)
transaction_amounts = re.findall(transaction_amount_regex, response_text)
statuses = re.findall(status_regex, response_text)

# Clean the transaction amounts (remove commas and convert to float)
transaction_amounts = [float(amount.replace(",", "")) for amount in transaction_amounts]

# Create a dictionary with the extracted data
data = {
    "Trade ID": trade_ids,
    "Trade Date": trade_dates,
    "Transaction Amount": transaction_amounts,
    "Status": statuses
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)