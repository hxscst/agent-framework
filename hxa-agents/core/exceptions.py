class HxaAgentsException(Exception):
    """HxaAgents基础异常类"""
    pass

class LLMException(HxaAgentsException):
    """LLM相关异常"""
    pass

class AgentException(HxaAgentsException):
    """Agent相关异常"""
    pass

class ConfigException(HxaAgentsException):
    """配置相关异常"""
    pass

class ToolException(HxaAgentsException):
    """工具相关异常"""
    pass