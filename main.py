from fastapi import FastAPI

app = FastAPI()


@app.post("/predict")
async def root():
    return {"message": "Hello world"}



@app.get("/predict")
async def root():
    return {"message": "Hello india"}