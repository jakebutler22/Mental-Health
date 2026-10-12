from typing import Literal, Annotated
from pydantic import BaseModel, ConfigDict, Field

class StrictModel(BaseModel):
    model_config = ConfigDict(extra='forbid')

class SessionStart(StrictModel):
    request_id: str = Field(min_length=1, max_length=100, pattern=r'^[a-zA-Z0-9_-]+$')
    skill: Literal['breathing', 'grounding']
    conversation_id: str | None = None
    recommendation_request_id: str | None = None

class SessionUpdate(StrictModel):
    version: int = Field(ge=0, strict=True)
    state: Literal['active', 'paused', 'completed', 'stopped', 'interrupted']
    active_elapsed_ms: int = Field(ge=0, le=86400000, strict=True)
    step: int = Field(default=0, ge=0, le=5, strict=True)
    cycles: int = Field(default=0, ge=0, le=6, strict=True)
    skipped_steps: list[Annotated[int, Field(strict=True)]] = Field(default_factory=list, max_length=5)

class PreferencesUpdate(StrictModel):
    explicit_balloon_color: Literal['red', 'sage', 'blue', 'plum'] | None = None
    simple_view: bool | None = None
    reduced_motion: bool | None = None

class ChatMessage(StrictModel):
    request_id: str = Field(min_length=1, max_length=100, pattern=r'^[a-zA-Z0-9_-]+$')
    text: str = Field(min_length=1, max_length=500)
