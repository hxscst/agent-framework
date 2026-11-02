from typing import Optional
from .message import Message
from .llm import HxaAgentsLLM
from .config import Config
from abc import ABC, abstractmethod

class Agent(ABC):
    def __init__(
            self, 
            name:str,
            llm: HxaAgentsLLM,
            system_prompt: Optional[str] = None,
            config: Optional[Config]  = None
    ):
        self.config = config 
        self.system_prompt = system_prompt
        self.name = name
        self.llm = llm
        self._history: list[Message] = []

    @abstractmethod
    def run(self, input_text: str, **kwargs) -> str:
        """运行Agent"""
        pass

    def add_message(self, message: Message) :
        """添加消息"""
        self._history.append(message)

    def get_history(self) -> list[Message]:
        """返回所有消息"""
        return self._history.copy()

    def clear_history(self):
        """清空消息"""
        self._history.clear()