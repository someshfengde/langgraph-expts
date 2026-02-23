"""Configuration helpers for LangGraph experiments."""

from dataclasses import dataclass
import os

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    """Runtime settings loaded from environment variables."""

    openai_api_key: str | None
    anthropic_api_key: str | None
    langsmith_api_key: str | None



def load_settings() -> Settings:
    """Load environment variables from .env and return typed settings."""

    load_dotenv()
    return Settings(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"),
        langsmith_api_key=os.getenv("LANGSMITH_API_KEY"),
    )
