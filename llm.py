"""
LLM client configuration for Roundtable multi-agent discussions.

Supports any OpenAI-compatible API endpoint.
Copied from tau_helper with enhancements for multi-agent roundtable.
"""

import os
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables from .env
_env_path = Path(__file__).parent / ".env"
load_dotenv(_env_path)


def get_llm_client(
    model: Optional[str] = None,
    api_key: Optional[str] = None,
    base_url: Optional[str] = None,
    temperature: float = 0.7,  # Higher default for creative brainstorming
    max_tokens: Optional[int] = None,
    seed: Optional[int] = None,
) -> ChatOpenAI:
    """
    Create a LangChain ChatOpenAI client.
    
    Args:
        model: Model name (defaults to DEFAULT_MODEL from .env)
        api_key: API key (defaults to DEFAULT_API_KEY from .env)
        base_url: API base URL (defaults to DEFAULT_BASE_URL from .env)
        temperature: Sampling temperature (default: 0.7 for creative discussions)
        max_tokens: Maximum tokens in response (optional)
        seed: Random seed for reproducibility (optional)
    
    Returns:
        Configured ChatOpenAI instance
    """
    model = model or os.getenv("DEFAULT_MODEL", "gpt-4o")
    api_key = api_key or os.getenv("DEFAULT_API_KEY")
    base_url = base_url or os.getenv("DEFAULT_BASE_URL", "https://api.openai.com/v1")
    
    if not api_key:
        raise ValueError(
            "API key not provided. Set DEFAULT_API_KEY in .env or pass api_key parameter."
        )
    
    config = {
        "model": model,
        "openai_api_key": api_key,
        "openai_api_base": base_url,
        "temperature": temperature,
    }
    
    if max_tokens:
        config["max_tokens"] = max_tokens
    
    if seed is not None:
        config["seed"] = seed
    
    return ChatOpenAI(**config)


def get_participant_models() -> list[dict]:
    """
    Get all configured participant models for the roundtable.
    
    Returns:
        List of model configurations (name, key, base_url)
    """
    participants = []
    
    # Check for MODEL1, MODEL2, MODEL3, etc.
    i = 1
    while True:
        model = os.getenv(f"MODEL{i}")
        api_key = os.getenv(f"API_KEY{i}")
        base_url = os.getenv(f"BASE_URL{i}", "https://api.openai.com/v1")
        
        if not model or not api_key:
            break
            
        participants.append({
            "name": model,
            "api_key": api_key,
            "base_url": base_url,
            "label": f"Participant {i}"
        })
        i += 1
    
    # Fallback to default if no participants configured
    if not participants:
        default_model = os.getenv("DEFAULT_MODEL")
        default_key = os.getenv("DEFAULT_API_KEY")
        default_url = os.getenv("DEFAULT_BASE_URL", "https://api.openai.com/v1")
        
        if default_model and default_key:
            participants.append({
                "name": default_model,
                "api_key": default_key,
                "base_url": default_url,
                "label": "Participant 1"
            })
    
    return participants


def get_moderator_llm(
    model: Optional[str] = None,
    api_key: Optional[str] = None,
    base_url: Optional[str] = None,
    temperature: float = 0.3,  # Lower for more structured facilitation
) -> ChatOpenAI:
    """
    Get the moderator LLM that facilitates the discussion.
    
    Args:
        model: Model name (defaults to MODERATOR_MODEL from .env)
        api_key: API key (defaults to MODERATOR_API_KEY from .env)
        base_url: API base URL (defaults to MODERATOR_BASE_URL from .env)
        temperature: Sampling temperature (default: 0.3 for consistent facilitation)
    
    Returns:
        Configured ChatOpenAI instance
    """
    model = model or os.getenv("MODERATOR_MODEL")
    api_key = api_key or os.getenv("MODERATOR_API_KEY")
    base_url = base_url or os.getenv("MODERATOR_BASE_URL")
    
    # Fallback to default model if moderator not configured
    if not model or not api_key:
        model = os.getenv("DEFAULT_MODEL", "gpt-4o")
        api_key = os.getenv("DEFAULT_API_KEY")
        base_url = os.getenv("DEFAULT_BASE_URL", "https://api.openai.com/v1")
    
    return get_llm_client(
        model=model,
        api_key=api_key,
        base_url=base_url,
        temperature=temperature,
    )

