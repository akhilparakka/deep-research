from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
REASONING_MODEL_NAME = "o4-mini-2025-04-16"
BASIC_MODEL_NAME = "gpt-4o-2024-08-06"
PORT = int(os.getenv("PORT", "8000"))
TEAM_MEMBERS = ["researcher", "coder", "browser", "reporter"]

__all__ = [
    "REASONING_MODEL_NAME",
    "BASIC_MODEL_NAME",
    "OPENAI_API_KEY",
    "TEAM_MEMBERS",
    "PORT",
]
