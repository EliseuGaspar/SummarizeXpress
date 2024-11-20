from datetime import datetime

from pydantic import BaseModel


class SummaryBase(BaseModel):
    original_text: str
    summarized_text: str
    summary_length: int


class SummaryCreate(SummaryBase):
    pass


class SummaryResponse(SummaryBase):
    id: int
    created_at: datetime
    user_id: int

    class Config:
        orm_mode = True
