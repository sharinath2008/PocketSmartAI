from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from services.gemini import analyze_budget


app = FastAPI(
    title="PocketSmart AI",
    description="AI-powered smart budget and recommendation system",
    version="1.0.0"
)

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "result": None
        }
    )


@app.post("/analyze", response_class=HTMLResponse)
async def analyze(
    request: Request,
    income: float = Form(...),
    expenses: str = Form(...)
):
    try:
        result = await analyze_budget(
            income=income,
            expenses=expenses
        )

        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={
                "result": result,
                "income": income,
                "expenses": expenses
            }
        )

    except Exception as error:

        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={
                "result": f"Error: {error}",
                "income": income,
                "expenses": expenses
            }
        )
