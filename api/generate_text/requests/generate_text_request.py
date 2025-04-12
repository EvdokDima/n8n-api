from pydantic import BaseModel
from api.generate_text.enums.ai_model_enum import AIModel

class GenerateTextRequest(BaseModel):
    model: AIModel
    content: str