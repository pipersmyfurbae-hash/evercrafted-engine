from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class EngineInput(BaseModel):
    input_type: str
    input_data: dict
    constraints: dict = {}

@app.get("/")
def root():
    return {"status": "Evercrafted Engine Running"}

@app.post("/run-engine")
def run_engine(data: EngineInput):
    feeling = data.input_data.get("feeling", "").lower()

    if "calm" in feeling or "peaceful" in feeling:
        palette = ["soft green", "muted white", "sage"]
        formula = "open_arc"
        vibe = "serene and airy"
    elif "romantic" in feeling or "love" in feeling:
        palette = ["blush", "rose", "cream"]
        formula = "crescent"
        vibe = "soft and intimate"
    elif "bold" in feeling or "dramatic" in feeling:
        palette = ["black", "deep red", "gold"]
        formula = "radial_burst"
        vibe = "strong and sculptural"
    else:
        palette = ["neutral beige", "greenery"]
        formula = "organic"
        vibe = "natural and balanced"

    return {
        "message": "Engine processed emotion",
        "input": feeling,
        "output": {
            "title": f"{vibe.title()} Wreath",
            "formula": formula,
            "palette": palette,
            "score": 0.85
        }
    }
