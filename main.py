from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import os
import uvicorn

from api.generate_text import generate_text_router
from api.generate_image import generate_image_router
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:63342",
    "http://127.0.0.1",
    "http://127.0.0.1:8080",
    "http://127.0.0.1:63342",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Разрешаем все методы
    allow_headers=["*"],  # Разрешаем все заголовки
)

app.include_router(generate_text_router.router, tags=["Text"])
app.include_router(generate_image_router.router, tags=["Image"])
@app.get("/api")
async def root():
    return {"message": "ok"}

if __name__ == "__main__":
    server_address = os.getenv("SERVER_ADDRESS", "0.0.0.0:8080")
    host, port = server_address.split(":")
    uvicorn.run(app, host=host, port=int(port))