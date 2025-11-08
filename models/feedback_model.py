from pydantic import BaseModel
from datetime import datetime

class Feedback(BaseModel):
    user_id: int
    item_id: int
    action: str
    timestamp: datetime
