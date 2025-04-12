from pydantic import BaseModel
from api.generate_image.enums.ai_model_enum import AIModel

class GenerateImageRequest(BaseModel):
    model: AIModel
    content: str