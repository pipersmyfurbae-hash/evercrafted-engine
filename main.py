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
    return {
        "message": "Engine received input",
        "input_type": data.input_type,
        "output": {
            "title": "Sample Wreath",
            "formula": "crescent",
            "score": 0.82
        }
    }
