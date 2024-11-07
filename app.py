import fitz  # PyMuPDF for PDF reading
import openai  # OpenAI for GPT-4 analysis

# Replace with your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

def extract_text_from_pdf(pdf_path):
    """Extracts text from each page of a PDF document."""
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text("text")
    return text

def preprocess_text(text):
    """Cleans the text for easier analysis."""
    # Basic cleaning steps (e.g., removing extra spaces)
    text = " ".join(text.split())
    return text

def gpt_extract_insights(text, prompt):
    """Uses GPT API to generate insights based on a prompt."""
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt + "\n\n" + text,
        max_tokens=300,
        temperature=0.5
    )
    return response.choices[0].text.strip()

def analyze_for_investor(pdf_path):
    # Step 1: Extract and preprocess text from PDF
    raw_text = extract_text_from_pdf(pdf_path)
    clean_text = preprocess_text(raw_text)
    
    # Step 2: Define specific prompts for GPT-4 to retrieve insights
    prompts = {
        "Growth Prospects": "Extract future growth prospects from the following text: ",
        "Business Changes": "Identify any significant changes in the business structure or strategy: ",
        "Earnings Impact": "Highlight key factors that could impact next year's earnings and growth: "
    }
    
    # Step 3: Retrieve insights for each prompt
    insights = {}
    for category, prompt in prompts.items():
        insights[category] = gpt_extract_insights(clean_text, prompt)
    
    return insights

# Example usage
pdf_path = "path/to/your/Document.pdf"  # Replace with the actual path to your PDF
report = analyze_for_investor(pdf_path)
print(report)
