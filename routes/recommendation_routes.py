from fastapi import APIRouter
from typing import List
from models.feedback_model import Feedback

router = APIRouter()

# GET endpoint
@router.get("/recommendation")
def get_recommendation():
    return {"message": "Here are some recommendations"}

# POST endpoint
@router.post("/recommend/track-action")
def track_action(feedbacks: List[Feedback]):
    # This is where you would process/save feedbacks
    return {"received_feedback": feedbacks}
