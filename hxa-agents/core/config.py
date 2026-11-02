"""配置管理"""
import os 
from pydantic import BaseModel

class Config(BaseModel):

    # LLM配置
    default_model: str = "gpt-6.1-terra"
    default_provider: str = "OpenAI"
    temperature: float = 0.2

    # 系统配置
    debug: bool = False
    log_level: str = "INFO"

    # 其他配置

    @classmethod
    def from_env(cls) -> "Config":
        """从环境变量创建配置。"""
        return cls(
            debug = os.getenv("DEBUG", False).lower() == "true",
            log_level=os.getenv("LOG_LEVEL", "INFO")
        )

    def to_dict(self):
        """转换为字典"""
        return self.model_dump()