import os
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

from multi_tool_agent import prompt

def get_custom_message(paths: str) -> str:
    """Prints a custom message when the user asks for it.

    Args:
        None.

    Returns:
        dict: status and result.
    """
    return "This is a custom message from the Ollama agent. You can ask me anything and I will respond accordingly."

root_agent = LlmAgent(
    # LiteLLM knows how to connect to a local Ollama server by default
    # Proxying via the openai standards
    model=LiteLlm(model=os.getenv("MODEL")), 
    name="ollama_gemma_agent",
    instruction=prompt.ROOT_AGENT_INSTR,
    tools=[get_custom_message]
)