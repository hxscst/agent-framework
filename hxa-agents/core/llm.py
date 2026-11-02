import os 
from typing import Literal, Optional, Iterator, Dict
from openai import OpenAI
from .exceptions import LLMException

class HxaAgentsLLM:
    """ hxa llm"""
    def __init__(
            self, 
            model, 
            base_url, 
            api_key, 
            timeout, 
            **kwargs
    ):
        self.model = model
        self.api_key = api_key
        self.base_url = base_url
        self.timeout = timeout
        self.kwargs = kwargs
        self.client = self._create_client()
        
    def _create_client(self) -> OpenAI:
        return OpenAI(
            api_key=self.api_key,
            base_url=self.base_url,
            timeout=self.timeout
        )

    def invoke(self, messages, text={}, temperature: float = 0):
        """
        使用 Responses API 流式调用AI模型
        """
        print(f"{self.model}思考中。。。")

        try:
            collected_content = []
            completed = False
            with self.client.responses.create(
                input=messages, temperature=temperature, model=self.model, stream=True, text=text
            ) as response:
                for event in response:
                    if event.type == "response.output_text.delta":
                        print(event.delta, end="", flush=True)
                        collected_content.append(event.delta)
                    elif event.type == "response.completed":
                        completed = True
                    elif event.type == "response.failed":
                        raise LLMException(f"模型生成失败：{event.response.error}")
                    elif event.type == "response.incomplete":
                        raise LLMException(
                            f"模型生成不完整：{event.response.incomplete_details}"
                        )
                    elif event.type == "error":
                        raise LLMException(event.message)
            print()

            if not completed:
                raise LLMException("流已结束，但未收到 response.completed 事件")
            return "".join(collected_content)
        except Exception as e:
            raise LLMException(f"LLM调用失败: {str(e)}")