import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv

from agno.tools.duckduckgo import DuckDuckGoTools

load_dotenv()

def build_agent():
    return Agent(
        model=Groq(id="llama-3.3-70b-versatile"),
        tools=[DuckDuckGoTools],
        markdown=True,
        instructions="Your are a helpful and expert travel agent. You create detailed travel itineraries for users based on their preferences.",
        add_datetime_to_context=True
    )

agent = build_agent()

agent.print_response("Is it safe to travel to UAE today?")
