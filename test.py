import fitz
from vertexai.preview.language_models import GenerativeModel

# Step 1: Extract text from the PDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

pdf_text = extract_text_from_pdf("path_to_your_pdf.pdf")

# Step 2: Initialize the generative model
model = GenerativeModel.from_pretrained("text-bison-001")

# Step 3: Create a custom prompt for extraction
prompt = """
Please extract the following information from the text: 
1. Trade Date
2. Transaction Amount
3. Counterparty

Text: {}
""".format(pdf_text)

# Step 4: Get the response from the model
response = model.predict(prompt)
trade_info = response.text.split("\n")
trade_data = {
    "trade_date": trade_info[0].split(":")[1].strip(),
    "transaction_amount": trade_info[1].split(":")[1].strip(),
    "counterparty": trade_info[2].split(":")[1].strip()
}

# Step 5: Output the extracted trade data
print(trade_data)