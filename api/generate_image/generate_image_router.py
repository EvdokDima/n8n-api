from datetime import datetime
from fastapi import APIRouter

from api.generate_image.requests.generate_image_request import GenerateImageRequest
from api.generate_image.responses.generate_image_response import GenerateImageResponse

from g4f.client import Client
router = APIRouter()

@router.post("/generate-image", response_model=GenerateImageResponse)
async def generate_text(request: GenerateImageRequest):
    client = Client()

    response = await client.images.async_generate(
        model=request.model.value,
        prompt=request.content,
        response_format="url"
    )

    print(f"Generated image URL: {response.data[0].url}")

    return GenerateImageResponse(
        model=request.model,
        image_url=response.data[0].url,
        generated_at=datetime.utcnow(),
    )