"""
Roundtable: Multi-agent brainstorming discussion system.

Multiple AI models discuss a question in rounds, building on each other's ideas.
"""

from typing import List, Dict, Optional
from dataclasses import dataclass, field
from langchain.schema import HumanMessage, AIMessage, SystemMessage

# Handle both package and standalone imports
try:
    from .llm import get_llm_client, get_participant_models, get_moderator_llm
except ImportError:
    from llm import get_llm_client, get_participant_models, get_moderator_llm


@dataclass
class Participant:
    """A participant in the roundtable discussion."""
    name: str
    label: str
    llm: any
    contributions: List[str] = field(default_factory=list)


@dataclass
class Discussion:
    """A complete roundtable discussion."""
    question: str
    rounds: List[Dict] = field(default_factory=list)
    final_summary: Optional[str] = None


class Roundtable:
    """
    Manages a multi-agent roundtable discussion.
    
    Multiple AI models brainstorm together, building on each other's ideas
    across multiple rounds of discussion.
    """
    
    def __init__(
        self,
        max_rounds: int = 3,
        temperature: float = 0.7,
        moderator_enabled: bool = True,
        tools_enabled: bool = False,
    ):
        """
        Initialize the roundtable.
        
        Args:
            max_rounds: Maximum number of discussion rounds
            temperature: Temperature for participant models (creativity level)
            moderator_enabled: Whether to use a moderator to guide discussion
            tools_enabled: Whether to enable external knowledge tools
        """
        self.max_rounds = max_rounds
        self.temperature = temperature
        self.moderator_enabled = moderator_enabled
        self.tools_enabled = tools_enabled
        
        # Initialize participants
        self.participants = self._initialize_participants()
        
        # Initialize moderator if enabled
        self.moderator = get_moderator_llm() if moderator_enabled else None
        
        # Load tools if enabled
        self.tools = None
        if tools_enabled:
            try:
                try:
                    from .tools import AVAILABLE_TOOLS
                except ImportError:
                    from tools import AVAILABLE_TOOLS
                self.tools = AVAILABLE_TOOLS
                if self.tools:
                    print(f"✅ Loaded {len(self.tools)} external knowledge tools")
            except Exception as e:
                print(f"⚠️ Failed to load tools: {e}")
                self.tools = None
        
        if not self.participants:
            raise ValueError(
                "No participants configured. Set MODEL1, API_KEY1, etc. in .env"
            )
    
    def _initialize_participants(self) -> List[Participant]:
        """Initialize all participant LLMs from configuration."""
        participants = []
        
        for config in get_participant_models():
            llm = get_llm_client(
                model=config["name"],
                api_key=config["api_key"],
                base_url=config["base_url"],
                temperature=self.temperature,
            )
            
            participant = Participant(
                name=config["name"],
                label=config["label"],
                llm=llm,
            )
            participants.append(participant)
        
        return participants
    
    def discuss(self, question: str, verbose: bool = True) -> Discussion:
        """
        Conduct a roundtable discussion on a question.
        
        Args:
            question: The question or topic to discuss
            verbose: Whether to print progress
        
        Returns:
            Complete discussion with all rounds and summary
        """
        discussion = Discussion(question=question)
        
        if verbose:
            print(f"\n🎯 Question: {question}\n")
            print(f"👥 Participants: {len(self.participants)}")
            for p in self.participants:
                print(f"   • {p.label}: {p.name}")
            if self.tools_enabled and self.tools:
                print(f"🔧 Tools: {len(self.tools)} available")
                for tool in self.tools:
                    print(f"   • {tool.name}")
            print(f"\n{'='*80}\n")
        
        # Conduct discussion rounds
        for round_num in range(1, self.max_rounds + 1):
            if verbose:
                print(f"🔄 Round {round_num}/{self.max_rounds}")
                print(f"{'-'*80}\n")
            
            round_data = self._conduct_round(round_num, discussion, verbose)
            discussion.rounds.append(round_data)
        
        # Generate final summary
        if self.moderator_enabled:
            discussion.final_summary = self._generate_summary(discussion, verbose)
        
        return discussion
    
    def _conduct_round(
        self,
        round_num: int,
        discussion: Discussion,
        verbose: bool,
    ) -> Dict:
        """Conduct a single round of discussion."""
        round_data = {
            "round_number": round_num,
            "contributions": []
        }
        
        for participant in self.participants:
            # Build context from previous contributions
            context = self._build_context(discussion, participant)
            
            # Get participant's contribution
            prompt = self._create_participant_prompt(
                discussion.question,
                round_num,
                context,
            )
            
            response = participant.llm.invoke(prompt)
            contribution = response.content
            
            # Store contribution
            participant.contributions.append(contribution)
            round_data["contributions"].append({
                "participant": participant.label,
                "model": participant.name,
                "text": contribution,
            })
            
            if verbose:
                print(f"💬 {participant.label} ({participant.name}):")
                print(f"{contribution}\n")
        
        return round_data
    
    def _build_context(self, discussion: Discussion, current_participant: Participant) -> str:
        """Build context string from previous discussion rounds."""
        if not discussion.rounds:
            return ""
        
        context_parts = []
        
        for round_data in discussion.rounds:
            round_num = round_data["round_number"]
            context_parts.append(f"\n--- Round {round_num} ---")
            
            for contrib in round_data["contributions"]:
                if contrib["participant"] != current_participant.label:
                    context_parts.append(
                        f"\n{contrib['participant']}: {contrib['text']}"
                    )
        
        # Add current round contributions (from other participants)
        if discussion.rounds and len(discussion.rounds[-1]["contributions"]) > 0:
            latest_round = discussion.rounds[-1]
            for contrib in latest_round["contributions"]:
                if contrib["participant"] != current_participant.label:
                    context_parts.append(
                        f"\n{contrib['participant']}: {contrib['text']}"
                    )
        
        return "\n".join(context_parts)
    
    def _create_participant_prompt(
        self,
        question: str,
        round_num: int,
        context: str,
    ) -> List:
        """Create the prompt for a participant's contribution."""
        system_msg = (
            "You are a thoughtful participant in a roundtable discussion. "
            "Your goal is to contribute meaningful insights, build on others' ideas, "
            "and help the group reach a well-reasoned conclusion."
        )
        
        # Add tool information if available
        if self.tools:
            tools_desc = "\n\nAvailable tools for research:\n"
            for tool in self.tools:
                tools_desc += f"- {tool.name}: {tool.description}\n"
            system_msg += tools_desc
        
        if round_num == 1:
            user_msg = (
                f"We're discussing: {question}\n\n"
                f"This is Round {round_num}. Please share your initial thoughts and insights. "
                f"Be specific, insightful, and concise (2-4 sentences)."
            )
        else:
            user_msg = (
                f"We're discussing: {question}\n\n"
                f"This is Round {round_num}. Here's what others have said:\n"
                f"{context}\n\n"
                f"Please respond by:\n"
                f"1. Building on the strongest ideas\n"
                f"2. Adding new perspectives or addressing gaps\n"
                f"3. Helping move toward a conclusion\n\n"
                f"Keep it concise (2-4 sentences)."
            )
        
        return [
            SystemMessage(content=system_msg),
            HumanMessage(content=user_msg),
        ]
    
    def _generate_summary(self, discussion: Discussion, verbose: bool) -> str:
        """Generate a final summary of the discussion using the moderator."""
        if not self.moderator:
            return ""
        
        if verbose:
            print(f"\n{'='*80}")
            print("📊 Generating Final Summary...\n")
        
        # Compile all contributions
        all_contributions = []
        for round_data in discussion.rounds:
            round_num = round_data["round_number"]
            all_contributions.append(f"\n--- Round {round_num} ---")
            for contrib in round_data["contributions"]:
                all_contributions.append(
                    f"\n{contrib['participant']}: {contrib['text']}"
                )
        
        contributions_text = "\n".join(all_contributions)
        
        prompt = [
            SystemMessage(content=(
                "You are a skilled moderator synthesizing a roundtable discussion. "
                "Your task is to create a clear, balanced summary that captures:\n"
                "1. Key insights and agreements\n"
                "2. Diverse perspectives\n"
                "3. Practical conclusions or recommendations\n"
                "Be concise but comprehensive."
            )),
            HumanMessage(content=(
                f"Question discussed: {discussion.question}\n\n"
                f"Discussion:\n{contributions_text}\n\n"
                f"Please provide a final summary of this roundtable discussion."
            )),
        ]
        
        response = self.moderator.invoke(prompt)
        summary = response.content
        
        if verbose:
            print(f"📋 Final Summary:")
            print(f"{summary}\n")
        
        return summary
    
    def export_discussion(self, discussion: Discussion, format: str = "markdown") -> str:
        """
        Export the discussion in various formats.
        
        Args:
            discussion: The discussion to export
            format: Export format (markdown, json, text)
        
        Returns:
            Formatted discussion string
        """
        if format == "markdown":
            return self._export_markdown(discussion)
        elif format == "json":
            import json
            return json.dumps(discussion.__dict__, indent=2)
        else:  # text
            return self._export_text(discussion)
    
    def _export_markdown(self, discussion: Discussion) -> str:
        """Export discussion as markdown."""
        lines = [
            f"# Roundtable Discussion\n",
            f"## Question\n",
            f"{discussion.question}\n",
            f"\n## Discussion\n",
        ]
        
        for round_data in discussion.rounds:
            round_num = round_data["round_number"]
            lines.append(f"\n### Round {round_num}\n")
            
            for contrib in round_data["contributions"]:
                lines.append(
                    f"\n**{contrib['participant']}** ({contrib['model']}):\n"
                )
                lines.append(f"{contrib['text']}\n")
        
        if discussion.final_summary:
            lines.append(f"\n## Final Summary\n")
            lines.append(f"{discussion.final_summary}\n")
        
        return "\n".join(lines)
    
    def _export_text(self, discussion: Discussion) -> str:
        """Export discussion as plain text."""
        lines = [
            f"ROUNDTABLE DISCUSSION",
            f"=" * 80,
            f"\nQuestion: {discussion.question}\n",
        ]
        
        for round_data in discussion.rounds:
            round_num = round_data["round_number"]
            lines.append(f"\n--- Round {round_num} ---\n")
            
            for contrib in round_data["contributions"]:
                lines.append(
                    f"{contrib['participant']} ({contrib['model']}):"
                )
                lines.append(f"{contrib['text']}\n")
        
        if discussion.final_summary:
            lines.append(f"\n{'-' * 80}")
            lines.append(f"FINAL SUMMARY:")
            lines.append(f"{'-' * 80}")
            lines.append(f"{discussion.final_summary}\n")
        
        return "\n".join(lines)

