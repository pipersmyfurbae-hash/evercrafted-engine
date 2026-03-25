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

def build_option(vibe, formula, palette, density, score):
    return {
        "title": f"{vibe.title()} Wreath",
        "formula": formula,
        "palette": palette,
        "density": density,
        "score": score
    }

@app.post("/run-engine")
def run_engine(data: EngineInput):
    feeling = data.input_data.get("feeling", "").lower()

    # Base emotion mapping
    if "calm" in feeling or "peaceful" in feeling:
        base_palette = ["soft green", "muted white", "sage"]
    elif "romantic" in feeling or "love" in feeling:
        base_palette = ["blush", "rose", "cream"]
    elif "bold" in feeling or "dramatic" in feeling:
        base_palette = ["black", "deep red", "gold"]
    else:
        base_palette = ["neutral beige", "greenery"]

    # Three distinct design directions
    option_1 = build_option(
        "light and minimal",
        "open_arc",
        base_palette,
        "low",
        0.82
    )

    option_2 = build_option(
        "balanced and classic",
        "crescent",
        base_palette,
        "medium",
        0.86
    )

    option_3 = build_option(
        "full and dramatic",
        "radial_burst",
        base_palette,
        "high",
        0.89
    )

    return {
        "message": "Engine generated distinct design options",
        "input": feeling,
        "outputs": [option_1, option_2, option_3]
    }
