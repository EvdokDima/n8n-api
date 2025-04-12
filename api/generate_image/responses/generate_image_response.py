from datetime import datetime
from pydantic import BaseModel

from api.generate_image.enums.ai_model_enum import AIModel


class GenerateImageResponse(BaseModel):
    model: AIModel
    image_url: str
    generated_at: datetime