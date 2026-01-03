from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def main_page():
    return {"hi": "u da realest main page"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)

