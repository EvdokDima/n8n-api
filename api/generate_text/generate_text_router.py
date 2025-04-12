from datetime import datetime
from fastapi import APIRouter

from api.generate_text.requests.generate_text_request import GenerateTextRequest
from api.generate_text.responses.generate_text_response import GenerateTextResponse

from g4f.client import Client

router = APIRouter()

@router.post("/generate-text", response_model=GenerateTextResponse)
async def generate_text(request: GenerateTextRequest):

    client = Client()

    response = client.chat.completions.create(
        model=request.model,
        messages=[{"role": "user", "content": request.content}],
        web_search=False
    )

    return GenerateTextResponse(
        model=request.model,
        text=response.choices[0].message.content,
        generated_at=datetime.utcnow(),
    )