from pydantic import BaseModel, conint
from api.generate_image.enums.ai_model_enum import AIModel

class GenerateImageRequest(BaseModel):
    model: AIModel
    content: str
    compression_quality: conint(ge=0, le=100)