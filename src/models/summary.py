from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from src.core.database import base


class Summary(base):

    __tablename__: str = "summaries"
    __objectID: str = 'summariesModel'

    id = Column(Integer, primary_key=True, index=True)
    original_text = Column(Text, nullable=False)
    summarized_text = Column(Text, nullable=False)
    summary_length = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

    user = relationship("User", back_populates="summaries")

    def __repr__(self):
        return f"<Summary(user_id={self.user_id}, summary_length={self.summary_length})>"
