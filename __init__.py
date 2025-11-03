"""
Roundtable: Multi-Agent Brainstorming System

A LangChain-powered system where multiple AI models discuss questions
in a collaborative roundtable format.
"""

from .roundtable import Roundtable, Discussion, Participant
from .llm import get_llm_client, get_participant_models, get_moderator_llm

__version__ = "0.1.0"
__all__ = [
    "Roundtable",
    "Discussion",
    "Participant",
    "get_llm_client",
    "get_participant_models",
    "get_moderator_llm",
]

