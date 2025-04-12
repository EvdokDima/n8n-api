from fastapi import FastAPI
import os
import uvicorn

from api.generate_text import generate_text_router
from api.generate_image import generate_image_router
app = FastAPI()

app.include_router(generate_text_router.router, tags=["Text"])
app.include_router(generate_image_router.router, tags=["Image"])
@app.get("/api")
async def root():
    return {"message": "ok"}

if __name__ == "__main__":
    server_address = os.getenv("SERVER_ADDRESS", "0.0.0.0:8080")
    host, port = server_address.split(":")
    uvicorn.run(app, host=host, port=int(port))