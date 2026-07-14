from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class GrayConfigSchema(BaseModel):
    """灰度配置数据模型，强约束，防止配置写错"""
    oauth_force_claude_version_check: bool
    strip_orphan_tool_block_strict: bool
    enable_unsigned_thinking_downgrade: bool
    third_party_proxy_support: List[str]


class AgentRequest(BaseModel):
    """Agent接收用户请求体"""
    user_query: str
    session_id: Optional[str] = None
    model_provider: str = Field(default="azure", description="第三方代理厂商")


class AgentResponse(BaseModel):
    """Agent输出响应体"""
    content: str
    thinking_block: Optional[str] = None
    tool_calls: List[Dict[str, Any]] = Field(default_factory=list)
    provider: str


class ToolCallBlock(BaseModel):
    """工具调用结构化块"""
    tool_name: str
    arguments: Dict[str, Any]
