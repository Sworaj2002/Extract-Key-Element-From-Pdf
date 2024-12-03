# Extract-Key-Element-From-Pdf
This project uses GPT-4 and PyMuPDF to extract and analyze key insights from business/financial PDFs like investor call transcripts. It focuses on growth prospects, business changes, and earnings impact, providing investors with a quick, automated summary of critical information for informed decision-making
# Investor Insight Analysis from PDF using GPT-4

This project extracts and analyzes insights from a PDF document related to business performance using OpenAI's GPT-4. It is specifically designed for investors to get summarized insights on topics like growth prospects, business changes, and earnings impact from financial reports or investor call transcripts

## Requirements

- Python 3.x
- `PyMuPDF` (fitz) for PDF reading
- `openai` library for GPT-4 integration
- An OpenAI API key to access GPT-4

## Setup

python -m venv env
env/bin/activate  # On Windows use `env\Scripts\activate`.

pip install -r requirements.txt
## Set up OpenAI API Key:
Replace "YOUR_OPENAI_API_KEY" in app.py with your actual OpenAI API key to authenticate the GPT-4 requests.
1. Prepare your PDF file:
Make sure your file is in PDF format and contains text that is readable (not an image-based PDF).
2. Run the analysis:
To extract and analyze insights from the PDF, run the following command in your terminal:


python app.py


### 1. Clone the repository:
   ```bash
   git clone https://github.com/Sworaj2002/Extract-Key-Element-From-Pdf
   cd Extract-Key-Element-From-Pdf
