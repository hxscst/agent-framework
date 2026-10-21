from hello_agents import SimpleAgent, HelloAgentsLLM
from hello_agents.tools import CalculatorTool
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == "__main__":
    
    llm = HelloAgentsLLM(
        api_key = os.getenv("LLM_API_KEY"),
        base_url= os.getenv("LLM_BASE_URL"),
        model = os.getenv("LLM_MODEL_ID")
    )

    agent = SimpleAgent(
        name="AI助手",
        llm=llm,
        system_prompt="你是一个有用的AI助手"
    )

    response = agent.run("你好！请介绍一下自己")
    print(response)
    calculator = CalculatorTool()
    response = agent.run("请帮我计算 2 + 3 * 4")
    print(response)

    # 查看对话历史
    print(f"历史消息数: {len(agent.get_history())}")
