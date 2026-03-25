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

def build_variant(vibe, formula, palette, score, suffix):
    return {
        "title": f"{vibe.title()} Wreath {suffix}",
        "formula": formula,
        "palette": palette,
        "score": score
    }

@app.post("/run-engine")
def run_engine(data: EngineInput):
    feeling = data.input_data.get("feeling", "").lower()

    if "calm" in feeling or "peaceful" in feeling:
        base = {
            "vibe": "serene and airy",
            "formula": "open_arc",
            "palette": ["soft green", "muted white", "sage"]
        }
    elif "romantic" in feeling or "love" in feeling:
        base = {
            "vibe": "soft and intimate",
            "formula": "crescent",
            "palette": ["blush", "rose", "cream"]
        }
    elif "bold" in feeling or "dramatic" in feeling:
        base = {
            "vibe": "strong and sculptural",
            "formula": "radial_burst",
            "palette": ["black", "deep red", "gold"]
        }
    else:
        base = {
            "vibe": "natural and balanced",
            "formula": "organic",
            "palette": ["neutral beige", "greenery"]
        }

    outputs = [
        build_variant(base["vibe"], base["formula"], base["palette"], 0.83, "A"),
        build_variant(base["vibe"], base["formula"], base["palette"], 0.86, "B"),
        build_variant(base["vibe"], base["formula"], base["palette"], 0.88, "C"),
    ]

    return {
        "message": "Engine generated multiple designs",
        "input": feeling,
        "outputs": outputs
    }
