from fastapi import FastAPI

app = FastAPI(title="Orders")


@app.get("/health")
def health():
    return {"status": "ok"}
