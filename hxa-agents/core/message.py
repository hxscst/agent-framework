
from typing import Literal, Dict, Any, Optional
from datetime import datetime 
from pydantic import BaseModel

MessageRole = Literal["user", "assistant", "tool", "system"]

class Message(BaseModel):

    role: MessageRole
    content: str
    timestamp: datetime = None
    metadata: Optional[Dict[str, Any]] = None

    def __init__(self, role: MessageRole, content, timestamp, **kwargs):
        self.role = role
        self.content = content
        self.timestamp = timestamp
        self.kwargs = kwargs

    def to_dict(self) :
        return {
            "role": self.role,
            "content": self.content
        }

    def __str__(self) :
        return f"[{self.role}] {self.content}"