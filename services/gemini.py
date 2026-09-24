import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY is missing. "
        "Create a .env file and add your Gemini API key."
    )


client = genai.Client(
    api_key=API_KEY
)


async def analyze_budget(income: float, expenses: str) -> str:

    prompt = f"""
You are PocketSmart AI, a friendly personal budgeting assistant.

Analyze the user's monthly financial information.

Monthly income:
₹{income:,.2f}

Monthly expenses:
{expenses}

Give the user a useful and easy-to-understand financial analysis.

Include:

1. Total estimated expenses
2. Remaining money
3. Major spending categories
4. Spending observations
5. Practical ways to save money
6. A suggested monthly budget
7. A short summary

Rules:

- Use Indian Rupees (₹).
- Do not make assumptions about information that was not provided.
- Do not provide investment, stock-market, cryptocurrency,
  or other high-risk financial advice.
- Keep the recommendations practical.
- Use headings and bullet points.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
