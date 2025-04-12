from api.generate_image.requests.generate_image_request import GenerateImageRequest
from g4f.client import Client

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from io import BytesIO
from PIL import Image
import pillow_avif
import requests

router = APIRouter()

@router.post("/generate-image", response_class=StreamingResponse)
async def generate_avif_image(request: GenerateImageRequest):
    try:
        client = Client()
        response = await client.images.async_generate(
            model=request.model.value,
            prompt=request.content,
            response_format="url"
        )

        img_data = requests.get(response.data[0].url).content
        img = Image.open(BytesIO(img_data))

        output_buffer = BytesIO()
        img.save(
            output_buffer,
            format="AVIF",
            quality=request.compression_quality,
            save_all=True
        )
        output_buffer.seek(0)

        return StreamingResponse(
            output_buffer,
            media_type="image/avif",
            headers={"Content-Disposition": "attachment; filename=image.avif"}
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))