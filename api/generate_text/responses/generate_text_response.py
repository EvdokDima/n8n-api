from datetime import datetime
from pydantic import BaseModel
from api.generate_text.enums.ai_model_enum import AIModel

class GenerateTextResponse(BaseModel):
    model: AIModel
    text: str
    generated_at: datetime